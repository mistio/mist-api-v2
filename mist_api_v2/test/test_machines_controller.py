# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request

from mist_api_v2.test import BaseTestCase

unittest.TestLoader.sortTestMethodsUsing = \
    lambda _, x, y: - 1 if any(
        k in y for k in ['delete', 'remove', 'destroy']) else 1


class TestMachinesController(BaseTestCase):
    """MachinesController integration test stubs"""

    def test_associate_key(self):
        """Test case for associate_key

        Associate a key with a machine
        """
        key_machine_association = {
  "port" : 0,
  "user" : "user",
  "key" : "key"
}
        inject_vault_credentials_into_request(key_machine_association)
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/associate-key'.format(machine="example_machine"),
            method='PUT',
            headers=headers,
            data=json.dumps(key_machine_association),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clone_machine(self):
        """Test case for clone_machine

        Clone machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/clone'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_console(self):
        """Test case for console

        Open console
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/console'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_machine(self):
        """Test case for create_machine

        Create machine
        """
        create_machine_request = {
  "name" : "example_machine",
  "size" : "example_size",
  "image" : "example_image"
}
        inject_vault_credentials_into_request(create_machine_request)
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines',
            method='POST',
            headers=headers,
            data=json.dumps(create_machine_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_destroy_machine(self):
        """Test case for destroy_machine

        Destroy machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/destroy'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disassociate_key(self):
        """Test case for disassociate_key

        Disassociate a key from a machine
        """
        key_machine_disassociation = {
  "key" : "key"
}
        inject_vault_credentials_into_request(key_machine_disassociation)
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/disassociate-key'.format(machine="example_machine"),
            method='DELETE',
            headers=headers,
            data=json.dumps(key_machine_disassociation),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_machine(self):
        """Test case for edit_machine

        Edit machine
        """
        query_string = [('name', "renamed_example_machine")]
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}'.format(machine="example_machine"),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_expose_machine(self):
        """Test case for expose_machine

        Expose machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/expose'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_machine(self):
        """Test case for get_machine

        Get machine
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}'.format(machine="example_machine"),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_machines(self):
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
        headers = { 
            'Accept': 'application/json',
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reboot_machine(self):
        """Test case for reboot_machine

        Reboot machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/reboot'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rename_machine(self):
        """Test case for rename_machine

        Rename machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/rename'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resize_machine(self):
        """Test case for resize_machine

        Resize machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/resize'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resume_machine(self):
        """Test case for resume_machine

        Resume machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/resume'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ssh(self):
        """Test case for ssh

        Open secure shell
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/ssh'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_machine(self):
        """Test case for start_machine

        Start machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/start'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_machine(self):
        """Test case for stop_machine

        Stop machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/stop'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suspend_machine(self):
        """Test case for suspend_machine

        Suspend machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/suspend'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_undefine_machine(self):
        """Test case for undefine_machine

        Undefine machine
        """
        headers = { 
            'Authorization': create_short_lived_token(),
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/undefine'.format(machine="example_machine"),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
