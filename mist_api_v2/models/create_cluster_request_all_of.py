# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cluster_providers import ClusterProviders
from mist_api_v2 import util

from mist_api_v2.models.cluster_providers import ClusterProviders  # noqa: E501

class CreateClusterRequestAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title=None, provider=None):  # noqa: E501
        """CreateClusterRequestAllOf - a model defined in OpenAPI

        :param title: The title of this CreateClusterRequestAllOf.  # noqa: E501
        :type title: str
        :param provider: The provider of this CreateClusterRequestAllOf.  # noqa: E501
        :type provider: ClusterProviders
        """
        self.openapi_types = {
            'title': str,
            'provider': ClusterProviders
        }

        self.attribute_map = {
            'title': 'title',
            'provider': 'provider'
        }

        self._title = title
        self._provider = provider

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClusterRequestAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClusterRequest_allOf of this CreateClusterRequestAllOf.  # noqa: E501
        :rtype: CreateClusterRequestAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self):
        """Gets the title of this CreateClusterRequestAllOf.

        The name of the cluster to create  # noqa: E501

        :return: The title of this CreateClusterRequestAllOf.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateClusterRequestAllOf.

        The name of the cluster to create  # noqa: E501

        :param title: The title of this CreateClusterRequestAllOf.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def provider(self):
        """Gets the provider of this CreateClusterRequestAllOf.


        :return: The provider of this CreateClusterRequestAllOf.
        :rtype: ClusterProviders
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateClusterRequestAllOf.


        :param provider: The provider of this CreateClusterRequestAllOf.
        :type provider: ClusterProviders
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider
