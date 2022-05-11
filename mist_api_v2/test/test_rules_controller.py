# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.add_rule_request import AddRuleRequest  # noqa: E501
from mist_api_v2.models.edit_rule_request import EditRuleRequest  # noqa: E501
from mist_api_v2.models.get_rule_response import GetRuleResponse  # noqa: E501
from mist_api_v2.models.list_rules_response import ListRulesResponse  # noqa: E501
from mist_api_v2.models.rule import Rule  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestRulesController(BaseTestCase):
    """RulesController integration test stubs"""

    def test_add_rule(self):
        """Test case for add_rule

        Add rule
        """
        add_rule_request = {
  "trigger_after" : {
    "period" : "period",
    "offset" : 5
  },
  "data_type" : "logs",
  "window" : {
    "period" : "period",
    "stop" : 1,
    "start" : 6
  },
  "queries" : [ {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  }, {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  } ],
  "actions" : [ {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  }, {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  } ],
  "frequency" : {
    "period" : "period",
    "every" : 5
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/rules',
            method='POST',
            headers=headers,
            data=json.dumps(add_rule_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rule(self):
        """Test case for delete_rule

        Delete rule
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule='my-rule'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_rule(self):
        """Test case for edit_rule

        Update rule
        """
        edit_rule_request = {
  "trigger_after" : {
    "period" : "period",
    "offset" : 5
  },
  "window" : {
    "period" : "period",
    "stop" : 1,
    "start" : 6
  },
  "queries" : [ {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  }, {
    "threshold" : 0.8008281904610115,
    "aggregation" : "aggregation",
    "operator" : "operator",
    "target" : "target"
  } ],
  "actions" : [ {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  }, {
    "emails" : [ "emails", "emails" ],
    "teams" : [ "teams", "teams" ],
    "action" : "action",
    "type" : "type",
    "users" : [ "users", "users" ],
    "command" : "command"
  } ],
  "frequency" : {
    "period" : "period",
    "every" : 5
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule='my-rule'),
            method='POST',
            headers=headers,
            data=json.dumps(edit_rule_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rule(self):
        """Test case for get_rule

        Get rule
        """
        query_string = [('sort', '-name'),
                        ('only', 'id')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule='my-rule'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_rules(self):
        """Test case for list_rules

        List rules
        """
        query_string = [('search', 'total_run_count:5'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('at', '2021-07-21T17:32:28Z')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
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
        query_string = [('name', 'my-renamed-rule')]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule='my-rule'),
            method='PATCH',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_toggle_rule(self):
        """Test case for toggle_rule

        Toggle rule
        """
        query_string = [('action', 'disable')]
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/rules/{rule}'.format(rule='my-rule'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
