# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.resource_count import ResourceCount
from mist_api_v2 import util

from mist_api_v2.models.resource_count import ResourceCount  # noqa: E501

class OrgResourcesSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, clouds=None, stacks=None, clusters=None, machines=None, volumes=None, buckets=None, networks=None, zones=None, images=None, keys=None, scripts=None, templates=None, tunnels=None, secrets=None, schedules=None, rules=None, teams=None, members=None):  # noqa: E501
        """OrgResourcesSummary - a model defined in OpenAPI

        :param clouds: The clouds of this OrgResourcesSummary.  # noqa: E501
        :type clouds: ResourceCount
        :param stacks: The stacks of this OrgResourcesSummary.  # noqa: E501
        :type stacks: ResourceCount
        :param clusters: The clusters of this OrgResourcesSummary.  # noqa: E501
        :type clusters: ResourceCount
        :param machines: The machines of this OrgResourcesSummary.  # noqa: E501
        :type machines: ResourceCount
        :param volumes: The volumes of this OrgResourcesSummary.  # noqa: E501
        :type volumes: ResourceCount
        :param buckets: The buckets of this OrgResourcesSummary.  # noqa: E501
        :type buckets: ResourceCount
        :param networks: The networks of this OrgResourcesSummary.  # noqa: E501
        :type networks: ResourceCount
        :param zones: The zones of this OrgResourcesSummary.  # noqa: E501
        :type zones: ResourceCount
        :param images: The images of this OrgResourcesSummary.  # noqa: E501
        :type images: ResourceCount
        :param keys: The keys of this OrgResourcesSummary.  # noqa: E501
        :type keys: ResourceCount
        :param scripts: The scripts of this OrgResourcesSummary.  # noqa: E501
        :type scripts: ResourceCount
        :param templates: The templates of this OrgResourcesSummary.  # noqa: E501
        :type templates: ResourceCount
        :param tunnels: The tunnels of this OrgResourcesSummary.  # noqa: E501
        :type tunnels: ResourceCount
        :param secrets: The secrets of this OrgResourcesSummary.  # noqa: E501
        :type secrets: ResourceCount
        :param schedules: The schedules of this OrgResourcesSummary.  # noqa: E501
        :type schedules: ResourceCount
        :param rules: The rules of this OrgResourcesSummary.  # noqa: E501
        :type rules: ResourceCount
        :param teams: The teams of this OrgResourcesSummary.  # noqa: E501
        :type teams: ResourceCount
        :param members: The members of this OrgResourcesSummary.  # noqa: E501
        :type members: ResourceCount
        """
        self.openapi_types = {
            'clouds': ResourceCount,
            'stacks': ResourceCount,
            'clusters': ResourceCount,
            'machines': ResourceCount,
            'volumes': ResourceCount,
            'buckets': ResourceCount,
            'networks': ResourceCount,
            'zones': ResourceCount,
            'images': ResourceCount,
            'keys': ResourceCount,
            'scripts': ResourceCount,
            'templates': ResourceCount,
            'tunnels': ResourceCount,
            'secrets': ResourceCount,
            'schedules': ResourceCount,
            'rules': ResourceCount,
            'teams': ResourceCount,
            'members': ResourceCount
        }

        self.attribute_map = {
            'clouds': 'clouds',
            'stacks': 'stacks',
            'clusters': 'clusters',
            'machines': 'machines',
            'volumes': 'volumes',
            'buckets': 'buckets',
            'networks': 'networks',
            'zones': 'zones',
            'images': 'images',
            'keys': 'keys',
            'scripts': 'scripts',
            'templates': 'templates',
            'tunnels': 'tunnels',
            'secrets': 'secrets',
            'schedules': 'schedules',
            'rules': 'rules',
            'teams': 'teams',
            'members': 'members'
        }

        self._clouds = clouds
        self._stacks = stacks
        self._clusters = clusters
        self._machines = machines
        self._volumes = volumes
        self._buckets = buckets
        self._networks = networks
        self._zones = zones
        self._images = images
        self._keys = keys
        self._scripts = scripts
        self._templates = templates
        self._tunnels = tunnels
        self._secrets = secrets
        self._schedules = schedules
        self._rules = rules
        self._teams = teams
        self._members = members

    @classmethod
    def from_dict(cls, dikt) -> 'OrgResourcesSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrgResourcesSummary of this OrgResourcesSummary.  # noqa: E501
        :rtype: OrgResourcesSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def clouds(self):
        """Gets the clouds of this OrgResourcesSummary.


        :return: The clouds of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        """Sets the clouds of this OrgResourcesSummary.


        :param clouds: The clouds of this OrgResourcesSummary.
        :type clouds: ResourceCount
        """

        self._clouds = clouds

    @property
    def stacks(self):
        """Gets the stacks of this OrgResourcesSummary.


        :return: The stacks of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        """Sets the stacks of this OrgResourcesSummary.


        :param stacks: The stacks of this OrgResourcesSummary.
        :type stacks: ResourceCount
        """

        self._stacks = stacks

    @property
    def clusters(self):
        """Gets the clusters of this OrgResourcesSummary.


        :return: The clusters of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this OrgResourcesSummary.


        :param clusters: The clusters of this OrgResourcesSummary.
        :type clusters: ResourceCount
        """

        self._clusters = clusters

    @property
    def machines(self):
        """Gets the machines of this OrgResourcesSummary.


        :return: The machines of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._machines

    @machines.setter
    def machines(self, machines):
        """Sets the machines of this OrgResourcesSummary.


        :param machines: The machines of this OrgResourcesSummary.
        :type machines: ResourceCount
        """

        self._machines = machines

    @property
    def volumes(self):
        """Gets the volumes of this OrgResourcesSummary.


        :return: The volumes of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this OrgResourcesSummary.


        :param volumes: The volumes of this OrgResourcesSummary.
        :type volumes: ResourceCount
        """

        self._volumes = volumes

    @property
    def buckets(self):
        """Gets the buckets of this OrgResourcesSummary.


        :return: The buckets of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this OrgResourcesSummary.


        :param buckets: The buckets of this OrgResourcesSummary.
        :type buckets: ResourceCount
        """

        self._buckets = buckets

    @property
    def networks(self):
        """Gets the networks of this OrgResourcesSummary.


        :return: The networks of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this OrgResourcesSummary.


        :param networks: The networks of this OrgResourcesSummary.
        :type networks: ResourceCount
        """

        self._networks = networks

    @property
    def zones(self):
        """Gets the zones of this OrgResourcesSummary.


        :return: The zones of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this OrgResourcesSummary.


        :param zones: The zones of this OrgResourcesSummary.
        :type zones: ResourceCount
        """

        self._zones = zones

    @property
    def images(self):
        """Gets the images of this OrgResourcesSummary.


        :return: The images of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this OrgResourcesSummary.


        :param images: The images of this OrgResourcesSummary.
        :type images: ResourceCount
        """

        self._images = images

    @property
    def keys(self):
        """Gets the keys of this OrgResourcesSummary.


        :return: The keys of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this OrgResourcesSummary.


        :param keys: The keys of this OrgResourcesSummary.
        :type keys: ResourceCount
        """

        self._keys = keys

    @property
    def scripts(self):
        """Gets the scripts of this OrgResourcesSummary.


        :return: The scripts of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this OrgResourcesSummary.


        :param scripts: The scripts of this OrgResourcesSummary.
        :type scripts: ResourceCount
        """

        self._scripts = scripts

    @property
    def templates(self):
        """Gets the templates of this OrgResourcesSummary.


        :return: The templates of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this OrgResourcesSummary.


        :param templates: The templates of this OrgResourcesSummary.
        :type templates: ResourceCount
        """

        self._templates = templates

    @property
    def tunnels(self):
        """Gets the tunnels of this OrgResourcesSummary.


        :return: The tunnels of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._tunnels

    @tunnels.setter
    def tunnels(self, tunnels):
        """Sets the tunnels of this OrgResourcesSummary.


        :param tunnels: The tunnels of this OrgResourcesSummary.
        :type tunnels: ResourceCount
        """

        self._tunnels = tunnels

    @property
    def secrets(self):
        """Gets the secrets of this OrgResourcesSummary.


        :return: The secrets of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this OrgResourcesSummary.


        :param secrets: The secrets of this OrgResourcesSummary.
        :type secrets: ResourceCount
        """

        self._secrets = secrets

    @property
    def schedules(self):
        """Gets the schedules of this OrgResourcesSummary.


        :return: The schedules of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this OrgResourcesSummary.


        :param schedules: The schedules of this OrgResourcesSummary.
        :type schedules: ResourceCount
        """

        self._schedules = schedules

    @property
    def rules(self):
        """Gets the rules of this OrgResourcesSummary.


        :return: The rules of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this OrgResourcesSummary.


        :param rules: The rules of this OrgResourcesSummary.
        :type rules: ResourceCount
        """

        self._rules = rules

    @property
    def teams(self):
        """Gets the teams of this OrgResourcesSummary.


        :return: The teams of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this OrgResourcesSummary.


        :param teams: The teams of this OrgResourcesSummary.
        :type teams: ResourceCount
        """

        self._teams = teams

    @property
    def members(self):
        """Gets the members of this OrgResourcesSummary.


        :return: The members of this OrgResourcesSummary.
        :rtype: ResourceCount
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this OrgResourcesSummary.


        :param members: The members of this OrgResourcesSummary.
        :type members: ResourceCount
        """

        self._members = members