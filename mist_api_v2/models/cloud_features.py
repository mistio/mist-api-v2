# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CloudFeatures(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compute=True, dns=False):  # noqa: E501
        """CloudFeatures - a model defined in OpenAPI

        :param compute: The compute of this CloudFeatures.  # noqa: E501
        :type compute: bool
        :param dns: The dns of this CloudFeatures.  # noqa: E501
        :type dns: bool
        """
        self.openapi_types = {
            'compute': bool,
            'dns': bool
        }

        self.attribute_map = {
            'compute': 'compute',
            'dns': 'dns'
        }

        self._compute = compute
        self._dns = dns

    @classmethod
    def from_dict(cls, dikt) -> 'CloudFeatures':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CloudFeatures of this CloudFeatures.  # noqa: E501
        :rtype: CloudFeatures
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compute(self):
        """Gets the compute of this CloudFeatures.

        Enable compute services  # noqa: E501

        :return: The compute of this CloudFeatures.
        :rtype: bool
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this CloudFeatures.

        Enable compute services  # noqa: E501

        :param compute: The compute of this CloudFeatures.
        :type compute: bool
        """

        self._compute = compute

    @property
    def dns(self):
        """Gets the dns of this CloudFeatures.

        Enable DNS services  # noqa: E501

        :return: The dns of this CloudFeatures.
        :rtype: bool
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this CloudFeatures.

        Enable DNS services  # noqa: E501

        :param dns: The dns of this CloudFeatures.
        :type dns: bool
        """

        self._dns = dns
