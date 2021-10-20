import connexion


def create_snapshot(machine):  # noqa: E501
    """Create snapshot

    Create snapshots of target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: object
    """
    return 'do some magic!'


def list_snapshots(machine):  # noqa: E501
    """List snapshots

    List snapshots of target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: ListSnapshotsResponse
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [machine], total = list_resources(
            auth_context, 'machine', search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    auth_context.check_perm('machine', 'read', machine.id)
    auth_context.check_perm('machine', 'list_snapshots', machine.id)
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
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [machine], total = list_resources(
            auth_context, 'machine', search=machine, limit=1)
    except ValueError:
        return 'Machine does not exist', 404
    auth_context.check_perm('machine', 'read', machine.id)
    auth_context.check_perm('machine', 'list_snapshots', machine.id)
    auth_context.check_perm('machine', 'create_snapshots', machine.id)
    machine.ctl.remove_snapshot()
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
    return 'do some magic!'
