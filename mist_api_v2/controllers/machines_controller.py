import logging
import uuid

import connexion

import mist.api.machines.methods as methods

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
from mist.api.tasks import clone_machine_async
from mist.api.helpers import select_plan

from mist_api_v2 import util
from mist_api_v2.models.create_machine_request import CreateMachineRequest  # noqa: E501
from mist_api_v2.models.create_machine_response import CreateMachineResponse  # noqa: E501
from mist_api_v2.models.edit_machine_request import EditMachineRequest  # noqa: E501
from mist_api_v2.models.get_machine_response import GetMachineResponse  # noqa: E501
from mist_api_v2.models.list_machines_response import ListMachinesResponse  # noqa: E501
from mist_api_v2.models.key_machine_association import KeyMachineAssociation  # noqa: E501
from mist.api.keys.models import Key  # noqa: E501

from .base import list_resources, get_resource


def clone_machine(machine, name, run_async=True):  # noqa: E501
    """Clone machine

    Clone target machine # noqa: E501

    :param machine:
    :type machine: str
    :param name:
    :type name: str
    :param run_async:
    :type run_async: bool

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'clone', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    job = 'clone_machine'
    job_id = uuid.uuid4().hex
    if run_async:  # noqa: W606
        args = (auth_context.serialize(), machine.id, name)
        kwargs = {'job': job, 'job_id': job_id}
        clone_machine_async.send_with_options(
            args=args, kwargs=kwargs, delay=1_000)
    else:
        try:
            machine.ctl.clone(name)
        except ForbiddenError as e:
            return str(e), 403
    return 'Machine clone issued successfully'


def console(machine):  # noqa: E501
    """Open console

    Open VNC console on target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    from mist.api.methods import get_console_proxy_uri
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(
            auth_context, 'machine',
            search=f'{machine} state!=terminated',
            limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    cloud_id = machine.cloud.id
    try:
        auth_context.check_perm("cloud", "read", cloud_id)
        auth_context.check_perm("machine", "read", machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    if not machine.cloud.ctl.has_feature('console'):
        return 'Action not supported', 501
    proxy_uri, console_type, retcode, error = \
        get_console_proxy_uri(auth_context, machine)
    if retcode != 200:
        return error, retcode
    if proxy_uri is None:
        console_url = machine.cloud.ctl.compute.connection.ex_open_console(
            machine.machine_id
        )
        headers = {'Location': console_url}
    else:
        headers = {'Location': proxy_uri}
    return '', 302, headers


def create_machine(create_machine_request=None, run_async=True):  # noqa: E501
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if create_machine_request.cloud:
        cloud_search = create_machine_request.cloud
    elif create_machine_request.provider:
        cloud_search = (f'provider={create_machine_request.provider} '
                        f'enabled=True')
    else:
        cloud_search = 'enabled=True'

    clouds, total = list_resources_v1(
        auth_context, 'cloud', search=cloud_search
    )
    if not total:
        return 'Cloud not found', 404

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

    # If many clouds are found, we will attempt to generate a plan
    # for each one of them. If plans cannot be generated for some clouds,
    # these clouds will be skipped and only consider the rest. This means that
    # some errors (no permission, resource not found etc.) will be handled
    # and will never be seen by the user, something we don't want when
    # we only have a single cloud.
    one_cloud = (total == 1)
    valid_plans = []
    for cloud in clouds:
        try:
            auth_context.check_perm('cloud', 'create_resources', cloud.id)
        except PolicyUnauthorizedError as exc:
            if one_cloud:
                return exc.args[0], 403
            continue

        plan = {
            'cloud': {
                'id': cloud.id,
                'name': cloud.name,
            }
        }

        try:
            cloud.ctl.compute.generate_plan(auth_context, plan, **kwargs)
        except Exception as exc:
            if one_cloud:
                logging.warn(
                    'Failed to generate plan for cloud %s with exception %s',
                    cloud.name, repr(exc))
            else:
                logging.debug(
                    'Failed to generate plan for cloud %s with exception %s',
                    cloud.name, repr(exc))
                continue
            if isinstance(exc, NotFoundError):
                return exc.args[0], 404
            elif isinstance(exc, (BadRequestError,
                                  MachineNameValidationError)):
                return exc.args[0], 400
            elif isinstance(exc, (ForbiddenError, PolicyUnauthorizedError)):
                return exc.args[0], 403
            else:
                return 'Service Unavailable', 503

        valid_plans.append(plan.copy())

    if not valid_plans:
        return 'No valid plan could be generated', 400

    optimize = create_machine_request.optimize or 'cost'
    plan = select_plan(valid_plans, optimize, auth_context)
    if not plan:
        return f'Could not optimize for value: {optimize}', 400

    # TODO save
    # TODO template

    if create_machine_request.dry is not None:
        dry = create_machine_request.dry
    else:
        dry = False

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
        if run_async:
            multicreate_async_v2.send(
                auth_context.serialize(), plan, job_id=job_id, job=job
            )
        else:
            multicreate_async_v2(
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'destroy', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    try:
        machine.ctl.destroy()
    except ForbiddenError:
        return 'Action not supported on target machine', 422
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
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

    try:
        auth_context.check_perm('machine', 'edit', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(auth_context, 'machine', search=machine,
                              only=only,
                              deref=deref)
    except NotFoundError:
        return 'Machine does not exist', 404
    return GetMachineResponse(data=result['data'], meta=result['meta'])


def list_machines(cloud=None, search=None, sort=None, start=0, limit=100, only=None, deref='auto', at=None):  # noqa: E501
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
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListMachinesResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'machine', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'reboot', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        machine.ctl.reboot()
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    except BadRequestError as e:
        return str(e), 400
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'rename', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation
    try:
        auth_context.check_perm('machine', 'rename', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        result = machine.ctl.rename(name)
    except ForbiddenError:
        return 'Action not supported on target machine', 422
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
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
    try:
        _, constraints = auth_context.check_perm(
            'machine', 'resize', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
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
    try:
        result = machine.ctl.resize(size.id, {})
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    except BadRequestError as e:
        return str(e), 400
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'resume', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation

    try:
        auth_context.check_perm('machine', 'resume', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        result = machine.ctl.resume()
    except ForbiddenError:
        return 'Action not supported on target machine', 422
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    search = f'{machine} state=running'
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=search, limit=1)
    except ValueError:
        try:
            [machine], _ = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
            if machine.state != 'running':
                return 'Machine is not running', 400
        except ValueError:
            pass
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm("cloud", "read", machine.cloud.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        ssh_uri = prepare_ssh_uri(auth_context, machine)
    except ForbiddenError:
        return 'You are not authorized to perform this action', 403
    return 'Found', 302, {'Location': ssh_uri}


def start_machine(machine):  # noqa: E501
    """Start machine

    Start target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'start', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    try:
        machine.ctl.start()
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    return 'Started machine `%s`' % machine.name, 200


def stop_machine(machine):  # noqa: E501
    """Stop machine

    Stop target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'stop', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    try:
        machine.ctl.stop()
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    return 'Stopped machine `%s`' % machine.name, 200


def suspend_machine(machine):  # noqa: E501
    """Suspend machine

    Suspend target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    if not methods.run_pre_action_hooks(machine, 'suspend', auth_context.user):
        return 'OK', 200  # webhook requires stopping action propagation
    try:
        auth_context.check_perm('machine', 'suspend', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    try:
        result = machine.ctl.suspend()
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    methods.run_post_action_hooks(
        machine, 'suspend', auth_context.user, result)
    return 'Machine suspend issued successfully'


def undefine_machine(machine, delete_domain_image=False):  # noqa: E501
    """Undefine machine

    Undefine target machine # noqa: E501

    :param machine:
    :type machine: str

    :param delete_domain_image:
    :type machine: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(auth_context, 'machine',
                                          search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'undefine', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403

    try:
        machine.ctl.undefine(delete_domain_image=delete_domain_image)
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    except BadRequestError as e:
        return str(e), 400
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
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        key.ctl.associate(machine, username=ssh_user, port=ssh_port)
    except BadRequestError as e:
        return str(e), 400
    except (MachineUnauthorizedError, ServiceUnavailableError):
        return 'Could not connect to target machine', 503
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
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        key.ctl.disassociate(machine)
    except (MachineUnauthorizedError, ServiceUnavailableError):
        return 'Could not connect to target machine', 503
    return 'Disassociation successful', 200
