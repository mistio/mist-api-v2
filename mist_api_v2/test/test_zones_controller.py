# coding: utf-8

from __future__ import absolute_import
import importlib
import unittest

from flask import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.test import BaseTestCase

try:
    setup_module_name = 'ZonesController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXIST = False
else:
    SETUP_MODULES_EXIST = True


def delay(seconds):
    def decorator(func):
        def wrapper(self):
            time.sleep(seconds)
            func(self)
        return wrapper
    return decorator


unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1


class TestZonesController(BaseTestCase):
    """ZonesController integration test stubs"""

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

    def test_create_zone(self):
        """Test case for create_zone

        Create zone
        """
        create_zone_request = {
  "name" : "example_zone",
  "cloud" : "example_cloud"
}
        inject_vault_credentials_into_request(create_zone_request)
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/zones',
            method='POST',
            headers=headers,
            data=json.dumps(create_zone_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_zone(self):
        """Test case for edit_zone

        Edit zone
        """
        query_string = [('name', "renamed_example_zone")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/zones/{zone}'.format(zone="example_zone"),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zone(self):
        """Test case for get_zone

        Get zone
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/zones/{zone}'.format(zone="example_zone"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_zones(self):
        """Test case for list_zones

        List zones
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
            '/api/v2/zones',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if setup_module_name == 'clusters':
    TestZonesController.test_destroy_cluster = delay(seconds=200)(
        TestZonesController.test_destroy_cluster)

if __name__ == '__main__':
    unittest.main()
