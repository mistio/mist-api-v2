# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.create_cluster_request_all_of import CreateClusterRequestAllOf
from mist_api_v2 import util

from mist_api_v2.models.create_cluster_request_all_of import CreateClusterRequestAllOf  # noqa: E501

class CreateClusterRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, cloud=None, provider=None, role_arn=None, network=None, subnets=None, security_groups=None, desired_nodes=None, nodegroup_role_arn=None, nodegroup_size=None, nodegroup_disk_size=None, location=None):  # noqa: E501
        """CreateClusterRequest - a model defined in OpenAPI

        :param name: The name of this CreateClusterRequest.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this CreateClusterRequest.  # noqa: E501
        :type cloud: str
        :param provider: The provider of this CreateClusterRequest.  # noqa: E501
        :type provider: str
        :param role_arn: The role_arn of this CreateClusterRequest.  # noqa: E501
        :type role_arn: str
        :param network: The network of this CreateClusterRequest.  # noqa: E501
        :type network: str
        :param subnets: The subnets of this CreateClusterRequest.  # noqa: E501
        :type subnets: List[str]
        :param security_groups: The security_groups of this CreateClusterRequest.  # noqa: E501
        :type security_groups: List[str]
        :param desired_nodes: The desired_nodes of this CreateClusterRequest.  # noqa: E501
        :type desired_nodes: float
        :param nodegroup_role_arn: The nodegroup_role_arn of this CreateClusterRequest.  # noqa: E501
        :type nodegroup_role_arn: str
        :param nodegroup_size: The nodegroup_size of this CreateClusterRequest.  # noqa: E501
        :type nodegroup_size: str
        :param nodegroup_disk_size: The nodegroup_disk_size of this CreateClusterRequest.  # noqa: E501
        :type nodegroup_disk_size: float
        :param location: The location of this CreateClusterRequest.  # noqa: E501
        :type location: str
        """
        self.openapi_types = {
            'name': str,
            'cloud': str,
            'provider': str,
            'role_arn': str,
            'network': str,
            'subnets': List[str],
            'security_groups': List[str],
            'desired_nodes': float,
            'nodegroup_role_arn': str,
            'nodegroup_size': str,
            'nodegroup_disk_size': float,
            'location': str
        }

        self.attribute_map = {
            'name': 'name',
            'cloud': 'cloud',
            'provider': 'provider',
            'role_arn': 'role_arn',
            'network': 'network',
            'subnets': 'subnets',
            'security_groups': 'security_groups',
            'desired_nodes': 'desired_nodes',
            'nodegroup_role_arn': 'nodegroup_role_arn',
            'nodegroup_size': 'nodegroup_size',
            'nodegroup_disk_size': 'nodegroup_disk_size',
            'location': 'location'
        }

        self._name = name
        self._cloud = cloud
        self._provider = provider
        self._role_arn = role_arn
        self._network = network
        self._subnets = subnets
        self._security_groups = security_groups
        self._desired_nodes = desired_nodes
        self._nodegroup_role_arn = nodegroup_role_arn
        self._nodegroup_size = nodegroup_size
        self._nodegroup_disk_size = nodegroup_disk_size
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClusterRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClusterRequest of this CreateClusterRequest.  # noqa: E501
        :rtype: CreateClusterRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateClusterRequest.

        The cluster's name  # noqa: E501

        :return: The name of this CreateClusterRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClusterRequest.

        The cluster's name  # noqa: E501

        :param name: The name of this CreateClusterRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this CreateClusterRequest.

        The cloud the cluster belongs to  # noqa: E501

        :return: The cloud of this CreateClusterRequest.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CreateClusterRequest.

        The cloud the cluster belongs to  # noqa: E501

        :param cloud: The cloud of this CreateClusterRequest.
        :type cloud: str
        """
        if cloud is None:
            raise ValueError("Invalid value for `cloud`, must not be `None`")  # noqa: E501

        self._cloud = cloud

    @property
    def provider(self):
        """Gets the provider of this CreateClusterRequest.


        :return: The provider of this CreateClusterRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateClusterRequest.


        :param provider: The provider of this CreateClusterRequest.
        :type provider: str
        """
        allowed_values = ["amazon", "azure", "digitalocean", "google", "kubernetes", "openshift", "linode"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def role_arn(self):
        """Gets the role_arn of this CreateClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf  # noqa: E501

        :return: The role_arn of this CreateClusterRequest.
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this CreateClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf  # noqa: E501

        :param role_arn: The role_arn of this CreateClusterRequest.
        :type role_arn: str
        """
        if role_arn is None:
            raise ValueError("Invalid value for `role_arn`, must not be `None`")  # noqa: E501

        self._role_arn = role_arn

    @property
    def network(self):
        """Gets the network of this CreateClusterRequest.

        Name or ID of the network to be associated with the cluster. If not given the default network will be selected  # noqa: E501

        :return: The network of this CreateClusterRequest.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this CreateClusterRequest.

        Name or ID of the network to be associated with the cluster. If not given the default network will be selected  # noqa: E501

        :param network: The network of this CreateClusterRequest.
        :type network: str
        """

        self._network = network

    @property
    def subnets(self):
        """Gets the subnets of this CreateClusterRequest.

        IDs of the subnets to be associated with the cluster. At least 2 subnets in different availability zones are required, if not given the default subnets will be used  # noqa: E501

        :return: The subnets of this CreateClusterRequest.
        :rtype: List[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this CreateClusterRequest.

        IDs of the subnets to be associated with the cluster. At least 2 subnets in different availability zones are required, if not given the default subnets will be used  # noqa: E501

        :param subnets: The subnets of this CreateClusterRequest.
        :type subnets: List[str]
        """

        self._subnets = subnets

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateClusterRequest.

        The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane  # noqa: E501

        :return: The security_groups of this CreateClusterRequest.
        :rtype: List[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateClusterRequest.

        The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane  # noqa: E501

        :param security_groups: The security_groups of this CreateClusterRequest.
        :type security_groups: List[str]
        """

        self._security_groups = security_groups

    @property
    def desired_nodes(self):
        """Gets the desired_nodes of this CreateClusterRequest.

        The initial number of nodes to provision for the nodegroup. Defaults to 2  # noqa: E501

        :return: The desired_nodes of this CreateClusterRequest.
        :rtype: float
        """
        return self._desired_nodes

    @desired_nodes.setter
    def desired_nodes(self, desired_nodes):
        """Sets the desired_nodes of this CreateClusterRequest.

        The initial number of nodes to provision for the nodegroup. Defaults to 2  # noqa: E501

        :param desired_nodes: The desired_nodes of this CreateClusterRequest.
        :type desired_nodes: float
        """

        self._desired_nodes = desired_nodes

    @property
    def nodegroup_role_arn(self):
        """Gets the nodegroup_role_arn of this CreateClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role to associate with the node group  # noqa: E501

        :return: The nodegroup_role_arn of this CreateClusterRequest.
        :rtype: str
        """
        return self._nodegroup_role_arn

    @nodegroup_role_arn.setter
    def nodegroup_role_arn(self, nodegroup_role_arn):
        """Sets the nodegroup_role_arn of this CreateClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role to associate with the node group  # noqa: E501

        :param nodegroup_role_arn: The nodegroup_role_arn of this CreateClusterRequest.
        :type nodegroup_role_arn: str
        """

        self._nodegroup_role_arn = nodegroup_role_arn

    @property
    def nodegroup_size(self):
        """Gets the nodegroup_size of this CreateClusterRequest.

        Name or ID of size to use for the nodes. If not provided, the t3.medium size will be used  # noqa: E501

        :return: The nodegroup_size of this CreateClusterRequest.
        :rtype: str
        """
        return self._nodegroup_size

    @nodegroup_size.setter
    def nodegroup_size(self, nodegroup_size):
        """Sets the nodegroup_size of this CreateClusterRequest.

        Name or ID of size to use for the nodes. If not provided, the t3.medium size will be used  # noqa: E501

        :param nodegroup_size: The nodegroup_size of this CreateClusterRequest.
        :type nodegroup_size: str
        """

        self._nodegroup_size = nodegroup_size

    @property
    def nodegroup_disk_size(self):
        """Gets the nodegroup_disk_size of this CreateClusterRequest.

        The disk size for the nodegroup. Defaults to 20 GBs  # noqa: E501

        :return: The nodegroup_disk_size of this CreateClusterRequest.
        :rtype: float
        """
        return self._nodegroup_disk_size

    @nodegroup_disk_size.setter
    def nodegroup_disk_size(self, nodegroup_disk_size):
        """Sets the nodegroup_disk_size of this CreateClusterRequest.

        The disk size for the nodegroup. Defaults to 20 GBs  # noqa: E501

        :param nodegroup_disk_size: The nodegroup_disk_size of this CreateClusterRequest.
        :type nodegroup_disk_size: float
        """

        self._nodegroup_disk_size = nodegroup_disk_size

    @property
    def location(self):
        """Gets the location of this CreateClusterRequest.

        The name of the location to create the cluster in  # noqa: E501

        :return: The location of this CreateClusterRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateClusterRequest.

        The name of the location to create the cluster in  # noqa: E501

        :param location: The location of this CreateClusterRequest.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location
