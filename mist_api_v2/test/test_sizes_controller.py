# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.get_size_response import GetSizeResponse  # noqa: E501
from mist_api_v2.models.list_sizes_response import ListSizesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: -1 if any(k in y for k in ['delete', 'remove']) else 1


class TestSizesController(BaseTestCase):
    """SizesController integration test stubs"""

    def test_get_size(self):
        """Test case for get_size

        Get size
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/sizes/{size}'.format(size="'size_example'"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_sizes(self):
        """Test case for list_sizes

        List sizes
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
            '/api/v2/sizes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
