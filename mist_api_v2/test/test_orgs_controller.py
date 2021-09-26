import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'OrgsController'.replace('Controller', '').lower()
    setup_module = importlib.import_module(
        f'mist_api_v2.test.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True

@pytest.fixture(scope="class")
def setup(owner_api_token):
    if SETUP_MODULE_EXISTS:
        setup_module.setup(owner_api_token)
        yield
        setup_module.teardown(owner_api_token)
    else:
        yield


@pytest.mark.usefixtures("setup")
class TestOrgsController:
    """OrgsController integration test stubs"""

    def test_get_member(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_member

        Get Org
        """
        query_string = [('only', "id")]
        uri = mist_core.uri + '/api/v2/orgs/{org}/members/{member}'.format(org="example_org", member="example_member") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_org(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_org

        Get Org
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/orgs/{org}'.format(org="example_org") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

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

    def test_list_orgs(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_orgs

        List orgs
        """
        query_string = [('allorgs', "'allorgs_example'"),
                        ('search', "name:Acme"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/orgs' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestOrgsController):
    attr = getattr(TestOrgsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestOrgsController, key, pytest.mark.last(attr))
