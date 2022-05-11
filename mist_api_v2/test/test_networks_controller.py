# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.create_network_request import CreateNetworkRequest  # noqa: E501
from mist_api_v2.models.create_network_response import CreateNetworkResponse  # noqa: E501
from mist_api_v2.models.get_network_response import GetNetworkResponse  # noqa: E501
from mist_api_v2.models.list_networks_response import ListNetworksResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestNetworksController(BaseTestCase):
    """NetworksController integration test stubs"""

    def test_create_network(self):
        """Test case for create_network

        Create network
        """
        create_network_request = {
  "cloud" : "my-cloud",
  "template" : "{}",
  "extra" : "{}",
  "name" : "my-network",
  "save" : true,
  "dry" : true,
  "tags" : "{}"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/networks',
            method='POST',
            headers=headers,
            data=json.dumps(create_network_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_network(self):
        """Test case for delete_network

        Delete network
        """
        query_string = [('cloud', 'my-cloud')]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/networks/{network}'.format(network='my-network'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_network(self):
        """Test case for edit_network

        Edit network
        """
        query_string = [('name', 'my-renamed-network')]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/networks/{network}'.format(network='my-network'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_network(self):
        """Test case for get_network

        Get network
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/networks/{network}'.format(network='my-network'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_networks(self):
        """Test case for list_networks

        List networks
        """
        query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'cinet3'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/networks',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
