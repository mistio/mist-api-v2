import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'VolumesController'.replace('Controller', '').lower()
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


class TestVolumesController:
    """VolumesController integration test stubs"""

    def test_create_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_volume

        Create volume
        """
        create_volume_request = {
  "template" : "{}",
  "quantity" : 0,
  "ex_disk_type" : "pd-standard",
  "ex_volume_type" : "standard",
  "save" : "true",
  "dry" : "true",
  "tags" : "{}",
  "cloud" : "my-cloud",
  "ex_iops" : "ex_iops",
  "size" : 1,
  "extra" : "{}",
  "name" : "my-volume",
  "location" : "us-central1-a"
}
        if 'overwrite_request' in setup_data:
            create_volume_request = setup_data['overwrite_request']
        else:
            for k in create_volume_request:
                if k in setup_data:
                    create_volume_request[k] = setup_data[k]
                elif k == 'name' and resource_name_singular in setup_data:
                    create_volume_request[k] = setup_data[
                        resource_name_singular]
        inject_vault_credentials(create_volume_request)
        uri = mist_core.uri + '/api/v2/volumes'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_volume_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_delete_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_volume

        Delete volume
        """
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(
            volume=setup_data.get('volume') or 'my-volume')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_edit_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_volume

        Edit volume
        """
        query_string = setup_data.get('query_string', {}).get(
            'edit_volume')
        if not query_string:
            query_string = [('name', 'my-renamed-volume')]
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(
            volume=setup_data.get('volume') or 'my-volume')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_volume

        Get volume
        """
        query_string = setup_data.get('query_string', {}).get(
            'get_volume')
        if not query_string:
            query_string = [('only', 'id'),
        query_string = setup_data.get('query_string', {}).get(
            'get_volume')
        if not query_string:
                            ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(
            volume=setup_data.get('volume') or 'my-volume')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_volumes(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_volumes

        List volumes
        """
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
            query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
                            ('search', 'location:Amsterdam'),
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
                            ('sort', '-name'),
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
                            ('start', '50'),
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
                            ('limit', '56'),
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
                            ('only', 'id'),
        query_string = setup_data.get('query_string', {}).get(
            'list_volumes')
        if not query_string:
                            ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/volumes'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestVolumesController):
    attr = getattr(TestVolumesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestVolumesController, key, pytest.mark.order('last')(attr))

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
    TestVolumesController = pytest.mark.usefixtures('setup')(
        TestVolumesController)
