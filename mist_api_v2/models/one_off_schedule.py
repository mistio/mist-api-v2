# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class OneOffSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datetime=None):  # noqa: E501
        """OneOffSchedule - a model defined in OpenAPI

        :param datetime: The datetime of this OneOffSchedule.  # noqa: E501
        :type datetime: str
        """
        self.openapi_types = {
            'datetime': str
        }

        self.attribute_map = {
            'datetime': 'datetime'
        }

        self._datetime = datetime

    @classmethod
    def from_dict(cls, dikt) -> 'OneOffSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OneOffSchedule of this OneOffSchedule.  # noqa: E501
        :rtype: OneOffSchedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datetime(self):
        """Gets the datetime of this OneOffSchedule.

        When one_off schedule should run, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The datetime of this OneOffSchedule.
        :rtype: str
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this OneOffSchedule.

        When one_off schedule should run, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param datetime: The datetime of this OneOffSchedule.
        :type datetime: str
        """
        if datetime is None:
            raise ValueError("Invalid value for `datetime`, must not be `None`")  # noqa: E501

        self._datetime = datetime
