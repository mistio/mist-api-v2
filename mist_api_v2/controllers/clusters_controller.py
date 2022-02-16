import uuid
import connexion

from mist.api.methods import list_resources as list_resources_v1

from mist.api.exceptions import PolicyUnauthorizedError
from mist.api.tasks import create_cluster_async

from mist_api_v2.models.create_cluster_request import CreateClusterRequest  # noqa: E501
from mist_api_v2.models.create_cluster_response import CreateClusterResponse  # noqa: E501
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
    except KeyError:
        return 'Authentication failed', 401

    if create_cluster_request.cloud:
        cloud_search = create_cluster_request.cloud
    elif create_cluster_request.provider:
        cloud_search = (f'provider={create_cluster_request.provider}')
    else:
        cloud_search = ''

    cloud_search = f'{cloud_search} container_enabled=True'

    clouds, _ = list_resources_v1(auth_context,
                                  'cloud',
                                  search=cloud_search)
    selected_cloud = None
    for cloud in clouds:
        try:
            auth_context.check_perm('cluster', 'create', cloud.id)
            auth_context.check_perm('cloud', 'read', cloud.id)
            auth_context.check_perm('cloud', 'create_resources', cloud.id)
            kwargs = cloud.validate_create_cluster_request(
                auth_context,
                create_cluster_request)
        except Exception as exc:
            if clouds.count() == 1:
                if isinstance(exc, PolicyUnauthorizedError):
                    return ('You are not authorized to perform this action',
                            403)
                else:
                    return exc.args[0], 400
            continue
        else:
            selected_cloud = cloud
            break

    if selected_cloud is None:
        return 'Cloud not found', 404

    job_id = uuid.uuid4().hex
    job = 'create_cluster'
    create_cluster_async.send(auth_context.serialize(),
                              selected_cloud.id,
                              job_id=job_id,
                              job=job,
                              **kwargs
                              )
    return CreateClusterResponse(job_id=job_id)


def destroy_cluster(cluster):  # noqa: E501
    """Destroy cluster

    Destroy target clusters # noqa: E501

    :param cluster:
    :type cluster: str

    :rtype: None
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [cluster], total = list_resources_v1(auth_context, 'cluster',
                                             search=cluster,
                                             limit=1)
    except ValueError:
        return 'Cluster not found', 404
    try:
        auth_context.check_perm('cluster', 'destroy', cluster.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    result = cluster.ctl.destroy()
    if not result:
        return 'Cluster not found', 404
    return 'Cluster destruction successful', 200


def get_cluster(cluster, only=None, deref=None, credentials=False):  # noqa: E501
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    result = get_resource(auth_context, 'cluster', search=cluster, only=only,
                          deref=deref)

    if not result['data']:
        return 'Cluster not found', 404

    if credentials:
        try:
            auth_context.check_perm(
                'cluster', 'read_credentials', result['data']['id'])
        except PolicyUnauthorizedError:
            return 'You are not authorized to perform this action', 403
    else:
        result['data']['credentials']['token'] = '***CENSORED***'

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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    result = list_resources(
        auth_context, 'cluster', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref
    )

    for item in result['data']:
        item['credentials']['token'] = '***CENSORED***'
    return ListClustersResponse(data=result['data'], meta=result['meta'])
