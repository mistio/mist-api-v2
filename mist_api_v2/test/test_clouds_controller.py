# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.add_cloud_request import AddCloudRequest  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_clouds_response import ListCloudsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestCloudsController(BaseTestCase):
    """CloudsController integration test stubs"""

    def test_add_cloud(self):
        """Test case for add_cloud

        Add cloud
        """
        add_cloud_request = {
  "features" : {
    "compute" : true,
    "dns" : false
  },
  "provider" : "amazon",
  "title" : "title"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clouds',
            method='POST',
            headers=headers,
            data=json.dumps(add_cloud_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_cloud(self):
        """Test case for delete_cloud

        Delete cloud
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clouds/{cloud}'.format(cloud='cloud_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cloud(self):
        """Test case for get_cloud

        Get cloud
        """
        headers = { 
        }
        response = self.client.open(
            '/api/v2/clouds/{cloud}'.format(cloud='cloud_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_clouds(self):
        """Test case for list_clouds

        List clouds
        """
        query_string = [('filter', provider:packet AND status:enabled),
                        ('sort', -title)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clouds',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
