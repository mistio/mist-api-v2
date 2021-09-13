# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.frequency import Frequency  # noqa: E501
from mist_api_v2.models.get_rule_response import GetRuleResponse  # noqa: E501
from mist_api_v2.models.list_rules_response import ListRulesResponse  # noqa: E501
from mist_api_v2.models.query import Query  # noqa: E501
from mist_api_v2.models.rule import Rule  # noqa: E501
from mist_api_v2.models.rule_action import RuleAction  # noqa: E501
from mist_api_v2.models.selector import Selector  # noqa: E501
from mist_api_v2.models.trigger_after import TriggerAfter  # noqa: E501
from mist_api_v2.models.window import Window  # noqa: E501
from mist_api_v2.test import BaseTestCase

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1

class TestRulesController(BaseTestCase):
    """RulesController integration test stubs"""

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
            '/api/v2/rules/{rule}'.format(rule=example_rule),
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
            '/api/v2/rules/{rule}'.format(rule=example_rule),
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
            '/api/v2/rules/{rule}'.format(rule=example_rule),
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
            '/api/v2/rules/{rule}'.format(rule=example_rule),
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
            '/api/v2/rules/{rule}'.format(rule=example_rule),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
