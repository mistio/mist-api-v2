import connexion
import mongoengine as me
import hvac

from mist.api.exceptions import NotFoundError
from mist.api.users.models import Organization
from mist.api.helpers import trigger_session_update
from mist_api_v2 import util
from mist_api_v2.models.get_org_member_response import GetOrgMemberResponse  # noqa: E501
from mist_api_v2.models.get_org_response import GetOrgResponse  # noqa: E501
from mist_api_v2.models.list_org_members_response import ListOrgMembersResponse  # noqa: E501
from mist_api_v2.models.list_org_teams_response import ListOrgTeamsResponse  # noqa: E501
from mist_api_v2.models.list_orgs_response import ListOrgsResponse  # noqa: E501
from mist_api_v2.models.patch_organization_request import PatchOrganizationRequest  # noqa: E501
from mist_api_v2.models.create_organization_request import CreateOrganizationRequest  # noqa: E501

from .base import list_resources, get_resource, get_org_resources_summary


def create_org(create_organization_request=None):  # noqa: E501
    """Create org

    Create an organization. # noqa: E501

    :param create_organization_request:
    :type create_organization_request: dict | bytes

    :rtype: Org
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if connexion.request.is_json:
        create_organization_request = CreateOrganizationRequest.from_dict(connexion.request.get_json())  # noqa: E501

    if auth_context.user.can_create_org is False:
        return 'User is not authorized to create an organization', 403

    name = create_organization_request.name

    if Organization.objects(name=name).first():
        return f'Organization with name {name} already exists', 400

    org = Organization()
    org.add_member_to_team('Owners', auth_context.user)
    org.name = name

    try:
        org.save()
    except (me.ValidationError, me.OperationError) as exc:
        return f'Failed to create organization with exception: {exc!r}', 400

    org.reload()
    auth_context.token.orgs.append(org)
    auth_context.token.save()
    trigger_session_update(auth_context.user, ['user'])
    return org.as_dict_v2()


def update_org(org, patch_organization_request=None):  # noqa: E501
    """update_org

    Update organization # noqa: E501

    :param org: Organization id
    :type org: str
    :param patch_organization_request:
    :type patch_organization_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        patch_organization_request = PatchOrganizationRequest.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401

    if not auth_context.is_owner():
        return 'Only owners can edit the organization', 403

    try:
        organization = Organization.objects.get(id=org)
    except Organization.DoesNotExist:
        return f'Organization {org} not found', 404

    if patch_organization_request.name:
        organization.name = patch_organization_request.name
        try:
            organization.save()
        except (me.ValidationError, me.OperationError) as exc:
            return f'Failed to edit organization with exception: {exc!r}', 400
        else:
            return 'Organization name updated succesfully', 200

    vault_address = patch_organization_request.vault.address
    secrets_engine_path = patch_organization_request.vault.secrets_engine_path
    token = patch_organization_request.vault.token
    role_id = patch_organization_request.vault.role_id
    secret_id = patch_organization_request.vault.secret_id

    if vault_address is not None:
        if secrets_engine_path is None:
            return 'Vault secrets engine path is required', 400

        client = hvac.Client(url=vault_address)
        if token:
            client.token = token
        elif role_id and secret_id:
            try:
                client.auth.approle.login(role_id=role_id, secret_id=secret_id)
            except (hvac.exceptions.InvalidRequest,
                    hvac.exceptions.VaultDown) as exc:
                return 'Failed to authenticate to vault {exc!r}', 400
        else:
            return 'Either token or approle credentials are required', 400

        try:
            is_authenticated = client.is_authenticated()
        except hvac.exceptions.VaultDown as exc:
            return f'Failed to connect to Vault instance: {exc!r}', 503

        if is_authenticated is False:
            return 'Failed to authenticate with credentials provided', 400

        organization.vault_address = vault_address
        organization.vault_secret_engine_path = secrets_engine_path
        organization.vault_role_id = role_id
        organization.vault_secret_id = secret_id
        organization.vault_token = token

        try:
            organization.save()
        except (me.ValidationError, me.OperationError) as exc:
            return f'Failed to edit organization with exception: {exc!r}', 400
        else:
            return 'Organization Vault updated succesfully', 200

    # Reenable Mist Portal vault for organization
    if vault_address == '' and organization.vault_address:
        organization.vault_address = ''
        organization.vault_secret_engine_path = ''
        organization.vault_token = ''
        organization.vault_role_id = ''
        organization.vault_secret_id = ''
        try:
            organization.save()
        except (me.ValidationError, me.OperationError) as exc:
            return f'Failed to edit organization with exception: {exc!r}', 400
        else:
            return 'Organization Vault updated succesfully', 200

    return 'Invalid request', 400


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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401

    search = f'id={org}'
    try:
        org = get_resource(auth_context, 'orgs', search=search)['data']
    except NotFoundError:
        return 'Organization does not exist', 404
    try:
        [member] = filter(lambda user: user['id'] == member,
                          org.get('members', []))
    except ValueError:
        return "Member does not exist", 404
    meta = {
        'total': len(org.get('members')),
        'returned': 1
    }
    result = {
        'data': member,
        'meta': meta
    }

    return GetOrgMemberResponse(data=result['data'], meta=result['meta'])


