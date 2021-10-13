import json
import uuid
import connexion

from mist.api import tasks

from mist.api.logs.methods import log_event
from mist.api.scripts.models import ExecutableScript
from mist.api.scripts.models import AnsibleScript
from mist.api.exceptions import BadRequestError
from mist.api.exceptions import ScriptNameExistsError
from mist.api.exceptions import ForbiddenError
from mist.api.tag.methods import add_tags_to_resource
from mist.api.tasks import async_session_update
from mist.api.machines.models import Machine
from mist.api.helpers import mac_verify

from mist_api_v2.controllers.security_controller_ import info_from_ApiKeyAuth
from mist_api_v2.controllers.security_controller_ import info_from_CookieAuth
from mist_api_v2.models.add_script_request import AddScriptRequest  # noqa: E501
from mist_api_v2.models.get_script_response import GetScriptResponse  # noqa: E501
from mist_api_v2.models.list_scripts_response import ListScriptsResponse  # noqa: E501
from mist_api_v2.models.run_script_request import RunScriptRequest

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
    api_key = connexion.request.headers.get('Authorization')
    session_id = connexion.request.cookies.get('session.id')
    if api_key:
        auth_info = info_from_ApiKeyAuth(api_key, None)
    elif session_id:
        auth_info = info_from_CookieAuth(session_id, None)
    else:
        auth_info = None
    if auth_info is None:
        auth_context = None
    else:
        auth_context = auth_info['auth_context']
    from mist.api.scripts.models import Script
    if auth_context is None:
        params = dict(connexion.request.args)
        try:
            mac_verify(params)
        except Exception as exc:
            raise ForbiddenError(exc.args)
        script_id = params['object_id']
        script = Script.objects.get(id=script_id, deleted=None)
    else:
        result = get_resource(auth_context, 'script', search=script)
        result_data = result.get('data')
        if not result_data:
            return 'Script does not exist', 404
        script_id = result_data.get('id')
        script = Script.objects.get(owner=auth_context.owner,
                                    id=script_id, deleted=None)
        auth_context.check_perm('script', 'read', script_id)
    return script.ctl.get_file()


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
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'script', search=script)
    result_data = result.get('data')
    if not result_data:
        return 'Script does not exist', 404
    from mist.api.scripts.models import Script
    script_id = result_data.get('id')
    script = Script.objects.get(owner=auth_context.owner,
                                id=script_id, deleted=None)
    return script.ctl.generate_signed_url_v2()


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


def run_script(script, run_script_request=None):  # noqa: E501
    """Run script

    Start a script job to run the script. # noqa: E501

    :param script:
    :type script: str
    :param run_script_request:
    :type run_script_request: dict | bytes

    :rtype: RunScriptResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    if connexion.request.is_json:
        run_script_request = RunScriptRequest.from_dict(connexion.request.get_json())  # noqa: E501
    result = get_resource(auth_context, 'script', search=script)
    result_data = result.get('data')
    if not result_data:
        return 'Script does not exist', 404
    from mist.api.scripts.models import Script
    script_id = result_data.get('id')
    script = Script.objects.get(owner=auth_context.owner,
                                id=script_id, deleted=None)
    params = run_script_request.to_dict()
    script_params = params.get('params', '')
    su = (params.get('su') or '').lower() == 'true'
    env = params.get('env')
    job_id = params.get('job_id')
    if not job_id:
        job = 'run_script'
        job_id = uuid.uuid4().hex
    else:
        job = None
    if isinstance(env, dict):
        env = json.dumps(env)
    machine = params.get('machine')
    result = get_resource(auth_context, 'machine', search=machine)
    result_data = result.get('data')
    if not result_data:
        return f"Machine {machine} doesn't exist", 404
    machine_id = result_data.get('id')
    machine = Machine.objects.get(id=machine_id,
                                  state__ne='terminated')
    cloud_id = machine.cloud.id
    auth_context.check_perm("cloud", "read", cloud_id)
    auth_context.check_perm("machine", "run_script", machine.id)
    auth_context.check_perm('script', 'run', script_id)
    job_id = job_id or uuid.uuid4().hex
    tasks.run_script.send_with_options(
        args=(auth_context.serialize(), script.id, machine.id),
        kwargs={
            "params": script_params,
            "env": env,
            "su": su,
            "job_id": job_id,
            "job": job
        },
        delay=1_000
    )
    return {'job_id': job_id, 'job': job}
