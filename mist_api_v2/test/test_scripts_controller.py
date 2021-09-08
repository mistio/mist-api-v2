# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.get_script_response import GetScriptResponse  # noqa: E501
from mist_api_v2.models.list_scripts_response import ListScriptsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestScriptsController(BaseTestCase):
    """ScriptsController integration test stubs"""

    def test_delete_script(self):
        """Test case for delete_script

        Delete script
        """
        print('Hello@@@@@@@@')
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='script_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_script(self):
        """Test case for edit_script

        Edit script
        """
        print('Hello@@@@@@@@')
        query_string = [('name', "'name_example'"),
                        ('description', "'description_example'")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='script_example'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_script(self):
        """Test case for get_script

        Get script
        """
        print('Hello@@@@@@@@')
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='script_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_scripts(self):
        """Test case for list_scripts

        List scripts
        """
        print('Hello@@@@@@@@')
        query_string = [('search', "install-tensorflow"),
                        ('sort', "-name"),
                        ('start', "3"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
