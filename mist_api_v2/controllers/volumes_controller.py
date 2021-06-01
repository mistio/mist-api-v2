import connexion

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
    if connexion.request.is_json:
        create_volume_request = CreateVolumeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_volume(volume, name=None):  # noqa: E501
    """Edit volume

    Edit target volume # noqa: E501

    :param volume:
    :type volume: str
    :param name: New volume name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


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
