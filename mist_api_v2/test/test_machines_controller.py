# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.create_machine_request import CreateMachineRequest  # noqa: E501
from mist_api_v2.models.create_machine_response import CreateMachineResponse  # noqa: E501
from mist_api_v2.models.get_machine_response import GetMachineResponse  # noqa: E501
from mist_api_v2.models.key_machine_association import KeyMachineAssociation  # noqa: E501
from mist_api_v2.models.key_machine_disassociation import KeyMachineDisassociation  # noqa: E501
from mist_api_v2.models.list_machines_response import ListMachinesResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


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
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/associate-key'.format(machine='machine_example'),
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
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/clone'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_console(self):
        """Test case for console

        Open console
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/console'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_machine(self):
        """Test case for create_machine

        Create machine
        """
        create_machine_request = {
  "template" : "{}",
  "image" : "",
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
  "size" : "",
  "schedules" : [ "", "" ],
  "extra" : "",
  "name" : "name",
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
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'special-key',
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
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/destroy'.format(machine='machine_example'),
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
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/disassociate-key'.format(machine='machine_example'),
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
        query_string = [('name', "'name_example'")]
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}'.format(machine='machine_example'),
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
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/expose'.format(machine='machine_example'),
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
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}'.format(machine='machine_example'),
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
            'Authorization': 'special-key',
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
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/reboot'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rename_machine(self):
        """Test case for rename_machine

        Rename machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/rename'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resize_machine(self):
        """Test case for resize_machine

        Resize machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/resize'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resume_machine(self):
        """Test case for resume_machine

        Resume machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/resume'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ssh(self):
        """Test case for ssh

        Open secure shell
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/ssh'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_machine(self):
        """Test case for start_machine

        Start machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/start'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_machine(self):
        """Test case for stop_machine

        Stop machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/stop'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suspend_machine(self):
        """Test case for suspend_machine

        Suspend machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/suspend'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_undefine_machine(self):
        """Test case for undefine_machine

        Undefine machine
        """
        headers = { 
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/machines/{machine}/actions/undefine'.format(machine='machine_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
