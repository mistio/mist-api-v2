import connexion
import six

from mist_api_v2.models.get_org_member_response import GetOrgMemberResponse  # noqa: E501
from mist_api_v2.models.get_org_response import GetOrgResponse  # noqa: E501
from mist_api_v2.models.list_org_members_response import ListOrgMembersResponse  # noqa: E501
from mist_api_v2.models.list_org_teams_response import ListOrgTeamsResponse  # noqa: E501
from mist_api_v2.models.list_orgs_response import ListOrgsResponse  # noqa: E501
from mist_api_v2 import util

from .base import list_resources


def get_member(org, member, only=None):  # noqa: E501
    """Get Member

    Get details about target member # noqa: E501

    :param org: 
    :type org: str
    :param member: 
    :type member: str
    :param only: Only return these fields
    :type only: str

    :rtype: GetOrgMemberResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    org = list_resources(auth_context, 'orgs', search=org)
    try:
        member = org.members.get(member)
    except ValueError:
        return "Member does not exist", 404
    meta = {
        'total': len(org.members),
        'returned': 1
    }
    result = {
        'data': member.as_dict_v2(only=only),
        'meta': meta
    }
    return GetOrgMemberResponse(data=result['date'], meta=result['meta'])

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
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [org], total = list_resources(auth_context, 'orgs', search=org,
                                      only=only, deref=deref)
    except ValueError:
        return 'Org does not exist', 404
    meta = {
        'total': total,
        'returned': 1
    }
    result = {
        'data': org,
        'meta': meta
    }
    return GetOrgResponse(data=result['data'], meta=result['meta'])


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
    auth_context = connexion.context['token_info']['auth_context']
    org_members = auth_context.org.members
    total = len(org_members)
    if not limit:
        limit = 100
    org_members = org_members.order_by(sort)[0:limit-1]
    meta = {
        'total': total,
        'returned': len(org_teams),
        'sort': sort,
        'start': start
    }
    result = {
        'data': [i.as_dict_v2(deref or '', only or '') for i in org_teams],
        'meta': meta
    }
    return ListOrgMembersResponse(data=result['data'], meta=result['meta'])

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
    auth_context = connexion.context['token_info']['auth_context']
    org_teams = auth_context.org.teams
    total = len(org_members)
    if not limit:
        limit = 100
    org_teams = org_teams.order_by(sort)[0:limit-1]
    meta = {
        'total': total,
        'returned': len(org_members),
        'sort': sort,
        'start': start
    }
    result = {
        'data': [i.as_dict_v2(deref or '', only or '') for i in org_members],
        'meta': meta
    }
    return ListOrgTeamsResponse(data=result['data'], meta=result['meta'])


def list_orgs(all=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List orgs

    List orgs owned by the requester. If parameter all is True and requester is an admin then all orgs will be listed. # noqa: E501

    :param all: Return all existing organizations
    :type all: bool
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
    auth_context = connexion.context['token_info']['auth_context']
    
    result = list_resources(auth_context, 'orgs', search=search, only=only,
                            sort=sort, start=start, limit=limit, deref=deref,
                            all_orgs=all)
    return ListOrgsResponse(data=result['data'], meta=result['meta'])

