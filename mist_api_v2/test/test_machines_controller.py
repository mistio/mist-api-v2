import time
import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'ClustersController'.replace('Controller', '').lower()
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


@pytest.fixture(autouse=True)
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    if method_name == 'test_create_cluster':
        time.sleep(200)


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
        config.inject_vault_credentials(key_machine_association)
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/associate-key'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=key_machine_association)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_clone_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for clone_machine

        Clone machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/clone'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_console(self, pretty_print, mist_core, owner_api_token):
        """Test case for console

        Open console
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/console'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_create_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_machine

        Create machine
        """
        create_machine_request = {
  "name" : "example_machine",
  "size" : "example_size",
  "image" : "example_image"
}
        config.inject_vault_credentials(create_machine_request)
        uri = mist_core.uri + '/api/v2/machines' 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=create_machine_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_destroy_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for destroy_machine

        Destroy machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/destroy'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_disassociate_key(self, pretty_print, mist_core, owner_api_token):
        """Test case for disassociate_key

        Disassociate a key from a machine
        """
        key_machine_disassociation = {
  "key" : "key"
}
        config.inject_vault_credentials(key_machine_disassociation)
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/disassociate-key'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=key_machine_disassociation)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_edit_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_machine

        Edit machine
        """
        query_string = [('name', "renamed_example_machine")]
        uri = mist_core.uri + '/api/v2/machines/{machine}'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_expose_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for expose_machine

        Expose machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/expose'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_machine

        Get machine
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/machines/{machine}'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_machines(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_machines

        List machines
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "state:running"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/machines' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_reboot_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for reboot_machine

        Reboot machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/reboot'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_rename_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for rename_machine

        Rename machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/rename'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_resize_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for resize_machine

        Resize machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/resize'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_resume_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for resume_machine

        Resume machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/resume'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_ssh(self, pretty_print, mist_core, owner_api_token):
        """Test case for ssh

        Open secure shell
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/ssh'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_start_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for start_machine

        Start machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/start'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_stop_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for stop_machine

        Stop machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/stop'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_suspend_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for suspend_machine

        Suspend machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/suspend'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_undefine_machine(self, pretty_print, mist_core, owner_api_token):
        """Test case for undefine_machine

        Undefine machine
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/actions/undefine'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestClustersController):
    attr = getattr(TestClustersController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestClustersController, key, pytest.mark.order("last")(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    @pytest.fixture(scope="class")
    def setup(owner_api_token):
        _setup_module.setup(owner_api_token)
        yield
        _setup_module.teardown(owner_api_token)
    TestMachinesController = pytest.mark.usefixtures("setup")(TestMachinesController)
