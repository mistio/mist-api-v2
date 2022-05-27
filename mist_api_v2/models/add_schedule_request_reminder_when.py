# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AddScheduleRequestReminderWhen(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, unit=None):  # noqa: E501
        """AddScheduleRequestReminderWhen - a model defined in OpenAPI

        :param value: The value of this AddScheduleRequestReminderWhen.  # noqa: E501
        :type value: int
        :param unit: The unit of this AddScheduleRequestReminderWhen.  # noqa: E501
        :type unit: str
        """
        self.openapi_types = {
            'value': int,
            'unit': str
        }

        self.attribute_map = {
            'value': 'value',
            'unit': 'unit'
        }

        self._value = value
        self._unit = unit

    @classmethod
    def from_dict(cls, dikt) -> 'AddScheduleRequestReminderWhen':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddScheduleRequest_reminder_when of this AddScheduleRequestReminderWhen.  # noqa: E501
        :rtype: AddScheduleRequestReminderWhen
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this AddScheduleRequestReminderWhen.


        :return: The value of this AddScheduleRequestReminderWhen.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AddScheduleRequestReminderWhen.


        :param value: The value of this AddScheduleRequestReminderWhen.
        :type value: int
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this AddScheduleRequestReminderWhen.


        :return: The unit of this AddScheduleRequestReminderWhen.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AddScheduleRequestReminderWhen.


        :param unit: The unit of this AddScheduleRequestReminderWhen.
        :type unit: str
        """
        allowed_values = ["seconds", "minutes", "hours", "days"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"
                .format(unit, allowed_values)
            )

        self._unit = unit
