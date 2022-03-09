# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.resource_type import ResourceType
from mist_api_v2 import util

from mist_api_v2.models.resource_type import ResourceType  # noqa: E501

class ResourceIds(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource_type=None, resource_ids=None):  # noqa: E501
        """ResourceIds - a model defined in OpenAPI

        :param resource_type: The resource_type of this ResourceIds.  # noqa: E501
        :type resource_type: ResourceType
        :param resource_ids: The resource_ids of this ResourceIds.  # noqa: E501
        :type resource_ids: List[str]
        """
        self.openapi_types = {
            'resource_type': ResourceType,
            'resource_ids': List[str]
        }

        self.attribute_map = {
            'resource_type': 'resource_type',
            'resource_ids': 'resource_ids'
        }

        self._resource_type = resource_type
        self._resource_ids = resource_ids

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceIds':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceIds of this ResourceIds.  # noqa: E501
        :rtype: ResourceIds
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_type(self):
        """Gets the resource_type of this ResourceIds.


        :return: The resource_type of this ResourceIds.
        :rtype: ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ResourceIds.


        :param resource_type: The resource_type of this ResourceIds.
        :type resource_type: ResourceType
        """

        self._resource_type = resource_type

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ResourceIds.


        :return: The resource_ids of this ResourceIds.
        :rtype: List[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ResourceIds.


        :param resource_ids: The resource_ids of this ResourceIds.
        :type resource_ids: List[str]
        """

        self._resource_ids = resource_ids
