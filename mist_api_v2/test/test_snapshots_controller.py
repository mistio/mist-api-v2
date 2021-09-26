import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'SnapshotsController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULES_EXIST = False
else:
    SETUP_MODULES_EXIST = True


class TestSnapshotsController:
    """SnapshotsController integration test stubs"""

    def test_create_snapshot(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_snapshot

        Create snapshot
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_snapshots(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_snapshots

        List machine snapshots
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots'.format(machine="example_machine") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_remove_snapshot(self, pretty_print, mist_core, owner_api_token):
        """Test case for remove_snapshot

        Remove snapshot
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(machine="example_machine", snapshot="example_snapshot") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_revert_to_snapshot(self, pretty_print, mist_core, owner_api_token):
        """Test case for revert_to_snapshot

        Revert to snapshot
        """

        if SETUP_MODULES_EXIST:
            @classmethod
            def setUpClass(cls):
                setup_module.setup()

            @classmethod
            def tearDownClass(cls):
                setup_module.teardown()

        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(machine="example_machine", snapshot="example_snapshot") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestSnapshotsController):
    attr = getattr(TestSnapshotsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestSnapshotsController, key, pytest.mark.last(attr))
