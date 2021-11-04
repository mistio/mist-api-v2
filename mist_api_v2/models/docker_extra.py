# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.docker_extra_limits import DockerExtraLimits
from mist_api_v2 import util

from mist_api_v2.models.docker_extra_limits import DockerExtraLimits  # noqa: E501

class DockerExtra(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, environment=None, command=None, limits=None):  # noqa: E501
        """DockerExtra - a model defined in OpenAPI

        :param environment: The environment of this DockerExtra.  # noqa: E501
        :type environment: object
        :param command: The command of this DockerExtra.  # noqa: E501
        :type command: str
        :param limits: The limits of this DockerExtra.  # noqa: E501
        :type limits: DockerExtraLimits
        """
        self.openapi_types = {
            'environment': object,
            'command': str,
            'limits': DockerExtraLimits
        }

        self.attribute_map = {
            'environment': 'environment',
            'command': 'command',
            'limits': 'limits'
        }

        self._environment = environment
        self._command = command
        self._limits = limits

    @classmethod
    def from_dict(cls, dikt) -> 'DockerExtra':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DockerExtra of this DockerExtra.  # noqa: E501
        :rtype: DockerExtra
        """
        return util.deserialize_model(dikt, cls)

    @property
    def environment(self):
        """Gets the environment of this DockerExtra.

        Key, value pairs of environment variables to set inside the container  # noqa: E501

        :return: The environment of this DockerExtra.
        :rtype: object
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this DockerExtra.

        Key, value pairs of environment variables to set inside the container  # noqa: E501

        :param environment: The environment of this DockerExtra.
        :type environment: object
        """

        self._environment = environment

    @property
    def command(self):
        """Gets the command of this DockerExtra.

        Command to run specified as a string  # noqa: E501

        :return: The command of this DockerExtra.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this DockerExtra.

        Command to run specified as a string  # noqa: E501

        :param command: The command of this DockerExtra.
        :type command: str
        """

        self._command = command

    @property
    def limits(self):
        """Gets the limits of this DockerExtra.


        :return: The limits of this DockerExtra.
        :rtype: DockerExtraLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this DockerExtra.


        :param limits: The limits of this DockerExtra.
        :type limits: DockerExtraLimits
        """

        self._limits = limits