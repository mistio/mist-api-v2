import connexion

from mist.api.exceptions import BadRequestError
from mist.api.exceptions import ForbiddenError
from mist.api.exceptions import PolicyUnauthorizedError

import mist.api.machines.methods as methods


def create_snapshot(machine, name):  # noqa: E501
    """Create snapshot

    Create snapshots of target machine # noqa: E501

    :param machine:
    :type machine: str
    :param name:
    :type name: str

    :rtype: object
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(
            auth_context, 'machine', search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'read', machine.id)
        auth_context.check_perm('machine', 'list_snapshots', machine.id)
        auth_context.check_perm('machine', 'create_snapshots', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        result = machine.ctl.create_snapshot(name)
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    except BadRequestError as e:
        return str(e), 400
    methods.run_post_action_hooks(
        machine, 'create_snapshot', auth_context.user, result)
    return {'name': name}


def list_snapshots(machine):  # noqa: E501
    """List snapshots

    List snapshots of target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: ListSnapshotsResponse
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(
            auth_context, 'machine', search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'read', machine.id)
        auth_context.check_perm('machine', 'list_snapshots', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    return machine.ctl.list_snapshots()


def remove_snapshot(machine, snapshot):  # noqa: E501
    """Remove snapshot

    Remove target machine snapshot # noqa: E501

    :param machine:
    :type machine: str
    :param snapshot:
    :type snapshot: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(
            auth_context, 'machine', search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'read', machine.id)
        auth_context.check_perm('machine', 'list_snapshots', machine.id)
        auth_context.check_perm('machine', 'create_snapshots', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        result = machine.ctl.remove_snapshot(snapshot)
    except ForbiddenError:
        return 'Action not supported on target machine', 422
    except BadRequestError as e:
        return str(e), 400
    methods.run_post_action_hooks(
        machine, 'remove_snapshot', auth_context.user, result)
    return 'Snapshot removed successfully'


def revert_to_snapshot(machine, snapshot):  # noqa: E501
    """Revert to snapshot

    Revert machine to snapshot # noqa: E501

    :param machine:
    :type machine: str
    :param snapshot:
    :type snapshot: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [machine], total = list_resources(
            auth_context, 'machine', search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    try:
        auth_context.check_perm('machine', 'read', machine.id)
        auth_context.check_perm('machine', 'list_snapshots', machine.id)
        auth_context.check_perm('machine', 'revert_to_snapshots', machine.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    try:
        result = machine.ctl.revert_to_snapshot(snapshot)
    except BadRequestError as e:
        return str(e), 400
    methods.run_post_action_hooks(
        machine, 'revert_to_snapshot', auth_context.user, result)
    return 'Revert machine to snapshot issued successfully'
