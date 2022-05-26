import logging
import connexion

from mist.api.methods import list_resources
from mist.api.tag.methods import get_tags
from mist.api.tag.methods import add_tags_to_resource
from mist.api.tag.methods import remove_tags_from_resource
from mist.api.tag.methods import modify_security_tags
from mist.api.exceptions import PolicyUnauthorizedError

from mist_api_v2.models.list_tags_response import ListTagsResponse  # noqa: E501
from mist_api_v2.models.tag_resources_request import TagResourcesRequest  # noqa: E501

log = logging.getLogger(__name__)


def list_tags(types=None, search='', sort='key', start=0, limit=100, only='', deref=None):  # noqa: E501
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

    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    data, meta = get_tags(auth_context, types=types or [],
                          search=search, sort=sort, start=start, limit=limit,
                          only=only, deref=deref)

    return ListTagsResponse(data, meta)


def tag_resources(tag_resources_request=None):  # noqa: E501
    """Tag Resources

    Batch operation for adding/removing tags from a list of resources. # noqa: E501

    :param tag_resources_request:
    :type tag_resources_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tag_resources_request = TagResourcesRequest.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401

    for op in tag_resources_request.operations:
        tags = {tag.key: tag.value for tag in op.tags}

        for resource in op.resources:
            resource_type = resource.resource_type.rstrip('s')
            resource_id = resource.resource_id
            try:
                resource_obj = list_resources(auth_context, resource_type,
                                              search=resource_id)[0][0]
            except IndexError:
                return f"{resource_type} ({resource_id}) doesn't exist", 400
            try:
                auth_context.check_perm(resource_type, 'edit_tags',
                                        resource_obj.id)
            except PolicyUnauthorizedError:
                return 'You are not authorized to perform this action', 403

            if not modify_security_tags(auth_context, tags, resource_obj):
                return 'You are not authorized to perform this action', 403

            if not op.operation or op.operation == 'add':
                add_tags_to_resource(auth_context.owner, resource_obj,
                                     tags)
            if op.operation == 'remove':
                remove_tags_from_resource(auth_context.owner, resource_obj,
                                          tags)

    return 'Tags succesfully updated', 200
