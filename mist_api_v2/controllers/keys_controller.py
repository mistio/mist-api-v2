import os
import time
import logging

import connexion
import six

import mongoengine as me

from mist.api import config
from mist.api.logs.methods import log_event

from mist_api_v2.models.add_key_request import AddKeyRequest  # noqa: E501
from mist_api_v2.models.add_key_response import AddKeyResponse  # noqa: E501
from mist_api_v2.models.get_key_response import GetKeyResponse  # noqa: E501
from mist_api_v2.models.list_keys_response import ListKeysResponse  # noqa: E501

from mist_api_v2 import util


logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)


def add_key(add_key_request=None):  # noqa: E501
    """Add key

    Adds a new key and returns the key's id. ADD permission required on key. # noqa: E501

    :param add_key_request:
    :type add_key_request: dict | bytes

    :rtype: AddKeyResponse
    """
    if connexion.request.is_json:
        add_key_request = AddKeyRequest.from_dict(connexion.request.get_json())  # noqa: E501

    from mist.api.exceptions import BadRequestError, KeyExistsError
    from mist.api.keys.models import SignedSSHKey, SSHKey, Key
    from mist.api.tag.methods import add_tags_to_resource

    auth_context = connexion.context['token_info']['auth_context']
    key_tags, _ = auth_context.check_perm("key", "add", None)

    if add_key_request.generate:
        key = SSHKey()
        key.ctl.generate()
        if add_key_request.dry:  # If dry generate requested then we're done
            log_event(
                auth_context.owner.id, 'request', 'generate_key',
                key_id=key.id, user_id=auth_context.user.id,
            )
            return AddKeyResponse(private=key.private, public=key.public)

        add_key_request.private = key.private

    try:
        if add_key_request.certificate:
            key = SignedSSHKey.add(
                auth_context.owner,
                add_key_request.name,
                private=add_key_request.private,
                certificate=add_key_request.certificate
            )
        else:
            key = SSHKey.add(
                auth_context.owner,
                add_key_request.name,
                private=add_key_request.private
            )
    except BadRequestError as exc:
        return exc.args[0], 400
    except KeyExistsError as exc:
        return exc.args[0], 409
    # Set ownership.
    key.assign_to(auth_context.user)

    # Add tags returned by RBAC check
    if key_tags:
        add_tags_to_resource(auth_context.owner, key, list(key_tags.items()))

    log_event(
        auth_context.owner.id, 'request', 'add_key',
        key_id=key.id, user_id=auth_context.user.id,
    )
    return AddKeyResponse(key.id)


def delete_key(key):  # noqa: E501
    """Delete key

    Delete target key # noqa: E501

    :param key: 
    :type key: str

    :rtype: None
    """
    from mist.api.keys.models import Key
    from mist.api.keys.methods import delete_key as m_delete_key

    auth_context = connexion.context['token_info']['auth_context']
    key_id = key
    try:
        key = Key.objects.get(owner=auth_context.owner, id=key_id,
                              deleted=None)
    except me.DoesNotExist:
        return 'Key does not exist', 404

    auth_context.check_perm('key', 'remove', key.id)
    m_delete_key(auth_context.owner, key_id)
    log_event(
        auth_context.owner.id, 'request', 'generate_key',
        key_id=key.id, user_id=auth_context.user.id,
    )

    return 'Deleted key `%s`' % key.name, 200


def edit_key(key, name=None, default=None):  # noqa: E501
    """Edit key

    Edit target key # noqa: E501

    :param key:
    :type key: str
    :param name: New key name
    :type name: str
    :param default: Set as default
    :type default: bool

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [key], total = list_resources(auth_context, 'key',
                                      search=key, limit=1)
    except ValueError:
        return 'Key does not exist', 404

    auth_context.check_perm('key', 'edit', key.id)
    log_event(
        auth_context.owner.id, 'request', 'edit_key',
        key_id=key.id, user_id=auth_context.user.id,
        key_name=key.name, key_default=key.default,
        new_name=name, new_default=default
    )
    if name:
        key.name = name
    if default:
        key.ctl.set_default()
    return 'Updated key `%s`' % key.name, 200


def get_key(key, private=False):  # noqa: E501
    """Get key

    Get details about target key # noqa: E501

    :param key: 
    :type key: str
    :param read_private:
    :type key: bool

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    from mist.api.logs.methods import log_event
    try:
        [key], total = list_resources(auth_context, 'key',
                                      search=key, limit=1)
    except ValueError:
        return 'Key does not exist', 404

    meta = {
        'total_matching': total,
        'total_returned': 1,
    }

    response = {
        'data': key.as_dict(),
        'meta': meta
    }

    if private:
        auth_context.check_perm('key', 'read_private', key.id)
        log_event(
            auth_context.owner.id, 'request', 'read_private',
            key_id=key.id, user_id=auth_context.user.id,
        )
        response['data']['private'] = key.private
    return response


def list_keys(search=None, sort=None, start=0, limit=100, only=None):  # noqa: E501
    """List keys

    List keys owned by the active org. READ permission required on key. # noqa: E501

    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int

    :rtype: ListKeysResponse
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    keys, total = list_resources(auth_context, 'key', search=search,
                                 only=only, sort=sort, limit=limit)
    meta = {
        'total_matching': total,
        'total_returned': keys.count(),
        'sort': sort,
        'start': start
    }

    return {
        'data': [c.as_dict() for c in keys],
        'meta': meta
    }