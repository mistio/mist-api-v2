# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.kubernetes_cloud_features import KubernetesCloudFeatures
from mist_api_v2.models.kubernetes_credentials import KubernetesCredentials
from mist_api_v2 import util

from mist_api_v2.models.kubernetes_cloud_features import KubernetesCloudFeatures  # noqa: E501
from mist_api_v2.models.kubernetes_credentials import KubernetesCredentials  # noqa: E501

class KubernetesCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None, features=None):  # noqa: E501
        """KubernetesCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this KubernetesCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this KubernetesCloudRequest.  # noqa: E501
        :type credentials: KubernetesCredentials
        :param features: The features of this KubernetesCloudRequest.  # noqa: E501
        :type features: KubernetesCloudFeatures
        """
        self.openapi_types = {
            'provider': str,
            'credentials': KubernetesCredentials,
            'features': KubernetesCloudFeatures
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
    def from_dict(cls, dikt) -> 'KubernetesCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KubernetesCloudRequest of this KubernetesCloudRequest.  # noqa: E501
        :rtype: KubernetesCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this KubernetesCloudRequest.


        :return: The provider of this KubernetesCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this KubernetesCloudRequest.


        :param provider: The provider of this KubernetesCloudRequest.
        :type provider: str
        """
        allowed_values = ["kubernetes"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this KubernetesCloudRequest.


        :return: The credentials of this KubernetesCloudRequest.
        :rtype: KubernetesCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this KubernetesCloudRequest.


        :param credentials: The credentials of this KubernetesCloudRequest.
        :type credentials: KubernetesCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this KubernetesCloudRequest.


        :return: The features of this KubernetesCloudRequest.
        :rtype: KubernetesCloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this KubernetesCloudRequest.


        :param features: The features of this KubernetesCloudRequest.
        :type features: KubernetesCloudFeatures
        """

        self._features = features
