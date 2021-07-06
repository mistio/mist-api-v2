# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class KeyMachineDisassociation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key=None):  # noqa: E501
        """KeyMachineDisassociation - a model defined in OpenAPI

        :param key: The key of this KeyMachineDisassociation.  # noqa: E501
        :type key: str
        """
        self.openapi_types = {
            'key': str
        }

        self.attribute_map = {
            'key': 'key'
        }

        self._key = key

    @classmethod
    def from_dict(cls, dikt) -> 'KeyMachineDisassociation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KeyMachineDisassociation of this KeyMachineDisassociation.  # noqa: E501
        :rtype: KeyMachineDisassociation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this KeyMachineDisassociation.

        Name or ID of the SSH key to disassociate  # noqa: E501

        :return: The key of this KeyMachineDisassociation.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this KeyMachineDisassociation.

        Name or ID of the SSH key to disassociate  # noqa: E501

        :param key: The key of this KeyMachineDisassociation.
        :type key: str
        """

        self._key = key