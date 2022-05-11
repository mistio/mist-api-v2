# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.create_zone_request import CreateZoneRequest  # noqa: E501
from mist_api_v2.models.create_zone_response import CreateZoneResponse  # noqa: E501
from mist_api_v2.models.get_zone_response import GetZoneResponse  # noqa: E501
from mist_api_v2.models.list_zones_response import ListZonesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestZonesController(BaseTestCase):
    """ZonesController integration test stubs"""

    def test_create_zone(self):
        """Test case for create_zone

        Create zone
        """
        create_zone_request = {
  "name" : "my-zone",
  "cloud" : "my-cloud"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/zones',
            method='POST',
            headers=headers,
            data=json.dumps(create_zone_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_zone(self):
        """Test case for delete_zone

        Delete zone
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/zones/{zone}'.format(zone='my-zone'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_zone(self):
        """Test case for edit_zone

        Edit zone
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/zones/{zone}'.format(zone='my-zone'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zone(self):
        """Test case for get_zone

        Get zone
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/zones/{zone}'.format(zone='my-zone'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_zones(self):
        """Test case for list_zones

        List zones
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
            '/api/v2/zones',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
