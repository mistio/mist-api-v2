import connexion

from mist.api import config
from mist.api.helpers import delete_none
from mist.api.tag.methods import add_tags_to_resource
from mist.api.helpers import trigger_session_update
from mist.api.tasks import async_session_update

from mist_api_v2.models.create_volume_request import CreateVolumeRequest  # noqa: E501
from mist_api_v2.models.get_volume_response import GetVolumeResponse  # noqa: E501
from mist_api_v2.models.list_volumes_response import ListVolumesResponse  # noqa: E501

from .base import list_resources, get_resource


def create_volume(create_volume_request=None):  # noqa: E501
    """Create volume

    Creates one or more volumes on the specified cloud. If async is true, a jobId will be returned. READ permission required on cloud. CREATE_RESOURCES permission required on cloud. READ permission required on location. CREATE_RESOURCES permission required on location. CREATE permission required on volume. # noqa: E501

    :param create_volume_request:
    :type create_volume_request: dict | bytes

    :rtype: CreateVolumeResponse
    """
    from mist.api.methods import list_resources
    if connexion.request.is_json:
        create_volume_request = CreateVolumeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    params = delete_none(create_volume_request.to_dict())
    auth_context = connexion.context['token_info']['auth_context']
    tags, _ = auth_context.check_perm("network", "add", None)
    try:
        [cloud], total = list_resources(
            auth_context, 'cloud', search=params.pop('cloud'), limit=1)
    except ValueError:
        return 'Cloud does not exist', 404
    if not hasattr(cloud.ctl, 'storage'):
        raise NotImplementedError()
    try:
        [location], total = list_resources(
            auth_context, 'location', search=params.pop('location'), limit=1)
    except ValueError:
        return 'Location does not exist', 404
    params['location'] = location.id
    auth_context.check_perm("cloud", "read", cloud.id)
    auth_context.check_perm("cloud", "create_resources", cloud.id)
    auth_context.check_perm("location", "read", location.id)
    auth_context.check_perm("location", "create_resources", location.id)
    tags, _ = auth_context.check_perm("volume", "create", None)
    volume = cloud.ctl.storage.create_volume(**params)
    owner = auth_context.owner
    if tags:
        add_tags_to_resource(owner, volume, tags)
    volume.assign_to(auth_context.user)
    trigger_session_update(owner.id, ['volumes'])
    if config.HAS_RBAC:
        owner.mapper.update(
            volume,
            callback=async_session_update,
            args=(owner.id, ['volumes'], )
        )
    return volume.as_dict()


def edit_volume(volume, name=None):  # noqa: E501
    """Edit volume

    Edit target volume # noqa: E501

    :param volume:
    :type volume: str
    :param name: New volume name
    :type name: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [volume], total = list_resources(
            auth_context, 'volume', search=volume, limit=1)
    except ValueError:
        return 'Volume does not exist', 404
    auth_context.check_perm('volume', 'edit', volume.id)
    # TODO: Implement volume.ctl.rename()
    return 'Volume succesfully updated'


def delete_volume(volume):  # noqa: E501
    """Delete volume

    Delete target volume # noqa: E501

    :param volume:
    :type volume: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [volume], _ = list_resources(auth_context, 'volume',
                                     search=volume, limit=1)
    except ValueError:
        return 'Volume does not exist', 404

    cloud = volume.cloud
    # SEC
    auth_context.check_perm('cloud', 'read', cloud.id)
    auth_context.check_perm('volume', 'remove', volume.id)

    volume.ctl.delete()

    return 'Destroyed volume `%s`' % volume.name, 200


def get_volume(volume, only=None, deref=None):  # noqa: E501
    """Get volume

    Get details about target volume # noqa: E501

    :param volume:
    :type volume: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetVolumeResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(
        auth_context, 'volume', search=volume, only=only, deref=deref)
    return GetVolumeResponse(data=result['data'], meta=result['meta'])


def list_volumes(cloud=None, search=None, sort=None, start=0, limit=100, only=None, deref='auto'):  # noqa: E501
    """List volumes

    List volumes owned by the active org. READ permission required on volume &amp; cloud. # noqa: E501

    :param cloud:
    :type cloud: str
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

    :rtype: ListVolumesResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(
        auth_context, 'volume', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref)
    return ListVolumesResponse(data=result['data'], meta=result['meta'])
