import logging
import connexion
import mongoengine as me

from mist.api.helpers import get_resource_model
from mist.api.tag.methods import get_tags
from mist.api.tag.methods import add_tags_to_resource
from mist.api.tag.methods import remove_tags_from_resource
from mist.api.tag.methods import modify_security_tags
from mist.api.exceptions import PolicyUnauthorizedError

from mist_api_v2.models.list_tags_response import ListTagsResponse  # noqa: E501
from mist_api_v2.models.tag_resources_request import TagResourcesRequest  # noqa: E501

log = logging.getLogger(__name__)


def list_tags(verbose=None, resource=None, search='', sort='key', start=0, limit=100, only='', deref=None):  # noqa: E501
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

    data, meta = get_tags(auth_context, verbose=verbose, resource=resource,
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

    for resource in tag_resources_request.resources:
        resource_type = resource.resource_type
        resource_id = resource.resource_id
        resource_tags = resource.tag

        try:
            resource_model = get_resource_model(resource_type)
        except KeyError:
            continue
        try:
            resource_obj = resource_model.objects.get(
                owner=auth_context.owner, id=resource_id)
        except me.DoesNotExist:
            log.error('%s with id %s does not exist', resource_type,
                      resource_id)
            continue
        try:
            auth_context.check_perm(resource_type, 'edit_tags',
                                    resource_obj.id)
        except PolicyUnauthorizedError:
            return 'You are not authorized to perform this action', 403

        # split the tags into two lists: those that will be added
        # and those that will be removed
        tags_to_add = [(tag.key, tag.value) for tag in [
            tag for tag in resource_tags if (tag.op or '+') == '+']]
        # also extract the keys from all the tags to be deleted
        tags_to_remove = [tag.key for tag in [
            tag for tag in resource_tags if (tag.op or '+') == '-']]

        if not modify_security_tags(auth_context, tags_to_add, resource_obj):
            auth_context._raise(resource_type, 'edit_security_tags')

        if tags_to_add:
            add_tags_to_resource(auth_context.owner, resource_obj,
                                 tags_to_add)
        if tags_to_remove:
            remove_tags_from_resource(auth_context.owner, resource_obj,
                                      tags_to_remove)

    return 'Tags succesfully updated', 200
