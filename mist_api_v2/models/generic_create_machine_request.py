# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class GenericCreateMachineRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, net=None, disks=None, volumes=None):  # noqa: E501
        """GenericCreateMachineRequest - a model defined in OpenAPI

        :param net: The net of this GenericCreateMachineRequest.  # noqa: E501
        :type net: object
        :param disks: The disks of this GenericCreateMachineRequest.  # noqa: E501
        :type disks: object
        :param volumes: The volumes of this GenericCreateMachineRequest.  # noqa: E501
        :type volumes: List[object]
        """
        self.openapi_types = {
            'net': object,
            'disks': object,
            'volumes': List[object]
        }

        self.attribute_map = {
            'net': 'net',
            'disks': 'disks',
            'volumes': 'volumes'
        }

        self._net = net
        self._disks = disks
        self._volumes = volumes

    @classmethod
    def from_dict(cls, dikt) -> 'GenericCreateMachineRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GenericCreateMachineRequest of this GenericCreateMachineRequest.  # noqa: E501
        :rtype: GenericCreateMachineRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def net(self):
        """Gets the net of this GenericCreateMachineRequest.


        :return: The net of this GenericCreateMachineRequest.
        :rtype: object
        """
        return self._net

    @net.setter
    def net(self, net):
        """Sets the net of this GenericCreateMachineRequest.


        :param net: The net of this GenericCreateMachineRequest.
        :type net: object
        """

        self._net = net

    @property
    def disks(self):
        """Gets the disks of this GenericCreateMachineRequest.


        :return: The disks of this GenericCreateMachineRequest.
        :rtype: object
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this GenericCreateMachineRequest.


        :param disks: The disks of this GenericCreateMachineRequest.
        :type disks: object
        """

        self._disks = disks

    @property
    def volumes(self):
        """Gets the volumes of this GenericCreateMachineRequest.


        :return: The volumes of this GenericCreateMachineRequest.
        :rtype: List[object]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this GenericCreateMachineRequest.


        :param volumes: The volumes of this GenericCreateMachineRequest.
        :type volumes: List[object]
        """

        self._volumes = volumes
