# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class TokenAuth(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, token=None):  # noqa: E501
        """TokenAuth - a model defined in OpenAPI

        :param token: The token of this TokenAuth.  # noqa: E501
        :type token: str
        """
        self.openapi_types = {
            'token': str
        }

        self.attribute_map = {
            'token': 'token'
        }

        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'TokenAuth':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TokenAuth of this TokenAuth.  # noqa: E501
        :rtype: TokenAuth
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self):
        """Gets the token of this TokenAuth.

        The Vault token that will be used to authenticate against the new Vault. Either token or both role_id and secret_id must be specified  # noqa: E501

        :return: The token of this TokenAuth.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenAuth.

        The Vault token that will be used to authenticate against the new Vault. Either token or both role_id and secret_id must be specified  # noqa: E501

        :param token: The token of this TokenAuth.
        :type token: str
        """

        self._token = token
