# coding: utf-8

from __future__ import absolute_import
import time
import importlib
import unittest

from flask import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.test import BaseTestCase

try:
    setup_module_name = 'NetworksController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXIST = False
else:
    SETUP_MODULES_EXIST = True


def post_delay(seconds):
    def decorator(func):
        def wrapper(self):
            func(self)
            time.sleep(seconds)
        return wrapper
    return decorator


unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1


class TestNetworksController(BaseTestCase):
    """NetworksController integration test stubs"""

    if SETUP_MODULES_EXIST:
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

    def test_create_network(self):
        """Test case for create_network

        Create network
        """
        create_network_request = {
  "name" : "example_network",
  "cloud" : "example_cloud"
}
        inject_vault_credentials_into_request(create_network_request)
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/networks',
            method='POST',
            headers=headers,
            data=json.dumps(create_network_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_network(self):
        """Test case for edit_network

        Edit network
        """
        query_string = [('name', "renamed_example_network")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/networks/{network}'.format(network="example_network"),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_network(self):
        """Test case for get_network

        Get network
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/networks/{network}'.format(network="example_network"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_networks(self):
        """Test case for list_networks

        List networks
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "cinet3"),
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
            '/api/v2/networks',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if setup_module_name == 'clusters':
    TestNetworksController.test_create_cluster = post_delay(seconds=200)(
        TestNetworksController.test_create_cluster)

if __name__ == '__main__':
    unittest.main()
