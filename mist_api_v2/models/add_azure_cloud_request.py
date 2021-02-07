# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.azure_credentials import AzureCredentials
from mist_api_v2 import util

from mist_api_v2.models.azure_credentials import AzureCredentials  # noqa: E501

class AddAzureCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None):  # noqa: E501
        """AddAzureCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this AddAzureCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this AddAzureCloudRequest.  # noqa: E501
        :type credentials: AzureCredentials
        """
        self.openapi_types = {
            'provider': str,
            'credentials': AzureCredentials
        }

        self.attribute_map = {
            'provider': 'provider',
            'credentials': 'credentials'
        }

        self._provider = provider
        self._credentials = credentials

    @classmethod
    def from_dict(cls, dikt) -> 'AddAzureCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddAzureCloudRequest of this AddAzureCloudRequest.  # noqa: E501
        :rtype: AddAzureCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this AddAzureCloudRequest.


        :return: The provider of this AddAzureCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AddAzureCloudRequest.


        :param provider: The provider of this AddAzureCloudRequest.
        :type provider: str
        """
        allowed_values = ["azure"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this AddAzureCloudRequest.


        :return: The credentials of this AddAzureCloudRequest.
        :rtype: AzureCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AddAzureCloudRequest.


        :param credentials: The credentials of this AddAzureCloudRequest.
        :type credentials: AzureCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials