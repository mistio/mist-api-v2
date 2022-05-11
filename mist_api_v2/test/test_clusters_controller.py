# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.create_cluster_request import CreateClusterRequest  # noqa: E501
from mist_api_v2.models.create_cluster_response import CreateClusterResponse  # noqa: E501
from mist_api_v2.models.destroy_cluster_response import DestroyClusterResponse  # noqa: E501
from mist_api_v2.models.get_cluster_response import GetClusterResponse  # noqa: E501
from mist_api_v2.models.list_clusters_response import ListClustersResponse  # noqa: E501
from mist_api_v2.models.scale_nodepool_request import ScaleNodepoolRequest  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestClustersController(BaseTestCase):
    """ClustersController integration test stubs"""

    def test_create_cluster(self):
        """Test case for create_cluster

        Create cluster
        """
        create_cluster_request = {
  "name" : "my-cluster",
  "provider" : "google",
  "location" : "europe-west2-b"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clusters',
            method='POST',
            headers=headers,
            data=json.dumps(create_cluster_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_destroy_cluster(self):
        """Test case for destroy_cluster

        Destroy cluster
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clusters/{cluster}'.format(cluster='my-cluster'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cluster(self):
        """Test case for get_cluster

        Get cluster
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto'),
                        ('credentials', False)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clusters/{cluster}'.format(cluster='my-cluster'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_clusters(self):
        """Test case for list_clusters

        List clusters
        """
        query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'created_by:csk'),
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
            '/api/v2/clusters',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scale_nodepool(self):
        """Test case for scale_nodepool

        Scale cluster nodepool
        """
        scale_nodepool_request = {
  "desired_nodes" : 0,
  "max_nodes" : 1,
  "autoscaling" : true,
  "min_nodes" : 6
}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/clusters/{cluster}/nodepools/{nodepool}'.format(cluster='my-cluster', nodepool='my-nodepool-name'),
            method='POST',
            headers=headers,
            data=json.dumps(scale_nodepool_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
