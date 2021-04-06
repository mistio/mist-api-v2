# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.kvm_create_machine_request_disks import KvmCreateMachineRequestDisks
from mist_api_v2.models.kvm_create_machine_request_net import KvmCreateMachineRequestNet
from mist_api_v2 import util

from mist_api_v2.models.kvm_create_machine_request_disks import KvmCreateMachineRequestDisks  # noqa: E501
from mist_api_v2.models.kvm_create_machine_request_net import KvmCreateMachineRequestNet  # noqa: E501

class KvmCreateMachineRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, disks=None, net=None):  # noqa: E501
        """KvmCreateMachineRequest - a model defined in OpenAPI

        :param disks: The disks of this KvmCreateMachineRequest.  # noqa: E501
        :type disks: KvmCreateMachineRequestDisks
        :param net: The net of this KvmCreateMachineRequest.  # noqa: E501
        :type net: KvmCreateMachineRequestNet
        """
        self.openapi_types = {
            'disks': KvmCreateMachineRequestDisks,
            'net': KvmCreateMachineRequestNet
        }

        self.attribute_map = {
            'disks': 'disks',
            'net': 'net'
        }

        self._disks = disks
        self._net = net

    @classmethod
    def from_dict(cls, dikt) -> 'KvmCreateMachineRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KvmCreateMachineRequest of this KvmCreateMachineRequest.  # noqa: E501
        :rtype: KvmCreateMachineRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def disks(self):
        """Gets the disks of this KvmCreateMachineRequest.


        :return: The disks of this KvmCreateMachineRequest.
        :rtype: KvmCreateMachineRequestDisks
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this KvmCreateMachineRequest.


        :param disks: The disks of this KvmCreateMachineRequest.
        :type disks: KvmCreateMachineRequestDisks
        """

        self._disks = disks

    @property
    def net(self):
        """Gets the net of this KvmCreateMachineRequest.


        :return: The net of this KvmCreateMachineRequest.
        :rtype: KvmCreateMachineRequestNet
        """
        return self._net

    @net.setter
    def net(self, net):
        """Sets the net of this KvmCreateMachineRequest.


        :param net: The net of this KvmCreateMachineRequest.
        :type net: KvmCreateMachineRequestNet
        """

        self._net = net
