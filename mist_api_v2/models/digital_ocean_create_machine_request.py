# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.one_ofobjectobject import OneOfobjectobject
from mist_api_v2 import util

from mist_api_v2.models.one_ofobjectobject import OneOfobjectobject  # noqa: E501

class DigitalOceanCreateMachineRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, volumes=None):  # noqa: E501
        """DigitalOceanCreateMachineRequest - a model defined in OpenAPI

        :param volumes: The volumes of this DigitalOceanCreateMachineRequest.  # noqa: E501
        :type volumes: List[OneOfobjectobject]
        """
        self.openapi_types = {
            'volumes': List[OneOfobjectobject]
        }

        self.attribute_map = {
            'volumes': 'volumes'
        }

        self._volumes = volumes

    @classmethod
    def from_dict(cls, dikt) -> 'DigitalOceanCreateMachineRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DigitalOceanCreateMachineRequest of this DigitalOceanCreateMachineRequest.  # noqa: E501
        :rtype: DigitalOceanCreateMachineRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def volumes(self):
        """Gets the volumes of this DigitalOceanCreateMachineRequest.


        :return: The volumes of this DigitalOceanCreateMachineRequest.
        :rtype: List[OneOfobjectobject]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this DigitalOceanCreateMachineRequest.


        :param volumes: The volumes of this DigitalOceanCreateMachineRequest.
        :type volumes: List[OneOfobjectobject]
        """

        self._volumes = volumes