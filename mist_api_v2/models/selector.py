# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class Selector(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, ids=None, include=None):  # noqa: E501
        """Selector - a model defined in OpenAPI

        :param type: The type of this Selector.  # noqa: E501
        :type type: str
        :param ids: The ids of this Selector.  # noqa: E501
        :type ids: List[str]
        :param include: The include of this Selector.  # noqa: E501
        :type include: List[str]
        """
        self.openapi_types = {
            'type': str,
            'ids': List[str],
            'include': List[str]
        }

        self.attribute_map = {
            'type': 'type',
            'ids': 'ids',
            'include': 'include'
        }

        self._type = type
        self._ids = ids
        self._include = include

    @classmethod
    def from_dict(cls, dikt) -> 'Selector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Selector of this Selector.  # noqa: E501
        :rtype: Selector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this Selector.

        one of \"machines\" or \"tags\"  # noqa: E501

        :return: The type of this Selector.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Selector.

        one of \"machines\" or \"tags\"  # noqa: E501

        :param type: The type of this Selector.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ids(self):
        """Gets the ids of this Selector.

        a list of UUIDs in case type is \"machines\"  # noqa: E501

        :return: The ids of this Selector.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this Selector.

        a list of UUIDs in case type is \"machines\"  # noqa: E501

        :param ids: The ids of this Selector.
        :type ids: List[str]
        """

        self._ids = ids

    @property
    def include(self):
        """Gets the include of this Selector.

        a list of tags in case type is \"tags\"  # noqa: E501

        :return: The include of this Selector.
        :rtype: List[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this Selector.

        a list of tags in case type is \"tags\"  # noqa: E501

        :param include: The include of this Selector.
        :type include: List[str]
        """

        self._include = include
