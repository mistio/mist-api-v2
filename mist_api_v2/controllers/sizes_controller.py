import connexion
from mist.api.exceptions import NotFoundError

from mist_api_v2 import util
from mist_api_v2.models.get_size_response import GetSizeResponse  # noqa: E501
from mist_api_v2.models.list_sizes_response import ListSizesResponse  # noqa: E501

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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(
            auth_context, 'size', search=size, only=only, deref=deref)
    except NotFoundError:
        return 'Size does not exist', 404

    return GetSizeResponse(data=result['data'], meta=result['meta'])


def list_sizes(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListSizesResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'size', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at)
    return ListSizesResponse(data=result['data'], meta=result['meta'])
