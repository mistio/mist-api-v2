# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, errors=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param id: The id of this InlineResponse200.  # noqa: E501
        :type id: str
        :param errors: The errors of this InlineResponse200.  # noqa: E501
        :type errors: List[str]
        """
        self.openapi_types = {
            'id': str,
            'errors': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'errors': 'errors'
        }

        self._id = id
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this InlineResponse200.


        :return: The id of this InlineResponse200.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200.


        :param id: The id of this InlineResponse200.
        :type id: str
        """

        self._id = id

    @property
    def errors(self):
        """Gets the errors of this InlineResponse200.


        :return: The errors of this InlineResponse200.
        :rtype: List[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse200.


        :param errors: The errors of this InlineResponse200.
        :type errors: List[str]
        """

        self._errors = errors
