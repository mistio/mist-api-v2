import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'ScriptsController'.replace('Controller', '').lower()
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
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    if method_name == 'test_create_cluster':
        time.sleep(240)
    elif method_name == 'test_destroy_cluster':
        time.sleep(120)


class TestScriptsController:
    """ScriptsController integration test stubs"""

    def test_add_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_script

        Add script
        """
        add_script_request = {
  "entrypoint" : "entrypoint.sh",
  "name" : "example-script",
  "description" : "description",
  "exec_type" : "executable",
  "script" : "#!/usr/bin/env bash\necho Hello, World!",
  "location_type" : "inline"
}
        for k in add_script_request:
            if k in setup_data:
                add_script_request[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                add_script_request[k] = setup_data[resource_name_singular]
        inject_vault_credentials(add_script_request)
        uri = mist_core.uri + '/api/v2/scripts'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_script_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_delete_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_script

        Delete script
        """
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('script') or 'example-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_download_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for download_script

        Download script
        """
        uri = mist_core.uri + '/api/v2/scripts/{script}/file'.format(
            script=setup_data.get('script') or 'example-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_edit_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_script

        Edit script
        """
        query_string = [('name', 'renamed-example-script'),
                        ('description', 'description')]
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('script') or 'example-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_generate_script_url(self, pretty_print, mist_core, owner_api_token):
        """Test case for generate_script_url

        Generate script url
        """
        uri = mist_core.uri + '/api/v2/scripts/{script}/url'.format(
            script=setup_data.get('script') or 'example-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_script

        Get script
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('script') or 'example-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_scripts(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_scripts

        List scripts
        """
        query_string = [('search', 'example-script'),
                        ('sort', '-name'),
                        ('start', '3'),
                        ('limit', '56'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/scripts'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_run_script(self, pretty_print, mist_core, owner_api_token):
        """Test case for run_script

        Run script
        """
        run_script_request = {
  "su" : "false",
  "machine" : "example-machine",
  "job_id" : "ab74e2f0b7ae4999b1e4013e20dac418",
  "params" : "-v",
  "env" : "EXAMPLE_VAR=123"
}
        for k in run_script_request:
            if k in setup_data:
                run_script_request[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                run_script_request[k] = setup_data[resource_name_singular]
        inject_vault_credentials(run_script_request)
        uri = mist_core.uri + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('script') or 'example-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=run_script_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestScriptsController):
    attr = getattr(TestScriptsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestScriptsController, key, pytest.mark.order('last')(attr))

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
    TestScriptsController = pytest.mark.usefixtures('setup')(
        TestScriptsController)
