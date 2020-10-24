import os
import time
import logging

import connexion
import six

import mongoengine as me

from mist.api import config

from mist_api_v2.models.add_cloud_request import AddCloudRequest  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_clouds_response import ListCloudsResponse  # noqa: E501
from mist_api_v2 import util


logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)


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

    result = add_cloud_v_2(
        auth_context.owner,
        add_cloud_request.title,
        add_cloud_request.provider,
        add_cloud_request.credentials.to_dict()
    )

    cloud_id = result['cloud_id']
    monitoring = result.get('monitoring')
    errors = result.get('errors')

    cloud = Cloud.objects.get(owner=auth_context.owner, id=cloud_id)

    if cloud_tags:
        add_tags_to_resource(owner, cloud, list(cloud_tags.items()))

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
    from mist.api.clouds.models import Cloud
    auth_context = connexion.context['token_info']['auth_context']
    cloud_id = cloud
    try:
        Cloud.objects.get(owner=auth_context.owner, id=cloud_id, deleted=None)
    except Cloud.DoesNotExist:
        return 'Cloud does not exist', 404
    auth_context.check_perm('cloud', 'remove', cloud_id)
    delete_cloud(auth_context.owner, cloud_id)
    return None


def get_cloud(cloud):  # noqa: E501
    """Get cloud

    Get details about target cloud # noqa: E501

    :param cloud: 
    :type cloud: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [cloud], total = list_resources(auth_context, 'cloud',
                                        search=cloud, limit=1)
    except ValueError:
        return 'Cloud does not exist', 404

    meta = {
        'total_matching': total,
        'total_returned': 1,
    }
    return {
        'data': cloud.as_dict_v2(),
        'meta': meta
    }


def list_clouds(search=None, sort=None, start=0, limit=100, only=None):  # noqa: E501
    """List clouds

    List clouds owned by the active org. READ permission required on cloud. # noqa: E501

    :param filter: Only return results matching filter
    :type filter: str
    :param sort: Order results by
    :type sort: str

    :rtype: ListCloudsResponse
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    clouds, total = list_resources(auth_context, 'cloud', search=search,
                                   only=only, sort=sort, limit=limit)
    meta = {
        'total_matching': total,
        'total_returned': clouds.count(),
        'sort': sort,
        'start': start
    }
    return {
        'data': [c.as_dict_v2() for c in clouds],
        'meta': meta
    }
