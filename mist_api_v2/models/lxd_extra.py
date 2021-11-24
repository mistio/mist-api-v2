# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class LXDExtra(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ephemeral=None):  # noqa: E501
        """LXDExtra - a model defined in OpenAPI

        :param ephemeral: The ephemeral of this LXDExtra.  # noqa: E501
        :type ephemeral: bool
        """
        self.openapi_types = {
            'ephemeral': bool
        }

        self.attribute_map = {
            'ephemeral': 'ephemeral'
        }

        self._ephemeral = ephemeral

    @classmethod
    def from_dict(cls, dikt) -> 'LXDExtra':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LXDExtra of this LXDExtra.  # noqa: E501
        :rtype: LXDExtra
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ephemeral(self):
        """Gets the ephemeral of this LXDExtra.

        Whether to destroy the container on shutdown, defaults to False  # noqa: E501

        :return: The ephemeral of this LXDExtra.
        :rtype: bool
        """
        return self._ephemeral

    @ephemeral.setter
    def ephemeral(self, ephemeral):
        """Sets the ephemeral of this LXDExtra.

        Whether to destroy the container on shutdown, defaults to False  # noqa: E501

        :param ephemeral: The ephemeral of this LXDExtra.
        :type ephemeral: bool
        """

        self._ephemeral = ephemeral
