import json
import time
import importlib

import pytest

from misttests.config import MIST_URL
from misttests.integration.api.helpers import assert_response_found
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']
REDIRECT_OPERATIONS = ['ssh', 'console']

resource_name = 'SchedulesController'.replace('Controller', '').lower()
resource_name_singular = resource_name.strip('s')
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def after_test(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    test_operation = method_name.replace('test_', '')
    callback = setup_data.get(test_operation, {}).get('callback')
    if callable(callback):
        assert callback()
    else:
        sleep = setup_data.get(test_operation, {}).get('sleep')
        if sleep:
            time.sleep(sleep)


class TestSchedulesController:
    """SchedulesController integration test stubs"""

    def test_add_schedule(self, pretty_print, owner_api_token):
        """Test case for add_schedule

        Add schedule
        """
        add_schedule_request = setup_data.get('add_schedule', {}).get(
            'request_body') or json.loads("""{
  "expires" : "2022-06-01 T00:00:00",
  "reminder" : {
    "message" : "message",
    "when" : {
      "unit" : "seconds",
      "value" : 6
    }
  },
  "name" : "backup-schedule",
  "description" : "Backup schedule",
  "run_immediately" : false,
  "selectors" : [ {
    "type" : "tags",
    "include" : [ "dev" ]
  } ],
  "actions" : [ {
    "action_type" : "start"
  } ],
  "when" : {
    "schedule_type" : "interval",
    "unit" : "minutes",
    "value" : 15
  },
  "enabled" : true
}""", strict=False)
        uri = MIST_URL + '/api/v2/schedules'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_schedule_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'add_schedule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_delete_schedule(self, pretty_print, owner_api_token):
        """Test case for delete_schedule

        Delete schedule
        """
        uri = MIST_URL + '/api/v2/schedules/{schedule}'.format(
            schedule=setup_data.get('delete_schedule', {}).get('schedule') or setup_data.get('schedule') or 'deleted-schedule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        if 'delete_schedule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_edit_schedule(self, pretty_print, owner_api_token):
        """Test case for edit_schedule

        Edit schedule
        """
        edit_schedule_request = setup_data.get('edit_schedule', {}).get(
            'request_body') or json.loads("""{
  "expires" : "2024-06-01 T00:00:00",
  "reminder" : {
    "message" : "message",
    "when" : {
      "unit" : "seconds",
      "value" : 6
    }
  },
  "name" : "schedule-name",
  "description" : "Edited Schedule",
  "selectors" : [ {
    "type" : "tags",
    "include" : [ "dev" ]
  } ],
  "actions" : [ {
    "action_type" : "start"
  } ],
  "when" : {
    "schedule_type" : "interval",
    "unit" : "minutes",
    "value" : 15
  },
  "enabled" : true
}""", strict=False)
        uri = MIST_URL + '/api/v2/schedules/{schedule}'.format(
            schedule=setup_data.get('edit_schedule', {}).get('schedule') or setup_data.get('schedule') or 'edited-schedule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=edit_schedule_request)
        request_method = getattr(request, 'PATCH'.lower())
        response = request_method()
        if 'edit_schedule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_get_schedule(self, pretty_print, owner_api_token):
        """Test case for get_schedule

        Get schedule
        """
        query_string = setup_data.get('get_schedule', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/schedules/{schedule}'.format(
            schedule=setup_data.get('get_schedule', {}).get('schedule') or setup_data.get('schedule') or 'retrieved-schedule')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_schedule' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_schedules(self, pretty_print, owner_api_token):
        """Test case for list_schedules

        List schedules
        """
        query_string = setup_data.get('list_schedules', {}).get('query_string') or [('search', 'schedule-name'),
                        ('sort', '-name'),
                        ('start', '3'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/schedules'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_schedules' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestSchedulesController, method_name)
        setattr(TestSchedulesController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestSchedulesController):
        attr = getattr(TestSchedulesController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestSchedulesController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            global setup_data
            setup_data = _setup_module.setup(owner_api_token) or {}
            yield
            _setup_module.teardown(owner_api_token, setup_data)
            class_setup_done = True
    TestSchedulesController = pytest.mark.usefixtures('setup')(
        TestSchedulesController)
