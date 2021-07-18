# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class Log(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job_id=None, org=None):  # noqa: E501
        """Log - a model defined in OpenAPI

        :param job_id: The job_id of this Log.  # noqa: E501
        :type job_id: str
        :param org: The org of this Log.  # noqa: E501
        :type org: str
        """
        self.openapi_types = {
            'job_id': str,
            'org': str
        }

        self.attribute_map = {
            'job_id': 'job_id',
            'org': 'org'
        }

        self._job_id = job_id
        self._org = org

    @classmethod
    def from_dict(cls, dikt) -> 'Log':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Log of this Log.  # noqa: E501
        :rtype: Log
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self):
        """Gets the job_id of this Log.


        :return: The job_id of this Log.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Log.


        :param job_id: The job_id of this Log.
        :type job_id: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def org(self):
        """Gets the org of this Log.


        :return: The org of this Log.
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this Log.


        :param org: The org of this Log.
        :type org: str
        """
        if org is None:
            raise ValueError("Invalid value for `org`, must not be `None`")  # noqa: E501

        self._org = org
