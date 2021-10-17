# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.data_type import DataType
from mist_api_v2.models.frequency import Frequency
from mist_api_v2.models.query import Query
from mist_api_v2.models.rule_action import RuleAction
from mist_api_v2.models.selector import Selector
from mist_api_v2.models.trigger_after import TriggerAfter
from mist_api_v2.models.window import Window
from mist_api_v2 import util

from mist_api_v2.models.data_type import DataType  # noqa: E501
from mist_api_v2.models.frequency import Frequency  # noqa: E501
from mist_api_v2.models.query import Query  # noqa: E501
from mist_api_v2.models.rule_action import RuleAction  # noqa: E501
from mist_api_v2.models.selector import Selector  # noqa: E501
from mist_api_v2.models.trigger_after import TriggerAfter  # noqa: E501
from mist_api_v2.models.window import Window  # noqa: E501

class AddRuleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, queries=None, window=None, frequency=None, trigger_after=None, actions=None, selectors=None, data_type=None):  # noqa: E501
        """AddRuleRequest - a model defined in OpenAPI

        :param queries: The queries of this AddRuleRequest.  # noqa: E501
        :type queries: List[Query]
        :param window: The window of this AddRuleRequest.  # noqa: E501
        :type window: Window
        :param frequency: The frequency of this AddRuleRequest.  # noqa: E501
        :type frequency: Frequency
        :param trigger_after: The trigger_after of this AddRuleRequest.  # noqa: E501
        :type trigger_after: TriggerAfter
        :param actions: The actions of this AddRuleRequest.  # noqa: E501
        :type actions: List[RuleAction]
        :param selectors: The selectors of this AddRuleRequest.  # noqa: E501
        :type selectors: Selector
        :param data_type: The data_type of this AddRuleRequest.  # noqa: E501
        :type data_type: DataType
        """
        self.openapi_types = {
            'queries': List[Query],
            'window': Window,
            'frequency': Frequency,
            'trigger_after': TriggerAfter,
            'actions': List[RuleAction],
            'selectors': Selector,
            'data_type': DataType
        }

        self.attribute_map = {
            'queries': 'queries',
            'window': 'window',
            'frequency': 'frequency',
            'trigger_after': 'trigger_after',
            'actions': 'actions',
            'selectors': 'selectors',
            'data_type': 'data_type'
        }

        self._queries = queries
        self._window = window
        self._frequency = frequency
        self._trigger_after = trigger_after
        self._actions = actions
        self._selectors = selectors
        self._data_type = data_type

    @classmethod
    def from_dict(cls, dikt) -> 'AddRuleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddRuleRequest of this AddRuleRequest.  # noqa: E501
        :rtype: AddRuleRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def queries(self):
        """Gets the queries of this AddRuleRequest.


        :return: The queries of this AddRuleRequest.
        :rtype: List[Query]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this AddRuleRequest.


        :param queries: The queries of this AddRuleRequest.
        :type queries: List[Query]
        """
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501

        self._queries = queries

    @property
    def window(self):
        """Gets the window of this AddRuleRequest.


        :return: The window of this AddRuleRequest.
        :rtype: Window
        """
        return self._window

    @window.setter
    def window(self, window):
        """Sets the window of this AddRuleRequest.


        :param window: The window of this AddRuleRequest.
        :type window: Window
        """
        if window is None:
            raise ValueError("Invalid value for `window`, must not be `None`")  # noqa: E501

        self._window = window

    @property
    def frequency(self):
        """Gets the frequency of this AddRuleRequest.


        :return: The frequency of this AddRuleRequest.
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this AddRuleRequest.


        :param frequency: The frequency of this AddRuleRequest.
        :type frequency: Frequency
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def trigger_after(self):
        """Gets the trigger_after of this AddRuleRequest.


        :return: The trigger_after of this AddRuleRequest.
        :rtype: TriggerAfter
        """
        return self._trigger_after

    @trigger_after.setter
    def trigger_after(self, trigger_after):
        """Sets the trigger_after of this AddRuleRequest.


        :param trigger_after: The trigger_after of this AddRuleRequest.
        :type trigger_after: TriggerAfter
        """
        if trigger_after is None:
            raise ValueError("Invalid value for `trigger_after`, must not be `None`")  # noqa: E501

        self._trigger_after = trigger_after

    @property
    def actions(self):
        """Gets the actions of this AddRuleRequest.


        :return: The actions of this AddRuleRequest.
        :rtype: List[RuleAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AddRuleRequest.


        :param actions: The actions of this AddRuleRequest.
        :type actions: List[RuleAction]
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def selectors(self):
        """Gets the selectors of this AddRuleRequest.


        :return: The selectors of this AddRuleRequest.
        :rtype: Selector
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this AddRuleRequest.


        :param selectors: The selectors of this AddRuleRequest.
        :type selectors: Selector
        """
        if selectors is None:
            raise ValueError("Invalid value for `selectors`, must not be `None`")  # noqa: E501

        self._selectors = selectors

    @property
    def data_type(self):
        """Gets the data_type of this AddRuleRequest.


        :return: The data_type of this AddRuleRequest.
        :rtype: DataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this AddRuleRequest.


        :param data_type: The data_type of this AddRuleRequest.
        :type data_type: DataType
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type
