# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CreateOrgRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, logo=None):  # noqa: E501
        """CreateOrgRequest - a model defined in OpenAPI

        :param name: The name of this CreateOrgRequest.  # noqa: E501
        :type name: str
        :param description: The description of this CreateOrgRequest.  # noqa: E501
        :type description: str
        :param logo: The logo of this CreateOrgRequest.  # noqa: E501
        :type logo: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'logo': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'logo': 'logo'
        }

        self._name = name
        self._description = description
        self._logo = logo

    @classmethod
    def from_dict(cls, dikt) -> 'CreateOrgRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateOrgRequest of this CreateOrgRequest.  # noqa: E501
        :rtype: CreateOrgRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateOrgRequest.


        :return: The name of this CreateOrgRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrgRequest.


        :param name: The name of this CreateOrgRequest.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateOrgRequest.


        :return: The description of this CreateOrgRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOrgRequest.


        :param description: The description of this CreateOrgRequest.
        :type description: str
        """

        self._description = description

    @property
    def logo(self):
        """Gets the logo of this CreateOrgRequest.


        :return: The logo of this CreateOrgRequest.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this CreateOrgRequest.


        :param logo: The logo of this CreateOrgRequest.
        :type logo: str
        """

        self._logo = logo