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

resource_name = 'SecretsController'.replace('Controller', '').lower()
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


class TestSecretsController:
    """SecretsController integration test stubs"""

    def test_create_secret(self, pretty_print, owner_api_token):
        """Test case for create_secret

        Create secret
        """
        create_secret_request = setup_data.get('create_secret', {}).get(
            'request_body') or json.loads("""null""", strict=False)
        uri = MIST_URL + '/api/v2/secrets'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_secret_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'create_secret' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_secret(self, pretty_print, owner_api_token):
        """Test case for delete_secret

        Delete secret
        """
        uri = MIST_URL + '/api/v2/secrets/{secret}'.format(
            secret=setup_data.get('delete_secret', {}).get('secret') or setup_data.get('secret') or 'secret_example')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_secret' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_secret(self, pretty_print, owner_api_token):
        """Test case for edit_secret

        Edit secret
        """
        edit_secret_request = setup_data.get('edit_secret', {}).get(
            'request_body') or json.loads("""{
  "secret" : "{}"
}""", strict=False)
        uri = MIST_URL + '/api/v2/secrets/{secret}'.format(
            secret=setup_data.get('edit_secret', {}).get('secret') or setup_data.get('secret') or 'secret_example')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=edit_secret_request)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'edit_secret' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_secret(self, pretty_print, owner_api_token):
        """Test case for get_secret

        Get secret
        """
        query_string = setup_data.get('get_secret', {}).get('query_string') or [('value', True)]
        uri = MIST_URL + '/api/v2/secrets/{secret}'.format(
            secret=setup_data.get('get_secret', {}).get('secret') or setup_data.get('secret') or 'secret_example')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_secret' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_secrets(self, pretty_print, owner_api_token):
        """Test case for list_secrets

        List secrets
        """
        query_string = setup_data.get('list_secrets', {}).get('query_string') or [('search', 'name:clouds/EC2-Tokyo'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id')]
        uri = MIST_URL + '/api/v2/secrets'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_secrets' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestSecretsController, method_name)
        setattr(TestSecretsController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestSecretsController):
        attr = getattr(TestSecretsController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestSecretsController, key, pytest.mark.order('last')(attr))

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
    TestSecretsController = pytest.mark.usefixtures('setup')(
        TestSecretsController)
