# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cloud_features import CloudFeatures
from mist_api_v2.models.supported_providers import SupportedProviders
from mist_api_v2 import util

from mist_api_v2.models.cloud_features import CloudFeatures  # noqa: E501
from mist_api_v2.models.supported_providers import SupportedProviders  # noqa: E501

class GenericCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None, features=None):  # noqa: E501
        """GenericCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this GenericCloudRequest.  # noqa: E501
        :type provider: SupportedProviders
        :param credentials: The credentials of this GenericCloudRequest.  # noqa: E501
        :type credentials: object
        :param features: The features of this GenericCloudRequest.  # noqa: E501
        :type features: CloudFeatures
        """
        self.openapi_types = {
            'provider': SupportedProviders,
            'credentials': object,
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
    def from_dict(cls, dikt) -> 'GenericCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GenericCloudRequest of this GenericCloudRequest.  # noqa: E501
        :rtype: GenericCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this GenericCloudRequest.


        :return: The provider of this GenericCloudRequest.
        :rtype: SupportedProviders
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this GenericCloudRequest.


        :param provider: The provider of this GenericCloudRequest.
        :type provider: SupportedProviders
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this GenericCloudRequest.


        :return: The credentials of this GenericCloudRequest.
        :rtype: object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this GenericCloudRequest.


        :param credentials: The credentials of this GenericCloudRequest.
        :type credentials: object
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this GenericCloudRequest.


        :return: The features of this GenericCloudRequest.
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this GenericCloudRequest.


        :param features: The features of this GenericCloudRequest.
        :type features: CloudFeatures
        """

        self._features = features
