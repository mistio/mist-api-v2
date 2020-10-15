import os
import time
import logging

import connexion
import six

import mongoengine as me

from mist.api import config

from mist_api_v2.models.action import Action  # noqa: E501
from mist_api_v2.models.frequency import Frequency  # noqa: E501
from mist_api_v2.models.list_rules_response import ListRulesResponse  # noqa: E501
from mist_api_v2.models.query import Query  # noqa: E501
from mist_api_v2.models.rule import Rule  # noqa: E501
from mist_api_v2.models.selector import Selector  # noqa: E501
from mist_api_v2.models.trigger_after import TriggerAfter  # noqa: E501
from mist_api_v2.models.window import Window  # noqa: E501
from mist_api_v2 import util


logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)


def add_rule(queries, window, frequency, trigger_after, actions, selectors):  # noqa: E501
    """Add rule

    Add a new rule, READ permission required on target resource, ADD permission required on Rule # noqa: E501

    :param queries: 
    :type queries: list | bytes
    :param window: 
    :type window: dict | bytes
    :param frequency: 
    :type frequency: dict | bytes
    :param trigger_after: 
    :type trigger_after: dict | bytes
    :param actions: 
    :type actions: list | bytes
    :param selectors: 
    :type selectors: dict | bytes

    :rtype: Rule
    """
    if connexion.request.is_json:
        queries = [Query.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        window =  Window.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        frequency =  Frequency.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        trigger_after =  TriggerAfter.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        actions = [Action.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        selectors =  Selector.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_rule(rule):  # noqa: E501
    """Delete rule

    Delete a rule given its UUID. # noqa: E501

    :param rule: 
    :type rule: str

    :rtype: None
    """
    return 'do some magic!'


def list_rules(search=None, sort=None, start=0, limit=100):  # noqa: E501
    """Get rules

    Return a filtered list of rules # noqa: E501

    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str

    :rtype: ListRulesResponse
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    rules, total = list_resources(auth_context, 'rule',
                                   search=search, sort=sort, limit=limit)
    meta = {
        'total_matching': total,
        'total_returned': rules.count(),
        'sort': sort,
        'start': start
    }
    return {
        'data': [c.as_dict() for c in rules],
        'meta': meta
    }


def rename_rule(rule, action):  # noqa: E501
    """Rename rule

    Rename a rule # noqa: E501

    :param rule: 
    :type rule: str
    :param action: 
    :type action: str

    :rtype: None
    """
    return 'do some magic!'


def toggle_rule(rule, action):  # noqa: E501
    """Toggle rule

    Enable or disable a rule # noqa: E501

    :param rule: 
    :type rule: str
    :param action: 
    :type action: str

    :rtype: None
    """
    return 'do some magic!'


def update_rule(rule, queries=None, window=None, frequency=None, trigger_after=None, actions=None, selectors=None):  # noqa: E501
    """Update rule

    Update a rule given its UUID, EDIT permission required on rule # noqa: E501

    :param rule: 
    :type rule: str
    :param queries: 
    :type queries: list | bytes
    :param window: 
    :type window: dict | bytes
    :param frequency: 
    :type frequency: dict | bytes
    :param trigger_after: 
    :type trigger_after: dict | bytes
    :param actions: 
    :type actions: list | bytes
    :param selectors: 
    :type selectors: dict | bytes

    :rtype: Rule
    """
    if connexion.request.is_json:
        queries = [Query.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        window =  Window.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        frequency =  Frequency.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        trigger_after =  TriggerAfter.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        actions = [Action.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        selectors =  Selector.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_rule(rule):  # noqa: E501
    """Get rule

    Get details about target rule # noqa: E501

    :param rule: 
    :type rule: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [rule], total = list_resources(auth_context, 'rule',
                                        search=rule, limit=1)
    except me.DoesNotExist:
        return 'Cloud does not exist', 404

    meta = {
        'total_matching': total,
        'total_returned': 1,
    }
    return {
        'data': rule.as_dict(),
        'meta': meta
    }
