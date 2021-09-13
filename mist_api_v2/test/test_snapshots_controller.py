# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.models.list_snapshots_response import ListSnapshotsResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: -1 if any(k in y for k in ['delete', 'remove']) else 1


class TestSnapshotsController(BaseTestCase):
    """SnapshotsController integration test stubs"""

    def test_create_snapshot(self):
        """Test case for create_snapshot

        Create snapshot
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots'.format(machine="example_machine"),
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
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots'.format(machine="example_machine"),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_snapshot(self):
        """Test case for remove_snapshot

        Remove snapshot
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(machine="example_machine", snapshot="example_snapshot"),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_revert_to_snapshot(self):
        """Test case for revert_to_snapshot

        Revert to snapshot
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(machine="example_machine", snapshot="example_snapshot"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
