import json
import uuid
import connexion

from mist.api import tasks

from mist.api.scripts.models import ExecutableScript
from mist.api.scripts.models import AnsibleScript
from mist.api.exceptions import BadRequestError, NotFoundError
from mist.api.exceptions import ScriptNameExistsError
from mist.api.exceptions import PolicyUnauthorizedError
from mist.api.tag.methods import add_tags_to_resource
from mist.api.tasks import async_session_update
from mist.api.machines.models import Machine
from mist.api.helpers import mac_verify

from mist_api_v2 import util
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        script_tags, _ = auth_context.check_perm("script", "add", None)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
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
        return "Param 'exec_type' must be in ('executable', 'ansible').", 400
    try:
        script = script_cls.add(auth_context.owner, name, **kwargs)
    except BadRequestError as e:
        return str(e), 400
    except ScriptNameExistsError as e:
        return str(e), 409
    # Set ownership.
    script.assign_to(auth_context.user)
    if script_tags:
        add_tags_to_resource(auth_context.owner,
                             [{'resource_type': 'script',
                               'resource_id': script.id}],
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(auth_context, 'script', search=script)
    except NotFoundError:
        return 'Script does not exist', 404
    result_data = result.get('data')
    from mist.api.scripts.models import Script
    script_id = result_data.get('id')
    try:
        auth_context.check_perm('script', 'remove', script_id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    script = Script.objects.get(owner=auth_context.owner, id=script_id,
                                deleted=None)
    script.ctl.delete()
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
        except ValueError as e:
            return str(e), 400
        script_id = params['object_id']
        script = Script.objects.get(id=script_id, deleted=None)
    else:
        try:
            result = get_resource(auth_context, 'script', search=script)
        except NotFoundError:
            return 'Script does not exist', 404
        result_data = result.get('data')
        script_id = result_data.get('id')
        script = Script.objects.get(owner=auth_context.owner,
                                    id=script_id, deleted=None)
        try:
            auth_context.check_perm('script', 'read', script_id)
        except PolicyUnauthorizedError:
            return 'You are not authorized to perform this action', 403
    try:
        file_kwargs = script.ctl.get_file()
    except BadRequestError as e:
        return str(e), 400
    return file_kwargs['body']


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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [script], total = list_resources(auth_context, 'script',
                                         search=script, limit=1)
    except ValueError:
        return 'Script does not exist', 404
    try:
        auth_context.check_perm('script', 'edit', script.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    script.ctl.edit(name, description)
    return 'Updated script `%s`' % script.name, 200


def generate_script_url(script):  # noqa: E501
    """Generate script url

    Generate url for fetching script file # noqa: E501

    :param script:
    :type script: str

    :rtype: InlineResponse2001
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(auth_context, 'script', search=script)
    except NotFoundError:
        return 'Script does not exist', 404
    result_data = result.get('data')
    from mist.api.scripts.models import Script
    script_id = result_data.get('id')
    script = Script.objects.get(owner=auth_context.owner,
                                id=script_id, deleted=None)
    try:
        return script.ctl.generate_signed_url_v2()
    except ValueError as e:
        return str(e), 400


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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(auth_context, 'script',
                              search=script, only=only, deref=deref)
    except NotFoundError:
        return 'Script does not exist', 404
    return GetScriptResponse(data=result['data'], meta=result['meta'])


def list_scripts(search=None, sort=None, start=None, limit=None, only=None, deref=None, at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListScriptsResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(auth_context, 'script', search=search,
                            only=only, sort=sort, limit=limit,
                            deref=deref, at=at)
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if connexion.request.is_json:
        run_script_request = RunScriptRequest.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        result = get_resource(auth_context, 'script', search=script)
    except NotFoundError:
        return 'Script does not exist', 404
    result_data = result.get('data')
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
    try:
        result = get_resource(auth_context, 'machine', search=machine)
    except NotFoundError:
        return "Machine does not exist", 404

    result_data = result.get('data')
    machine_id = result_data.get('id')
    machine = Machine.objects.get(id=machine_id,
                                  state__ne='terminated')
    cloud_id = machine.cloud.id
    try:
        auth_context.check_perm("cloud", "read", cloud_id)
        auth_context.check_perm("machine", "run_script", machine.id)
        auth_context.check_perm('script', 'run', script_id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
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
