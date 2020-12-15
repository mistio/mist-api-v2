# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ResponseMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total=None, returned=None, sort=None, start=None):  # noqa: E501
        """ResponseMetadata - a model defined in OpenAPI

        :param total: The total of this ResponseMetadata.  # noqa: E501
        :type total: int
        :param returned: The returned of this ResponseMetadata.  # noqa: E501
        :type returned: int
        :param sort: The sort of this ResponseMetadata.  # noqa: E501
        :type sort: str
        :param start: The start of this ResponseMetadata.  # noqa: E501
        :type start: int
        """
        self.openapi_types = {
            'total': int,
            'returned': int,
            'sort': str,
            'start': int
        }

        self.attribute_map = {
            'total': 'total',
            'returned': 'returned',
            'sort': 'sort',
            'start': 'start'
        }

        self._total = total
        self._returned = returned
        self._sort = sort
        self._start = start

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseMetadata of this ResponseMetadata.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self):
        """Gets the total of this ResponseMetadata.

        Total items matching the query  # noqa: E501

        :return: The total of this ResponseMetadata.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ResponseMetadata.

        Total items matching the query  # noqa: E501

        :param total: The total of this ResponseMetadata.
        :type total: int
        """

        self._total = total

    @property
    def returned(self):
        """Gets the returned of this ResponseMetadata.

        Number of items in response  # noqa: E501

        :return: The returned of this ResponseMetadata.
        :rtype: int
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """Sets the returned of this ResponseMetadata.

        Number of items in response  # noqa: E501

        :param returned: The returned of this ResponseMetadata.
        :type returned: int
        """

        self._returned = returned

    @property
    def sort(self):
        """Gets the sort of this ResponseMetadata.

        Sort order of results  # noqa: E501

        :return: The sort of this ResponseMetadata.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ResponseMetadata.

        Sort order of results  # noqa: E501

        :param sort: The sort of this ResponseMetadata.
        :type sort: str
        """

        self._sort = sort

    @property
    def start(self):
        """Gets the start of this ResponseMetadata.

        Index of first response item in total matching items  # noqa: E501

        :return: The start of this ResponseMetadata.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ResponseMetadata.

        Index of first response item in total matching items  # noqa: E501

        :param start: The start of this ResponseMetadata.
        :type start: int
        """

        self._start = start
