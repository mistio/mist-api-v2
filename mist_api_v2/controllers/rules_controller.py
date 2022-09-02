import logging

import connexion

from mongoengine import ValidationError

from mist.api import config
from mist.api.helpers import delete_none
from mist.api.rules.models import RULES

from mist.api.exceptions import BadRequestError
from mist.api.exceptions import PolicyUnauthorizedError

from mist_api_v2 import util
from mist_api_v2.models.add_rule_request import AddRuleRequest  # noqa: E501
from mist_api_v2.models.edit_rule_request import EditRuleRequest  # noqa: E501

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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        auth_context.check_perm('rule', 'add', None)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    kwargs = add_rule_request.to_dict()
    arbitrary = kwargs['selectors'] is None
    delete_none(kwargs)
    if len(kwargs.get('conditions')) > 1:
        raise NotImplementedError()
    data_type = kwargs.get('conditions')[0].pop('data_type')
    queries = kwargs.get('conditions')[0].pop('query')
    window = kwargs.get('conditions')[0].pop('window')
    kwargs.pop('conditions')
    kwargs['queries'] = [queries]
    kwargs['window'] = window
    schedule_type = kwargs.get('when').pop('schedule_type')
    if schedule_type != 'interval':
        raise BadRequestError('Invalid schedule type')
    # Get the proper Rule subclass.
    rule_key = f'{"arbitrary" if arbitrary else "resource"}-{data_type}'
    rule_cls = RULES[rule_key]
    # Add new rule.
    try:
        rule = rule_cls.add(auth_context, **kwargs)
    except BadRequestError as e:
        return str(e), 400
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    try:
        auth_context.check_perm('rule', 'delete', rule.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    rule.ctl.set_auth_context(auth_context)
    rule.ctl.delete()
    Notification.objects(
        owner=auth_context.owner, rtype='rule', rid=rule.id
    ).delete()
    return 'Rule deleted succesfully', 200


def edit_rule(rule, edit_rule_request=None):  # noqa: E501
    """Update rule

    Edit a rule given its UUID, EDIT permission required on rule # noqa: E501

    :param rule:
    :type rule: str
    :param edit_rule_request:
    :type edit_rule_request: dict | bytes

    :rtype: Rule
    """
    from mist.api.methods import list_resources
    from mist.api.notifications.models import Notification
    if connexion.request.is_json:
        edit_rule_request = EditRuleRequest.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    try:
        auth_context.check_perm('rule', 'edit', rule.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    rule.ctl.set_auth_context(auth_context)
    kwargs = delete_none(edit_rule_request.to_dict())
    if kwargs.get('conditions', []):
        data_type = kwargs.get('conditions')[0].pop('data_type')
        queries = kwargs.get('conditions')[0].pop('query')
        window = kwargs.get('conditions')[0].pop('window')
        kwargs.pop('conditions')
        kwargs['queries'] = [queries]
        kwargs['window'] = window
    if kwargs.get('when', {}):
        schedule_type = kwargs.get('when').pop('schedule_type')
        if schedule_type != 'interval':
            raise BadRequestError('Invalid schedule type')
    try:
        rule.ctl.update(**kwargs)
    except (BadRequestError, ValidationError) as e:
        return str(e), 400
    Notification.objects(
        owner=auth_context.owner, rtype='rule', rid=rule.id
    ).delete()
    return rule.as_dict()


def list_rules(search=None, sort=None, start=0, limit=100, at=None):  # noqa: E501
    """Get rules

    Return a filtered list of rules # noqa: E501

    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListRulesResponse
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    rules, total = list_resources(auth_context, 'rule',
                                  search=search, sort=sort, limit=limit, at=at)
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    try:
        auth_context.check_perm('rule', 'write', rule.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
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
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        [rule], total = list_resources(
            auth_context, 'rule', search=rule, limit=1)
    except ValueError:
        return 'Rule does not exist', 404
    try:
        auth_context.check_perm('rule', 'write', rule.id)
    except PolicyUnauthorizedError:
        return 'You are not authorized to perform this action', 403
    if not auth_context.is_owner():
        return 'You are not authorized to perform this action', 403
    getattr(rule.ctl, action)()
    return 'Rule toggled succesfully'


def get_rule(rule):  # noqa: E501
    """Get rule

    Get details about target rule # noqa: E501

    :param rule:
    :type rule: str

    :rtype: None
    """
    from mist.api.methods import list_resources
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
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
