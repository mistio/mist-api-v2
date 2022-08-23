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

resource_name = 'LocationsController'.replace('Controller', '').lower()
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


class TestLocationsController:
    """LocationsController integration test stubs"""

    def test_get_location(self, pretty_print, owner_api_token):
        """Test case for get_location

        Get location
        """
        query_string = setup_data.get('get_location', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/locations/{location}'.format(
            location=setup_data.get('get_location', {}).get('location') or setup_data.get('location') or 'us-central1-a')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_location' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_locations(self, pretty_print, owner_api_token):
        """Test case for list_locations

        List locations
        """
        query_string = setup_data.get('list_locations', {}).get('query_string') or [('cloud', 'my-cloud'),
                        ('search', 'cinet3'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/locations'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_locations' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestLocationsController, method_name)
        setattr(TestLocationsController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestLocationsController):
        attr = getattr(TestLocationsController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestLocationsController, key, pytest.mark.order('last')(attr))

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
    TestLocationsController = pytest.mark.usefixtures('setup')(
        TestLocationsController)
