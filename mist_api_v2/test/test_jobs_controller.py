# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.get_job_response import GetJobResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestJobsController(BaseTestCase):
    """JobsController integration test stubs"""

    def test_get_job(self):
        """Test case for get_job

        Get job
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/jobs/{job_id}'.format(job_id='ab74e2f0b7ae4999b1e4013e20dac418'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
