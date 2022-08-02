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

resource_name = 'ZonesController'.replace('Controller', '').lower()
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


class TestZonesController:
    """ZonesController integration test stubs"""

    def test_create_record(self, pretty_print, owner_api_token):
        """Test case for create_record

        Create record
        """
        create_record_request = setup_data.get('create_record', {}).get(
            'request_body') or json.loads("""{
  "name" : "my-record",
  "value" : "123.23.23.2"
}""", strict=False)
        uri = MIST_URL + '/api/v2/zones/{zone}/records'.format(
            zone=setup_data.get('create_record', {}).get('zone') or setup_data.get('zone') or 'my-zone')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_record_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'create_record' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_create_zone(self, pretty_print, owner_api_token):
        """Test case for create_zone

        Create zone
        """
        create_zone_request = setup_data.get('create_zone', {}).get(
            'request_body') or json.loads("""{
  "name" : "my-zone",
  "cloud" : "my-cloud"
}""", strict=False)
        uri = MIST_URL + '/api/v2/zones'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_zone_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'create_zone' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_record(self, pretty_print, owner_api_token):
        """Test case for delete_record

        Delete record
        """
        query_string = setup_data.get('delete_record', {}).get('query_string') or [('cloud', 'my-cloud')]
        uri = MIST_URL + '/api/v2/zones/{zone}/records/{record}'.format(
            zone=setup_data.get('delete_record', {}).get('zone') or setup_data.get('zone') or 'my-zone', record=setup_data.get('delete_record', {}).get('record') or setup_data.get('record') or 'my-zone')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_record' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_zone(self, pretty_print, owner_api_token):
        """Test case for delete_zone

        Delete zone
        """
        uri = MIST_URL + '/api/v2/zones/{zone}'.format(
            zone=setup_data.get('delete_zone', {}).get('zone') or setup_data.get('zone') or 'my-zone')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_zone' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_zone(self, pretty_print, owner_api_token):
        """Test case for edit_zone

        Edit zone
        """
        uri = MIST_URL + '/api/v2/zones/{zone}'.format(
            zone=setup_data.get('edit_zone', {}).get('zone') or setup_data.get('zone') or 'my-zone')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        if 'edit_zone' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_record(self, pretty_print, owner_api_token):
        """Test case for get_record

        Get record
        """
        query_string = setup_data.get('get_record', {}).get('query_string') or [('cloud', 'my-cloud'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/zones/{zone}/records/{record}'.format(
            zone=setup_data.get('get_record', {}).get('zone') or setup_data.get('zone') or 'my-zone', record=setup_data.get('get_record', {}).get('record') or setup_data.get('record') or 'my-record')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_record' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_zone(self, pretty_print, owner_api_token):
        """Test case for get_zone

        Get zone
        """
        query_string = setup_data.get('get_zone', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/zones/{zone}'.format(
            zone=setup_data.get('get_zone', {}).get('zone') or setup_data.get('zone') or 'my-zone')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_zone' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_records(self, pretty_print, owner_api_token):
        """Test case for list_records

        List records
        """
        query_string = setup_data.get('list_records', {}).get('query_string') or [('cloud', 'my-cloud'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/zones/{zone}/records'.format(
            zone=setup_data.get('list_records', {}).get('zone') or setup_data.get('zone') or 'my-zone')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_records' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_zones(self, pretty_print, owner_api_token):
        """Test case for list_zones

        List zones
        """
        query_string = setup_data.get('list_zones', {}).get('query_string') or [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'cinet3'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/zones'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_zones' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestZonesController, method_name)
        setattr(TestZonesController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestZonesController):
        attr = getattr(TestZonesController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestZonesController, key, pytest.mark.order('last')(attr))

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
    TestZonesController = pytest.mark.usefixtures('setup')(
        TestZonesController)
