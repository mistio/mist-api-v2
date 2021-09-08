# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.add_cloud_request import AddCloudRequest  # noqa: E501
from mist_api_v2.models.edit_cloud_request import EditCloudRequest  # noqa: E501
from mist_api_v2.models.get_cloud_response import GetCloudResponse  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_clouds_response import ListCloudsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestCloudsController(BaseTestCase):
    """CloudsController integration test stubs"""

    def test_add_cloud(self):
        """Test case for add_cloud

        Add cloud
        """
        print('Hello@@@@@@@@')
        add_cloud_request = {
  "name" : "example_aws_cloud",
  "provider" : "amazon",
  "credentials" : {
    "apikey" : "apikey",
    "apisecret" : "apisecret",
    "region" : "region"
  }
}
        inject_vault_credentials_into_request(add_cloud_request)
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
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
        print('Hello@@@@@@@@')
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clouds/{cloud}'.format(cloud='cloud_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_cloud(self):
        """Test case for edit_cloud

        Edit cloud
        """
        print('Hello@@@@@@@@')
        edit_cloud_request = {
  "name" : "renamed_example_cloud"
}
        inject_vault_credentials_into_request(edit_cloud_request)
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clouds/{cloud}'.format(cloud='cloud_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(edit_cloud_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cloud(self):
        """Test case for get_cloud

        Get cloud
        """
        print('Hello@@@@@@@@')
        query_string = [('sort', "-name"),
                        ('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/clouds/{cloud}'.format(cloud='cloud_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_clouds(self):
        """Test case for list_clouds

        List clouds
        """
        print('Hello@@@@@@@@')
        query_string = [('search', "provider:amazon"),
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
            '/api/v2/clouds',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
