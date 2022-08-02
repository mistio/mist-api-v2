# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CreateRecordRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, cloud=None, value=None, type='A', ttl=300):  # noqa: E501
        """CreateRecordRequest - a model defined in OpenAPI

        :param name: The name of this CreateRecordRequest.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this CreateRecordRequest.  # noqa: E501
        :type cloud: str
        :param value: The value of this CreateRecordRequest.  # noqa: E501
        :type value: str
        :param type: The type of this CreateRecordRequest.  # noqa: E501
        :type type: str
        :param ttl: The ttl of this CreateRecordRequest.  # noqa: E501
        :type ttl: int
        """
        self.openapi_types = {
            'name': str,
            'cloud': str,
            'value': str,
            'type': str,
            'ttl': int
        }

        self.attribute_map = {
            'name': 'name',
            'cloud': 'cloud',
            'value': 'value',
            'type': 'type',
            'ttl': 'ttl'
        }

        self._name = name
        self._cloud = cloud
        self._value = value
        self._type = type
        self._ttl = ttl

    @classmethod
    def from_dict(cls, dikt) -> 'CreateRecordRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateRecordRequest of this CreateRecordRequest.  # noqa: E501
        :rtype: CreateRecordRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateRecordRequest.


        :return: The name of this CreateRecordRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRecordRequest.


        :param name: The name of this CreateRecordRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this CreateRecordRequest.


        :return: The cloud of this CreateRecordRequest.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CreateRecordRequest.


        :param cloud: The cloud of this CreateRecordRequest.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def value(self):
        """Gets the value of this CreateRecordRequest.


        :return: The value of this CreateRecordRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateRecordRequest.


        :param value: The value of this CreateRecordRequest.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def type(self):
        """Gets the type of this CreateRecordRequest.


        :return: The type of this CreateRecordRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRecordRequest.


        :param type: The type of this CreateRecordRequest.
        :type type: str
        """
        allowed_values = ["A", "AAAA", "CNAME"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this CreateRecordRequest.


        :return: The ttl of this CreateRecordRequest.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateRecordRequest.


        :param ttl: The ttl of this CreateRecordRequest.
        :type ttl: int
        """

        self._ttl = ttl
