# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.get_image_response import GetImageResponse  # noqa: E501
from mist_api_v2.models.list_images_response import ListImagesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestImagesController(BaseTestCase):
    """ImagesController integration test stubs"""

    def test_get_image(self):
        """Test case for get_image

        Get image
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/images/{image}'.format(image='ubuntu-1604-xenial-v20210928'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_images(self):
        """Test case for list_images

        List images
        """
        query_string = [('cloud', 'my-cloud'),
                        ('search', 'os_type:windows'),
                        ('sort', '-name'),
                        ('start', '50'),
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
            '/api/v2/images',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
