# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AzureCredentials(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tenant_id=None, subscription_id=None, key=None, secret=None):  # noqa: E501
        """AzureCredentials - a model defined in OpenAPI

        :param tenant_id: The tenant_id of this AzureCredentials.  # noqa: E501
        :type tenant_id: str
        :param subscription_id: The subscription_id of this AzureCredentials.  # noqa: E501
        :type subscription_id: str
        :param key: The key of this AzureCredentials.  # noqa: E501
        :type key: str
        :param secret: The secret of this AzureCredentials.  # noqa: E501
        :type secret: str
        """
        self.openapi_types = {
            'tenant_id': str,
            'subscription_id': str,
            'key': str,
            'secret': str
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'subscription_id': 'subscriptionId',
            'key': 'key',
            'secret': 'secret'
        }

        self._tenant_id = tenant_id
        self._subscription_id = subscription_id
        self._key = key
        self._secret = secret

    @classmethod
    def from_dict(cls, dikt) -> 'AzureCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AzureCredentials of this AzureCredentials.  # noqa: E501
        :rtype: AzureCredentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureCredentials.

        Your Azure tenant ID  # noqa: E501

        :return: The tenant_id of this AzureCredentials.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureCredentials.

        Your Azure tenant ID  # noqa: E501

        :param tenant_id: The tenant_id of this AzureCredentials.
        :type tenant_id: str
        """

        self._tenant_id = tenant_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AzureCredentials.

        Your Azure subscription ID  # noqa: E501

        :return: The subscription_id of this AzureCredentials.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AzureCredentials.

        Your Azure subscription ID  # noqa: E501

        :param subscription_id: The subscription_id of this AzureCredentials.
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def key(self):
        """Gets the key of this AzureCredentials.

        Your Azure key  # noqa: E501

        :return: The key of this AzureCredentials.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AzureCredentials.

        Your Azure key  # noqa: E501

        :param key: The key of this AzureCredentials.
        :type key: str
        """

        self._key = key

    @property
    def secret(self):
        """Gets the secret of this AzureCredentials.

        Your Azure secret  # noqa: E501

        :return: The secret of this AzureCredentials.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this AzureCredentials.

        Your Azure secret  # noqa: E501

        :param secret: The secret of this AzureCredentials.
        :type secret: str
        """

        self._secret = secret