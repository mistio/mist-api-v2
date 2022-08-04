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

resource_name = 'AuthController'.replace('Controller', '').lower()
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


class TestAuthController:
    """AuthController integration test stubs"""

    def test_create_token(self, pretty_print, owner_api_token):
        """Test case for create_token

        Create token
        """
        uri = MIST_URL + '/api/v2/auth/tokens'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'create_token' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_describe_auth(self, pretty_print, owner_api_token):
        """Test case for describe_auth

        Authentication info
        """
        uri = MIST_URL + '/api/v2/auth'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'describe_auth' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_sessions(self, pretty_print, owner_api_token):
        """Test case for list_sessions

        List sessions
        """
        query_string = setup_data.get('list_sessions', {}).get('query_string') or [('search', 'search_example'),
                        ('sort', '-last_active'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/auth/sessions'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_sessions' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_tokens(self, pretty_print, owner_api_token):
        """Test case for list_tokens

        List API tokens
        """
        query_string = setup_data.get('list_tokens', {}).get('query_string') or [('search', 'search_example'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/auth/tokens'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_tokens' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_login(self, pretty_print, owner_api_token):
        """Test case for login

        Sign in to the portal
        """
        body = setup_data.get('login', {}).get(
            'request_body') or json.loads("""None""", strict=False)
        uri = MIST_URL + '/api/v2/auth/sessions'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=body)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'login' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestAuthController, method_name)
        setattr(TestAuthController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestAuthController):
        attr = getattr(TestAuthController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestAuthController, key, pytest.mark.order('last')(attr))

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
    TestAuthController = pytest.mark.usefixtures('setup')(
        TestAuthController)
