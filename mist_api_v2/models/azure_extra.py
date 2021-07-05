# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AzureExtra(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource_group=None, storage_account_type=None, user=None, password=None):  # noqa: E501
        """AzureExtra - a model defined in OpenAPI

        :param resource_group: The resource_group of this AzureExtra.  # noqa: E501
        :type resource_group: str
        :param storage_account_type: The storage_account_type of this AzureExtra.  # noqa: E501
        :type storage_account_type: str
        :param user: The user of this AzureExtra.  # noqa: E501
        :type user: str
        :param password: The password of this AzureExtra.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'resource_group': str,
            'storage_account_type': str,
            'user': str,
            'password': str
        }

        self.attribute_map = {
            'resource_group': 'resource_group',
            'storage_account_type': 'storage_account_type',
            'user': 'user',
            'password': 'password'
        }

        self._resource_group = resource_group
        self._storage_account_type = storage_account_type
        self._user = user
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'AzureExtra':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AzureExtra of this AzureExtra.  # noqa: E501
        :rtype: AzureExtra
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_group(self):
        """Gets the resource_group of this AzureExtra.

        A new or existing resource group. If not provided a `mist` resource group will be used.  # noqa: E501

        :return: The resource_group of this AzureExtra.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this AzureExtra.

        A new or existing resource group. If not provided a `mist` resource group will be used.  # noqa: E501

        :param resource_group: The resource_group of this AzureExtra.
        :type resource_group: str
        """

        self._resource_group = resource_group

    @property
    def storage_account_type(self):
        """Gets the storage_account_type of this AzureExtra.

        Specifies the storage account type for the OS disk. Defaults to `StandardSSD_LRS`  # noqa: E501

        :return: The storage_account_type of this AzureExtra.
        :rtype: str
        """
        return self._storage_account_type

    @storage_account_type.setter
    def storage_account_type(self, storage_account_type):
        """Sets the storage_account_type of this AzureExtra.

        Specifies the storage account type for the OS disk. Defaults to `StandardSSD_LRS`  # noqa: E501

        :param storage_account_type: The storage_account_type of this AzureExtra.
        :type storage_account_type: str
        """
        allowed_values = ["Premium_LRS", "Premium_ZRS", "StandardSSD_LRS", "StandardSSD_ZRS", "Standard_LRS"]  # noqa: E501
        if storage_account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `storage_account_type` ({0}), must be one of {1}"
                .format(storage_account_type, allowed_values)
            )

        self._storage_account_type = storage_account_type

    @property
    def user(self):
        """Gets the user of this AzureExtra.

        The machine username. Defaults to azureuser  # noqa: E501

        :return: The user of this AzureExtra.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AzureExtra.

        The machine username. Defaults to azureuser  # noqa: E501

        :param user: The user of this AzureExtra.
        :type user: str
        """

        self._user = user

    @property
    def password(self):
        """Gets the password of this AzureExtra.

        The machine password. Only used on Microsoft images  # noqa: E501

        :return: The password of this AzureExtra.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AzureExtra.

        The machine password. Only used on Microsoft images  # noqa: E501

        :param password: The password of this AzureExtra.
        :type password: str
        """

        self._password = password