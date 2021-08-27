# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AlibabaNet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, security_group=None):  # noqa: E501
        """AlibabaNet - a model defined in OpenAPI

        :param security_group: The security_group of this AlibabaNet.  # noqa: E501
        :type security_group: str
        """
        self.openapi_types = {
            'security_group': str
        }

        self.attribute_map = {
            'security_group': 'security_group'
        }

        self._security_group = security_group

    @classmethod
    def from_dict(cls, dikt) -> 'AlibabaNet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlibabaNet of this AlibabaNet.  # noqa: E501
        :rtype: AlibabaNet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def security_group(self):
        """Gets the security_group of this AlibabaNet.

        Name of the security group to assign to the machine. If not provided a default 'mistio' security group will be created.  # noqa: E501

        :return: The security_group of this AlibabaNet.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this AlibabaNet.

        Name of the security group to assign to the machine. If not provided a default 'mistio' security group will be created.  # noqa: E501

        :param security_group: The security_group of this AlibabaNet.
        :type security_group: str
        """

        self._security_group = security_group
