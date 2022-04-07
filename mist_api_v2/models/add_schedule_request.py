# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AddScheduleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, task_enabled=None, action=None, params=None, selectors=None, schedule_type=None, schedule_entry=None, start_after=None, run_immediately=None):  # noqa: E501
        """AddScheduleRequest - a model defined in OpenAPI

        :param name: The name of this AddScheduleRequest.  # noqa: E501
        :type name: str
        :param description: The description of this AddScheduleRequest.  # noqa: E501
        :type description: str
        :param task_enabled: The task_enabled of this AddScheduleRequest.  # noqa: E501
        :type task_enabled: bool
        :param action: The action of this AddScheduleRequest.  # noqa: E501
        :type action: str
        :param params: The params of this AddScheduleRequest.  # noqa: E501
        :type params: str
        :param selectors: The selectors of this AddScheduleRequest.  # noqa: E501
        :type selectors: List[object]
        :param schedule_type: The schedule_type of this AddScheduleRequest.  # noqa: E501
        :type schedule_type: str
        :param schedule_entry: The schedule_entry of this AddScheduleRequest.  # noqa: E501
        :type schedule_entry: str
        :param start_after: The start_after of this AddScheduleRequest.  # noqa: E501
        :type start_after: str
        :param run_immediately: The run_immediately of this AddScheduleRequest.  # noqa: E501
        :type run_immediately: bool
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'task_enabled': bool,
            'action': str,
            'params': str,
            'selectors': List[object],
            'schedule_type': str,
            'schedule_entry': str,
            'start_after': str,
            'run_immediately': bool
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'task_enabled': 'task_enabled',
            'action': 'action',
            'params': 'params',
            'selectors': 'selectors',
            'schedule_type': 'schedule_type',
            'schedule_entry': 'schedule_entry',
            'start_after': 'start_after',
            'run_immediately': 'run_immediately'
        }

        self._name = name
        self._description = description
        self._task_enabled = task_enabled
        self._action = action
        self._params = params
        self._selectors = selectors
        self._schedule_type = schedule_type
        self._schedule_entry = schedule_entry
        self._start_after = start_after
        self._run_immediately = run_immediately

    @classmethod
    def from_dict(cls, dikt) -> 'AddScheduleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddScheduleRequest of this AddScheduleRequest.  # noqa: E501
        :rtype: AddScheduleRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AddScheduleRequest.

        The name of the schedule  # noqa: E501

        :return: The name of this AddScheduleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddScheduleRequest.

        The name of the schedule  # noqa: E501

        :param name: The name of this AddScheduleRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this AddScheduleRequest.

        The description of the schedule  # noqa: E501

        :return: The description of this AddScheduleRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddScheduleRequest.

        The description of the schedule  # noqa: E501

        :param description: The description of this AddScheduleRequest.
        :type description: str
        """

        self._description = description

    @property
    def task_enabled(self):
        """Gets the task_enabled of this AddScheduleRequest.

        Schedule status (enabled, disabled)  # noqa: E501

        :return: The task_enabled of this AddScheduleRequest.
        :rtype: bool
        """
        return self._task_enabled

    @task_enabled.setter
    def task_enabled(self, task_enabled):
        """Sets the task_enabled of this AddScheduleRequest.

        Schedule status (enabled, disabled)  # noqa: E501

        :param task_enabled: The task_enabled of this AddScheduleRequest.
        :type task_enabled: bool
        """

        self._task_enabled = task_enabled

    @property
    def action(self):
        """Gets the action of this AddScheduleRequest.

        The action that a schedule performs on a resource  # noqa: E501

        :return: The action of this AddScheduleRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AddScheduleRequest.

        The action that a schedule performs on a resource  # noqa: E501

        :param action: The action of this AddScheduleRequest.
        :type action: str
        """
        allowed_values = ["reboot", "destroy", "notify", "start", "stop", "delete"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def params(self):
        """Gets the params of this AddScheduleRequest.

        Schedule parameters  # noqa: E501

        :return: The params of this AddScheduleRequest.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this AddScheduleRequest.

        Schedule parameters  # noqa: E501

        :param params: The params of this AddScheduleRequest.
        :type params: str
        """

        self._params = params

    @property
    def selectors(self):
        """Gets the selectors of this AddScheduleRequest.


        :return: The selectors of this AddScheduleRequest.
        :rtype: List[object]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this AddScheduleRequest.


        :param selectors: The selectors of this AddScheduleRequest.
        :type selectors: List[object]
        """

        self._selectors = selectors

    @property
    def schedule_type(self):
        """Gets the schedule_type of this AddScheduleRequest.

        The type of the schedule  # noqa: E501

        :return: The schedule_type of this AddScheduleRequest.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this AddScheduleRequest.

        The type of the schedule  # noqa: E501

        :param schedule_type: The schedule_type of this AddScheduleRequest.
        :type schedule_type: str
        """
        allowed_values = ["crontab", "interval", "one_off"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def schedule_entry(self):
        """Gets the schedule_entry of this AddScheduleRequest.

        The date that schedule starts. The format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :return: The schedule_entry of this AddScheduleRequest.
        :rtype: str
        """
        return self._schedule_entry

    @schedule_entry.setter
    def schedule_entry(self, schedule_entry):
        """Sets the schedule_entry of this AddScheduleRequest.

        The date that schedule starts. The format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :param schedule_entry: The schedule_entry of this AddScheduleRequest.
        :type schedule_entry: str
        """

        self._schedule_entry = schedule_entry

    @property
    def start_after(self):
        """Gets the start_after of this AddScheduleRequest.

        The date after that schedule starts. The format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :return: The start_after of this AddScheduleRequest.
        :rtype: str
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this AddScheduleRequest.

        The date after that schedule starts. The format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :param start_after: The start_after of this AddScheduleRequest.
        :type start_after: str
        """

        self._start_after = start_after

    @property
    def run_immediately(self):
        """Gets the run_immediately of this AddScheduleRequest.

        Decides if the schedule runs immediately of not  # noqa: E501

        :return: The run_immediately of this AddScheduleRequest.
        :rtype: bool
        """
        return self._run_immediately

    @run_immediately.setter
    def run_immediately(self, run_immediately):
        """Sets the run_immediately of this AddScheduleRequest.

        Decides if the schedule runs immediately of not  # noqa: E501

        :param run_immediately: The run_immediately of this AddScheduleRequest.
        :type run_immediately: bool
        """

        self._run_immediately = run_immediately
