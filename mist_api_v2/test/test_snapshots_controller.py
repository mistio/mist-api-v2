# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.list_snapshots_response import ListSnapshotsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestSnapshotsController(BaseTestCase):
    """SnapshotsController integration test stubs"""

    def test_create_snapshot(self):
        """Test case for create_snapshot

        Create snapshot
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_snapshots(self):
        """Test case for list_snapshots

        List machine snapshots
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots'.format(machine='machine_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_snapshot(self):
        """Test case for remove_snapshot

        Remove snapshot
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(machine='machine_example', snapshot='snapshot_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_revert_to_snapshot(self):
        """Test case for revert_to_snapshot

        Revert to snapshot
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(machine='machine_example', snapshot='snapshot_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
