import connexion
import six

from mist_api_v2.models.get_size_response import GetSizeResponse  # noqa: E501
from mist_api_v2.models.list_sizes_response import ListSizesResponse  # noqa: E501
from mist_api_v2 import util

from .base import list_resources, get_resource


def get_size(size, only=None, deref=None):  # noqa: E501
    """Get size

    Get details about target size # noqa: E501

    :param size:
    :type size: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetSizeResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(
        auth_context, 'size', search=volume, only=only, deref=deref)
    return GetSizeResponse(data=result['data'], meta=result['meta'])


def list_sizes(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List sizes

    List sizes owned by the active org. READ permission required on size &amp; cloud. # noqa: E501

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

    :rtype: ListSizesResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(
        auth_context, 'size', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref)
    return ListSizesResponse(data=result['data'], meta=result['meta'])