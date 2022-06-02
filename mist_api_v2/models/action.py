# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.action_all_of import ActionAllOf
from mist_api_v2 import util

from mist_api_v2.models.action_all_of import ActionAllOf  # noqa: E501

class Action(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, users=None, teams=None, emails=None, action=None, command=None, script=None, params=None):  # noqa: E501
        """Action - a model defined in OpenAPI

        :param type: The type of this Action.  # noqa: E501
        :type type: str
        :param users: The users of this Action.  # noqa: E501
        :type users: List[str]
        :param teams: The teams of this Action.  # noqa: E501
        :type teams: List[str]
        :param emails: The emails of this Action.  # noqa: E501
        :type emails: List[str]
        :param action: The action of this Action.  # noqa: E501
        :type action: str
        :param command: The command of this Action.  # noqa: E501
        :type command: str
        :param script: The script of this Action.  # noqa: E501
        :type script: str
        :param params: The params of this Action.  # noqa: E501
        :type params: str
        """
        self.openapi_types = {
            'type': str,
            'users': List[str],
            'teams': List[str],
            'emails': List[str],
            'action': str,
            'command': str,
            'script': str,
            'params': str
        }

        self.attribute_map = {
            'type': 'type',
            'users': 'users',
            'teams': 'teams',
            'emails': 'emails',
            'action': 'action',
            'command': 'command',
            'script': 'script',
            'params': 'params'
        }

        self._type = type
        self._users = users
        self._teams = teams
        self._emails = emails
        self._action = action
        self._command = command
        self._script = script
        self._params = params

    @classmethod
    def from_dict(cls, dikt) -> 'Action':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Action of this Action.  # noqa: E501
        :rtype: Action
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this Action.


        :return: The type of this Action.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Action.


        :param type: The type of this Action.
        :type type: str
        """
        allowed_values = ["run_script"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def users(self):
        """Gets the users of this Action.

        a list of user to be notified, denoted by their UUIDs   # noqa: E501

        :return: The users of this Action.
        :rtype: List[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Action.

        a list of user to be notified, denoted by their UUIDs   # noqa: E501

        :param users: The users of this Action.
        :type users: List[str]
        """

        self._users = users

    @property
    def teams(self):
        """Gets the teams of this Action.

        a list of teams, denoted by their UUIDs, whose users will be notified   # noqa: E501

        :return: The teams of this Action.
        :rtype: List[str]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Action.

        a list of teams, denoted by their UUIDs, whose users will be notified   # noqa: E501

        :param teams: The teams of this Action.
        :type teams: List[str]
        """

        self._teams = teams

    @property
    def emails(self):
        """Gets the emails of this Action.

        a list of e-mails to send a notification to   # noqa: E501

        :return: The emails of this Action.
        :rtype: List[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Action.

        a list of e-mails to send a notification to   # noqa: E501

        :param emails: The emails of this Action.
        :type emails: List[str]
        """

        self._emails = emails

    @property
    def action(self):
        """Gets the action of this Action.

        the type of the action to be executed   # noqa: E501

        :return: The action of this Action.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Action.

        the type of the action to be executed   # noqa: E501

        :param action: The action of this Action.
        :type action: str
        """
        allowed_values = ["start", "stop", "reboot", "destroy", "notify", "delete"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def command(self):
        """Gets the command of this Action.

        Command that is about to run  # noqa: E501

        :return: The command of this Action.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Action.

        Command that is about to run  # noqa: E501

        :param command: The command of this Action.
        :type command: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def script(self):
        """Gets the script of this Action.

        Name or ID of the script to run  # noqa: E501

        :return: The script of this Action.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Action.

        Name or ID of the script to run  # noqa: E501

        :param script: The script of this Action.
        :type script: str
        """
        if script is None:
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script

    @property
    def params(self):
        """Gets the params of this Action.


        :return: The params of this Action.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Action.


        :param params: The params of this Action.
        :type params: str
        """

        self._params = params
