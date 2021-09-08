# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token

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
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/jobs/{job_id}'.format(job_id='job_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
