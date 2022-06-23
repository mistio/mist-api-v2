# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ExistingScript(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, script_id=None):  # noqa: E501
        """ExistingScript - a model defined in OpenAPI

        :param script_id: The script_id of this ExistingScript.  # noqa: E501
        :type script_id: str
        """
        self.openapi_types = {
            'script_id': str
        }

        self.attribute_map = {
            'script_id': 'scriptId'
        }

        self._script_id = script_id

    @classmethod
    def from_dict(cls, dikt) -> 'ExistingScript':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExistingScript of this ExistingScript.  # noqa: E501
        :rtype: ExistingScript
        """
        return util.deserialize_model(dikt, cls)

    @property
    def script_id(self):
        """Gets the script_id of this ExistingScript.

        the Id of the existing script to be executed   # noqa: E501

        :return: The script_id of this ExistingScript.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this ExistingScript.

        the Id of the existing script to be executed   # noqa: E501

        :param script_id: The script_id of this ExistingScript.
        :type script_id: str
        """
        if script_id is None:
            raise ValueError("Invalid value for `script_id`, must not be `None`")  # noqa: E501

        self._script_id = script_id