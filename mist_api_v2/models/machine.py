# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class Machine(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, cloud=None, tags=None, created_by=None, owned_by=None, default=None, state=None):  # noqa: E501
        """Machine - a model defined in OpenAPI

        :param id: The id of this Machine.  # noqa: E501
        :type id: str
        :param name: The name of this Machine.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this Machine.  # noqa: E501
        :type cloud: str
        :param tags: The tags of this Machine.  # noqa: E501
        :type tags: object
        :param created_by: The created_by of this Machine.  # noqa: E501
        :type created_by: str
        :param owned_by: The owned_by of this Machine.  # noqa: E501
        :type owned_by: str
        :param default: The default of this Machine.  # noqa: E501
        :type default: bool
        :param state: The state of this Machine.  # noqa: E501
        :type state: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'cloud': str,
            'tags': object,
            'created_by': str,
            'owned_by': str,
            'default': bool,
            'state': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'cloud': 'cloud',
            'tags': 'tags',
            'created_by': 'created_by',
            'owned_by': 'owned_by',
            'default': 'default',
            'state': 'state'
        }

        self._id = id
        self._name = name
        self._cloud = cloud
        self._tags = tags
        self._created_by = created_by
        self._owned_by = owned_by
        self._default = default
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'Machine':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Machine of this Machine.  # noqa: E501
        :rtype: Machine
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Machine.


        :return: The id of this Machine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Machine.


        :param id: The id of this Machine.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Machine.


        :return: The name of this Machine.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Machine.


        :param name: The name of this Machine.
        :type name: str
        """

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this Machine.


        :return: The cloud of this Machine.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this Machine.


        :param cloud: The cloud of this Machine.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def tags(self):
        """Gets the tags of this Machine.


        :return: The tags of this Machine.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Machine.


        :param tags: The tags of this Machine.
        :type tags: object
        """

        self._tags = tags

    @property
    def created_by(self):
        """Gets the created_by of this Machine.


        :return: The created_by of this Machine.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Machine.


        :param created_by: The created_by of this Machine.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def owned_by(self):
        """Gets the owned_by of this Machine.


        :return: The owned_by of this Machine.
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by):
        """Sets the owned_by of this Machine.


        :param owned_by: The owned_by of this Machine.
        :type owned_by: str
        """

        self._owned_by = owned_by

    @property
    def default(self):
        """Gets the default of this Machine.


        :return: The default of this Machine.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Machine.


        :param default: The default of this Machine.
        :type default: bool
        """

        self._default = default

    @property
    def state(self):
        """Gets the state of this Machine.


        :return: The state of this Machine.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Machine.


        :param state: The state of this Machine.
        :type state: str
        """
        allowed_values = ["running", "starting", "stopping", "stopped", "pending", "suspended", "terminated", "error", "rebooting", "paused", "reconfiguring", "unknown"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state
