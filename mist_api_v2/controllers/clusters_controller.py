import uuid
import connexion
import mongoengine as me
import libcloud

from mist.api.methods import list_resources as list_resources_v1

from mist.api.exceptions import NotFoundError, PolicyUnauthorizedError
from mist.api.exceptions import BadRequestError
from mist.api.tasks import create_cluster_async, destroy_cluster_async

from mist_api_v2 import util
from mist_api_v2.models.create_cluster_request import CreateClusterRequest  # noqa: E501
from mist_api_v2.models.create_cluster_response import CreateClusterResponse  # noqa: E501
from mist_api_v2.models.get_cluster_response import GetClusterResponse  # noqa: E501
from mist_api_v2.models.list_clusters_response import ListClustersResponse  # noqa: E501
from mist_api_v2.models.destroy_cluster_response import DestroyClusterResponse  # noqa: E501
from mist_api_v2.models.scale_nodepool_request import ScaleNodepoolRequest  # noqa: E501

from .base import list_resources
from .base import get_resource


def create_cluster(create_cluster_request=None):  # noqa: E501
    """Create cluster

    Create a new cluster and return the cluster&#39;s id # noqa: E501

    :param create_cluster_request:
    :type create_cluster_request: dict | bytes

    :rtype: CreateClusterResponse
    """
    request_json = {}
    if connexion.request.is_json:
        request_json = connexion.request.get_json()
        create_cluster_request = CreateClusterRequest.from_dict(request_json)  # noqa: E501
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
            kwargs = cloud.ctl.container.validate_create_cluster_request(
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

    charts = [chart for chart in create_cluster_request.templates or []
              if chart['type'] == 'helm']
    kwargs['helm_charts'] = charts
    kwargs['waiters'] = request_json.get("waiters")
    job_id = uuid.uuid4().hex
    kwargs['job_id'] = job_id
    kwargs['job'] = 'create_cluster'
    args = (auth_context.serialize(), selected_cloud.id,)
    create_cluster_async.send_with_options(
        args=args,
        kwargs=kwargs,
        delay=3_000,
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

    args = (auth_context.serialize(), cluster.id)
    job_id = uuid.uuid4().hex
    job = 'destroy_cluster'
    kwargs = {
        'job_id': job_id,
        'job': job
    }
    destroy_cluster_async.send_with_options(
        args=args,
        kwargs=kwargs,
        delay=3_000,
    )

    return DestroyClusterResponse(job_id=job_id,
                                  cloud=cluster.cloud.id,
                                  cluster=cluster.id), 200


def get_new_cluster_credentials(auth_context, cluster):
    """
    Fetch fresh cluster credentials from provider

    :param cluster:
    :type cluster: str

    :rtype: dict
    """
    from mist.api.methods import list_resources
    items, _ = list_resources(auth_context, 'cluster', search=cluster)
    if len(items) == 0:
        raise NotFoundError
    cluster_object = items[0]
    return cluster_object.ctl.get_credentials()


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

    try:
        result = get_resource(auth_context, 'cluster', search=cluster,
                              only=only,
                              deref=deref)
    except NotFoundError:
        return 'Cluster does not exist', 404

    if credentials:
        try:
            auth_context.check_perm(
                'cluster', 'read_credentials', result['data']['id'])
            result['data']['credentials'] = get_new_cluster_credentials(
                auth_context, cluster)
        except PolicyUnauthorizedError:
            return 'You are not authorized to perform this action', 403
        except NotFoundError:
            return 'Cluster does not exist', 404
    else:
        try:
            result['data']['credentials']['token'] = '***CENSORED***'
        except KeyError:
            pass

    return GetClusterResponse(data=result['data'], meta=result['meta'])


def list_clusters(cloud=None, search=None, sort=None, start=0, limit=100, only=None, deref=None, at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListClustersResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'cluster', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at
    )

    for item in result['data']:
        try:
            item['credentials']['token'] = '***CENSORED***'
        except KeyError:
            pass
    return ListClustersResponse(data=result['data'], meta=result['meta'])


def scale_nodepool(cluster, nodepool, scale_nodepool_request=None):  # noqa: E501
    """Scale cluster nodepool

    Scale the nodes of the specified nodepool # noqa: E501

    :param cluster:
    :type cluster: str
    :param nodepool:
    :type nodepool: str
    :param scale_nodepool_request:
    :type scale_nodepool_request: dict | bytes

    :rtype: None
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401

    if connexion.request.is_json:
        scale_nodepool_request = ScaleNodepoolRequest.from_dict(connexion.request.get_json())  # noqa: E501

    clusters, total = list_resources_v1(
        auth_context, 'cluster', search=cluster)
    if total == 0:
        return 'Cluster does not exist', 404

    cluster = clusters[0]

    try:
        nodepool = cluster.nodepools.get(name=nodepool)
    except me.DoesNotExist:
        return 'Nodepool does not exist', 404

    try:
        auth_context.check_perm('cloud', 'read', cluster.cloud.id)
        auth_context.check_perm('cloud', 'create_resources', cluster.cloud.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    try:
        cluster.cloud.ctl.container.validate_scale_nodepool_request(
            auth_context=auth_context,
            cluster=cluster,
            nodepool=nodepool,
            desired_nodes=scale_nodepool_request.desired_nodes,
            min_nodes=scale_nodepool_request.min_nodes,
            max_nodes=scale_nodepool_request.max_nodes,
            autoscaling=scale_nodepool_request.autoscaling)
    except BadRequestError as exc:
        return exc.args[0], 400

    try:
        cluster.cloud.ctl.container.scale_nodepool(
            auth_context=auth_context,
            cluster=cluster,
            nodepool=nodepool,
            desired_nodes=scale_nodepool_request.desired_nodes,
            min_nodes=scale_nodepool_request.min_nodes,
            max_nodes=scale_nodepool_request.max_nodes,
            autoscaling=scale_nodepool_request.autoscaling)
    except (libcloud.common.exceptions.BaseHTTPError,
            libcloud.common.types.LibcloudError) as exc:
        return exc.args[0], 400

    return 'Nodepool scaling started', 200
