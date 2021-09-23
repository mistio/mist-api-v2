import time
import logging

import connexion

import mongoengine as me

from mist.api import config

from mist_api_v2.models.add_cloud_request import AddCloudRequest  # noqa: E501
from mist_api_v2.models.edit_cloud_request import EditCloudRequest  # noqa: E501
from mist_api_v2.models.get_cloud_response import GetCloudResponse  # noqa: E501
from mist_api_v2.models.list_clouds_response import ListCloudsResponse  # noqa: E501

from mist.api.exceptions import CloudExistsError
from mist.api.exceptions import CloudUnauthorizedError

from .base import list_resources, get_resource


logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)

# dict that maps provider name aliases to
# names expected by add_cloud_v2
PROVIDER_ALIASES = {
    'equinix': 'equinixmetal',
    'alibaba': 'aliyun_ecs'
}


def mongo_connect(*args, **kwargs):
    """Connect mongoengine to mongo db. This connection is reused everywhere"""
    exc = None
    for _ in range(30):
        try:
            log.info("Attempting to connect to %s at %s...", config.MONGO_DB,
                     config.MONGO_URI)
            me.connect(db=config.MONGO_DB, host=config.MONGO_URI)
        except Exception as e:
            log.warning("Error connecting to mongo, will retry in 1 sec: %r",
                        e)
            time.sleep(1)
            exc = e
        else:
            log.info("Connected...")
            break
    else:
        log.critical("Unable to connect to %s at %s: %r", config.MONGO_DB,
                     config.MONGO_URI, exc)
        raise exc


try:
    import uwsgi  # noqa
except ImportError:
    log.debug('Not in uwsgi context')
    mongo_connect()
else:
    log.info('Uwsgi context')
    from uwsgidecorators import postfork
    mongo_connect = postfork(mongo_connect)


def add_cloud(add_cloud_request=None):  # noqa: E501
    """Add cloud

    Adds a new cloud and returns the cloud&#39;s id. ADD permission required on cloud. # noqa: E501

    :param add_cloud_request:
    :type add_cloud_request: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        add_cloud_request = AddCloudRequest.from_dict(connexion.request.get_json())  # noqa: E501

    from mist.api.clouds.models import Cloud
    from mist.api.clouds.methods import add_cloud_v_2
    from mist.api.helpers import trigger_session_update
    from mist.api.tasks import async_session_update
    from mist.api.tag.methods import add_tags_to_resource

    auth_context = connexion.context['token_info']['auth_context']
    cloud_tags, _ = auth_context.check_perm('cloud', 'add', None)
    provider = add_cloud_request.provider
    provider = PROVIDER_ALIASES.get(provider, provider)
    params = add_cloud_request.to_dict()
    credentials = params['credentials']
    features = params.get('features', {})
    del params['name']
    del params['credentials']
    if features:
        del features['compute']
        del params['features']
        params.update(features)
    params.update(credentials)
    try:
        result = add_cloud_v_2(
            auth_context.owner,
            add_cloud_request.name,
            provider,
            params
        )
    except CloudExistsError as exc:
        return exc.args[0], 409
    except CloudUnauthorizedError as exc:
        return exc.args[0], 403

    cloud_id = result['cloud_id']
    monitoring = result.get('monitoring')
    errors = result.get('errors')

    cloud = Cloud.objects.get(owner=auth_context.owner, id=cloud_id)

    if cloud_tags:
        add_tags_to_resource(auth_context.owner, cloud,
                             list(cloud_tags.items()))

    # Set ownership.
    cloud.assign_to(auth_context.user)

    trigger_session_update(auth_context.owner.id, ['clouds'])

    # SEC
    # Update the RBAC & User/Ownership mappings with the new Cloud and finally
    # trigger a session update by registering it as a chained task.
    if config.HAS_RBAC:
        auth_context.owner.mapper.update(
            cloud,
            callback=async_session_update,
            args=(auth_context.owner.id, ['clouds'], )
        )

    c_count = Cloud.objects(owner=auth_context.owner, deleted=None).count()
    ret = cloud.as_dict_v2()
    ret['index'] = c_count - 1
    if errors:
        ret['errors'] = errors
    if monitoring:
        ret['monitoring'] = monitoring

    return ret


def delete_cloud(cloud):  # noqa: E501
    """Delete cloud

    Delete target cloud # noqa: E501

    :param cloud:
    :type cloud: str

    :rtype: None
    """
    from mist.api.clouds.methods import delete_cloud
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'cloud', search=cloud)
    result_data = result.get('data')
    if not result_data:
        return 'Cloud does not exist', 404
    cloud_id = result_data.get('id')
    auth_context.check_perm('cloud', 'remove', cloud_id)
    delete_cloud(auth_context.owner, cloud_id)
    return None, 200


def edit_cloud(cloud, edit_cloud_request=None):  # noqa: E501
    """Edit cloud

    Update target cloud title or credentials # noqa: E501

    :param cloud:
    :type cloud: str
    :param edit_cloud_request:
    :type edit_cloud_request: dict | bytes

    :rtype: None
    """
    from mist.api.clouds.models import Cloud
    from mist.api.helpers import trigger_session_update

    if connexion.request.is_json:
        edit_cloud_request = EditCloudRequest.from_dict(connexion.request.get_json())  # noqa: E501
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'cloud', search=cloud)
    result_data = result.get('data')
    if not result_data:
        return 'Cloud does not exist', 404
    cloud_id = result_data.get('id')
    cloud_obj = Cloud.objects.get(owner=auth_context.owner, id=cloud_id,
                                  deleted=None)
    rename = edit_cloud_request.name is not None and \
        edit_cloud_request.name != cloud_obj.name
    if rename:
        from mist.api.clouds.methods import rename_cloud
        new_name = edit_cloud_request.name
        rename_cloud(auth_context.owner, cloud_id, new_name)
    credentials = edit_cloud_request.credentials
    update_credentials = credentials is not None
    if update_credentials:
        auth_context.check_perm('cloud', 'edit', cloud_id)
        log.info(f'Updating cloud: {cloud_id}')
        new_credentials = {
            cred: value
            for cred, value in credentials.to_dict().items()
            if value is not None
        }
        cloud_obj.ctl.update(**new_credentials)
        log.info(f'Cloud {cloud_id} updated successfully.')
        trigger_session_update(auth_context.owner, ['clouds'])
    features = edit_cloud_request.features
    update_features = features is not None
    if update_features:
        if features.compute:
            cloud_obj.ctl.enable()
        else:
            cloud_obj.ctl.disable()
        if features.dns:
            cloud_obj.ctl.dns_enable()
        else:
            cloud_obj.ctl.dns_disable()
        if features.container:
            cloud_obj.ctl.container_enable()
        else:
            cloud_obj.ctl.container_disable()
    return None, 200


def get_cloud(cloud, sort=None, only=None, deref=None):  # noqa: E501
    """Get cloud

    Get details about target cloud # noqa: E501

    :param cloud:
    :type cloud: str
    :param sort: Order results by
    :type sort: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetCloudResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'cloud',
                          search=cloud, only=only, deref=deref)
    return GetCloudResponse(data=result['data'], meta=result['meta'])


def list_clouds(search=None, sort=None, start=0, limit=100, only=None, deref='auto'):  # noqa: E501
    """List clouds

    List clouds owned by the active org. READ permission required on cloud. # noqa: E501

    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: ListCloudsResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(auth_context, 'cloud', search=search,
                            only=only, sort=sort, limit=limit,
                            deref=deref)
    return ListCloudsResponse(data=result['data'], meta=result['meta'])
