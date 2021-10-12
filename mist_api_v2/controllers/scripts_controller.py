import connexion

from mist.api.logs.methods import log_event
from mist.api.scripts.models import ExecutableScript
from mist.api.scripts.models import AnsibleScript
from mist.api.exceptions import BadRequestError
from mist.api.exceptions import ScriptNameExistsError
from mist.api.tag.methods import add_tags_to_resource
from mist.api.tasks import async_session_update

from mist_api_v2.models.add_script_request import AddScriptRequest  # noqa: E501
from mist_api_v2.models.get_script_response import GetScriptResponse  # noqa: E501
from mist_api_v2.models.list_scripts_response import ListScriptsResponse  # noqa: E501

from .base import list_resources, get_resource


def add_script(add_script_request=None):  # noqa: E501
    """Add script

    Add script to user scripts # noqa: E501

    :param add_script_request:
    :type add_script_request: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        add_script_request = AddScriptRequest.from_dict(connexion.request.get_json())  # noqa: E501
    params = add_script_request.to_dict()
    auth_context = connexion.context['token_info']['auth_context']
    script_tags, _ = auth_context.check_perm("script", "add", None)
    kwargs = {}
    for key in params:
        if key is None:
            kwargs[key] = {}
        else:
            kwargs[key] = params[key]
    name = kwargs.pop('name')
    exec_type = kwargs.pop('exec_type')
    if exec_type == 'executable':
        script_cls = ExecutableScript
    elif exec_type == 'ansible':
        script_cls = AnsibleScript
    else:
        raise BadRequestError(
            "Param 'exec_type' must be in ('executable', 'ansible')."
        )
    try:
        script = script_cls.add(auth_context.owner, name, **kwargs)
    except ScriptNameExistsError as e:
        return str(e), 409
    # Set ownership.
    script.assign_to(auth_context.user)
    if script_tags:
        add_tags_to_resource(auth_context.owner, script,
                             list(script_tags.items()))
    script = script.as_dict()
    if 'job_id' in params:
        script['job_id'] = params['job_id']
    async_session_update.send(auth_context.owner.id, ['scripts'])
    return script, 200


def delete_script(script):  # noqa: E501
    """Delete script

    Delete target script # noqa: E501

    :param script:
    :type script: str

    :rtype: None
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'script', search=script)
    result_data = result.get('data')
    if not result_data:
        return 'Script does not exist', 404
    from mist.api.scripts.models import Script
    script_id = result_data.get('id')
    auth_context.check_perm('script', 'remove', script_id)
    script = Script.objects.get(owner=auth_context.owner, id=script_id,
                                deleted=None)
    script.ctl.delete()
    log_event(
        auth_context.owner.id, 'request', 'delete_script',
        script_id=script_id, user_id=auth_context.user.id,
    )
    return 'Deleted script `%s`' % script.name, 200


def download_script(script):  # noqa: E501
    """Download script

    Download script file or archive # noqa: E501

    :param script:
    :type script: str

    :rtype: file
    """
    return 'do some magic!'


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
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [script], total = list_resources(auth_context, 'script',
                                         search=script, limit=1)
    except ValueError:
        return 'Script does not exist', 404

    auth_context.check_perm('script', 'edit', script.id)
    script.ctl.edit(name, description)
    return 'Updated script `%s`' % script.name, 200


def generate_script_url(script):  # noqa: E501
    """Generate script url

    Generate url for fetching script file # noqa: E501

    :param script:
    :type script: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def get_script(script, only=None, deref='auto'):  # noqa: E501
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
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'script',
                          search=script, only=only, deref=deref)
    return GetScriptResponse(data=result['data'], meta=result['meta'])


def list_scripts(search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
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
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(auth_context, 'script', search=search,
                            only=only, sort=sort, limit=limit,
                            deref=deref)
    return ListScriptsResponse(data=result['data'], meta=result['meta'])
