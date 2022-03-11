from re import L
from unittest import result
import connexion
import six

from mist_api_v2.models.list_tags_response import ListTagsResponse  # noqa: E501
from mist_api_v2.models.resource_type import ResourceType  # noqa: E501
from mist_api_v2 import util
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

    tags=Tag.objects(owner=auth_context.owner)
    
    data = [{'key':k, 'value':v} for k,v in 
                set( ( t.key, t.value ) for t in tags )]
    meta = {
        'total': len(data),
        'returned': len(data),
        'sort': sort,
        'start': start
    }


    # if connexion.request.is_json:
    #     resource =  ResourceType.from_dict(connexion.request.get_json())  # noqa: E501
    return ListTagsResponse(data,meta) 
