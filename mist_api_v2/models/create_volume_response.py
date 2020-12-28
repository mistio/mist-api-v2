# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.create_machine_response_one_of import CreateMachineResponseOneOf
from mist_api_v2.models.create_machine_response_one_of1 import CreateMachineResponseOneOf1
from mist_api_v2 import util

from mist_api_v2.models.create_machine_response_one_of import CreateMachineResponseOneOf  # noqa: E501
from mist_api_v2.models.create_machine_response_one_of1 import CreateMachineResponseOneOf1  # noqa: E501

class CreateVolumeResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job_id=None, plan=None):  # noqa: E501
        """CreateVolumeResponse - a model defined in OpenAPI

        :param job_id: The job_id of this CreateVolumeResponse.  # noqa: E501
        :type job_id: str
        :param plan: The plan of this CreateVolumeResponse.  # noqa: E501
        :type plan: object
        """
        self.openapi_types = {
            'job_id': str,
            'plan': object
        }

        self.attribute_map = {
            'job_id': 'jobId',
            'plan': 'plan'
        }

        self._job_id = job_id
        self._plan = plan

    @classmethod
    def from_dict(cls, dikt) -> 'CreateVolumeResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateVolumeResponse of this CreateVolumeResponse.  # noqa: E501
        :rtype: CreateVolumeResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self):
        """Gets the job_id of this CreateVolumeResponse.


        :return: The job_id of this CreateVolumeResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateVolumeResponse.


        :param job_id: The job_id of this CreateVolumeResponse.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def plan(self):
        """Gets the plan of this CreateVolumeResponse.


        :return: The plan of this CreateVolumeResponse.
        :rtype: object
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this CreateVolumeResponse.


        :param plan: The plan of this CreateVolumeResponse.
        :type plan: object
        """

        self._plan = plan