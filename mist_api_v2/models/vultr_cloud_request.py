# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.vultr_cloud_features import VultrCloudFeatures
from mist_api_v2.models.vultr_credentials import VultrCredentials
from mist_api_v2 import util

from mist_api_v2.models.vultr_cloud_features import VultrCloudFeatures  # noqa: E501
from mist_api_v2.models.vultr_credentials import VultrCredentials  # noqa: E501

class VultrCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None, features=None):  # noqa: E501
        """VultrCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this VultrCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this VultrCloudRequest.  # noqa: E501
        :type credentials: VultrCredentials
        :param features: The features of this VultrCloudRequest.  # noqa: E501
        :type features: VultrCloudFeatures
        """
        self.openapi_types = {
            'provider': str,
            'credentials': VultrCredentials,
            'features': VultrCloudFeatures
        }

        self.attribute_map = {
            'provider': 'provider',
            'credentials': 'credentials',
            'features': 'features'
        }

        self._provider = provider
        self._credentials = credentials
        self._features = features

    @classmethod
    def from_dict(cls, dikt) -> 'VultrCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VultrCloudRequest of this VultrCloudRequest.  # noqa: E501
        :rtype: VultrCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this VultrCloudRequest.


        :return: The provider of this VultrCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VultrCloudRequest.


        :param provider: The provider of this VultrCloudRequest.
        :type provider: str
        """
        allowed_values = ["vultr"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this VultrCloudRequest.


        :return: The credentials of this VultrCloudRequest.
        :rtype: VultrCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this VultrCloudRequest.


        :param credentials: The credentials of this VultrCloudRequest.
        :type credentials: VultrCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this VultrCloudRequest.


        :return: The features of this VultrCloudRequest.
        :rtype: VultrCloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this VultrCloudRequest.


        :param features: The features of this VultrCloudRequest.
        :type features: VultrCloudFeatures
        """

        self._features = features
