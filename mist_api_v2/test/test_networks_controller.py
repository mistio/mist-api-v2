import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'NetworksController'.replace('Controller', '').lower()
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_retval = None


@pytest.fixture(autouse=True)
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    if method_name == 'test_create_cluster':
        time.sleep(200)


class TestNetworksController:
    """NetworksController integration test stubs"""

    def test_create_network(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_network

        Create network
        """
        create_network_request = {
  "name" : "example-network",
  "cloud" : "example-cloud"
}
        inject_vault_credentials(create_network_request)
        uri = mist_core.uri + '/api/v2/networks'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_network_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_edit_network(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_network

        Edit network
        """
        query_string = [('name', 'renamed-example-network')]
        uri = mist_core.uri + '/api/v2/networks/{network}'.format(
            network=setup_retval or 'example-network')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_network(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_network

        Get network
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/networks/{network}'.format(
            network=setup_retval or 'example-network')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_networks(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_networks

        List networks
        """
        query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'cinet3'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', '56'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/networks'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestNetworksController):
    attr = getattr(TestNetworksController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestNetworksController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            retval = _setup_module.setup(owner_api_token)
            if isinstance(retval, str):
                global setup_retval
                setup_retval = retval
            yield
            _setup_module.teardown(owner_api_token)
            class_setup_done = True
    TestNetworksController = pytest.mark.usefixtures('setup')(
        TestNetworksController)
