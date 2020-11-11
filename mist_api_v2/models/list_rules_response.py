# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.response_metadata import ResponseMetadata
from mist_api_v2.models.rule import Rule
from mist_api_v2 import util

from mist_api_v2.models.response_metadata import ResponseMetadata  # noqa: E501
from mist_api_v2.models.rule import Rule  # noqa: E501

class ListRulesResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None, meta=None):  # noqa: E501
        """ListRulesResponse - a model defined in OpenAPI

        :param data: The data of this ListRulesResponse.  # noqa: E501
        :type data: List[Rule]
        :param meta: The meta of this ListRulesResponse.  # noqa: E501
        :type meta: ResponseMetadata
        """
        self.openapi_types = {
            'data': List[Rule],
            'meta': ResponseMetadata
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'ListRulesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListRulesResponse of this ListRulesResponse.  # noqa: E501
        :rtype: ListRulesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListRulesResponse.


        :return: The data of this ListRulesResponse.
        :rtype: List[Rule]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListRulesResponse.


        :param data: The data of this ListRulesResponse.
        :type data: List[Rule]
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this ListRulesResponse.


        :return: The meta of this ListRulesResponse.
        :rtype: ResponseMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ListRulesResponse.


        :param meta: The meta of this ListRulesResponse.
        :type meta: ResponseMetadata
        """

        self._meta = meta