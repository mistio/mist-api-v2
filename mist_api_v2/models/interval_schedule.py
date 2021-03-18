# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class IntervalSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start_after=None, expires=None, max_run_count=None):  # noqa: E501
        """IntervalSchedule - a model defined in OpenAPI

        :param start_after: The start_after of this IntervalSchedule.  # noqa: E501
        :type start_after: datetime
        :param expires: The expires of this IntervalSchedule.  # noqa: E501
        :type expires: datetime
        :param max_run_count: The max_run_count of this IntervalSchedule.  # noqa: E501
        :type max_run_count: int
        """
        self.openapi_types = {
            'start_after': datetime,
            'expires': datetime,
            'max_run_count': int
        }

        self.attribute_map = {
            'start_after': 'start_after',
            'expires': 'expires',
            'max_run_count': 'max_run_count'
        }

        self._start_after = start_after
        self._expires = expires
        self._max_run_count = max_run_count

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
    def start_after(self):
        """Gets the start_after of this IntervalSchedule.

        The datetime when schedule should start running, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The start_after of this IntervalSchedule.
        :rtype: datetime
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this IntervalSchedule.

        The datetime when schedule should start running, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param start_after: The start_after of this IntervalSchedule.
        :type start_after: datetime
        """

        self._start_after = start_after

    @property
    def expires(self):
        """Gets the expires of this IntervalSchedule.

        The datetime when schedule should expire, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The expires of this IntervalSchedule.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this IntervalSchedule.

        The datetime when schedule should expire, e.g 2021-09-22T18:19:28Z  # noqa: E501

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
