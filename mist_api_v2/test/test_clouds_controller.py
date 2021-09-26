import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'CloudsController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True

@pytest.fixture(scope="class")
def setup(owner_api_token):
    if SETUP_MODULE_EXISTS:
        setup_module.setup(owner_api_token)
        yield
        setup_module.teardown(owner_api_token)
    else:
        yield


@pytest.mark.usefixtures("setup")
class TestCloudsController:
    """CloudsController integration test stubs"""

    def test_add_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_cloud

        Add cloud
        """
        add_cloud_request = {
  "name" : "example_cloud",
  "provider" : "google",
  "credentials" : {
    "projectId" : "projectId",
    "privateKey" : "privateKey",
    "email" : "email"
  }
}
        config.inject_vault_credentials(add_cloud_request)
        uri = mist_core.uri + '/api/v2/clouds' 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=add_cloud_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_delete_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_cloud

        Delete cloud
        """
        uri = mist_core.uri + '/api/v2/clouds/{cloud}'.format(cloud="example_cloud") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_edit_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_cloud

        Edit cloud
        """
        edit_cloud_request = {
  "name" : "renamed_example_cloud"
}
        config.inject_vault_credentials(edit_cloud_request)
        uri = mist_core.uri + '/api/v2/clouds/{cloud}'.format(cloud="example_cloud") 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=edit_cloud_request)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_cloud

        Get cloud
        """
        query_string = [('sort', "-name"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/clouds/{cloud}'.format(cloud="example_cloud") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_clouds(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_clouds

        List clouds
        """
        query_string = [('search', "provider:amazon"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/clouds' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestCloudsController):
    attr = getattr(TestCloudsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestCloudsController, key, pytest.mark.last(attr))
