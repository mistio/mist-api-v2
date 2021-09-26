import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'ClustersController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


@pytest.fixture(scope="class")
def setup(owner_api_token):
    if SETUP_MODULE_EXISTS:
        setup_module.setup(owner_api_token)
        yield
        setup_module.teardown(owner_api_token)
    else:
        yield


@pytest.mark.usefixtures("setup")
class TestClustersController:
    """ClustersController integration test stubs"""

    def test_create_cluster(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_cluster

        Create cluster
        """
        create_cluster_request = {
  "name" : "example-cluster",
  "cloud" : "example_cloud",
  "provider" : "google",
  "location" : "example_location"
}
        config.inject_vault_credentials(create_cluster_request)
        uri = mist_core.uri + '/api/v2/clusters' 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=create_cluster_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_destroy_cluster(self, pretty_print, mist_core, owner_api_token):
        """Test case for destroy_cluster

        Destroy cluster
        """
        uri = mist_core.uri + '/api/v2/clusters/{cluster}'.format(cluster="example-cluster") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_cluster(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_cluster

        Get cluster
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/clusters/{cluster}'.format(cluster="example-cluster") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_clusters(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_clusters

        List clusters
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "created_by:csk"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/clusters' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestClustersController):
    attr = getattr(TestClustersController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestClustersController, key, pytest.mark.last(attr))
