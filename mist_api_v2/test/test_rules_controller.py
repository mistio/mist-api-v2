import json
import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_found
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']
REDIRECT_OPERATIONS = ['ssh', 'console']

resource_name = 'RulesController'.replace('Controller', '').lower()
resource_name_singular = resource_name.strip('s')
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def after_test(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    test_operation = method_name.replace('test_', '')
    callback = setup_data.get(test_operation, {}).get('callback')
    if callable(callback):
        assert callback()
    else:
        sleep = setup_data.get(test_operation, {}).get('sleep')
        if sleep:
            time.sleep(sleep)


class TestRulesController:
    """RulesController integration test stubs"""

    def test_add_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_rule

        Add rule
        """
        add_rule_request = json.loads("""{
  "trigger_after" : {
    "period" : "period",
    "offset" : 5
  },
  "data_type" : "logs",
  "window" : {
    "period" : "period",
    "stop" : 1,
    "start" : 6
  },
  "selectors" : {
    "include" : [ "include", "include" ],
    "ids" : [ "ids", "ids" ],
    "type" : "machines"
  },
  "queries" : [ {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  }, {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  } ],
  "actions" : [ {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  }, {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  } ],
  "frequency" : {
    "period" : "period",
    "every" : 5
  }
}""", strict=False)
        request_body = setup_data.get('add_rule', {}).get(
            'request_body')
        if request_body:
            add_rule_request = request_body
        else:
            for k in add_rule_request:
                if k in setup_data:
                    add_rule_request[k] = setup_data[k]
                elif k == 'name' and resource_name_singular in setup_data:
                    add_rule_request[k] = setup_data[
                        resource_name_singular]
        inject_vault_credentials(add_rule_request)
        uri = mist_core.uri + '/api/v2/rules'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_rule_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'add_rule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_rule

        Delete rule
        """
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('delete_rule', {}).get('rule') or setup_data.get('rule') or 'my-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_rule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_rule

        Update rule
        """
        edit_rule_request = json.loads("""{
  "trigger_after" : {
    "period" : "period",
    "offset" : 5
  },
  "window" : {
    "period" : "period",
    "stop" : 1,
    "start" : 6
  },
  "selectors" : {
    "include" : [ "include", "include" ],
    "ids" : [ "ids", "ids" ],
    "type" : "machines"
  },
  "queries" : [ {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  }, {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  } ],
  "actions" : [ {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  }, {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  } ],
  "frequency" : {
    "period" : "period",
    "every" : 5
  }
}""", strict=False)
        request_body = setup_data.get('edit_rule', {}).get(
            'request_body')
        if request_body:
            edit_rule_request = request_body
        else:
            for k in edit_rule_request:
                if k in setup_data:
                    edit_rule_request[k] = setup_data[k]
                elif k == 'name' and resource_name_singular in setup_data:
                    edit_rule_request[k] = setup_data[
                        resource_name_singular]
        inject_vault_credentials(edit_rule_request)
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('edit_rule', {}).get('rule') or setup_data.get('rule') or 'my-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=edit_rule_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'edit_rule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_rule

        Get rule
        """
        query_string = setup_data.get('get_rule', {}).get('query_string') or [('sort', '-name'),
                        ('only', 'id')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('get_rule', {}).get('rule') or setup_data.get('rule') or 'my-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_rule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_rules(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_rules

        List rules
        """
        query_string = setup_data.get('list_rules', {}).get('query_string') or [('search', 'total_run_count:5'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', '56'),
                        ('only', 'id')]
        uri = mist_core.uri + '/api/v2/rules'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_rules' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_rename_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for rename_rule

        Rename rule
        """
        query_string = setup_data.get('rename_rule', {}).get('query_string') or [('name', 'my-renamed-rule')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('rename_rule', {}).get('rule') or setup_data.get('rule') or 'my-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PATCH'.lower())
        response = request_method()
        if 'rename_rule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_toggle_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for toggle_rule

        Toggle rule
        """
        query_string = setup_data.get('toggle_rule', {}).get('query_string') or [('action', 'disable')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('toggle_rule', {}).get('rule') or setup_data.get('rule') or 'my-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'toggle_rule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if resource_name == 'machines':
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestRulesController, method_name)
        setattr(TestRulesController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestRulesController):
        attr = getattr(TestRulesController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestRulesController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            global setup_data
            setup_data = _setup_module.setup(owner_api_token) or {}
            yield
            _setup_module.teardown(owner_api_token, setup_data)
            class_setup_done = True
    TestRulesController = pytest.mark.usefixtures('setup')(
        TestRulesController)
