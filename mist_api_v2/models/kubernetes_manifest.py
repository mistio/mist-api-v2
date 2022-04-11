# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class KubernetesManifest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None):  # noqa: E501
        """KubernetesManifest - a model defined in OpenAPI

        :param type: The type of this KubernetesManifest.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'type': str
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'KubernetesManifest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KubernetesManifest of this KubernetesManifest.  # noqa: E501
        :rtype: KubernetesManifest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this KubernetesManifest.


        :return: The type of this KubernetesManifest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KubernetesManifest.


        :param type: The type of this KubernetesManifest.
        :type type: str
        """
        allowed_values = ["manifest"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type