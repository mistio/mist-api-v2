import connexion
import six

from mist_api_v2.models.list_snapshots_response import (
    ListSnapshotsResponse,
)  # noqa: E501
from mist_api_v2 import util


def create_snapshot(machine):  # noqa: E501
    """Create snapshot

    Create snapshots of target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: object
    """
    return "do some magic!"


def list_snapshots(machine):  # noqa: E501
    """Suspend machine

    List snapshots of target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: ListSnapshotsResponse
    """
    return "do some magic!"


def remove_snapshot(machine, snapshot):  # noqa: E501
    """Remove snapshot

    Remove target machine snapshot # noqa: E501

    :param machine:
    :type machine: str
    :param snapshot:
    :type snapshot: str

    :rtype: None
    """
    return "do some magic!"


def revert_to_snapshot(machine, snapshot):  # noqa: E501
    """Revert to snapshot

    Revert machine to snapshot # noqa: E501

    :param machine:
    :type machine: str
    :param snapshot:
    :type snapshot: str

    :rtype: None
    """
    return "do some magic!"
