# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.create_secret_request import CreateSecretRequest  # noqa: E501
from mist_api_v2.models.edit_secret_request import EditSecretRequest  # noqa: E501
from mist_api_v2.models.get_secret_response import GetSecretResponse  # noqa: E501
from mist_api_v2.models.list_secrets_response import ListSecretsResponse  # noqa: E501
from mist_api_v2.models.secret import Secret  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestSecretsController(BaseTestCase):
    """SecretsController integration test stubs"""

    def test_create_secret(self):
        """Test case for create_secret

        Create secret
        """
        create_secret_request = {
  "name" : "name",
  "secret" : "{}"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/secrets',
            method='POST',
            headers=headers,
            data=json.dumps(create_secret_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_secret(self):
        """Test case for delete_secret

        Delete secret
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/secrets/{secret}'.format(secret='secret_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_secret(self):
        """Test case for edit_secret

        Edit secret
        """
        edit_secret_request = {
  "secret" : "{}"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/secrets/{secret}'.format(secret='secret_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(edit_secret_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_secret(self):
        """Test case for get_secret

        Get secret
        """
        query_string = [('value', True)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/secrets/{secret}'.format(secret='secret_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_secrets(self):
        """Test case for list_secrets

        List secrets
        """
        query_string = [('search', 'name:clouds/EC2-Tokyo'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/secrets',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
