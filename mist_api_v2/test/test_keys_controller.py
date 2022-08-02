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

resource_name = 'KeysController'.replace('Controller', '').lower()
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


class TestKeysController:
    """KeysController integration test stubs"""

    def test_add_key(self, pretty_print, owner_api_token):
        """Test case for add_key

        Add key
        """
        add_key_request = setup_data.get('add_key', {}).get(
            'request_body') or json.loads("""{
  "name" : "my-key",
  "private" : "-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0FPqri0cb2JZfXJ/DgYSF6vUp wmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/3j+skZ6UtW+5u09lHNsj6tQ5 1s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZwIDAQABAoGAFijko56+qGyN8M0RVyaRAXz++xTqHBLh 3tx4VgMtrQ+WEgCjhoTwo23KMBAuJGSYnRmoBZM3lMfTKevIkAidPExvYCdm5dYq3XToLkkLv5L2 pIIVOFMDG+KESnAFV7l2c+cnzRMW0+b6f8mR1CJzZuxVLL6Q02fvLi55/mbSYxECQQDeAw6fiIQX GukBI4eMZZt4nscy2o12KyYner3VpoeE+Np2q+Z3pvAMd/aNzQ/W9WaI+NRfcxUJrmfPwIGm63il AkEAxCL5HQb2bQr4ByorcMWm/hEP2MZzROV73yF41hPsRC9m66KrheO9HPTJuo3/9s5p+sqGxOlF L0NDt4SkosjgGwJAFklyR1uZ/wPJjj611cdBcztlPdqoxssQGnh85BzCj/u3WqBpE2vjvyyvyI5k X6zk7S0ljKtt2jny2+00VsBerQJBAJGC1Mg5Oydo5NwD6BiROrPxGo2bpTbu/fhrT8ebHkTz2epl U9VQQSQzY1oZMVX8i1m5WUTLPz2yLJIBQVdXqhMCQBGoiuSoSjafUhV7i1cEGpb88h5NBYZzWXGZ 37sJ5QsW+sJyoNde3xH8vdXhzU7eT82D6X/scw9RZz+/6rCJ4p0=\n-----END RSA PRIVATE KEY-----"
}""", strict=False)
        uri = MIST_URL + '/api/v2/keys'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_key_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'add_key' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_key(self, pretty_print, owner_api_token):
        """Test case for delete_key

        Delete key
        """
        uri = MIST_URL + '/api/v2/keys/{key}'.format(
            key=setup_data.get('delete_key', {}).get('key') or setup_data.get('key') or 'my-key')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_key' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_key(self, pretty_print, owner_api_token):
        """Test case for edit_key

        Edit key
        """
        query_string = setup_data.get('edit_key', {}).get('query_string') or [('name', 'my-renamed-key'),
                        ('default', True)]
        uri = MIST_URL + '/api/v2/keys/{key}'.format(
            key=setup_data.get('edit_key', {}).get('key') or setup_data.get('key') or 'my-key')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'edit_key' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_key(self, pretty_print, owner_api_token):
        """Test case for get_key

        Get key
        """
        query_string = setup_data.get('get_key', {}).get('query_string') or [('private', False),
                        ('sort', '-name'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/keys/{key}'.format(
            key=setup_data.get('get_key', {}).get('key') or setup_data.get('key') or 'my-key')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_key' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_keys(self, pretty_print, owner_api_token):
        """Test case for list_keys

        List keys
        """
        query_string = setup_data.get('list_keys', {}).get('query_string') or [('search', 'owned_by:csk@mist.io'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/keys'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_keys' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestKeysController, method_name)
        setattr(TestKeysController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestKeysController):
        attr = getattr(TestKeysController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestKeysController, key, pytest.mark.order('last')(attr))

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
    TestKeysController = pytest.mark.usefixtures('setup')(
        TestKeysController)
