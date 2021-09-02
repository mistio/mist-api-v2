# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.add_key_request import AddKeyRequest  # noqa: E501
from mist_api_v2.models.add_key_response import AddKeyResponse  # noqa: E501
from mist_api_v2.models.get_key_response import GetKeyResponse  # noqa: E501
from mist_api_v2.models.list_keys_response import ListKeysResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestKeysController(BaseTestCase):
    """KeysController integration test stubs"""

    def test_add_key(self):
        """Test case for add_key

        Add key
        """
        add_key_request = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/keys',
            method='POST',
            headers=headers,
            data=json.dumps(add_key_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_key(self):
        """Test case for delete_key

        Delete key
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/keys/{key}'.format(key='key_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_key(self):
        """Test case for edit_key

        Edit key
        """
        query_string = [('name', "'name_example'"),
                        ('default', "True")]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/keys/{key}'.format(key='key_example'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_key(self):
        """Test case for get_key

        Get key
        """
        query_string = [('private', "False"),
                        ('sort', "-name"),
                        ('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/keys/{key}'.format(key='key_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_keys(self):
        """Test case for list_keys

        List keys
        """
        query_string = [('search', "type:ssh"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/keys',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
