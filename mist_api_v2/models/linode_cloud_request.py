# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cloud_features import CloudFeatures
from mist_api_v2.models.linode_credentials import LinodeCredentials
from mist_api_v2 import util

from mist_api_v2.models.cloud_features import CloudFeatures  # noqa: E501
from mist_api_v2.models.linode_credentials import LinodeCredentials  # noqa: E501

class LinodeCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None, features=None):  # noqa: E501
        """LinodeCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this LinodeCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this LinodeCloudRequest.  # noqa: E501
        :type credentials: LinodeCredentials
        :param features: The features of this LinodeCloudRequest.  # noqa: E501
        :type features: CloudFeatures
        """
        self.openapi_types = {
            'provider': str,
            'credentials': LinodeCredentials,
            'features': CloudFeatures
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
    def from_dict(cls, dikt) -> 'LinodeCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinodeCloudRequest of this LinodeCloudRequest.  # noqa: E501
        :rtype: LinodeCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this LinodeCloudRequest.


        :return: The provider of this LinodeCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this LinodeCloudRequest.


        :param provider: The provider of this LinodeCloudRequest.
        :type provider: str
        """
        allowed_values = ["linode"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this LinodeCloudRequest.


        :return: The credentials of this LinodeCloudRequest.
        :rtype: LinodeCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this LinodeCloudRequest.


        :param credentials: The credentials of this LinodeCloudRequest.
        :type credentials: LinodeCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this LinodeCloudRequest.


        :return: The features of this LinodeCloudRequest.
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this LinodeCloudRequest.


        :param features: The features of this LinodeCloudRequest.
        :type features: CloudFeatures
        """

        self._features = features