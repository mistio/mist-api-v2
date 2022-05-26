# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.data_type import DataType
from mist_api_v2.models.query import Query
from mist_api_v2.models.window import Window
from mist_api_v2 import util

from mist_api_v2.models.data_type import DataType  # noqa: E501
from mist_api_v2.models.query import Query  # noqa: E501
from mist_api_v2.models.window import Window  # noqa: E501

class Condition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data_type=None, window=None, query=None):  # noqa: E501
        """Condition - a model defined in OpenAPI

        :param data_type: The data_type of this Condition.  # noqa: E501
        :type data_type: DataType
        :param window: The window of this Condition.  # noqa: E501
        :type window: Window
        :param query: The query of this Condition.  # noqa: E501
        :type query: Query
        """
        self.openapi_types = {
            'data_type': DataType,
            'window': Window,
            'query': Query
        }

        self.attribute_map = {
            'data_type': 'data_type',
            'window': 'window',
            'query': 'query'
        }

        self._data_type = data_type
        self._window = window
        self._query = query

    @classmethod
    def from_dict(cls, dikt) -> 'Condition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Condition of this Condition.  # noqa: E501
        :rtype: Condition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_type(self):
        """Gets the data_type of this Condition.


        :return: The data_type of this Condition.
        :rtype: DataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Condition.


        :param data_type: The data_type of this Condition.
        :type data_type: DataType
        """

        self._data_type = data_type

    @property
    def window(self):
        """Gets the window of this Condition.


        :return: The window of this Condition.
        :rtype: Window
        """
        return self._window

    @window.setter
    def window(self, window):
        """Sets the window of this Condition.


        :param window: The window of this Condition.
        :type window: Window
        """

        self._window = window

    @property
    def query(self):
        """Gets the query of this Condition.


        :return: The query of this Condition.
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Condition.


        :param query: The query of this Condition.
        :type query: Query
        """

        self._query = query