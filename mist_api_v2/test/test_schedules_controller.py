# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.add_schedule_request import AddScheduleRequest  # noqa: E501
from mist_api_v2.models.edit_schedule_request import EditScheduleRequest  # noqa: E501
from mist_api_v2.models.get_schedule_response import GetScheduleResponse  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_schedules_response import ListSchedulesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestSchedulesController(BaseTestCase):
    """SchedulesController integration test stubs"""

    def test_add_schedule(self):
        """Test case for add_schedule

        Add schedule
        """
        add_schedule_request = {
  "start_after" : "2022-06-01 T00:00:00",
  "schedule_type" : "one_off",
  "schedule_entry" : "2022-05-28 00:00:00",
  "name" : "backup-schedule",
  "description" : "This is a schedule",
  "action" : "start",
  "script_id" : "d5775984772949de820fa8279c306b30",
  "run_immediately" : false,
  "params" : "Parameters string",
  "selectors" : [ null, null ],
  "enabled" : true
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/schedules',
            method='POST',
            headers=headers,
            data=json.dumps(add_schedule_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_schedule(self):
        """Test case for delete_schedule

        Delete schedule
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/schedules/{schedule}'.format(schedule='deleted-schedule'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_schedule(self):
        """Test case for edit_schedule

        Edit schedule
        """
        edit_schedule_request = {
  "start_after" : "2022-06-01 00:00:00",
  "schedule_type" : "one_off",
  "schedule_entry" : "2022-05-28 00:00:00",
  "name" : "schedule-name",
  "description" : "This is a schedule that is about to be edited",
  "action" : "start",
  "script_id" : "d5775984772949de820fa8279c306b30",
  "params" : "Parameters string",
  "selectors" : [ null, null ],
  "enabled" : true
}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/schedules/{schedule}'.format(schedule='edited-schedule'),
            method='PATCH',
            headers=headers,
            data=json.dumps(edit_schedule_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedule(self):
        """Test case for get_schedule

        Get schedule
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/schedules/{schedule}'.format(schedule='retrieved-schedule'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_schedules(self):
        """Test case for list_schedules

        List schedules
        """
        query_string = [('search', 'schedule-name'),
                        ('sort', '-name'),
                        ('start', '3'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto')]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
            'CookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v2/schedules',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
