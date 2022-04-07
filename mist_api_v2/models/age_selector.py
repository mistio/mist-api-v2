# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AgeSelector(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, minutes=None):  # noqa: E501
        """AgeSelector - a model defined in OpenAPI

        :param type: The type of this AgeSelector.  # noqa: E501
        :type type: str
        :param minutes: The minutes of this AgeSelector.  # noqa: E501
        :type minutes: int
        """
        self.openapi_types = {
            'type': str,
            'minutes': int
        }

        self.attribute_map = {
            'type': 'type',
            'minutes': 'minutes'
        }

        self._type = type
        self._minutes = minutes

    @classmethod
    def from_dict(cls, dikt) -> 'AgeSelector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AgeSelector of this AgeSelector.  # noqa: E501
        :rtype: AgeSelector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this AgeSelector.

        age type  # noqa: E501

        :return: The type of this AgeSelector.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AgeSelector.

        age type  # noqa: E501

        :param type: The type of this AgeSelector.
        :type type: str
        """
        allowed_values = ["age"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def minutes(self):
        """Gets the minutes of this AgeSelector.

        an integer that represents the minutes passed from the creation of the resource  # noqa: E501

        :return: The minutes of this AgeSelector.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this AgeSelector.

        an integer that represents the minutes passed from the creation of the resource  # noqa: E501

        :param minutes: The minutes of this AgeSelector.
        :type minutes: int
        """

        self._minutes = minutes
