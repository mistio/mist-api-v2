# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class EquinixMetalExtra(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, project_id=None):  # noqa: E501
        """EquinixMetalExtra - a model defined in OpenAPI

        :param project_id: The project_id of this EquinixMetalExtra.  # noqa: E501
        :type project_id: str
        """
        self.openapi_types = {
            'project_id': str
        }

        self.attribute_map = {
            'project_id': 'project_id'
        }

        self._project_id = project_id

    @classmethod
    def from_dict(cls, dikt) -> 'EquinixMetalExtra':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EquinixMetalExtra of this EquinixMetalExtra.  # noqa: E501
        :rtype: EquinixMetalExtra
        """
        return util.deserialize_model(dikt, cls)

    @property
    def project_id(self):
        """Gets the project_id of this EquinixMetalExtra.

        Project UUID, if not given the first one available will be selected  # noqa: E501

        :return: The project_id of this EquinixMetalExtra.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EquinixMetalExtra.

        Project UUID, if not given the first one available will be selected  # noqa: E501

        :param project_id: The project_id of this EquinixMetalExtra.
        :type project_id: str
        """

        self._project_id = project_id