import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'SizesController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXIST = False
else:
    SETUP_MODULES_EXIST = True


class TestSizesController:
    """SizesController integration test stubs"""

    def test_get_size(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_size

        Get size
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/sizes/{size}'.format(size="example_size") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_sizes(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_sizes

        List sizes
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "cinet3"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/sizes' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestSizesController):
    attr = getattr(TestSizesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestSizesController, key, pytest.mark.last(attr))