def get_org(org, summary=None, only=None, deref=None):  # noqa: E501
    """Get Org

    Get details about target org # noqa: E501

    :param org:
    :type org: str
    :param summary: Return total number for each org specific resource
    :type summary: bool
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetOrgResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(auth_context, 'orgs', search=org, only=only)
    except NotFoundError:
        return 'Organization does not exist', 404
    # Get resource counts only if rbac checks pass
    if summary and result['meta']['returned'] == 1:
        result['data']['resources'] = get_org_resources_summary(
            auth_context, org_id=result['data']['id'])
    return GetOrgResponse(data=result['data'], meta=result['meta'])


def list_org_members(org, search=None, sort=None, start=None, limit=None, only=None, at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListOrgMembersResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    search = f'id={org}'
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    try:
        org = get_resource(auth_context, 'orgs', search=search, at=at)['data']
    except NotFoundError:
        return 'Organization does not exist', 404
    org_members = org.get('members', [])
    total = len(org_members)
    if not limit:
        limit = 100
    if sort:
        reverse = sort.find('-') != -1
        sort = sort.replace('-', '')
        sort = sort.replace('+', '')
        sort = sort.strip()
        org_members.sort(key=lambda user: user.get(sort, ""),
                         reverse=reverse)
    org_members = org_members[0:limit - 1]
    meta = {
        'total': total,
        'returned': len(org_members),
        'sort': sort,
        'start': start
    }
    result = {
        'data': org_members,
        'meta': meta
    }
    return ListOrgMembersResponse(data=result['data'], meta=result['meta'])


def list_org_teams(org, search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListOrgTeamsResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    search = f'id={org}'
    try:
        org = get_resource(auth_context, 'orgs', search=search, at=at)['data']
    except NotFoundError:
        return 'Organization does not exist', 404
    org_teams = org.get('teams', [])
    total = len(org_teams)
    if not limit:
        limit = 100
    if sort:
        reverse = sort.find('-') != -1
        sort = sort.replace('-', '')
        sort = sort.replace('+', '')
        sort = sort.strip()
        org_teams.sort(key=lambda team: team.get(sort, ''),
                       reverse=reverse)

    org_teams = org_teams[0:limit - 1]
    meta = {
        'total': total,
        'returned': len(org_teams),
        'sort': sort,
        'start': start
    }
    result = {
        'data': org_teams,
        'meta': meta
    }
    return ListOrgTeamsResponse(data=result['data'], meta=result['meta'])


def list_orgs(allorgs=None, search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListOrgsResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(auth_context, 'orgs', search=search, only=only,
                            sort=sort, start=start, limit=limit, deref=deref,
                            at=at)
    return ListOrgsResponse(data=result['data'], meta=result['meta'])
