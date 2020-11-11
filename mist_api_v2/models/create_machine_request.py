# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.supported_providers import SupportedProviders
from mist_api_v2 import util

from mist_api_v2.models.supported_providers import SupportedProviders  # noqa: E501

class CreateMachineRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, provider=None, cloud=None, location=None, size=None, image=None, net=None, key=None, disks=None, volumes=None, fqdn=None, cloudinit=None, scripts=None, schedules=None, tags=None, expiration=None, extra=None, monitoring=None, quantity=None, template=None, dry=None, save=None):  # noqa: E501
        """CreateMachineRequest - a model defined in OpenAPI

        :param name: The name of this CreateMachineRequest.  # noqa: E501
        :type name: str
        :param provider: The provider of this CreateMachineRequest.  # noqa: E501
        :type provider: SupportedProviders
        :param cloud: The cloud of this CreateMachineRequest.  # noqa: E501
        :type cloud: str
        :param location: The location of this CreateMachineRequest.  # noqa: E501
        :type location: str
        :param size: The size of this CreateMachineRequest.  # noqa: E501
        :type size: object
        :param image: The image of this CreateMachineRequest.  # noqa: E501
        :type image: object
        :param net: The net of this CreateMachineRequest.  # noqa: E501
        :type net: object
        :param key: The key of this CreateMachineRequest.  # noqa: E501
        :type key: object
        :param disks: The disks of this CreateMachineRequest.  # noqa: E501
        :type disks: object
        :param volumes: The volumes of this CreateMachineRequest.  # noqa: E501
        :type volumes: object
        :param fqdn: The fqdn of this CreateMachineRequest.  # noqa: E501
        :type fqdn: str
        :param cloudinit: The cloudinit of this CreateMachineRequest.  # noqa: E501
        :type cloudinit: str
        :param scripts: The scripts of this CreateMachineRequest.  # noqa: E501
        :type scripts: object
        :param schedules: The schedules of this CreateMachineRequest.  # noqa: E501
        :type schedules: object
        :param tags: The tags of this CreateMachineRequest.  # noqa: E501
        :type tags: object
        :param expiration: The expiration of this CreateMachineRequest.  # noqa: E501
        :type expiration: object
        :param extra: The extra of this CreateMachineRequest.  # noqa: E501
        :type extra: object
        :param monitoring: The monitoring of this CreateMachineRequest.  # noqa: E501
        :type monitoring: bool
        :param quantity: The quantity of this CreateMachineRequest.  # noqa: E501
        :type quantity: float
        :param template: The template of this CreateMachineRequest.  # noqa: E501
        :type template: object
        :param dry: The dry of this CreateMachineRequest.  # noqa: E501
        :type dry: bool
        :param save: The save of this CreateMachineRequest.  # noqa: E501
        :type save: bool
        """
        self.openapi_types = {
            'name': str,
            'provider': SupportedProviders,
            'cloud': str,
            'location': str,
            'size': object,
            'image': object,
            'net': object,
            'key': object,
            'disks': object,
            'volumes': object,
            'fqdn': str,
            'cloudinit': str,
            'scripts': object,
            'schedules': object,
            'tags': object,
            'expiration': object,
            'extra': object,
            'monitoring': bool,
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
            'image': 'image',
            'net': 'net',
            'key': 'key',
            'disks': 'disks',
            'volumes': 'volumes',
            'fqdn': 'fqdn',
            'cloudinit': 'cloudinit',
            'scripts': 'scripts',
            'schedules': 'schedules',
            'tags': 'tags',
            'expiration': 'expiration',
            'extra': 'extra',
            'monitoring': 'monitoring',
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
        self._image = image
        self._net = net
        self._key = key
        self._disks = disks
        self._volumes = volumes
        self._fqdn = fqdn
        self._cloudinit = cloudinit
        self._scripts = scripts
        self._schedules = schedules
        self._tags = tags
        self._expiration = expiration
        self._extra = extra
        self._monitoring = monitoring
        self._quantity = quantity
        self._template = template
        self._dry = dry
        self._save = save

    @classmethod
    def from_dict(cls, dikt) -> 'CreateMachineRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateMachineRequest of this CreateMachineRequest.  # noqa: E501
        :rtype: CreateMachineRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateMachineRequest.

        Specify machine name  # noqa: E501

        :return: The name of this CreateMachineRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMachineRequest.

        Specify machine name  # noqa: E501

        :param name: The name of this CreateMachineRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this CreateMachineRequest.


        :return: The provider of this CreateMachineRequest.
        :rtype: SupportedProviders
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateMachineRequest.


        :param provider: The provider of this CreateMachineRequest.
        :type provider: SupportedProviders
        """

        self._provider = provider

    @property
    def cloud(self):
        """Gets the cloud of this CreateMachineRequest.

        Specify cloud to provision on  # noqa: E501

        :return: The cloud of this CreateMachineRequest.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CreateMachineRequest.

        Specify cloud to provision on  # noqa: E501

        :param cloud: The cloud of this CreateMachineRequest.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def location(self):
        """Gets the location of this CreateMachineRequest.

        Where to provision e.g. region, datacenter, rack  # noqa: E501

        :return: The location of this CreateMachineRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateMachineRequest.

        Where to provision e.g. region, datacenter, rack  # noqa: E501

        :param location: The location of this CreateMachineRequest.
        :type location: str
        """

        self._location = location

    @property
    def size(self):
        """Gets the size of this CreateMachineRequest.

        Machine sizing spec e.g. cpu/ram/flavor  # noqa: E501

        :return: The size of this CreateMachineRequest.
        :rtype: object
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateMachineRequest.

        Machine sizing spec e.g. cpu/ram/flavor  # noqa: E501

        :param size: The size of this CreateMachineRequest.
        :type size: object
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def image(self):
        """Gets the image of this CreateMachineRequest.

        Operating System image to boot from  # noqa: E501

        :return: The image of this CreateMachineRequest.
        :rtype: object
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CreateMachineRequest.

        Operating System image to boot from  # noqa: E501

        :param image: The image of this CreateMachineRequest.
        :type image: object
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def net(self):
        """Gets the net of this CreateMachineRequest.

        Specify network configuration parameters  # noqa: E501

        :return: The net of this CreateMachineRequest.
        :rtype: object
        """
        return self._net

    @net.setter
    def net(self, net):
        """Sets the net of this CreateMachineRequest.

        Specify network configuration parameters  # noqa: E501

        :param net: The net of this CreateMachineRequest.
        :type net: object
        """

        self._net = net

    @property
    def key(self):
        """Gets the key of this CreateMachineRequest.

        Associate SSH key  # noqa: E501

        :return: The key of this CreateMachineRequest.
        :rtype: object
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateMachineRequest.

        Associate SSH key  # noqa: E501

        :param key: The key of this CreateMachineRequest.
        :type key: object
        """

        self._key = key

    @property
    def disks(self):
        """Gets the disks of this CreateMachineRequest.

        Configure local disks  # noqa: E501

        :return: The disks of this CreateMachineRequest.
        :rtype: object
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this CreateMachineRequest.

        Configure local disks  # noqa: E501

        :param disks: The disks of this CreateMachineRequest.
        :type disks: object
        """

        self._disks = disks

    @property
    def volumes(self):
        """Gets the volumes of this CreateMachineRequest.

        Configure of attached storage volumes, e.g. cloud disks  # noqa: E501

        :return: The volumes of this CreateMachineRequest.
        :rtype: object
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this CreateMachineRequest.

        Configure of attached storage volumes, e.g. cloud disks  # noqa: E501

        :param volumes: The volumes of this CreateMachineRequest.
        :type volumes: object
        """

        self._volumes = volumes

    @property
    def fqdn(self):
        """Gets the fqdn of this CreateMachineRequest.

        Add DNS A Record that points machine's public IP to this Fully Qualified Domain Name. Zone needs to be managed by a configured Cloud DNS provider  # noqa: E501

        :return: The fqdn of this CreateMachineRequest.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this CreateMachineRequest.

        Add DNS A Record that points machine's public IP to this Fully Qualified Domain Name. Zone needs to be managed by a configured Cloud DNS provider  # noqa: E501

        :param fqdn: The fqdn of this CreateMachineRequest.
        :type fqdn: str
        """

        self._fqdn = fqdn

    @property
    def cloudinit(self):
        """Gets the cloudinit of this CreateMachineRequest.

        Run this Cloud Init script on first boot  # noqa: E501

        :return: The cloudinit of this CreateMachineRequest.
        :rtype: str
        """
        return self._cloudinit

    @cloudinit.setter
    def cloudinit(self, cloudinit):
        """Sets the cloudinit of this CreateMachineRequest.

        Run this Cloud Init script on first boot  # noqa: E501

        :param cloudinit: The cloudinit of this CreateMachineRequest.
        :type cloudinit: str
        """

        self._cloudinit = cloudinit

    @property
    def scripts(self):
        """Gets the scripts of this CreateMachineRequest.

        Run post deploy scripts over SSH  # noqa: E501

        :return: The scripts of this CreateMachineRequest.
        :rtype: object
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this CreateMachineRequest.

        Run post deploy scripts over SSH  # noqa: E501

        :param scripts: The scripts of this CreateMachineRequest.
        :type scripts: object
        """

        self._scripts = scripts

    @property
    def schedules(self):
        """Gets the schedules of this CreateMachineRequest.

        Configure scheduled actions for the provisioned machine  # noqa: E501

        :return: The schedules of this CreateMachineRequest.
        :rtype: object
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this CreateMachineRequest.

        Configure scheduled actions for the provisioned machine  # noqa: E501

        :param schedules: The schedules of this CreateMachineRequest.
        :type schedules: object
        """

        self._schedules = schedules

    @property
    def tags(self):
        """Gets the tags of this CreateMachineRequest.

        Assign tags to provisioned machine  # noqa: E501

        :return: The tags of this CreateMachineRequest.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateMachineRequest.

        Assign tags to provisioned machine  # noqa: E501

        :param tags: The tags of this CreateMachineRequest.
        :type tags: object
        """

        self._tags = tags

    @property
    def expiration(self):
        """Gets the expiration of this CreateMachineRequest.

        Configure machine expiration  # noqa: E501

        :return: The expiration of this CreateMachineRequest.
        :rtype: object
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this CreateMachineRequest.

        Configure machine expiration  # noqa: E501

        :param expiration: The expiration of this CreateMachineRequest.
        :type expiration: object
        """

        self._expiration = expiration

    @property
    def extra(self):
        """Gets the extra of this CreateMachineRequest.

        Configure additional parameters  # noqa: E501

        :return: The extra of this CreateMachineRequest.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this CreateMachineRequest.

        Configure additional parameters  # noqa: E501

        :param extra: The extra of this CreateMachineRequest.
        :type extra: object
        """

        self._extra = extra

    @property
    def monitoring(self):
        """Gets the monitoring of this CreateMachineRequest.

        Enable monitoring of this machine  # noqa: E501

        :return: The monitoring of this CreateMachineRequest.
        :rtype: bool
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this CreateMachineRequest.

        Enable monitoring of this machine  # noqa: E501

        :param monitoring: The monitoring of this CreateMachineRequest.
        :type monitoring: bool
        """

        self._monitoring = monitoring

    @property
    def quantity(self):
        """Gets the quantity of this CreateMachineRequest.

        Provision multiple machines of this type  # noqa: E501

        :return: The quantity of this CreateMachineRequest.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateMachineRequest.

        Provision multiple machines of this type  # noqa: E501

        :param quantity: The quantity of this CreateMachineRequest.
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def template(self):
        """Gets the template of this CreateMachineRequest.


        :return: The template of this CreateMachineRequest.
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateMachineRequest.


        :param template: The template of this CreateMachineRequest.
        :type template: object
        """

        self._template = template

    @property
    def dry(self):
        """Gets the dry of this CreateMachineRequest.

        Return provisioning plan and exit without executing it  # noqa: E501

        :return: The dry of this CreateMachineRequest.
        :rtype: bool
        """
        return self._dry

    @dry.setter
    def dry(self, dry):
        """Sets the dry of this CreateMachineRequest.

        Return provisioning plan and exit without executing it  # noqa: E501

        :param dry: The dry of this CreateMachineRequest.
        :type dry: bool
        """

        self._dry = dry

    @property
    def save(self):
        """Gets the save of this CreateMachineRequest.

        Save provisioning plan as template  # noqa: E501

        :return: The save of this CreateMachineRequest.
        :rtype: bool
        """
        return self._save

    @save.setter
    def save(self, save):
        """Sets the save of this CreateMachineRequest.

        Save provisioning plan as template  # noqa: E501

        :param save: The save of this CreateMachineRequest.
        :type save: bool
        """

        self._save = save