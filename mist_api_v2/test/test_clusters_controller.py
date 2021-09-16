# coding: utf-8

from __future__ import absolute_import
import importlib
import unittest

from flask import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.test import BaseTestCase

try:
    setup_module_name = 'ClustersController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXISTS = False
else:
    SETUP_MODULES_EXISTS = True

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1


class TestClustersController(BaseTestCase):
    """ClustersController integration test stubs"""

    if SETUP_MODULES_EXISTS:
        @classmethod
        def get_test_client(cls):
            if not hasattr(cls, 'test_client'):
                cls.test_client = cls().create_app().test_client()
            return cls.test_client

        @classmethod
        def setUpClass(cls):
            setup_module.setup(cls.get_test_client())

        @classmethod
        def tearDownClass(cls):
            setup_module.teardown(cls.get_test_client())

    def test_create_cluster(self):
        """Test case for create_cluster

        Create cluster
        """
        create_cluster_request = {
  "name" : "example-cluster",
  "cloud" : "example_cloud",
  "provider" : "google",
  "location" : "example_location"
}
        inject_vault_credentials_into_request(create_cluster_request)
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clusters',
            method='POST',
            headers=headers,
            data=json.dumps(create_cluster_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_destroy_cluster(self):
        """Test case for destroy_cluster

        Destroy cluster
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clusters/{cluster}'.format(cluster="example-cluster"),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cluster(self):
        """Test case for get_cluster

        Get cluster
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clusters/{cluster}'.format(cluster="example-cluster"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_clusters(self):
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
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clusters',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
