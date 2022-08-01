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

resource_name = 'TagsController'.replace('Controller', '').lower()
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


class TestTagsController:
    """TagsController integration test stubs"""

    def test_list_tags(self, pretty_print, owner_api_token):
        """Test case for list_tags

        List tags
        """
        query_string = setup_data.get('list_tags', {}).get('query_string') or [('types', 'machines,clouds,keys'),
                        ('search', 'key:key1'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'key'),
                        ('deref', 'id')]
        uri = MIST_URL + '/api/v2/tags'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_tags' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_tag_resources(self, pretty_print, owner_api_token):
        """Test case for tag_resources

        Tag Resources
        """
        tag_resources_request = setup_data.get('tag_resources', {}).get(
            'request_body') or json.loads("""{
  "operations" : [ {
    "resources" : [ {
      "resource_id" : "resource_id"
    }, {
      "resource_id" : "resource_id"
    } ],
    "operation" : "add",
    "tags" : [ {
      "value" : "value",
      "key" : "key"
    }, {
      "value" : "value",
      "key" : "key"
    } ]
  }, {
    "resources" : [ {
      "resource_id" : "resource_id"
    }, {
      "resource_id" : "resource_id"
    } ],
    "operation" : "add",
    "tags" : [ {
      "value" : "value",
      "key" : "key"
    }, {
      "value" : "value",
      "key" : "key"
    } ]
  } ]
}""", strict=False)
        uri = MIST_URL + '/api/v2/tags'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=tag_resources_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        if 'tag_resources' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestTagsController, method_name)
        setattr(TestTagsController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestTagsController):
        attr = getattr(TestTagsController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestTagsController, key, pytest.mark.order('last')(attr))

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
    TestTagsController = pytest.mark.usefixtures('setup')(
        TestTagsController)
