import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'DatapointsController'.replace('Controller', '').lower()
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
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    if method_name == 'test_create_cluster':
        time.sleep(setup_data.get(f'{method_name}_timeout') or 240)
    elif method_name == 'test_destroy_cluster':
        time.sleep(setup_data.get(f'{method_name}_timeout') or 120)


class TestDatapointsController:
    """DatapointsController integration test stubs"""

    def test_get_datapoints(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_datapoints

        Get datapoints
        """
        query_string = [('query', 'system_load1'),
                        ('tags', 'cluster=east1,production'),
                        ('search', 'state:running'),
                        ('start', '1633096171'),
                        ('end', '1633096171'),
                        ('step', '5.0'),
                        ('time', '1633096171')]
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('get_datapoints')
        if overwrite_query_string:
            query_string = overwrite_query_string
        uri = mist_core.uri + '/api/v2/datapoints'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestDatapointsController):
    attr = getattr(TestDatapointsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestDatapointsController, key, pytest.mark.order('last')(attr))

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
    TestDatapointsController = pytest.mark.usefixtures('setup')(
        TestDatapointsController)
