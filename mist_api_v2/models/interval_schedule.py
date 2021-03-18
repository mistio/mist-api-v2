# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.base_schedule_entry import BaseScheduleEntry
from mist_api_v2.models.post_deploy_script import PostDeployScript
from mist_api_v2 import util

from mist_api_v2.models.base_schedule_entry import BaseScheduleEntry  # noqa: E501
from mist_api_v2.models.post_deploy_script import PostDeployScript  # noqa: E501

class IntervalSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, schedule_type=None, action=None, entry=None, script=None, start_after=None, expires=None, max_run_count=None, description=None):  # noqa: E501
        """IntervalSchedule - a model defined in OpenAPI

        :param schedule_type: The schedule_type of this IntervalSchedule.  # noqa: E501
        :type schedule_type: str
        :param action: The action of this IntervalSchedule.  # noqa: E501
        :type action: str
        :param entry: The entry of this IntervalSchedule.  # noqa: E501
        :type entry: BaseScheduleEntry
        :param script: The script of this IntervalSchedule.  # noqa: E501
        :type script: PostDeployScript
        :param start_after: The start_after of this IntervalSchedule.  # noqa: E501
        :type start_after: datetime
        :param expires: The expires of this IntervalSchedule.  # noqa: E501
        :type expires: datetime
        :param max_run_count: The max_run_count of this IntervalSchedule.  # noqa: E501
        :type max_run_count: int
        :param description: The description of this IntervalSchedule.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'schedule_type': str,
            'action': str,
            'entry': BaseScheduleEntry,
            'script': PostDeployScript,
            'start_after': datetime,
            'expires': datetime,
            'max_run_count': int,
            'description': str
        }

        self.attribute_map = {
            'schedule_type': 'schedule_type',
            'action': 'action',
            'entry': 'entry',
            'script': 'script',
            'start_after': 'start_after',
            'expires': 'expires',
            'max_run_count': 'max_run_count',
            'description': 'description'
        }

        self._schedule_type = schedule_type
        self._action = action
        self._entry = entry
        self._script = script
        self._start_after = start_after
        self._expires = expires
        self._max_run_count = max_run_count
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'IntervalSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IntervalSchedule of this IntervalSchedule.  # noqa: E501
        :rtype: IntervalSchedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_type(self):
        """Gets the schedule_type of this IntervalSchedule.


        :return: The schedule_type of this IntervalSchedule.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this IntervalSchedule.


        :param schedule_type: The schedule_type of this IntervalSchedule.
        :type schedule_type: str
        """
        allowed_values = ["interval"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def action(self):
        """Gets the action of this IntervalSchedule.


        :return: The action of this IntervalSchedule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IntervalSchedule.


        :param action: The action of this IntervalSchedule.
        :type action: str
        """
        allowed_values = ["start", "stop", "reboot", "destroy"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def entry(self):
        """Gets the entry of this IntervalSchedule.


        :return: The entry of this IntervalSchedule.
        :rtype: BaseScheduleEntry
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this IntervalSchedule.


        :param entry: The entry of this IntervalSchedule.
        :type entry: BaseScheduleEntry
        """
        if entry is None:
            raise ValueError("Invalid value for `entry`, must not be `None`")  # noqa: E501

        self._entry = entry

    @property
    def script(self):
        """Gets the script of this IntervalSchedule.


        :return: The script of this IntervalSchedule.
        :rtype: PostDeployScript
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this IntervalSchedule.


        :param script: The script of this IntervalSchedule.
        :type script: PostDeployScript
        """

        self._script = script

    @property
    def start_after(self):
        """Gets the start_after of this IntervalSchedule.

        Datetime when schedule should start running.  # noqa: E501

        :return: The start_after of this IntervalSchedule.
        :rtype: datetime
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this IntervalSchedule.

        Datetime when schedule should start running.  # noqa: E501

        :param start_after: The start_after of this IntervalSchedule.
        :type start_after: datetime
        """

        self._start_after = start_after

    @property
    def expires(self):
        """Gets the expires of this IntervalSchedule.

        Datetime when schedule should expire.  # noqa: E501

        :return: The expires of this IntervalSchedule.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this IntervalSchedule.

        Datetime when schedule should expire.  # noqa: E501

        :param expires: The expires of this IntervalSchedule.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def max_run_count(self):
        """Gets the max_run_count of this IntervalSchedule.


        :return: The max_run_count of this IntervalSchedule.
        :rtype: int
        """
        return self._max_run_count

    @max_run_count.setter
    def max_run_count(self, max_run_count):
        """Sets the max_run_count of this IntervalSchedule.


        :param max_run_count: The max_run_count of this IntervalSchedule.
        :type max_run_count: int
        """
        if max_run_count is not None and max_run_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_run_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_run_count = max_run_count

    @property
    def description(self):
        """Gets the description of this IntervalSchedule.


        :return: The description of this IntervalSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntervalSchedule.


        :param description: The description of this IntervalSchedule.
        :type description: str
        """

        self._description = description
