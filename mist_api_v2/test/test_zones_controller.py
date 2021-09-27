import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'ZonesController'.replace('Controller', '').lower()
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


class TestZonesController:
    """ZonesController integration test stubs"""

    def test_create_zone(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_zone

        Create zone
        """
        create_zone_request = {
  "name" : "example_zone",
  "cloud" : "example_cloud"
}
        config.inject_vault_credentials(create_zone_request)
        uri = mist_core.uri + '/api/v2/zones' 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=create_zone_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_edit_zone(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_zone

        Edit zone
        """
        query_string = [('name', "renamed_example_zone")]
        uri = mist_core.uri + '/api/v2/zones/{zone}'.format(zone="example_zone") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_zone(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_zone

        Get zone
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/zones/{zone}'.format(zone="example_zone") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_zones(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_zones

        List zones
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "cinet3"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/zones' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
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
    TestZonesController = pytest.mark.usefixtures("setup")(TestZonesController)

# Mark delete-related test methods as last to be run
for key in vars(TestZonesController):
    attr = getattr(TestZonesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestZonesController, key, pytest.mark.last(attr))
