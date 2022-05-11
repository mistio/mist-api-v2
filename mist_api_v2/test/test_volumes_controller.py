# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.create_volume_request import CreateVolumeRequest  # noqa: E501
from mist_api_v2.models.create_volume_response import CreateVolumeResponse  # noqa: E501
from mist_api_v2.models.get_volume_response import GetVolumeResponse  # noqa: E501
from mist_api_v2.models.list_volumes_response import ListVolumesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestVolumesController(BaseTestCase):
    """VolumesController integration test stubs"""

    def test_create_volume(self):
        """Test case for create_volume

        Create volume
        """
        create_volume_request = {
  "template" : "{}",
  "quantity" : 0,
  "ex_disk_type" : "pd-standard",
  "ex_volume_type" : "standard",
  "save" : true,
  "dry" : true,
  "tags" : "{}",
  "cloud" : "my-cloud",
  "ex_iops" : "ex_iops",
  "size" : 1,
  "extra" : "{}",
  "name" : "my-volume",
  "location" : "us-central1-a"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/volumes',
            method='POST',
            headers=headers,
            data=json.dumps(create_volume_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_volume(self):
        """Test case for delete_volume

        Delete volume
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/volumes/{volume}'.format(volume='my-volume'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_volume(self):
        """Test case for edit_volume

        Edit volume
        """
        query_string = [('name', 'my-renamed-volume')]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/volumes/{volume}'.format(volume='my-volume'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_volume(self):
        """Test case for get_volume

        Get volume
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/volumes/{volume}'.format(volume='my-volume'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_volumes(self):
        """Test case for list_volumes

        List volumes
        """
        query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'location:Amsterdam'),
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
            '/api/v2/volumes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
