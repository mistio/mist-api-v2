# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.patch_organization_request_vault import PatchOrganizationRequestVault
from mist_api_v2 import util

from mist_api_v2.models.patch_organization_request_vault import PatchOrganizationRequestVault  # noqa: E501

class PatchOrganizationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, vault=None):  # noqa: E501
        """PatchOrganizationRequest - a model defined in OpenAPI

        :param name: The name of this PatchOrganizationRequest.  # noqa: E501
        :type name: str
        :param vault: The vault of this PatchOrganizationRequest.  # noqa: E501
        :type vault: PatchOrganizationRequestVault
        """
        self.openapi_types = {
            'name': str,
            'vault': PatchOrganizationRequestVault
        }

        self.attribute_map = {
            'name': 'name',
            'vault': 'vault'
        }

        self._name = name
        self._vault = vault

    @classmethod
    def from_dict(cls, dikt) -> 'PatchOrganizationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PatchOrganizationRequest of this PatchOrganizationRequest.  # noqa: E501
        :rtype: PatchOrganizationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this PatchOrganizationRequest.

        The organization's name  # noqa: E501

        :return: The name of this PatchOrganizationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchOrganizationRequest.

        The organization's name  # noqa: E501

        :param name: The name of this PatchOrganizationRequest.
        :type name: str
        """

        self._name = name

    @property
    def vault(self):
        """Gets the vault of this PatchOrganizationRequest.


        :return: The vault of this PatchOrganizationRequest.
        :rtype: PatchOrganizationRequestVault
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this PatchOrganizationRequest.


        :param vault: The vault of this PatchOrganizationRequest.
        :type vault: PatchOrganizationRequestVault
        """

        self._vault = vault
