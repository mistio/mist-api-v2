# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AddKeyResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, private=None, public=None):  # noqa: E501
        """AddKeyResponse - a model defined in OpenAPI

        :param id: The id of this AddKeyResponse.  # noqa: E501
        :type id: str
        :param private: The private of this AddKeyResponse.  # noqa: E501
        :type private: str
        :param public: The public of this AddKeyResponse.  # noqa: E501
        :type public: str
        """
        self.openapi_types = {
            'id': str,
            'private': str,
            'public': str
        }

        self.attribute_map = {
            'id': 'id',
            'private': 'private',
            'public': 'public'
        }

        self._id = id
        self._private = private
        self._public = public

    @classmethod
    def from_dict(cls, dikt) -> 'AddKeyResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddKeyResponse of this AddKeyResponse.  # noqa: E501
        :rtype: AddKeyResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AddKeyResponse.


        :return: The id of this AddKeyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddKeyResponse.


        :param id: The id of this AddKeyResponse.
        :type id: str
        """

        self._id = id

    @property
    def private(self):
        """Gets the private of this AddKeyResponse.


        :return: The private of this AddKeyResponse.
        :rtype: str
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this AddKeyResponse.


        :param private: The private of this AddKeyResponse.
        :type private: str
        """

        self._private = private

    @property
    def public(self):
        """Gets the public of this AddKeyResponse.


        :return: The public of this AddKeyResponse.
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this AddKeyResponse.


        :param public: The public of this AddKeyResponse.
        :type public: str
        """

        self._public = public
