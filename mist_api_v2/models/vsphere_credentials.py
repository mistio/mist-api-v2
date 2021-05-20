# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class VsphereCredentials(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host=None, username=None, password=None, ca_cert_file=None):  # noqa: E501
        """VsphereCredentials - a model defined in OpenAPI

        :param host: The host of this VsphereCredentials.  # noqa: E501
        :type host: str
        :param username: The username of this VsphereCredentials.  # noqa: E501
        :type username: str
        :param password: The password of this VsphereCredentials.  # noqa: E501
        :type password: str
        :param ca_cert_file: The ca_cert_file of this VsphereCredentials.  # noqa: E501
        :type ca_cert_file: str
        """
        self.openapi_types = {
            'host': str,
            'username': str,
            'password': str,
            'ca_cert_file': str
        }

        self.attribute_map = {
            'host': 'host',
            'username': 'username',
            'password': 'password',
            'ca_cert_file': 'ca_cert_file'
        }

        self._host = host
        self._username = username
        self._password = password
        self._ca_cert_file = ca_cert_file

    @classmethod
    def from_dict(cls, dikt) -> 'VsphereCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VsphereCredentials of this VsphereCredentials.  # noqa: E501
        :rtype: VsphereCredentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self):
        """Gets the host of this VsphereCredentials.

        Your vSphere/vCenter host  # noqa: E501

        :return: The host of this VsphereCredentials.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this VsphereCredentials.

        Your vSphere/vCenter host  # noqa: E501

        :param host: The host of this VsphereCredentials.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def username(self):
        """Gets the username of this VsphereCredentials.

        Your username  # noqa: E501

        :return: The username of this VsphereCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VsphereCredentials.

        Your username  # noqa: E501

        :param username: The username of this VsphereCredentials.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this VsphereCredentials.

        Your password  # noqa: E501

        :return: The password of this VsphereCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VsphereCredentials.

        Your password  # noqa: E501

        :param password: The password of this VsphereCredentials.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def ca_cert_file(self):
        """Gets the ca_cert_file of this VsphereCredentials.

        CA certificate  # noqa: E501

        :return: The ca_cert_file of this VsphereCredentials.
        :rtype: str
        """
        return self._ca_cert_file

    @ca_cert_file.setter
    def ca_cert_file(self, ca_cert_file):
        """Sets the ca_cert_file of this VsphereCredentials.

        CA certificate  # noqa: E501

        :param ca_cert_file: The ca_cert_file of this VsphereCredentials.
        :type ca_cert_file: str
        """

        self._ca_cert_file = ca_cert_file
