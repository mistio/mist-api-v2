import json
import time
import importlib

import pytest

from misttests.config import MIST_URL
from misttests.integration.api.helpers import assert_response_found
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']
REDIRECT_OPERATIONS = ['ssh', 'console']

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


class TestScriptsController:
    """ScriptsController integration test stubs"""

    def test_add_script(self, pretty_print, owner_api_token):
        """Test case for add_script

        Add script
        """
        add_script_request = setup_data.get('add_script', {}).get(
            'request_body') or json.loads("""{
  "entrypoint" : "entrypoint.sh",
  "name" : "my-script",
  "description" : "description",
  "exec_type" : "executable",
  "script" : "#!/usr/bin/env bash\necho Hello, World!",
  "location_type" : "inline"
}""", strict=False)
        uri = MIST_URL + '/api/v2/scripts'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_script_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'add_script' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_script(self, pretty_print, owner_api_token):
        """Test case for delete_script

        Delete script
        """
        uri = MIST_URL + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('delete_script', {}).get('script') or setup_data.get('script') or 'my-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_script' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_download_script(self, pretty_print, owner_api_token):
        """Test case for download_script

        Download script
        """
        uri = MIST_URL + '/api/v2/scripts/{script}/file'.format(
            script=setup_data.get('download_script', {}).get('script') or setup_data.get('script') or 'my-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'download_script' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_script(self, pretty_print, owner_api_token):
        """Test case for edit_script

        Edit script
        """
        query_string = setup_data.get('edit_script', {}).get('query_string') or [('name', 'my-renamed-script'),
                        ('description', 'description')]
        uri = MIST_URL + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('edit_script', {}).get('script') or setup_data.get('script') or 'my-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'edit_script' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_generate_script_url(self, pretty_print, owner_api_token):
        """Test case for generate_script_url

        Generate script url
        """
        uri = MIST_URL + '/api/v2/scripts/{script}/url'.format(
            script=setup_data.get('generate_script_url', {}).get('script') or setup_data.get('script') or 'my-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'generate_script_url' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_script(self, pretty_print, owner_api_token):
        """Test case for get_script

        Get script
        """
        query_string = setup_data.get('get_script', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('get_script', {}).get('script') or setup_data.get('script') or 'my-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_script' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_scripts(self, pretty_print, owner_api_token):
        """Test case for list_scripts

        List scripts
        """
        query_string = setup_data.get('list_scripts', {}).get('query_string') or [('search', 'my-script'),
                        ('sort', '-name'),
                        ('start', '3'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/scripts'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_scripts' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_run_script(self, pretty_print, owner_api_token):
        """Test case for run_script

        Run script
        """
        run_script_request = setup_data.get('run_script', {}).get(
            'request_body') or json.loads("""{
  "su" : "false",
  "machine" : "my-machine",
  "job_id" : "ab74e2f0b7ae4999b1e4013e20dac418",
  "params" : "-v",
  "env" : "EXAMPLE_VAR=123"
}""", strict=False)
        uri = MIST_URL + '/api/v2/scripts/{script}'.format(
            script=setup_data.get('run_script', {}).get('script') or setup_data.get('script') or 'my-script')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=run_script_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'run_script' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestScriptsController, method_name)
        setattr(TestScriptsController, method_name,
                pytest.mark.order(order + 1)(method))
else:
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
