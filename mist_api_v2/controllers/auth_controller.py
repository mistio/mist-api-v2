import connexion

from mist_api_v2.models.auth_info import AuthInfo  # noqa: E501
from mist_api_v2 import util

from .base import list_resources  # , get_resource


def create_token():  # noqa: E501
    """Create token

    Create new API token # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def describe_auth():  # noqa: E501
    """Authentication info

    Return info about current authenticated session. # noqa: E501


    :rtype: AuthInfo
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    authinfo = AuthInfo(data={}, meta={})
    authinfo.data['user'] = auth_context.user.as_dict_v2()
    orgs_result = list_resources(
        auth_context, 'orgs', only='id,name,last_active')
    authinfo.data['orgs'] = orgs_result['data']
    return authinfo


def list_sessions(search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
    """List sessions

     # noqa: E501

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
    :param at: Limit results by specific datetime. Return resources created before or at, or deleted after or at, given datetime.
    :type at: str

    :rtype: object
    """
    at = util.deserialize_datetime(at)
    # session = request.environ['session']
    # # Get active sessions for the current user
    # session_tokens = SessionToken.objects(user_id=auth_context.user.id,
    #                                       revoked=False)
    # sessions_list = []
    # for token in session_tokens:
    #     if token.is_valid():
    #         public_view = token.get_public_view()
    #         if isinstance(session, SessionToken) and session.id == token.id:
    #             public_view['active'] = True
    #         sessions_list.append(public_view)

    # # If user is owner include all active sessions in the org context
    # if auth_context.is_owner():
    #    org_tokens = SessionToken.objects(org=auth_context.org, revoked=False)
    #     for token in org_tokens:
    #         if token.is_valid():
    #             public_view = token.get_public_view()
    #             if isinstance(session, SessionToken) and \
    #                session.id == token.id:
    #                 public_view['active'] = True
    #             try:
    #                 sessions_list.index(public_view)
    #             except ValueError:
    #                 sessions_list.append(public_view)

    # return sessions_list
    return 'do some magic!'


def list_tokens(search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
    """List API tokens

    List API tokens # noqa: E501

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
    :param at: Limit results by specific datetime. Return resources created before or at, or deleted after or at, given datetime.
    :type at: str

    :rtype: object
    """
    at = util.deserialize_datetime(at)
    return 'do some magic!'


def login(body=None):  # noqa: E501
    """Sign in to the portal

    Sign in # noqa: E501

    :param body:
    :type body:

    :rtype: AuthInfo
    """
    return 'do some magic!'
