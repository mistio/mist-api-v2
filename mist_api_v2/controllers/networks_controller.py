import connexion

from mist.api.networks.models import NETWORKS
from mist.api.helpers import delete_none
from mist.api.tag.methods import add_tags_to_resource

from mist.api.exceptions import BadRequestError, NotFoundError
from mist.api.exceptions import PolicyUnauthorizedError
from mist.api.exceptions import NetworkListingError

from mist_api_v2 import util
from mist_api_v2.models.create_network_request import CreateNetworkRequest  # noqa: E501
from mist_api_v2.models.get_network_response import GetNetworkResponse  # noqa: E501
from mist_api_v2.models.list_networks_response import ListNetworksResponse  # noqa: E501

from .base import list_resources, get_resource


def create_network(create_network_request=None):  # noqa: E501
    """Create network

    Creates one or more networks on the specified cloud. If async is true, a jobId will be returned. READ permission required on cloud. CREATE_RESOURCES permission required on cloud. CREATE permission required on network. # noqa: E501

    :param create_network_request:
    :type create_network_request: dict | bytes

    :rtype: CreateNetworkResponse
    """
    from mist.api.methods import list_resources
    if connexion.request.is_json:
        create_network_request = CreateNetworkRequest.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    params = delete_none(create_network_request.to_dict())
    try:
        tags, _ = auth_context.check_perm("network", "add", None)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        [cloud], total = list_resources(
            auth_context, 'cloud', search=params.pop('cloud'), limit=1)
    except ValueError:
        return 'Cloud does not exist', 404
    try:
        auth_context.check_perm('cloud', 'read', cloud.id)
        auth_context.check_perm('cloud', 'create_resources', cloud.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    if not hasattr(cloud.ctl, 'network'):
        return 'Network support is not available', 501
    # Create the new network
    network_params = {'name': params['name']}
    if 'extra' in params:
        network_params.update(params['extra'])
    try:
        network = NETWORKS[cloud.ctl.provider].add(
            cloud=cloud, **network_params)
    except BadRequestError as e:
        return str(e), 400
    except NetworkListingError as e:
        return str(e), 503
    network.assign_to(auth_context.user)
    if tags:
        add_tags_to_resource(auth_context.owner,
                             [{'resource_type': 'network',
                               'resource_id': network.id}],
                             tags)
    return network.as_dict()


def delete_network(network, cloud):  # noqa: E501
    """Delete network

    Delete target network # noqa: E501

    :param network:
    :type network: str
    :param cloud: Cloud the target network belongs to
    :type cloud: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [cloud], total = list_resources(
            auth_context, 'cloud', search=cloud, limit=1)
    except ValueError:
        return 'Cloud does not exist', 404
    try:
        [network], total = list_resources(
            auth_context, 'network', search=network, limit=1)
    except ValueError:
        return 'Network does not exist', 404
    try:
        auth_context.check_perm("cloud", "read", cloud.id)
        auth_context.check_perm('network', 'read', network.id)
        auth_context.check_perm('network', 'remove', network.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    network.ctl.delete()
    return 'Network deleted succesfully', 200


def edit_network(network, name=None):  # noqa: E501
    """Edit network

    Edit target network # noqa: E501

    :param network:
    :type network: str
    :param name: New network name
    :type name: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [network], total = list_resources(
            auth_context, 'network', search=network, limit=1)
    except ValueError:
        return 'Network does not exist', 404
    try:
        auth_context.check_perm('network', 'edit', network.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    network.ctl.rename(name)
    return 'Network succesfully updated'


def get_network(network, only=None, deref='auto'):  # noqa: E501
    """Get network

    Get details about target network # noqa: E501

    :param network:
    :type network: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetNetworkResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(
            auth_context, 'network', search=network, only=only, deref=deref)
    except NotFoundError:
        return 'Network does not exist', 404
    return GetNetworkResponse(data=result['data'], meta=result['meta'])


def list_networks(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref='auto', at=None):  # noqa: E501
    """List networks

    List networks owned by the active org. READ permission required on network &amp; cloud. # noqa: E501

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

    :rtype: ListNetworksResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'network', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at)
    return ListNetworksResponse(data=result['data'], meta=result['meta'])
