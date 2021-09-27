import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'ClustersController'.replace('Controller', '').lower()
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


class TestScriptsController:
    """ScriptsController integration test stubs"""

    def test_delete_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_script

        Delete script
        """
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(script="example_script") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_edit_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_script

        Edit script
        """
        query_string = [('name', "example_script"),
                        ('description', "'description_example'")]
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(script="example_script") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_script

        Get script
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(script="example_script") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_scripts(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_scripts

        List scripts
        """
        query_string = [('search', "install-tensorflow"),
                        ('sort', "-name"),
                        ('start', "3"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/scripts' 
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
    TestScriptsController = pytest.mark.usefixtures("setup")(TestScriptsController)

# Mark delete-related test methods as last to be run
for key in vars(TestScriptsController):
    attr = getattr(TestScriptsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestScriptsController, key, pytest.mark.last(attr))
