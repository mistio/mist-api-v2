import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'RulesController'.replace('Controller', '').lower()
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    if method_name == 'test_create_cluster':
        time.sleep(200)


class TestRulesController:
    """RulesController integration test stubs"""

    def test_add_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_rule

        Add rule
        """
        add_rule_request = {
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
}
        inject_vault_credentials(add_rule_request)
        uri = mist_core.uri + '/api/v2/rules'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_rule_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_delete_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_rule

        Delete rule
        """
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('rule') or 'example-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_rule

        Get rule
        """
        query_string = [('sort', '-name'),
                        ('only', 'id')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('rule') or 'example-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_rules(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_rules

        List rules
        """
        query_string = [('search', 'total_run_count:5'),
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
        assert_response_ok(response)
        print('Success!!!')

    def test_rename_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for rename_rule

        Rename rule
        """
        query_string = [('name', 'renamed-example-rule')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('rule') or 'example-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PATCH'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_toggle_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for toggle_rule

        Toggle rule
        """
        query_string = [('action', 'disable')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('rule') or 'example-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_update_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for update_rule

        Update rule
        """
        query_string = [('queries', '{}'),
                        ('window', '{}'),
                        ('frequency', '{}'),
                        ('trigger_after', '{}'),
                        ('actions', '{}'),
                        ('selectors', '{}')]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(
            rule=setup_data.get('rule') or 'example-rule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


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
            retval = _setup_module.setup(owner_api_token)
            if isinstance(retval, dict):
                global setup_data
                setup_data = retval
            yield
            _setup_module.teardown(owner_api_token)
            class_setup_done = True
    TestRulesController = pytest.mark.usefixtures('setup')(
        TestRulesController)
