# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cloud_features import CloudFeatures
from mist_api_v2.models.edit_cloud_request_any_of import EditCloudRequestAnyOf
from mist_api_v2 import util

from mist_api_v2.models.cloud_features import CloudFeatures  # noqa: E501
from mist_api_v2.models.edit_cloud_request_any_of import EditCloudRequestAnyOf  # noqa: E501

class EditCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, provider=None, credentials=None, features=None):  # noqa: E501
        """EditCloudRequest - a model defined in OpenAPI

        :param name: The name of this EditCloudRequest.  # noqa: E501
        :type name: str
        :param provider: The provider of this EditCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this EditCloudRequest.  # noqa: E501
        :type credentials: object
        :param features: The features of this EditCloudRequest.  # noqa: E501
        :type features: CloudFeatures
        """
        self.openapi_types = {
            'name': str,
            'provider': str,
            'credentials': object,
            'features': CloudFeatures
        }

        self.attribute_map = {
            'name': 'name',
            'provider': 'provider',
            'credentials': 'credentials',
            'features': 'features'
        }

        self._name = name
        self._provider = provider
        self._credentials = credentials
        self._features = features

    @classmethod
    def from_dict(cls, dikt) -> 'EditCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EditCloudRequest of this EditCloudRequest.  # noqa: E501
        :rtype: EditCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this EditCloudRequest.

        Updated name  # noqa: E501

        :return: The name of this EditCloudRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EditCloudRequest.

        Updated name  # noqa: E501

        :param name: The name of this EditCloudRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this EditCloudRequest.


        :return: The provider of this EditCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this EditCloudRequest.


        :param provider: The provider of this EditCloudRequest.
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
        """Gets the credentials of this EditCloudRequest.


        :return: The credentials of this EditCloudRequest.
        :rtype: object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this EditCloudRequest.


        :param credentials: The credentials of this EditCloudRequest.
        :type credentials: object
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this EditCloudRequest.


        :return: The features of this EditCloudRequest.
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this EditCloudRequest.


        :param features: The features of this EditCloudRequest.
        :type features: CloudFeatures
        """

        self._features = features
