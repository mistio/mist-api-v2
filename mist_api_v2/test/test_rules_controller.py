import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'RulesController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXIST = False
else:
    SETUP_MODULES_EXIST = True


class TestRulesController:
    """RulesController integration test stubs"""

    def test_add_rule(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_rule

        Add rule
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

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


# Mark delete-related test methods as last to be run
for key in vars(TestRulesController):
    attr = getattr(TestRulesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestRulesController, key, pytest.mark.last(attr))
