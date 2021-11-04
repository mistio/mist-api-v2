import uuid
import connexion

import mist.api.machines.methods as methods

from pyramid.renderers import render_to_response

from mist.api.helpers import delete_none
from mist.api.clouds.models import LibvirtCloud
from mist.api.exceptions import BadRequestError
from mist.api.exceptions import NotFoundError
from mist.api.exceptions import ForbiddenError
from mist.api.exceptions import MachineNameValidationError
from mist.api.exceptions import PolicyUnauthorizedError
from mist.api.exceptions import MachineUnauthorizedError
from mist.api.exceptions import ServiceUnavailableError

from mist.api.methods import list_resources as list_resources_v1
from mist.api.tasks import multicreate_async_v2

from mist_api_v2.models.create_machine_request import CreateMachineRequest  # noqa: E501
from mist_api_v2.models.create_machine_response import CreateMachineResponse  # noqa: E501
from mist_api_v2.models.edit_machine_request import EditMachineRequest  # noqa: E501
from mist_api_v2.models.get_machine_response import GetMachineResponse  # noqa: E501
from mist_api_v2.models.list_machines_response import ListMachinesResponse  # noqa: E501
from mist_api_v2.models.key_machine_association import KeyMachineAssociation  # noqa: E501
from mist.api.keys.models import Key  # noqa: E501

from .base import list_resources, get_resource


