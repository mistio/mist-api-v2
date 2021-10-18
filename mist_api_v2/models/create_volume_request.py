# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.supported_providers import SupportedProviders
from mist_api_v2 import util

from mist_api_v2.models.supported_providers import SupportedProviders  # noqa: E501

class CreateVolumeRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, provider=None, cloud=None, location=None, size=None, tags=None, extra=None, quantity=None, template=None, dry=None, save=None):  # noqa: E501
        """CreateVolumeRequest - a model defined in OpenAPI

        :param name: The name of this CreateVolumeRequest.  # noqa: E501
        :type name: str
        :param provider: The provider of this CreateVolumeRequest.  # noqa: E501
        :type provider: SupportedProviders
        :param cloud: The cloud of this CreateVolumeRequest.  # noqa: E501
        :type cloud: str
        :param location: The location of this CreateVolumeRequest.  # noqa: E501
        :type location: str
        :param size: The size of this CreateVolumeRequest.  # noqa: E501
        :type size: int
        :param tags: The tags of this CreateVolumeRequest.  # noqa: E501
        :type tags: object
        :param extra: The extra of this CreateVolumeRequest.  # noqa: E501
        :type extra: object
        :param quantity: The quantity of this CreateVolumeRequest.  # noqa: E501
        :type quantity: float
        :param template: The template of this CreateVolumeRequest.  # noqa: E501
        :type template: object
        :param dry: The dry of this CreateVolumeRequest.  # noqa: E501
        :type dry: bool
        :param save: The save of this CreateVolumeRequest.  # noqa: E501
        :type save: bool
        """
        self.openapi_types = {
            'name': str,
            'provider': SupportedProviders,
            'cloud': str,
            'location': str,
            'size': int,
            'tags': object,
            'extra': object,
            'quantity': float,
            'template': object,
            'dry': bool,
            'save': bool
        }

        self.attribute_map = {
            'name': 'name',
            'provider': 'provider',
            'cloud': 'cloud',
            'location': 'location',
            'size': 'size',
            'tags': 'tags',
            'extra': 'extra',
            'quantity': 'quantity',
            'template': 'template',
            'dry': 'dry',
            'save': 'save'
        }

        self._name = name
        self._provider = provider
        self._cloud = cloud
        self._location = location
        self._size = size
        self._tags = tags
        self._extra = extra
        self._quantity = quantity
        self._template = template
        self._dry = dry
        self._save = save

    @classmethod
    def from_dict(cls, dikt) -> 'CreateVolumeRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateVolumeRequest of this CreateVolumeRequest.  # noqa: E501
        :rtype: CreateVolumeRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateVolumeRequest.

        Specify volume name  # noqa: E501

        :return: The name of this CreateVolumeRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVolumeRequest.

        Specify volume name  # noqa: E501

        :param name: The name of this CreateVolumeRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this CreateVolumeRequest.


        :return: The provider of this CreateVolumeRequest.
        :rtype: SupportedProviders
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateVolumeRequest.


        :param provider: The provider of this CreateVolumeRequest.
        :type provider: SupportedProviders
        """

        self._provider = provider

    @property
    def cloud(self):
        """Gets the cloud of this CreateVolumeRequest.

        Specify cloud to provision on  # noqa: E501

        :return: The cloud of this CreateVolumeRequest.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CreateVolumeRequest.

        Specify cloud to provision on  # noqa: E501

        :param cloud: The cloud of this CreateVolumeRequest.
        :type cloud: str
        """
        if cloud is None:
            raise ValueError("Invalid value for `cloud`, must not be `None`")  # noqa: E501

        self._cloud = cloud

    @property
    def location(self):
        """Gets the location of this CreateVolumeRequest.

        Where to provision e.g. region, datacenter, rack  # noqa: E501

        :return: The location of this CreateVolumeRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateVolumeRequest.

        Where to provision e.g. region, datacenter, rack  # noqa: E501

        :param location: The location of this CreateVolumeRequest.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def size(self):
        """Gets the size of this CreateVolumeRequest.

        Volume sizing spec  # noqa: E501

        :return: The size of this CreateVolumeRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateVolumeRequest.

        Volume sizing spec  # noqa: E501

        :param size: The size of this CreateVolumeRequest.
        :type size: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def tags(self):
        """Gets the tags of this CreateVolumeRequest.

        Assign tags to provisioned volume  # noqa: E501

        :return: The tags of this CreateVolumeRequest.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVolumeRequest.

        Assign tags to provisioned volume  # noqa: E501

        :param tags: The tags of this CreateVolumeRequest.
        :type tags: object
        """

        self._tags = tags

    @property
    def extra(self):
        """Gets the extra of this CreateVolumeRequest.

        Configure additional parameters  # noqa: E501

        :return: The extra of this CreateVolumeRequest.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this CreateVolumeRequest.

        Configure additional parameters  # noqa: E501

        :param extra: The extra of this CreateVolumeRequest.
        :type extra: object
        """

        self._extra = extra

    @property
    def quantity(self):
        """Gets the quantity of this CreateVolumeRequest.

        Provision multiple volumes of this type  # noqa: E501

        :return: The quantity of this CreateVolumeRequest.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateVolumeRequest.

        Provision multiple volumes of this type  # noqa: E501

        :param quantity: The quantity of this CreateVolumeRequest.
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def template(self):
        """Gets the template of this CreateVolumeRequest.


        :return: The template of this CreateVolumeRequest.
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateVolumeRequest.


        :param template: The template of this CreateVolumeRequest.
        :type template: object
        """

        self._template = template

    @property
    def dry(self):
        """Gets the dry of this CreateVolumeRequest.

        Return provisioning plan and exit without executing it  # noqa: E501

        :return: The dry of this CreateVolumeRequest.
        :rtype: bool
        """
        return self._dry

    @dry.setter
    def dry(self, dry):
        """Sets the dry of this CreateVolumeRequest.

        Return provisioning plan and exit without executing it  # noqa: E501

        :param dry: The dry of this CreateVolumeRequest.
        :type dry: bool
        """

        self._dry = dry

    @property
    def save(self):
        """Gets the save of this CreateVolumeRequest.

        Save provisioning plan as template  # noqa: E501

        :return: The save of this CreateVolumeRequest.
        :rtype: bool
        """
        return self._save

    @save.setter
    def save(self, save):
        """Sets the save of this CreateVolumeRequest.

        Save provisioning plan as template  # noqa: E501

        :param save: The save of this CreateVolumeRequest.
        :type save: bool
        """

        self._save = save
