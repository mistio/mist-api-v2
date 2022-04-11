import connexion
import logging

from mist.api import config
from mist.api.exceptions import NotFoundError

from mist_api_v2 import util
from mist_api_v2.models.list_users_response import ListUsersResponse  # noqa: E501

from .base import list_resources, get_resource

logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)


def list_users(search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
    """List users

    Return current user if requester is not admin. Return all users for admin. # noqa: E501

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

    :rtype: ListUsersResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    if auth_context.user.role == "Admin":
        result = list_resources(
            auth_context, 'users', search=search, only=only,
            sort=sort, start=start, limit=limit, deref=deref, at=at)
    else:
        search = "id={}".format(auth_context.user.id)
        try:
            result = get_resource(auth_context, 'users', search=search)
        except NotFoundError:
            return 'User does not exist', 404

        result['meta'] = {
            'total': 1,
            'returned': 1
        }
    return ListUsersResponse(data=result['data'], meta=result['meta'])
