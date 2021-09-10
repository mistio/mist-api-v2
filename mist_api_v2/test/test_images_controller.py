# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.get_image_response import GetImageResponse  # noqa: E501
from mist_api_v2.models.list_images_response import ListImagesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: -1 if any(k in y for k in ['delete', 'remove']) else 1


class TestImagesController(BaseTestCase):
    """ImagesController integration test stubs"""

    def test_get_image(self):
        """Test case for get_image

        Get image
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/images/{image}'.format(image="'image_example'"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_images(self):
        """Test case for list_images

        List images
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "os_type:windows"),
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
            '/api/v2/images',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
