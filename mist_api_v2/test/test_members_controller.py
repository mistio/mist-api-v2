import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'MembersController'.replace('Controller', '').lower()
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


@pytest.fixture(scope="class")
def setup(owner_api_token):
    if SETUP_MODULE_EXISTS:
        _setup_module.setup(owner_api_token)
        yield
        _setup_module.teardown(owner_api_token)
    else:
        yield


@pytest.mark.usefixtures("setup")
class TestMembersController:
    """MembersController integration test stubs"""

    def test_list_org_members(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_org_members

        List org members
        """
        query_string = [('search', "email:dev@mist.io"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id")]
        uri = mist_core.uri + '/api/v2/orgs/{org}/members'.format(org="example_org") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestMembersController):
    attr = getattr(TestMembersController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestMembersController, key, pytest.mark.last(attr))
