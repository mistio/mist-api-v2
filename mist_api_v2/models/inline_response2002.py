# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class InlineResponse2002(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None):  # noqa: E501
        """InlineResponse2002 - a model defined in OpenAPI

        :param url: The url of this InlineResponse2002.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'url': str
        }

        self.attribute_map = {
            'url': 'url'
        }

        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self):
        """Gets the url of this InlineResponse2002.


        :return: The url of this InlineResponse2002.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse2002.


        :param url: The url of this InlineResponse2002.
        :type url: str
        """

        self._url = url
