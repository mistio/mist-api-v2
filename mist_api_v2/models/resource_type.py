# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ResourceType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CLOUDS = "clouds"
    CLUSTERS = "clusters"
    IMAGES = "images"
    KEYS = "keys"
    MACHINES = "machines"
    NETWORKS = "networks"
    SCRIPTS = "scripts"
    VOLUMES = "volumes"
    ZONES = "zones"
    def __init__(self):  # noqa: E501
        """ResourceType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceType of this ResourceType.  # noqa: E501
        :rtype: ResourceType
        """
        return util.deserialize_model(dikt, cls)
