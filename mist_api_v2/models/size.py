# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class Size(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, external_id=None, name=None, cloud=None, extra=None):  # noqa: E501
        """Size - a model defined in OpenAPI

        :param id: The id of this Size.  # noqa: E501
        :type id: str
        :param external_id: The external_id of this Size.  # noqa: E501
        :type external_id: str
        :param name: The name of this Size.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this Size.  # noqa: E501
        :type cloud: str
        :param extra: The extra of this Size.  # noqa: E501
        :type extra: object
        """
        self.openapi_types = {
            'id': str,
            'external_id': str,
            'name': str,
            'cloud': str,
            'extra': object
        }

        self.attribute_map = {
            'id': 'id',
            'external_id': 'external_id',
            'name': 'name',
            'cloud': 'cloud',
            'extra': 'extra'
        }

        self._id = id
        self._external_id = external_id
        self._name = name
        self._cloud = cloud
        self._extra = extra

    @classmethod
    def from_dict(cls, dikt) -> 'Size':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Size of this Size.  # noqa: E501
        :rtype: Size
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Size.


        :return: The id of this Size.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Size.


        :param id: The id of this Size.
        :type id: str
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this Size.


        :return: The external_id of this Size.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Size.


        :param external_id: The external_id of this Size.
        :type external_id: str
        """

        self._external_id = external_id

    @property
    def name(self):
        """Gets the name of this Size.


        :return: The name of this Size.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Size.


        :param name: The name of this Size.
        :type name: str
        """

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this Size.


        :return: The cloud of this Size.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this Size.


        :param cloud: The cloud of this Size.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def extra(self):
        """Gets the extra of this Size.


        :return: The extra of this Size.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Size.


        :param extra: The extra of this Size.
        :type extra: object
        """

        self._extra = extra