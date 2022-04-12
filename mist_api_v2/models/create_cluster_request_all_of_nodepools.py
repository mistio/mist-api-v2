# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CreateClusterRequestAllOfNodepools(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, autoscaling=False, min_nodes=None, max_nodes=None, nodes=None, size=None, disk_size=20, disk_type=None, preemptible=None):  # noqa: E501
        """CreateClusterRequestAllOfNodepools - a model defined in OpenAPI

        :param autoscaling: The autoscaling of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type autoscaling: bool
        :param min_nodes: The min_nodes of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type min_nodes: int
        :param max_nodes: The max_nodes of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type max_nodes: int
        :param nodes: The nodes of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type nodes: int
        :param size: The size of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type size: str
        :param disk_size: The disk_size of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type disk_size: int
        :param role_arn: The role_arn of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type role_arn: str
        :param disk_type: The disk_type of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type disk_type: str
        :param preemptible: The preemptible of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :type preemptible: bool
        """
        self.openapi_types = {
            'autoscaling': bool,
            'min_nodes': int,
            'max_nodes': int,
            'nodes': int,
            'size': str,
            'disk_size': int,
            'role_arn': str,
            'disk_type': str,
            'preemptible': bool
        }

        self.attribute_map = {
            'autoscaling': 'autoscaling',
            'min_nodes': 'min_nodes',
            'max_nodes': 'max_nodes',
            'nodes': 'nodes',
            'size': 'size',
            'disk_size': 'disk_size',
            'role_arn': 'role_arn',
            'disk_type': 'disk_type',
            'preemptible': 'preemptible'
        }

        self._autoscaling = autoscaling
        self._min_nodes = min_nodes
        self._max_nodes = max_nodes
        self._nodes = nodes
        self._size = size
        self._disk_size = disk_size
        self._role_arn = role_arn
        self._disk_type = disk_type
        self._preemptible = preemptible

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClusterRequestAllOfNodepools':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClusterRequest_allOf_nodepools of this CreateClusterRequestAllOfNodepools.  # noqa: E501
        :rtype: CreateClusterRequestAllOfNodepools
        """
        return util.deserialize_model(dikt, cls)

    @property
    def autoscaling(self):
        """Gets the autoscaling of this CreateClusterRequestAllOfNodepools.

        GKE only, set to true to enable autoscaling, requires min_nodes and max_nodes to be set.  # noqa: E501

        :return: The autoscaling of this CreateClusterRequestAllOfNodepools.
        :rtype: bool
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this CreateClusterRequestAllOfNodepools.

        GKE only, set to true to enable autoscaling, requires min_nodes and max_nodes to be set.  # noqa: E501

        :param autoscaling: The autoscaling of this CreateClusterRequestAllOfNodepools.
        :type autoscaling: bool
        """

        self._autoscaling = autoscaling

    @property
    def min_nodes(self):
        """Gets the min_nodes of this CreateClusterRequestAllOfNodepools.

        The minimum number of nodes the autoscaler should maintain. On EKS nodepools if this value is not provided it will implicitly be set equal to nodes value  # noqa: E501

        :return: The min_nodes of this CreateClusterRequestAllOfNodepools.
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        """Sets the min_nodes of this CreateClusterRequestAllOfNodepools.

        The minimum number of nodes the autoscaler should maintain. On EKS nodepools if this value is not provided it will implicitly be set equal to nodes value  # noqa: E501

        :param min_nodes: The min_nodes of this CreateClusterRequestAllOfNodepools.
        :type min_nodes: int
        """

        self._min_nodes = min_nodes

    @property
    def max_nodes(self):
        """Gets the max_nodes of this CreateClusterRequestAllOfNodepools.

        The maximum number of nodes the autoscaler should maintain. On EKS nodepools if this value is not provided it will implicitly be set equal to nodes value  # noqa: E501

        :return: The max_nodes of this CreateClusterRequestAllOfNodepools.
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        """Sets the max_nodes of this CreateClusterRequestAllOfNodepools.

        The maximum number of nodes the autoscaler should maintain. On EKS nodepools if this value is not provided it will implicitly be set equal to nodes value  # noqa: E501

        :param max_nodes: The max_nodes of this CreateClusterRequestAllOfNodepools.
        :type max_nodes: int
        """

        self._max_nodes = max_nodes

    @property
    def nodes(self):
        """Gets the nodes of this CreateClusterRequestAllOfNodepools.

        The number of nodes to provision for the cluster  # noqa: E501

        :return: The nodes of this CreateClusterRequestAllOfNodepools.
        :rtype: int
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this CreateClusterRequestAllOfNodepools.

        The number of nodes to provision for the cluster  # noqa: E501

        :param nodes: The nodes of this CreateClusterRequestAllOfNodepools.
        :type nodes: int
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def size(self):
        """Gets the size of this CreateClusterRequestAllOfNodepools.

        Name or ID of size to use for the nodes. If not provided, the t3.medium(EKS) or e2-medium(GKE) size will be used  # noqa: E501

        :return: The size of this CreateClusterRequestAllOfNodepools.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateClusterRequestAllOfNodepools.

        Name or ID of size to use for the nodes. If not provided, the t3.medium(EKS) or e2-medium(GKE) size will be used  # noqa: E501

        :param size: The size of this CreateClusterRequestAllOfNodepools.
        :type size: str
        """

        self._size = size

    @property
    def disk_size(self):
        """Gets the disk_size of this CreateClusterRequestAllOfNodepools.

        Size of the disk attached to each node, specified in GB.  # noqa: E501

        :return: The disk_size of this CreateClusterRequestAllOfNodepools.
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this CreateClusterRequestAllOfNodepools.

        Size of the disk attached to each node, specified in GB.  # noqa: E501

        :param disk_size: The disk_size of this CreateClusterRequestAllOfNodepools.
        :type disk_size: int
        """

        self._disk_size = disk_size

    @property
    def role_arn(self):
        """Gets the role_arn of this CreateClusterRequestAllOfNodepools.

        Amazon specific parameter.The Amazon Resource Name (ARN) of the IAM role to associate with the nodes. Required in order to create a cluster nodepool  # noqa: E501

        :return: The role_arn of this CreateClusterRequestAllOfNodepools.
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this CreateClusterRequestAllOfNodepools.

        Amazon specific parameter.The Amazon Resource Name (ARN) of the IAM role to associate with the nodes. Required in order to create a cluster nodepool  # noqa: E501

        :param role_arn: The role_arn of this CreateClusterRequestAllOfNodepools.
        :type role_arn: str
        """

        self._role_arn = role_arn

    @property
    def disk_type(self):
        """Gets the disk_type of this CreateClusterRequestAllOfNodepools.

        Google specific parameter.Type of the disk attached to each node. Defaults to pd-standard  # noqa: E501

        :return: The disk_type of this CreateClusterRequestAllOfNodepools.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this CreateClusterRequestAllOfNodepools.

        Google specific parameter.Type of the disk attached to each node. Defaults to pd-standard  # noqa: E501

        :param disk_type: The disk_type of this CreateClusterRequestAllOfNodepools.
        :type disk_type: str
        """

        self._disk_type = disk_type

    @property
    def preemptible(self):
        """Gets the preemptible of this CreateClusterRequestAllOfNodepools.

        Google specific parameter.Whether the nodes are created as preemptible machines. Defaults to false  # noqa: E501

        :return: The preemptible of this CreateClusterRequestAllOfNodepools.
        :rtype: bool
        """
        return self._preemptible

    @preemptible.setter
    def preemptible(self, preemptible):
        """Sets the preemptible of this CreateClusterRequestAllOfNodepools.

        Google specific parameter.Whether the nodes are created as preemptible machines. Defaults to false  # noqa: E501

        :param preemptible: The preemptible of this CreateClusterRequestAllOfNodepools.
        :type preemptible: bool
        """

        self._preemptible = preemptible
