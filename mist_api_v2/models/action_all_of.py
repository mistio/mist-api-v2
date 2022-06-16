# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ActionAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type=None):  # noqa: E501
        """ActionAllOf - a model defined in OpenAPI

        :param action_type: The action_type of this ActionAllOf.  # noqa: E501
        :type action_type: str
        """
        self.openapi_types = {
            'action_type': str
        }

        self.attribute_map = {
            'action_type': 'action_type'
        }

        self._action_type = action_type

    @classmethod
    def from_dict(cls, dikt) -> 'ActionAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Action_allOf of this ActionAllOf.  # noqa: E501
        :rtype: ActionAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this ActionAllOf.

        the action's type: notification, resource_action, run_script, webhook   # noqa: E501

        :return: The action_type of this ActionAllOf.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ActionAllOf.

        the action's type: notification, resource_action, run_script, webhook   # noqa: E501

        :param action_type: The action_type of this ActionAllOf.
        :type action_type: str
        """
        allowed_values = ["start", "stop", "reboot", "destroy", "notify", "delete", "resize", "run_script", "webhook"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"
                .format(action_type, allowed_values)
            )

        self._action_type = action_type
