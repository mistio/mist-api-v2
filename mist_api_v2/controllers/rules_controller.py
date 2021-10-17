import logging

import connexion

from mist.api import config
from mist.api.helpers import delete_none
from mist.api.rules.models import RULES

from mist_api_v2.models.add_rule_request import AddRuleRequest  # noqa: E501

logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)


def add_rule(add_rule_request=None):  # noqa: E501
    """Add rule

    Add a new rule, READ permission required on target resource, ADD permission required on Rule # noqa: E501

    :param add_rule_request:
    :type add_rule_request: dict | bytes

    :rtype: Rule
    """
    if connexion.request.is_json:
        add_rule_request = AddRuleRequest.from_dict(connexion.request.get_json())  # noqa: E501
    auth_context = connexion.context['token_info']['auth_context']
    kwargs = add_rule_request.to_dict()
    arbitrary = kwargs['selectors'] is None
    delete_none(kwargs)
    data_type = kwargs.pop('data_type')
    # Get the proper Rule subclass.
    rule_key = f'{"arbitrary" if arbitrary else "resource"}-{data_type}'
    rule_cls = RULES[rule_key]
    # Add new rule.
    rule = rule_cls.add(auth_context, **kwargs)
    # Advance rule counter.
    auth_context.owner.rule_counter += 1
    auth_context.owner.save()
    return rule.as_dict()


def delete_rule(rule):  # noqa: E501
    """Delete rule

    Delete a rule given its UUID. # noqa: E501

    :param rule:
    :type rule: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    from mist.api.notifications.models import Notification
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    auth_context.check_perm('rule', 'delete', rule.id)
    rule.ctl.set_auth_context(auth_context)
    rule.ctl.delete()
    Notification.objects(
        owner=auth_context.owner, rtype='rule', rid=rule.id
    ).delete()
    return 'Rule deleted succesfully', 200


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


def rename_rule(rule, name):  # noqa: E501
    """Rename rule

    Rename a rule # noqa: E501

    :param rule:
    :type rule: str
    :param name:
    :type name: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    auth_context.check_perm('rule', 'write', rule.id)
    if not auth_context.is_owner():
        return 'You are not authorized to perform this action', 403
    rule.ctl.rename(name)
    return 'Rule renamed succesfully'


def toggle_rule(rule, action):  # noqa: E501
    """Toggle rule

    Enable or disable a rule # noqa: E501

    :param rule:
    :type rule: str
    :param action:
    :type action: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    auth_context.check_perm('rule', 'write', rule.id)
    if not auth_context.is_owner():
        return 'You are not authorized to perform this action', 403
    getattr(rule.ctl, action)()
    return 'Rule toggled succesfully'


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
        window = Window.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        frequency = Frequency.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        trigger_after = TriggerAfter.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        actions = [Action.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        selectors = Selector.from_dict(connexion.request.get_json())  # noqa: E501
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
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404

    meta = {
        'total_matching': total,
        'total_returned': 1,
    }
    return {
        'data': rule.as_dict(),
        'meta': meta
    }
