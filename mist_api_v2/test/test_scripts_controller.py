# coding: utf-8

from __future__ import absolute_import
import time
import importlib
import unittest

from flask import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.test import BaseTestCase

try:
    setup_module_name = 'ScriptsController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXIST = False
else:
    SETUP_MODULES_EXIST = True


def post_delay(seconds):
    def decorator(func):
        def wrapper(self):
            func(self)
            time.sleep(seconds)
        return wrapper
    return decorator


unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1


class TestScriptsController(BaseTestCase):
    """ScriptsController integration test stubs"""

    if SETUP_MODULES_EXIST:
        @classmethod
        def get_test_client(cls):
            if not hasattr(cls, 'test_client'):
                cls.test_client = cls().create_app().test_client()
            return cls.test_client

        @classmethod
        def setUpClass(cls):
            setup_module.setup(cls.get_test_client())

        @classmethod
        def tearDownClass(cls):
            setup_module.teardown(cls.get_test_client())

    def test_delete_script(self):
        """Test case for delete_script

        Delete script
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script="example_script"),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_script(self):
        """Test case for edit_script

        Edit script
        """
        query_string = [('name', "example_script"),
                        ('description', "'description_example'")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script="example_script"),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_script(self):
        """Test case for get_script

        Get script
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/scripts/{script}'.format(script="example_script"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_scripts(self):
        """Test case for list_scripts

        List scripts
        """
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



if setup_module_name == 'clusters':
    TestScriptsController.test_create_cluster = post_delay(seconds=200)(
        TestScriptsController.test_create_cluster)

if __name__ == '__main__':
    unittest.main()
