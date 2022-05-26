# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.taggable_resource_types import TaggableResourceTypes
from mist_api_v2 import util

from mist_api_v2.models.taggable_resource_types import TaggableResourceTypes  # noqa: E501

class Resource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource_type=None, resource_id=None):  # noqa: E501
        """Resource - a model defined in OpenAPI

        :param resource_type: The resource_type of this Resource.  # noqa: E501
        :type resource_type: TaggableResourceTypes
        :param resource_id: The resource_id of this Resource.  # noqa: E501
        :type resource_id: str
        """
        self.openapi_types = {
            'resource_type': TaggableResourceTypes,
            'resource_id': str
        }

        self.attribute_map = {
            'resource_type': 'resource_type',
            'resource_id': 'resource_id'
        }

        self._resource_type = resource_type
        self._resource_id = resource_id

    @classmethod
    def from_dict(cls, dikt) -> 'Resource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Resource of this Resource.  # noqa: E501
        :rtype: Resource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_type(self):
        """Gets the resource_type of this Resource.


        :return: The resource_type of this Resource.
        :rtype: TaggableResourceTypes
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Resource.


        :param resource_type: The resource_type of this Resource.
        :type resource_type: TaggableResourceTypes
        """

        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this Resource.


        :return: The resource_id of this Resource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Resource.


        :param resource_id: The resource_id of this Resource.
        :type resource_id: str
        """

        self._resource_id = resource_id