# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.add_schedule_request_reminder_when import AddScheduleRequestReminderWhen
from mist_api_v2 import util

from mist_api_v2.models.add_schedule_request_reminder_when import AddScheduleRequestReminderWhen  # noqa: E501

class AddScheduleRequestReminder(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, when=None):  # noqa: E501
        """AddScheduleRequestReminder - a model defined in OpenAPI

        :param message: The message of this AddScheduleRequestReminder.  # noqa: E501
        :type message: str
        :param when: The when of this AddScheduleRequestReminder.  # noqa: E501
        :type when: AddScheduleRequestReminderWhen
        """
        self.openapi_types = {
            'message': str,
            'when': AddScheduleRequestReminderWhen
        }

        self.attribute_map = {
            'message': 'message',
            'when': 'when'
        }

        self._message = message
        self._when = when

    @classmethod
    def from_dict(cls, dikt) -> 'AddScheduleRequestReminder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddScheduleRequest_reminder of this AddScheduleRequestReminder.  # noqa: E501
        :rtype: AddScheduleRequestReminder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this AddScheduleRequestReminder.

        The reminder message to be sent  # noqa: E501

        :return: The message of this AddScheduleRequestReminder.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AddScheduleRequestReminder.

        The reminder message to be sent  # noqa: E501

        :param message: The message of this AddScheduleRequestReminder.
        :type message: str
        """

        self._message = message

    @property
    def when(self):
        """Gets the when of this AddScheduleRequestReminder.


        :return: The when of this AddScheduleRequestReminder.
        :rtype: AddScheduleRequestReminderWhen
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this AddScheduleRequestReminder.


        :param when: The when of this AddScheduleRequestReminder.
        :type when: AddScheduleRequestReminderWhen
        """

        self._when = when
