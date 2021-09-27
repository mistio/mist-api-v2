import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'RulesController'.replace('Controller', '').lower()
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


class TestRulesController:
    """RulesController integration test stubs"""

    def test_add_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_rule

        Add rule
        """
        query_string = [('queries', "{}"),
                        ('window', "{}"),
                        ('frequency', "{}"),
                        ('trigger_after', "{}"),
                        ('actions', "{}"),
                        ('selectors', "{}")]
        uri = mist_core.uri + '/api/v2/rules' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_delete_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_rule

        Delete rule
        """
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(rule="example_rule") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_rule

        Get rule
        """
        query_string = [('sort', "-name"),
                        ('only', "id")]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(rule="example_rule") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_rules(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_rules

        List rules
        """
        query_string = [('search', "total_run_count:5"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id")]
        uri = mist_core.uri + '/api/v2/rules' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_rename_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for rename_rule

        Rename rule
        """
        query_string = [('action', "renamed_example_rule")]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(rule="example_rule") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'PATCH'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_toggle_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for toggle_rule

        Toggle rule
        """
        query_string = [('action', "example_action")]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(rule="example_rule") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_update_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for update_rule

        Update rule
        """
        query_string = [('queries', "{}"),
                        ('window', "{}"),
                        ('frequency', "{}"),
                        ('trigger_after', "{}"),
                        ('actions', "{}"),
                        ('selectors', "{}")]
        uri = mist_core.uri + '/api/v2/rules/{rule}'.format(rule="example_rule") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    @pytest.fixture(scope="class")
    def setup(owner_api_token):
        _setup_module.setup(owner_api_token)
        yield
        _setup_module.teardown(owner_api_token)
    TestRulesController = pytest.mark.usefixtures("setup")(TestRulesController)

# Mark delete-related test methods as last to be run
for key in vars(TestRulesController):
    attr = getattr(TestRulesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestRulesController, key, pytest.mark.last(attr))
