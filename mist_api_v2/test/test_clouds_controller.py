import time
import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = CloudsController.replace('Controller', '').lower()
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


@pytest.fixture(autouse=True)
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    if method_name == 'test_create_cluster':
        time.sleep(200)


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
        setattr(TestCloudsController, key, pytest.mark.order("last")(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope="class")
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            _setup_module.setup(owner_api_token)
            yield
            _setup_module.teardown(owner_api_token)
            class_setup_done = True
    TestCloudsController = pytest.mark.usefixtures("setup")(TestCloudsController)
