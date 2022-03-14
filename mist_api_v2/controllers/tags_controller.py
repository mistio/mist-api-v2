import connexion


from mist_api_v2.models.list_tags_response import ListTagsResponse  # noqa: E501
from mist.api.tag.models import Tag


def list_tags(verbose=None, resource=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List tags

    List tags on resources owned by the active org. READ permission required on each resource. # noqa: E501

    :param verbose: Toggle displaying resource types and ids associated with each key value pair
    :type verbose: bool
    :param resource: Display tags on a single resource
    :type resource: dict | bytes
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

    :rtype: ListTagsResponse
    """
    # import ipdb; ipdb.set_trace()
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401

    tags = Tag.objects(owner=auth_context.owner)
    data = [{'key': k, 'value': v} for k, v in
            set((t.key, t.value) for t in tags)]
    if verbose:
        for kv in data:
            kv_temp = kv.copy()
            for resource_type in tags.filter(**kv_temp).distinct('resource_type'):  # noqa: E501
                kv[resource_type + 's'] = [tag.resource_id for tag in
                                           Tag.objects(**kv_temp, resource_type=resource_type)]  # noqa: E501

    meta = {
        'total': len(data),
        'returned': len(data),
        'sort': sort,
        'start': start
    }

    return ListTagsResponse(data, meta)
