import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'TeamsController'.replace('Controller', '').lower()
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


class TestTeamsController:
    """TeamsController integration test stubs"""

    def test_list_org_teams(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_org_teams

        List org teams
        """
        query_string = [('search', "name:finance"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/orgs/{org}/teams'.format(org="example_org") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    @pytest.fixture(scope="class")
    def setup(owner_api_token):
        _setup_module.setup(owner_api_token)
        yield
        _setup_module.teardown(owner_api_token)
    TestTeamsController = pytest.mark.usefixtures("setup")(TestTeamsController)

# Mark delete-related test methods as last to be run
for key in vars(TestTeamsController):
    attr = getattr(TestTeamsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestTeamsController, key, pytest.mark.last(attr))
