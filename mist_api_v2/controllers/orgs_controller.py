# import connexion
# import six

# from mist_api_v2.models.get_org_member_response import GetOrgMemberResponse  # noqa: E501
# from mist_api_v2.models.get_org_response import GetOrgResponse  # noqa: E501
# from mist_api_v2.models.list_org_members_response import ListOrgMembersResponse  # noqa: E501
# from mist_api_v2.models.list_org_teams_response import ListOrgTeamsResponse  # noqa: E501
# from mist_api_v2.models.list_orgs_response import ListOrgsResponse  # noqa: E501
# from mist_api_v2 import util


def get_member(org, member, only=None):  # noqa: E501
    """Get Org

    Get details about target member # noqa: E501

    :param org:
    :type org: str
    :param member:
    :type member: str
    :param only: Only return these fields
    :type only: str

    :rtype: GetOrgMemberResponse
    """
    return 'do some magic!'


def get_org(org, only=None, deref=None):  # noqa: E501
    """Get Org

    Get details about target org # noqa: E501

    :param org:
    :type org: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetOrgResponse
    """
    return 'do some magic!'


def list_org_members(org, search=None, sort=None, start=None, limit=None, only=None):  # noqa: E501
    """List org members

    List org members owned by the requester. The requester must be a member of the org. # noqa: E501

    :param org:
    :type org: str
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

    :rtype: ListOrgMembersResponse
    """
    return 'do some magic!'


def list_org_teams(org, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List org teams

    List teams in org. # noqa: E501

    :param org: Organization id
    :type org: str
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

    :rtype: ListOrgTeamsResponse
    """
    return 'do some magic!'


def list_orgs(allorgs=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List orgs

    List orgs owned by the requester. If parameter allorgs is true and requester is an admin then all orgs will be listed. # noqa: E501

    :param allorgs: Return all existing organizations
    :type allorgs: str
    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 100 max
    :type limit: int
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: ListOrgsResponse
    """
    return 'do some magic!'
