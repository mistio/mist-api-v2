import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'OrgsController'.replace('Controller', '').lower()
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


class TestOrgsController:
    """OrgsController integration test stubs"""

    def test_get_member(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_member

        Get Org
        """
        query_string = [('only', 'id')]
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('get_member')
        if overwrite_query_string:
            query_string = overwrite_query_string
        uri = mist_core.uri + '/api/v2/orgs/{org}/members/{member}'.format(
            org=setup_data.get('org') or 'my-org', member=setup_data.get('member') or 'my-member')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_org(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_org

        Get Org
        """
        query_string = [('only', 'id'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('get_org')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('deref', 'auto')]
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('get_org')
        if overwrite_query_string:
            query_string = overwrite_query_string
        uri = mist_core.uri + '/api/v2/orgs/{org}'.format(
            org=setup_data.get('org') or 'my-org')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_org_members(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_org_members

        List org members
        """
        query_string = [('search', 'email:dev@mist.io'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_members')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('sort', '-name'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_members')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('start', '50'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_members')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('limit', '56'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_members')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('only', 'id')]
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_members')
        if overwrite_query_string:
            query_string = overwrite_query_string
        uri = mist_core.uri + '/api/v2/orgs/{org}/members'.format(
            org=setup_data.get('org') or 'my-org')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_org_teams(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_org_teams

        List org teams
        """
        query_string = [('search', 'name:finance'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_teams')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('sort', '-name'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_teams')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('start', '50'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_teams')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('limit', '56'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_teams')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('only', 'id'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_teams')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('deref', 'auto')]
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_org_teams')
        if overwrite_query_string:
            query_string = overwrite_query_string
        uri = mist_core.uri + '/api/v2/orgs/{org}/teams'.format(
            org=setup_data.get('org') or 'my-org')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_orgs(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_orgs

        List orgs
        """
        query_string = [('allorgs', 'true'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('search', 'name:Acme'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('sort', '-name'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('start', '50'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('limit', '56'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('only', 'id'),
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
                        ('deref', 'auto')]
        overwrite_query_string = setup_data.get(
            'query_string', {}).get('list_orgs')
        if overwrite_query_string:
            query_string = overwrite_query_string
        uri = mist_core.uri + '/api/v2/orgs'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestOrgsController):
    attr = getattr(TestOrgsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestOrgsController, key, pytest.mark.order('last')(attr))

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
    TestOrgsController = pytest.mark.usefixtures('setup')(
        TestOrgsController)
