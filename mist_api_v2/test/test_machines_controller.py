import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'MachinesController'.replace('Controller', '').lower()
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
        time.sleep(240)
    elif method_name == 'test_destroy_cluster':
        time.sleep(120)


class TestMachinesController:
    """MachinesController integration test stubs"""

    def test_associate_key(self, pretty_print, mist_core, owner_api_token):
        """Test case for associate_key

        Associate a key with a machine
        """
        key_machine_association = {
  "port" : 0,
  "user" : "user",
  "key" : "key"
}
        for k in key_machine_association:
            if k in setup_data:
                key_machine_association[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                key_machine_association[k] = setup_data[resource_name_singular]
        inject_vault_credentials(key_machine_association)
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/associate-key'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=key_machine_association)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_clone_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for clone_machine

        Clone machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/clone'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_console(self, pretty_print, mist_core, owner_api_token):
        """Test case for console

        Open console
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/console'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_create_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_machine

        Create machine
        """
        create_machine_request = {
  "template" : "{}",
  "image" : "Debian",
  "quantity" : 1.4658129805029452,
  "disks" : {
    "disk_size" : 0,
    "disk_path" : "disk_path"
  },
  "fqdn" : "fqdn",
  "cloudinit" : "cloudinit",
  "volumes" : "",
  "save" : true,
  "dry" : true,
  "monitoring" : true,
  "tags" : "{}",
  "cloud" : "cloud",
  "size" : "m1.small",
  "schedules" : [ "", "" ],
  "extra" : "",
  "name" : "DB mirror",
  "location" : "location",
  "expiration" : {
    "date" : "2000-01-23T04:56:07.000+00:00",
    "action" : "stop",
    "notify" : {
      "period" : "minutes",
      "value" : 1
    },
    "notify_msg" : "notify_msg"
  },
  "net" : "",
  "scripts" : [ "", "" ],
  "key" : ""
}
        for k in create_machine_request:
            if k in setup_data:
                create_machine_request[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                create_machine_request[k] = setup_data[resource_name_singular]
        inject_vault_credentials(create_machine_request)
        uri = mist_core.uri + '/api/v2/machines'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_machine_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_destroy_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for destroy_machine

        Destroy machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/destroy'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_disassociate_key(self, pretty_print, mist_core, owner_api_token):
        """Test case for disassociate_key

        Disassociate a key from a machine
        """
        key_machine_disassociation = {
  "key" : "key"
}
        for k in key_machine_disassociation:
            if k in setup_data:
                key_machine_disassociation[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                key_machine_disassociation[k] = setup_data[resource_name_singular]
        inject_vault_credentials(key_machine_disassociation)
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/disassociate-key'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=key_machine_disassociation)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_edit_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_machine

        Edit machine
        """
        edit_machine_request = {
  "expiration" : {
    "date" : "date",
    "action" : "stop",
    "notify" : 0
  }
}
        for k in edit_machine_request:
            if k in setup_data:
                edit_machine_request[k] = setup_data[k]
            elif k == 'name' and resource_name_singular in setup_data:
                edit_machine_request[k] = setup_data[resource_name_singular]
        inject_vault_credentials(edit_machine_request)
        uri = mist_core.uri + '/api/v2/machines/{machine}'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=edit_machine_request)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_machine

        Get machine
        """
        query_string = [('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/machines/{machine}'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_machines(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_machines

        List machines
        """
        query_string = [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'state:running'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', '56'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/machines'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_reboot_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for reboot_machine

        Reboot machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/reboot'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_rename_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for rename_machine

        Rename machine
        """
        query_string = [('name', 'my-renamed-machine')]
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/rename'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_resize_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for resize_machine

        Resize machine
        """
        query_string = [('size', '9417745961a84bffbf6419e5of68faa5')]
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/resize'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_resume_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for resume_machine

        Resume machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/resume'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_ssh(self, pretty_print, mist_core, owner_api_token):
        """Test case for ssh

        Open secure shell
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/ssh'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_start_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for start_machine

        Start machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/start'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_stop_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for stop_machine

        Stop machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/stop'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_suspend_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for suspend_machine

        Suspend machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/suspend'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_undefine_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for undefine_machine

        Undefine machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/undefine'.format(
            machine=setup_data.get('machine') or 'my-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestMachinesController):
    attr = getattr(TestMachinesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestMachinesController, key, pytest.mark.order('last')(attr))

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
    TestMachinesController = pytest.mark.usefixtures('setup')(
        TestMachinesController)
