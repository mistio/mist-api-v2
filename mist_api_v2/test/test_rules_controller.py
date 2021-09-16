# coding: utf-8

from __future__ import absolute_import
import importlib
import unittest

from flask import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.test import BaseTestCase

try:
    setup_module_name = 'RulesController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXISTS = False
else:
    SETUP_MODULES_EXISTS = True

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1


class TestRulesController(BaseTestCase):
    """RulesController integration test stubs"""

    if SETUP_MODULES_EXISTS:
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

    def test_add_rule(self):
        """Test case for add_rule

        Add rule
        """
        query_string = [('queries', "{}"),
                        ('window', "{}"),
                        ('frequency', "{}"),
                        ('trigger_after', "{}"),
                        ('actions', "{}"),
                        ('selectors', "{}")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rule(self):
        """Test case for delete_rule

        Delete rule
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule="example_rule"),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rule(self):
        """Test case for get_rule

        Get rule
        """
        query_string = [('sort', "-name"),
                        ('only', "id")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule="example_rule"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rules(self):
        """Test case for list_rules

        List rules
        """
        query_string = [('search', "total_run_count:5"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rename_rule(self):
        """Test case for rename_rule

        Rename rule
        """
        query_string = [('action', "renamed_example_rule")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule="example_rule"),
            method='PATCH',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_toggle_rule(self):
        """Test case for toggle_rule

        Toggle rule
        """
        query_string = [('action', "example_action")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule="example_rule"),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_rule(self):
        """Test case for update_rule

        Update rule
        """
        query_string = [('queries', "{}"),
                        ('window', "{}"),
                        ('frequency', "{}"),
                        ('trigger_after', "{}"),
                        ('actions', "{}"),
                        ('selectors', "{}")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule="example_rule"),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
