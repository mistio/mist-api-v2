# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AddCloudRequestAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, provider=None):  # noqa: E501
        """AddCloudRequestAllOf - a model defined in OpenAPI

        :param name: The name of this AddCloudRequestAllOf.  # noqa: E501
        :type name: str
        :param provider: The provider of this AddCloudRequestAllOf.  # noqa: E501
        :type provider: str
        """
        self.openapi_types = {
            'name': str,
            'provider': str
        }

        self.attribute_map = {
            'name': 'name',
            'provider': 'provider'
        }

        self._name = name
        self._provider = provider

    @classmethod
    def from_dict(cls, dikt) -> 'AddCloudRequestAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddCloudRequest_allOf of this AddCloudRequestAllOf.  # noqa: E501
        :rtype: AddCloudRequestAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AddCloudRequestAllOf.

        The name of the cloud to add  # noqa: E501

        :return: The name of this AddCloudRequestAllOf.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddCloudRequestAllOf.

        The name of the cloud to add  # noqa: E501

        :param name: The name of this AddCloudRequestAllOf.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this AddCloudRequestAllOf.

        The provider of the cloud  # noqa: E501

        :return: The provider of this AddCloudRequestAllOf.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AddCloudRequestAllOf.

        The provider of the cloud  # noqa: E501

        :param provider: The provider of this AddCloudRequestAllOf.
        :type provider: str
        """
        allowed_values = ["alibaba", "amazon", "azure", "cloudsigma", "digitalocean", "equinix", "google", "ibm", "kvm", "kubevirt", "kubernetes", "openshift", "linode", "lxd", "maxihost", "onapp", "openstack", "other", "rackspace", "vcloud", "vsphere", "vultr"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider
