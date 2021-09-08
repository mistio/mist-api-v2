# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token

from mist_api_v2.models.get_org_member_response import GetOrgMemberResponse  # noqa: E501
from mist_api_v2.models.get_org_response import GetOrgResponse  # noqa: E501
from mist_api_v2.models.list_org_members_response import ListOrgMembersResponse  # noqa: E501
from mist_api_v2.models.list_org_teams_response import ListOrgTeamsResponse  # noqa: E501
from mist_api_v2.models.list_orgs_response import ListOrgsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestOrgsController(BaseTestCase):
    """OrgsController integration test stubs"""

    def test_get_member(self):
        """Test case for get_member

        Get Org
        """
        query_string = [('only', "id")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/orgs/{org}/members/{member}'.format(org='org_example', member='member_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org(self):
        """Test case for get_org

        Get Org
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/orgs/{org}'.format(org='org_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_org_members(self):
        """Test case for list_org_members

        List org members
        """
        query_string = [('search', "email:dev@mist.io"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/orgs/{org}/members'.format(org='org_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_org_teams(self):
        """Test case for list_org_teams

        List org teams
        """
        query_string = [('search', "name:finance"),
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
            '/api/v2/orgs/{org}/teams'.format(org='org_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_orgs(self):
        """Test case for list_orgs

        List orgs
        """
        query_string = [('allorgs', "'allorgs_example'"),
                        ('search', "name:Acme"),
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
            '/api/v2/orgs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
