# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.get_datapoints_response import GetDatapointsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestDatapointsController(BaseTestCase):
    """DatapointsController integration test stubs"""

    def test_get_datapoints(self):
        """Test case for get_datapoints

        Get datapoints
        """
        query_string = [('query', "'query_example'"),
                        ('tags', "'tags_example'"),
                        ('search', "'search_example'"),
                        ('start', "'start_example'"),
                        ('end', "'end_example'"),
                        ('step', "'step_example'"),
                        ('time', "'time_example'")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/datapoints',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
