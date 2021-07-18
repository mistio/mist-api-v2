# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util

class OneOfmapstring(Model):
    def __init__(self):
         self.openapi_types = {}
         self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> 'OneOfobjectstring':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict

        :rtype: OneOfobjectstring
        """
        return util.deserialize_model(dikt, cls)
