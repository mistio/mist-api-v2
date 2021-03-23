# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.base_schedule_all_of import BaseScheduleAllOf
from mist_api_v2.models.post_deploy_script import PostDeployScript
from mist_api_v2 import util

from mist_api_v2.models.base_schedule_all_of import BaseScheduleAllOf  # noqa: E501
from mist_api_v2.models.post_deploy_script import PostDeployScript  # noqa: E501

class BaseSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, schedule_type=None, script=None, action=None, description=None, every=None, period=None, start_after=None, expires=None, max_run_count=None, datetime=None, minute=None, hour=None, day_of_month=None, month_of_year=None, day_of_week=None):  # noqa: E501
        """BaseSchedule - a model defined in OpenAPI

        :param schedule_type: The schedule_type of this BaseSchedule.  # noqa: E501
        :type schedule_type: str
        :param script: The script of this BaseSchedule.  # noqa: E501
        :type script: PostDeployScript
        :param action: The action of this BaseSchedule.  # noqa: E501
        :type action: str
        :param description: The description of this BaseSchedule.  # noqa: E501
        :type description: str
        :param every: The every of this BaseSchedule.  # noqa: E501
        :type every: int
        :param period: The period of this BaseSchedule.  # noqa: E501
        :type period: str
        :param start_after: The start_after of this BaseSchedule.  # noqa: E501
        :type start_after: datetime
        :param expires: The expires of this BaseSchedule.  # noqa: E501
        :type expires: datetime
        :param max_run_count: The max_run_count of this BaseSchedule.  # noqa: E501
        :type max_run_count: int
        :param datetime: The datetime of this BaseSchedule.  # noqa: E501
        :type datetime: datetime
        :param minute: The minute of this BaseSchedule.  # noqa: E501
        :type minute: str
        :param hour: The hour of this BaseSchedule.  # noqa: E501
        :type hour: str
        :param day_of_month: The day_of_month of this BaseSchedule.  # noqa: E501
        :type day_of_month: str
        :param month_of_year: The month_of_year of this BaseSchedule.  # noqa: E501
        :type month_of_year: str
        :param day_of_week: The day_of_week of this BaseSchedule.  # noqa: E501
        :type day_of_week: str
        """
        self.openapi_types = {
            'schedule_type': str,
            'script': PostDeployScript,
            'action': str,
            'description': str,
            'every': int,
            'period': str,
            'start_after': datetime,
            'expires': datetime,
            'max_run_count': int,
            'datetime': datetime,
            'minute': str,
            'hour': str,
            'day_of_month': str,
            'month_of_year': str,
            'day_of_week': str
        }

        self.attribute_map = {
            'schedule_type': 'schedule_type',
            'script': 'script',
            'action': 'action',
            'description': 'description',
            'every': 'every',
            'period': 'period',
            'start_after': 'start_after',
            'expires': 'expires',
            'max_run_count': 'max_run_count',
            'datetime': 'datetime',
            'minute': 'minute',
            'hour': 'hour',
            'day_of_month': 'day_of_month',
            'month_of_year': 'month_of_year',
            'day_of_week': 'day_of_week'
        }

        self._schedule_type = schedule_type
        self._script = script
        self._action = action
        self._description = description
        self._every = every
        self._period = period
        self._start_after = start_after
        self._expires = expires
        self._max_run_count = max_run_count
        self._datetime = datetime
        self._minute = minute
        self._hour = hour
        self._day_of_month = day_of_month
        self._month_of_year = month_of_year
        self._day_of_week = day_of_week

    @classmethod
    def from_dict(cls, dikt) -> 'BaseSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BaseSchedule of this BaseSchedule.  # noqa: E501
        :rtype: BaseSchedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_type(self):
        """Gets the schedule_type of this BaseSchedule.


        :return: The schedule_type of this BaseSchedule.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this BaseSchedule.


        :param schedule_type: The schedule_type of this BaseSchedule.
        :type schedule_type: str
        """
        allowed_values = ["one_off", "crontab", "interval"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def script(self):
        """Gets the script of this BaseSchedule.


        :return: The script of this BaseSchedule.
        :rtype: PostDeployScript
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this BaseSchedule.


        :param script: The script of this BaseSchedule.
        :type script: PostDeployScript
        """

        self._script = script

    @property
    def action(self):
        """Gets the action of this BaseSchedule.


        :return: The action of this BaseSchedule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BaseSchedule.


        :param action: The action of this BaseSchedule.
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
    def description(self):
        """Gets the description of this BaseSchedule.


        :return: The description of this BaseSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseSchedule.


        :param description: The description of this BaseSchedule.
        :type description: str
        """

        self._description = description

    @property
    def every(self):
        """Gets the every of this BaseSchedule.


        :return: The every of this BaseSchedule.
        :rtype: int
        """
        return self._every

    @every.setter
    def every(self, every):
        """Sets the every of this BaseSchedule.


        :param every: The every of this BaseSchedule.
        :type every: int
        """
        if every is None:
            raise ValueError("Invalid value for `every`, must not be `None`")  # noqa: E501

        self._every = every

    @property
    def period(self):
        """Gets the period of this BaseSchedule.


        :return: The period of this BaseSchedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BaseSchedule.


        :param period: The period of this BaseSchedule.
        :type period: str
        """
        allowed_values = ["minutes", "hours", "days"]  # noqa: E501
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def start_after(self):
        """Gets the start_after of this BaseSchedule.

        The datetime when schedule should start running, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The start_after of this BaseSchedule.
        :rtype: datetime
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this BaseSchedule.

        The datetime when schedule should start running, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param start_after: The start_after of this BaseSchedule.
        :type start_after: datetime
        """

        self._start_after = start_after

    @property
    def expires(self):
        """Gets the expires of this BaseSchedule.

        The datetime when schedule should expire, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The expires of this BaseSchedule.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this BaseSchedule.

        The datetime when schedule should expire, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param expires: The expires of this BaseSchedule.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def max_run_count(self):
        """Gets the max_run_count of this BaseSchedule.


        :return: The max_run_count of this BaseSchedule.
        :rtype: int
        """
        return self._max_run_count

    @max_run_count.setter
    def max_run_count(self, max_run_count):
        """Sets the max_run_count of this BaseSchedule.


        :param max_run_count: The max_run_count of this BaseSchedule.
        :type max_run_count: int
        """
        if max_run_count is not None and max_run_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_run_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_run_count = max_run_count

    @property
    def datetime(self):
        """Gets the datetime of this BaseSchedule.

        When one_off schedule should run, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The datetime of this BaseSchedule.
        :rtype: datetime
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this BaseSchedule.

        When one_off schedule should run, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param datetime: The datetime of this BaseSchedule.
        :type datetime: datetime
        """
        if datetime is None:
            raise ValueError("Invalid value for `datetime`, must not be `None`")  # noqa: E501

        self._datetime = datetime

    @property
    def minute(self):
        """Gets the minute of this BaseSchedule.


        :return: The minute of this BaseSchedule.
        :rtype: str
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this BaseSchedule.


        :param minute: The minute of this BaseSchedule.
        :type minute: str
        """
        if minute is None:
            raise ValueError("Invalid value for `minute`, must not be `None`")  # noqa: E501

        self._minute = minute

    @property
    def hour(self):
        """Gets the hour of this BaseSchedule.


        :return: The hour of this BaseSchedule.
        :rtype: str
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this BaseSchedule.


        :param hour: The hour of this BaseSchedule.
        :type hour: str
        """
        if hour is None:
            raise ValueError("Invalid value for `hour`, must not be `None`")  # noqa: E501

        self._hour = hour

    @property
    def day_of_month(self):
        """Gets the day_of_month of this BaseSchedule.


        :return: The day_of_month of this BaseSchedule.
        :rtype: str
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this BaseSchedule.


        :param day_of_month: The day_of_month of this BaseSchedule.
        :type day_of_month: str
        """
        if day_of_month is None:
            raise ValueError("Invalid value for `day_of_month`, must not be `None`")  # noqa: E501

        self._day_of_month = day_of_month

    @property
    def month_of_year(self):
        """Gets the month_of_year of this BaseSchedule.


        :return: The month_of_year of this BaseSchedule.
        :rtype: str
        """
        return self._month_of_year

    @month_of_year.setter
    def month_of_year(self, month_of_year):
        """Sets the month_of_year of this BaseSchedule.


        :param month_of_year: The month_of_year of this BaseSchedule.
        :type month_of_year: str
        """
        if month_of_year is None:
            raise ValueError("Invalid value for `month_of_year`, must not be `None`")  # noqa: E501

        self._month_of_year = month_of_year

    @property
    def day_of_week(self):
        """Gets the day_of_week of this BaseSchedule.


        :return: The day_of_week of this BaseSchedule.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this BaseSchedule.


        :param day_of_week: The day_of_week of this BaseSchedule.
        :type day_of_week: str
        """
        if day_of_week is None:
            raise ValueError("Invalid value for `day_of_week`, must not be `None`")  # noqa: E501

        self._day_of_week = day_of_week
