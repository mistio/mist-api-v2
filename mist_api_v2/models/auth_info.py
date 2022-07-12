# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.auth_info_data import AuthInfoData
from mist_api_v2.models.response_metadata import ResponseMetadata
from mist_api_v2 import util

from mist_api_v2.models.auth_info_data import AuthInfoData  # noqa: E501
from mist_api_v2.models.response_metadata import ResponseMetadata  # noqa: E501

class AuthInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None, meta=None):  # noqa: E501
        """AuthInfo - a model defined in OpenAPI

        :param data: The data of this AuthInfo.  # noqa: E501
        :type data: AuthInfoData
        :param meta: The meta of this AuthInfo.  # noqa: E501
        :type meta: ResponseMetadata
        """
        self.openapi_types = {
            'data': AuthInfoData,
            'meta': ResponseMetadata
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'AuthInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AuthInfo of this AuthInfo.  # noqa: E501
        :rtype: AuthInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this AuthInfo.


        :return: The data of this AuthInfo.
        :rtype: AuthInfoData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AuthInfo.


        :param data: The data of this AuthInfo.
        :type data: AuthInfoData
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this AuthInfo.


        :return: The meta of this AuthInfo.
        :rtype: ResponseMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this AuthInfo.


        :param meta: The meta of this AuthInfo.
        :type meta: ResponseMetadata
        """

        self._meta = meta
