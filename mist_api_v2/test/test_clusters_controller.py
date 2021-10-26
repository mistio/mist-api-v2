import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'ClustersController'.replace('Controller', '').lower()
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


class TestClustersController:
    """ClustersController integration test stubs"""

    def test_create_cluster(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_cluster

        Create cluster
        """
        create_cluster_request = {
  "name" : "example-cluster",
  "cloud" : "example-cloud",
  "provider" : "google",
  "location" : "example-location"
}
        for k in create_cluster_request:
            if k in setup_data:
                create_cluster_request[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                create_cluster_request[k] = setup_data[resource_name_singular]
        inject_vault_credentials(create_cluster_request)
        uri = mist_core.uri + '/api/v2/clusters'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_cluster_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_destroy_cluster(self, pretty_print, mist_core, owner_api_token):
        """Test case for destroy_cluster

        Destroy cluster
        """
        uri = mist_core.uri + '/api/v2/clusters/{cluster}'.format(
            cluster=setup_data.get('cluster') or 'example-cluster')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_cluster(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_cluster

        Get cluster
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/clusters/{cluster}'.format(
            cluster=setup_data.get('cluster') or 'example-cluster')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_clusters(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_clusters

        List clusters
        """
        query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'created_by:csk'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', '56'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/clusters'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestClustersController):
    attr = getattr(TestClustersController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestClustersController, key, pytest.mark.order('last')(attr))

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
    TestClustersController = pytest.mark.usefixtures('setup')(
        TestClustersController)
