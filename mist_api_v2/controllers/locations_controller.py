import connexion
from mist.api.exceptions import NotFoundError

from mist_api_v2 import util
from mist_api_v2.models.get_location_response import GetLocationResponse  # noqa: E501
from mist_api_v2.models.list_locations_response import ListLocationsResponse  # noqa: E501

from .base import list_resources, get_resource


def get_location(location, only=None, deref=None):  # noqa: E501
    """Get location

    Get details about target location # noqa: E501

    :param location:
    :type location: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetLocationResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(
            auth_context, 'location', search=location, only=only, deref=deref)
    except NotFoundError:
        return 'Location does not exist', 404
    return GetLocationResponse(data=result['data'], meta=result['meta'])


def list_locations(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
    """List locations

    List locations owned by the active org. READ permission required on location &amp; cloud. # noqa: E501

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

    :rtype: ListLocationsResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'location', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at)
    return ListLocationsResponse(data=result['data'], meta=result['meta'])
