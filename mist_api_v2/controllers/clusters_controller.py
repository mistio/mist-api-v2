import connexion

from mist_api_v2.models.list_clusters_response import ListClustersResponse  # noqa: E501

from .base import list_resources


def create_cluster(create_cluster_request=None):  # noqa: E501
    """Create cluster

    Create a new cluster and return the cluster&#39;s id # noqa: E501

    :param create_cluster_request:
    :type create_cluster_request: dict | bytes

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def delete_cluster(cluster):  # noqa: E501
    """Delete cluster

    Delete target clusters # noqa: E501

    :param cluster:
    :type cluster: str

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'


def list_clusters(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
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
