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
    setup_module_name = 'VolumesController'.replace('Controller', '').lower()
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


class TestVolumesController(BaseTestCase):
    """VolumesController integration test stubs"""

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

    def test_create_volume(self):
        """Test case for create_volume

        Create volume
        """
        create_volume_request = {
  "name" : "example_volume",
  "size" : "example_size"
}
        inject_vault_credentials_into_request(create_volume_request)
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/volumes',
            method='POST',
            headers=headers,
            data=json.dumps(create_volume_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_volume(self):
        """Test case for delete_volume

        Delete volume
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/volumes/{volume}'.format(volume="example_volume"),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_volume(self):
        """Test case for edit_volume

        Edit volume
        """
        query_string = [('name', "renamed_example_volume")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/volumes/{volume}'.format(volume="example_volume"),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_volume(self):
        """Test case for get_volume

        Get volume
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/volumes/{volume}'.format(volume="example_volume"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_volumes(self):
        """Test case for list_volumes

        List volumes
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "location:Amsterdam"),
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
            '/api/v2/volumes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if setup_module_name == 'clusters':
    TestVolumesController.test_create_cluster = post_delay(seconds=200)(
        TestVolumesController.test_create_cluster)

if __name__ == '__main__':
    unittest.main()
