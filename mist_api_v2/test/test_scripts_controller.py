# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.add_script_request import AddScriptRequest  # noqa: E501
from mist_api_v2.models.get_script_response import GetScriptResponse  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.inline_response2001 import InlineResponse2001  # noqa: E501
from mist_api_v2.models.list_scripts_response import ListScriptsResponse  # noqa: E501
from mist_api_v2.models.run_script_request import RunScriptRequest  # noqa: E501
from mist_api_v2.models.run_script_response import RunScriptResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestScriptsController(BaseTestCase):
    """ScriptsController integration test stubs"""

    def test_add_script(self):
        """Test case for add_script

        Add script
        """
        add_script_request = {
  "entrypoint" : "entrypoint.sh",
  "name" : "my-script",
  "description" : "description",
  "exec_type" : "executable",
  "script" : "#!/usr/bin/env bash\necho Hello, World!",
  "location_type" : "inline"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/scripts',
            method='POST',
            headers=headers,
            data=json.dumps(add_script_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_script(self):
        """Test case for delete_script

        Delete script
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='my-script'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_download_script(self):
        """Test case for download_script

        Download script
        """
        headers = { 
            'Accept': 'application/octet-stream',
        }
        response = self.client.open(
            '/api/v2/scripts/{script}/file'.format(script='my-script'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_script(self):
        """Test case for edit_script

        Edit script
        """
        query_string = [('name', 'my-renamed-script'),
                        ('description', 'description')]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='my-script'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generate_script_url(self):
        """Test case for generate_script_url

        Generate script url
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/scripts/{script}/url'.format(script='my-script'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_script(self):
        """Test case for get_script

        Get script
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='my-script'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_scripts(self):
        """Test case for list_scripts

        List scripts
        """
        query_string = [('search', 'my-script'),
                        ('sort', '-name'),
                        ('start', '3'),
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
            '/api/v2/scripts',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_script(self):
        """Test case for run_script

        Run script
        """
        run_script_request = {
  "su" : "false",
  "machine" : "my-machine",
  "job_id" : "ab74e2f0b7ae4999b1e4013e20dac418",
  "params" : "-v",
  "env" : "EXAMPLE_VAR=123"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script='my-script'),
            method='POST',
            headers=headers,
            data=json.dumps(run_script_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
