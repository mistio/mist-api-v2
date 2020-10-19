import os
import time
import logging

import connexion
import six

import mongoengine as me

from mist.api import config

from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_keys_response import ListKeysResponse  # noqa: E501
from mist_api_v2 import util


logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)


def add_key(body=None):  # noqa: E501
    """Add key

    Adds a new key and returns the key's id. ADD permission required on key. # noqa: E501

    :param body: 
    :type body: 

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def delete_key(key):  # noqa: E501
    """Delete key

    Delete target key # noqa: E501

    :param key: 
    :type key: str

    :rtype: None
    """
    return 'do some magic!'


def get_key(key):  # noqa: E501
    """Get key

    Get details about target key # noqa: E501

    :param key: 
    :type key: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [key], total = list_resources(auth_context, 'key',
                                        search=key, limit=1)
    except me.DoesNotExist:
        return 'Cloud does not exist', 404

    meta = {
        'total_matching': total,
        'total_returned': 1,
    }
    return {
        'data': key.as_dict(),
        'meta': meta
    }


def list_keys(search=None, sort=None, start=0, limit=100):  # noqa: E501
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
    keys, total = list_resources(auth_context, 'key',
                                   search=search, sort=sort, limit=limit)
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