import connexion
import six

from mist_api_v2.models.list_users_response import ListUsersResponse  # noqa: E501
from mist_api_v2 import util


def list_users(search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
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

    :rtype: ListUsersResponse
    """
    return 'do some magic!'
