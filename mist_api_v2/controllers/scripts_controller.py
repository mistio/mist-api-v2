import connexion
import six

import mongoengine as me

from mist.api.logs.methods import log_event

from mist_api_v2.models.get_script_response import GetScriptResponse  # noqa: E501
from mist_api_v2.models.list_scripts_response import ListScriptsResponse  # noqa: E501
from mist_api_v2 import util

from .base import list_resources, get_resource


def delete_script(script):  # noqa: E501
    """Delete script

    Delete target script # noqa: E501

    :param script: 
    :type script: str

    :rtype: None
    """
    from mist.api.scripts.models import Script

    auth_context = connexion.context["token_info"]["auth_context"]
    script_id = script
    try:
        script = Script.objects.get(
            owner=auth_context.owner, id=script_id, deleted=None
        )
    except me.DoesNotExist:
        return "Script does not exist", 404

    auth_context.check_perm("script", "remove", script.id)
    script.ctl.delete()
    log_event(
        auth_context.owner.id,
        "request",
        "delete_script",
        script_id=script.id,
        user_id=auth_context.user.id,
    )

    return "Deleted script `%s`" % script.name, 200


def edit_script(script, name=None, description=None):  # noqa: E501
    """Edit script

    Edit target script # noqa: E501

    :param script: 
    :type script: str
    :param name: New script name
    :type name: str
    :param description: New script description
    :type description: str

    :rtype: None
    """
    from mist.api.methods import list_resources

    auth_context = connexion.context["token_info"]["auth_context"]
    try:
        [script], total = list_resources(auth_context, "script", search=script, limit=1)
    except ValueError:
        return "Script does not exist", 404

    auth_context.check_perm("script", "edit", script.id)
    script.ctl.edit(name, description)
    return "Updated script `%s`" % script.name, 200


def get_script(script, only=None, deref="auto"):  # noqa: E501
    """Get script

    Get details about target script # noqa: E501

    :param script: 
    :type script: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetScriptResponse
    """
    auth_context = connexion.context["token_info"]["auth_context"]
    result = get_resource(auth_context, "script", search=script, only=only, deref=deref)
    return GetScriptResponse(data=result["data"], meta=result["meta"])


def list_scripts(
    search=None, sort=None, start=None, limit=None, only=None, deref=None
):  # noqa: E501
    """List scripts

    List scripts owned by the active org. READ permission required on script. # noqa: E501

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

    :rtype: ListScriptsResponse
    """
    auth_context = connexion.context["token_info"]["auth_context"]
    result = list_resources(
        auth_context,
        "script",
        search=search,
        only=only,
        sort=sort,
        limit=limit,
        deref=deref,
    )
    return ListScriptsResponse(data=result["data"], meta=result["meta"])
