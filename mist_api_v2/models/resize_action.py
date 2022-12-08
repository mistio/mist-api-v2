# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ResizeAction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type=None, params=None):  # noqa: E501
        """ResizeAction - a model defined in OpenAPI

        :param action_type: The action_type of this ResizeAction.  # noqa: E501
        :type action_type: str
        :param params: The params of this ResizeAction.  # noqa: E501
        :type params: str
        """
        self.openapi_types = {
            'action_type': str,
            'params': str
        }

        self.attribute_map = {
            'action_type': 'action_type',
            'params': 'params'
        }

        self._action_type = action_type
        self._params = params

    @classmethod
    def from_dict(cls, dikt) -> 'ResizeAction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResizeAction of this ResizeAction.  # noqa: E501
        :rtype: ResizeAction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this ResizeAction.


        :return: The action_type of this ResizeAction.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ResizeAction.


        :param action_type: The action_type of this ResizeAction.
        :type action_type: str
        """
        allowed_values = ["resize"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def params(self):
        """Gets the params of this ResizeAction.

        the params of the resize action to be executed   # noqa: E501

        :return: The params of this ResizeAction.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ResizeAction.

        the params of the resize action to be executed   # noqa: E501

        :param params: The params of this ResizeAction.
        :type params: str
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")  # noqa: E501

        self._params = params