def clone_machine(machine):  # noqa: E501
    """Clone machine

    Clone target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm('machine', 'clone', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'clone_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    machine.ctl.clone()
    return 'Cloned machine `%s`' % machine.name, 200


def console(machine):  # noqa: E501
    """Open console

    Open VNC console on target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    from mist.api.methods import get_console_proxy_uri
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [machine], total = list_resources(
            auth_context, 'machine',
            search=f'{machine} state!=terminated',
            limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    cloud_id = machine.cloud.id
    auth_context.check_perm("cloud", "read", cloud_id)
    auth_context.check_perm("machine", "read", machine.id)
    if machine.cloud.ctl.has_feature('console'):
        return 'Action not supported', 501
    proxy_uri = get_console_proxy_uri()
    if proxy_uri is None:
        console_url = machine.cloud.ctl.compute.connection.ex_open_console(
            machine.machine_id
        )
        headers = {'Location': console_url}
        return '', 302, headers
    return render_to_response('../templates/novnc.pt', {'url': proxy_uri})


def create_machine(create_machine_request=None):  # noqa: E501
    """Create machine

    Creates one or more machines on the specified cloud.
    If async is true, a jobId will be returned.
    READ permission required on cloud.
    CREATE_RESOURCES permission required on cloud.
    READ permission required on location.
    CREATE_RESOURCES permission required on location.
    CREATE permission required on machine.
    RUN permission required on script.
    READ permission required on key.

    :param create_machine_request:
    :type create_machine_request: dict | bytes

    :rtype: CreateMachineResponse
    """

    if connexion.request.is_json:
        create_machine_request = CreateMachineRequest.from_dict(connexion.request.get_json())  # noqa: E501

    auth_context = connexion.context['token_info']['auth_context']
    plan = {}

    if create_machine_request.cloud:
        cloud_search = create_machine_request.cloud
    elif create_machine_request.provider:
        cloud_search = \
            f'provider:{create_machine_request.provider} enabled:True'
    else:
        cloud_search = ''
    # TODO handle multiple clouds
    # TODO add permissions constraint to list_resources
    try:
        # TODO use list_resources
        [cloud], _ = list_resources_v1(
            auth_context, 'cloud', search=cloud_search, limit=1
        )
    except ValueError:
        return 'Cloud does not exist', 404
    try:
        auth_context.check_perm('cloud', 'create_resources', cloud.id)
    except PolicyUnauthorizedError as exc:
        return exc.args[0], 403

    plan['cloud'] = {'id': cloud.id, 'name': cloud.name}

    kwargs = {
        'name': create_machine_request.name,
        'image': create_machine_request.image or {},
        'location': create_machine_request.location or '',
        'size': create_machine_request.size or {},
        'key': create_machine_request.key or {},
        'networks': create_machine_request.net or {},
        'volumes': create_machine_request.volumes or [],
        'disks': create_machine_request.disks or {},
        'extra': create_machine_request.extra or {},
        'scripts': create_machine_request.scripts or [],
        'schedules': create_machine_request.schedules or [],
        'cloudinit': create_machine_request.cloudinit or '',
        'fqdn': create_machine_request.fqdn or '',
        'monitoring': create_machine_request.monitoring,
        'request_tags': create_machine_request.tags or {},
        'expiration': create_machine_request.expiration,
        'quantity': create_machine_request.quantity or 1
    }

    try:
        cloud.ctl.compute.generate_plan(auth_context, plan, **kwargs)
    except NotFoundError as exc:
        return exc.args[0], 404
    except (BadRequestError,
            PolicyUnauthorizedError,
            MachineNameValidationError) as exc:
        return exc.args[0], 400
    except ForbiddenError as err:
        return err.args[0], 403
    # TODO save
    # TODO template

    if create_machine_request.dry is not None:
        dry = create_machine_request.dry
    else:
        dry = True

    # sensitive fields that shouldn't be returned in plan
    sensitive_fields = ['root_pass', ]
    user_plan = {key: plan[key] for key in plan
                 if key not in sensitive_fields}

    if dry:
        return CreateMachineResponse(plan=user_plan)
    else:
        # TODO job,job_id could also be passed as parameter
        job_id = uuid.uuid4().hex
        job = 'create_machine'
        # TODO add countdown=2
        multicreate_async_v2.send(
            auth_context.serialize(), plan, job_id=job_id, job=job
        )
        return CreateMachineResponse(plan=user_plan, job_id=job_id)


def destroy_machine(machine):  # noqa: E501
    """Destroy machine

    Destroy target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm('machine', 'destroy', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'destroy_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    machine.ctl.destroy()
    return 'Destroyed machine `%s`' % machine.name, 200


def edit_machine(machine, edit_machine_request=None):  # noqa: E501
    """Edit machine

    Edit target machine # noqa: E501

    :param machine:
    :type machine: str
    :param edit_machine_request:
    :type edit_machine_request: dict | bytes

    :rtype: None
    """
    from mist.api.methods import list_resources
    if connexion.request.is_json:
        edit_machine_request = EditMachineRequest.from_dict(connexion.request.get_json())  # noqa: E501
    params = delete_none(edit_machine_request.to_dict())
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if machine.cloud.owner != auth_context.owner:
        return 'Machine does not exist', 404
    # VMs in libvirt can be started no matter if they are terminated
    if machine.state == 'terminated' and not isinstance(machine.cloud,
                                                        LibvirtCloud):
        return 'Machine does not exist', 404
    log_event(
        auth_context.owner.id, 'request', 'edit_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    auth_context.check_perm('machine', 'edit', machine.id)
    machine.ctl.update(auth_context, params)
    return 'Machine successfully updated'


def get_machine(machine, only=None, deref=None):  # noqa: E501
    """Get machine

    Get details about target machine # noqa: E501

    :param machine:
    :type machine: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetMachineResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = get_resource(auth_context, 'machine', search=machine, only=only,
                          deref=deref)

    return GetMachineResponse(data=result['data'], meta=result['meta'])


def list_machines(cloud=None, search=None, sort=None, start=0, limit=100, only=None, deref='auto'):  # noqa: E501
    """List machines

    List machines owned by the active org. READ permission required on machine &amp; cloud. # noqa: E501

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

    :rtype: ListMachinesResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    result = list_resources(
        auth_context, 'machine', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref
    )
    return ListMachinesResponse(data=result['data'], meta=result['meta'])


def reboot_machine(machine):  # noqa: E501
    """Reboot machine

    Reboot target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm('machine', 'reboot', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'reboot_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    machine.ctl.reboot()
    return 'Rebooted machine `%s`' % machine.name, 200


def rename_machine(machine, name):  # noqa: E501
    """Rename machine

    Rename target machine # noqa: E501

    :param machine:
    :type machine: str
    :param name: New machine name
    :type name: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'rename', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation
    log_event(
        auth_context.owner.id, 'request', 'rename_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    auth_context.check_perm('machine', 'rename', machine.id)
    result = machine.ctl.rename(name)
    methods.run_post_action_hooks(machine, 'rename', auth_context.user, result)
    return 'Machine renamed successfully'


def resize_machine(machine, size):  # noqa: E501
    """Resize machine

    Resize target machine # noqa: E501

    :param machine:
    :type machine: str
    :param size:
    :type size: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'resize', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation
    try:
        [size], total = list_resources(auth_context, 'size',
                                       cloud=machine.cloud.id,
                                       search=size, limit=1)
    except ValueError:
        return 'Size does not exist', 404
    _, constraints = auth_context.check_perm(
        'machine', 'resize', machine.id)
    # check cost constraint
    cost_constraint = constraints.get('cost', {})
    if cost_constraint:
        try:
            from mist.rbac.methods import check_cost
            check_cost(auth_context.org, cost_constraint)
        except ImportError:
            pass
    # check size constraint
    size_constraint = constraints.get('size', {})
    if size_constraint:
        try:
            from mist.rbac.methods import check_size
            check_size(machine.cloud.id, size_constraint, size)
        except ImportError:
            pass
    log_event(
        auth_context.owner.id, 'request', 'resize_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    result = machine.ctl.resize(size.id, {})
    methods.run_post_action_hooks(machine, 'resize', auth_context.user, result)
    return 'Machine resize issued successfully'


def resume_machine(machine):  # noqa: E501
    """Resume machine

    Resume target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'resume', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation
    log_event(
        auth_context.owner.id, 'request', 'resume_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    auth_context.check_perm('machine', 'resume', machine.id)
    result = machine.ctl.resume()
    methods.run_post_action_hooks(machine, 'resume', auth_context.user, result)
    return 'Machine resume issued successfully'


def ssh(machine):  # noqa: E501
    """Open secure shell

    Open secure shell on target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    from mist.api.machines.methods import prepare_ssh_uri
    auth_context = connexion.context['token_info']['auth_context']
    search = f'{machine} state=running'
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=search, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm("cloud", "read", machine.cloud.id)

    ssh_uri = prepare_ssh_uri(auth_context, machine)

    return 'Found', 302, {'Location': ssh_uri}


def start_machine(machine):  # noqa: E501
    """Start machine

    Start target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm('machine', 'start', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'start_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    machine.ctl.start()
    return 'Started machine `%s`' % machine.name, 200


def stop_machine(machine):  # noqa: E501
    """Stop machine

    Stop target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm('machine', 'stop', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'stop_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    machine.ctl.stop()
    return 'Stopped machine `%s`' % machine.name, 200


def suspend_machine(machine):  # noqa: E501
    """Suspend machine

    Suspend target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'suspend', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation
    auth_context.check_perm('machine', 'suspend', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'suspend_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    result = machine.ctl.suspend()
    methods.run_post_action_hooks(
        machine, 'suspend', auth_context.user, result)
    return 'Machine suspend issued successfully'


def undefine_machine(machine):  # noqa: E501
    """Undefine machine

    Undefine target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404

    auth_context.check_perm('machine', 'undefine', machine.id)
    log_event(
        auth_context.owner.id, 'request', 'undefine_machine',
        machine_id=machine.id, user_id=auth_context.user.id,
    )
    machine.ctl.undefine()
    return 'Undefined machine `%s`' % machine.name, 200


def associate_key(machine, key_machine_association=None):  # noqa: E501
    """Associate a key with a machine

    Associate a key with a machine. # noqa: E501

    :param machine:
    :type machine: str
    :param key_machine_association:
    :type key_machine_association: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        key_machine_association = KeyMachineAssociation.from_dict(connexion.request.get_json())  # noqa: E501
    ssh_user = key_machine_association.user or 'root'
    ssh_port = key_machine_association.port or 22
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except Exception:
        return 'Authentication failed', 401
    try:
        [machine], _ = list_resources(auth_context, 'machine',
                                      search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        [key], _ = list_resources(auth_context, 'key',
                                  search=key_machine_association.key, limit=1)
    except Key.DoesNotExist:
        return 'Key id does not exist', 404
    try:
        auth_context.check_perm('machine', 'associate_key', machine.id)
        auth_context.check_perm('cloud', 'read', machine.cloud.id)
        auth_context.check_perm('key', 'read', key.id)
    except Exception:
        return 'You are not authorized to perform this action', 403
    try:
        key.ctl.associate(machine, username=ssh_user, port=ssh_port)
    except (MachineUnauthorizedError, ServiceUnavailableError):
        return 'Could not connect to target machine', 503
    except Exception:
        return 'Action not supported on target machine', 422
    return 'Association successful', 200


def disassociate_key(machine, key_machine_association=None):  # noqa: E501
    """Associate a key with a machine

    Disassociate a key from a machine. # noqa: E501

    :param machine:
    :type machine: str
    :param key_machine_association:
    :type key_machine_association: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        key_machine_association = KeyMachineAssociation.from_dict(connexion.request.get_json())  # noqa: E501
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except Exception:
        return 'Authentication failed', 401
    try:
        [machine], _ = list_resources(auth_context, 'machine',
                                      search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        [key], _ = list_resources(auth_context, 'key',
                                  search=key_machine_association.key, limit=1)
    except Key.DoesNotExist:
        return 'Key id does not exist', 404
    try:
        auth_context.check_perm("machine", "disassociate_key", machine.id)
        auth_context.check_perm("cloud", "read", machine.cloud.id)
    except Exception:
        return 'You are not authorized to perform this action', 403
    try:
        key.ctl.disassociate(machine)
    except (MachineUnauthorizedError, ServiceUnavailableError):
        return 'Could not connect to target machine', 503
    return 'Disassociation successful', 200
