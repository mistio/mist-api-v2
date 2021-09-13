# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.get_datapoints_response import GetDatapointsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1

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
            'Authorization': create_short_lived_token(),
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
