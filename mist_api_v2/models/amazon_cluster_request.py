# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AmazonClusterRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, role_arn=None, network=None, subnets=None, security_groups=None):  # noqa: E501
        """AmazonClusterRequest - a model defined in OpenAPI

        :param role_arn: The role_arn of this AmazonClusterRequest.  # noqa: E501
        :type role_arn: str
        :param network: The network of this AmazonClusterRequest.  # noqa: E501
        :type network: str
        :param subnets: The subnets of this AmazonClusterRequest.  # noqa: E501
        :type subnets: List[str]
        :param security_groups: The security_groups of this AmazonClusterRequest.  # noqa: E501
        :type security_groups: List[str]
        """
        self.openapi_types = {
            'role_arn': str,
            'network': str,
            'subnets': List[str],
            'security_groups': List[str]
        }

        self.attribute_map = {
            'role_arn': 'role_arn',
            'network': 'network',
            'subnets': 'subnets',
            'security_groups': 'security_groups'
        }

        self._role_arn = role_arn
        self._network = network
        self._subnets = subnets
        self._security_groups = security_groups

    @classmethod
    def from_dict(cls, dikt) -> 'AmazonClusterRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmazonClusterRequest of this AmazonClusterRequest.  # noqa: E501
        :rtype: AmazonClusterRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def role_arn(self):
        """Gets the role_arn of this AmazonClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf  # noqa: E501

        :return: The role_arn of this AmazonClusterRequest.
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this AmazonClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf  # noqa: E501

        :param role_arn: The role_arn of this AmazonClusterRequest.
        :type role_arn: str
        """
        if role_arn is None:
            raise ValueError("Invalid value for `role_arn`, must not be `None`")  # noqa: E501

        self._role_arn = role_arn

    @property
    def network(self):
        """Gets the network of this AmazonClusterRequest.

        Name or ID of the network to be associated with the cluster. If not given the default network will be selected  # noqa: E501

        :return: The network of this AmazonClusterRequest.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this AmazonClusterRequest.

        Name or ID of the network to be associated with the cluster. If not given the default network will be selected  # noqa: E501

        :param network: The network of this AmazonClusterRequest.
        :type network: str
        """

        self._network = network

    @property
    def subnets(self):
        """Gets the subnets of this AmazonClusterRequest.

        IDs of the subnets to be associated with the cluster. At least 2 subnets in different availability zones are required, if not given the default subnets will be used  # noqa: E501

        :return: The subnets of this AmazonClusterRequest.
        :rtype: List[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this AmazonClusterRequest.

        IDs of the subnets to be associated with the cluster. At least 2 subnets in different availability zones are required, if not given the default subnets will be used  # noqa: E501

        :param subnets: The subnets of this AmazonClusterRequest.
        :type subnets: List[str]
        """

        self._subnets = subnets

    @property
    def security_groups(self):
        """Gets the security_groups of this AmazonClusterRequest.

        The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane  # noqa: E501

        :return: The security_groups of this AmazonClusterRequest.
        :rtype: List[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this AmazonClusterRequest.

        The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane  # noqa: E501

        :param security_groups: The security_groups of this AmazonClusterRequest.
        :type security_groups: List[str]
        """

        self._security_groups = security_groups
