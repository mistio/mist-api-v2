# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CreateOrganizationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, super_org=False):  # noqa: E501
        """CreateOrganizationRequest - a model defined in OpenAPI

        :param name: The name of this CreateOrganizationRequest.  # noqa: E501
        :type name: str
        :param super_org: The super_org of this CreateOrganizationRequest.  # noqa: E501
        :type super_org: bool
        """
        self.openapi_types = {
            'name': str,
            'super_org': bool
        }

        self.attribute_map = {
            'name': 'name',
            'super_org': 'super_org'
        }

        self._name = name
        self._super_org = super_org

    @classmethod
    def from_dict(cls, dikt) -> 'CreateOrganizationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateOrganizationRequest of this CreateOrganizationRequest.  # noqa: E501
        :rtype: CreateOrganizationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateOrganizationRequest.


        :return: The name of this CreateOrganizationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrganizationRequest.


        :param name: The name of this CreateOrganizationRequest.
        :type name: str
        """

        self._name = name

    @property
    def super_org(self):
        """Gets the super_org of this CreateOrganizationRequest.


        :return: The super_org of this CreateOrganizationRequest.
        :rtype: bool
        """
        return self._super_org

    @super_org.setter
    def super_org(self, super_org):
        """Sets the super_org of this CreateOrganizationRequest.


        :param super_org: The super_org of this CreateOrganizationRequest.
        :type super_org: bool
        """

        self._super_org = super_org