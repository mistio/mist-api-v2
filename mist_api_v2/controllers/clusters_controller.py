import connexion

from mist.api.methods import list_resources as list_resources_v1

from mist.api.exceptions import ServiceUnavailableError

from mist_api_v2.models.create_cluster_request import CreateClusterRequest  # noqa: E501
from mist_api_v2.models.get_cluster_response import GetClusterResponse  # noqa: E501
from mist_api_v2.models.list_clusters_response import ListClustersResponse  # noqa: E501

from .base import list_resources
from .base import get_resource


def create_cluster(create_cluster_request=None):  # noqa: E501
    """Create cluster

    Create a new cluster and return the cluster&#39;s id # noqa: E501

    :param create_cluster_request:
    :type create_cluster_request: dict | bytes

    :rtype: CreateClusterResponse
    """
    if connexion.request.is_json:
        create_cluster_request = CreateClusterRequest.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except Exception:
        return 'Authentication failed', 401
    params = create_cluster_request.to_dict()
    try:
        [cloud], _ = list_resources_v1(auth_context, 'cloud',
                                       search=params.pop('cloud'),
                                       limit=1)
    except ValueError:
        return 'Cloud not found', 404
    try:
        auth_context.check_perm('cluster', 'create', cloud.id)
        auth_context.check_perm('cloud', 'read', cloud.id)
        auth_context.check_perm('cloud', 'create_resources', cloud.id)
    except Exception:
        return 'You are not authorized to perform this action', 403
    provider = params.pop('provider')
    kwargs = {k: v for k, v in params.items() if v is not None}
    if provider == 'google':
        kwargs['zone'] = kwargs.pop('location')
    try:
        result = cloud.ctl.container.create_cluster(**kwargs)
    except ServiceUnavailableError as e:
        return e.msg, e.http_code
    if not result:
        return 'Cluster creation failed', 409
    return 'Cluster creation successful', 200


def destroy_cluster(cluster):  # noqa: E501
    """Destroy cluster

    Destroy target clusters # noqa: E501

    :param cluster:
    :type cluster: str

    :rtype: None
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except Exception:
        return 'Authentication failed', 401
    cluster_name = cluster
    try:
        [cluster], total = list_resources_v1(auth_context, 'cluster',
                                             search=f'"{cluster_name}"',
                                             limit=1)
    except ValueError:
        return 'Cluster not found', 404
    try:
        auth_context.check_perm('cluster', 'destroy', cluster.id)
    except Exception:
        return 'You are not authorized to perform this action', 403
    result = cluster.ctl.destroy_cluster()
    if not result:
        return 'Cluster destruction failed', 404
    return 'Cluster destruction successful', 200


def get_cluster(cluster, only=None, deref=None):  # noqa: E501
    """Get cluster

    Get details about target cluster # noqa: E501

    :param cluster:
    :type cluster: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetClusterResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'cluster', search=cluster, only=only,
                          deref=deref)
    return GetClusterResponse(data=result['data'], meta=result['meta'])


def list_clusters(cloud=None, search=None, sort=None, start=0, limit=100, only=None, deref=None):  # noqa: E501
    """List clusters

    List clusters # noqa: E501

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

    :rtype: ListClustersResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(
        auth_context, 'cluster', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref
    )
    return ListClustersResponse(data=result['data'], meta=result['meta'])
