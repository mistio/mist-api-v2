import time
import importlib

import pytest

from misttests.config import MIST_URL
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests
from misttests.integration.api.utils import assert_equal, assert_in
from datetime import datetime

KEYS_URI = f'{MIST_URL}/api/v2/keys'
TAGS_URI = f'{MIST_URL}/api/v2/tags'

try:
    _setup_module = importlib.import_module(
        'misttests.integration.api.main.v2.setup.search_tags')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def after_test(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    test_operation = method_name.replace('test_', '')
    callback = setup_data.get(test_operation, {}).get('callback')
    if callable(callback):
        assert callback()
    else:
        sleep = setup_data.get(test_operation, {}).get('sleep')
        if sleep:
            time.sleep(sleep)


class TestSearchTags:
    """Search by tags in list_keys test stubs"""

    def test_search_fulltag(self, pretty_print, owner_api_token):
        """Test case for search Keys by full tag=key:value"""
        print(datetime.now().time())
        print("The tagged resources are ", setup_data['tagged'])

        print("Hitting the api:")
        # Checking if all Keys exist:
        query_string = [('only', 'id')]

        response = MistRequests(
            api_token=owner_api_token,
            uri=KEYS_URI,
            params=query_string).get()
        assert_response_ok(response)
        print(response.json()['data'])
        assert_equal(response['meta']['total'], setup_data['N_KEYS'])

        query_string = [('search', 'tag:dev,value1'), ('only', 'id')]
        response = MistRequests(
            api_token=owner_api_token,
            uri=KEYS_URI,
            params=query_string).get()
        assert_response_ok(response)
        print("List keys with query=", query_string)
        print(response.json()['data'])
        for id in setup_data['tagged']:
            assert_in(id, response.json()['data'])
        print('Success!!!')

    def test_search_only_tagkey(self, pretty_print, owner_api_token):
        """Test case for search Keys by tagkey"""
        print(datetime.now().time())
        print("The tagged resources are ", setup_data['tagged'])
        print("Hitting the api:")

        query_string = [('search', 'tag:dev'), ('only', 'id')]
        response = MistRequests(
            api_token=owner_api_token,
            uri=KEYS_URI,
            params=query_string).get()

        assert_response_ok(response)
        print("List keys with query=", query_string)
        print(response.json()['data'])
        for id in setup_data['tagged']:
            assert_in(id, response.json()['data'])
        print('Success!!!')

    def test_search_only_tagvalue(self, pretty_print, owner_api_token):
        """Test case for search Keys by tagValue"""
        print(datetime.now().time())
        print("The tagged resources are ", setup_data['tagged'])
        print("Hitting the api:")

        query_string = [('search', 'tag:dev'), ('only', 'id')]
        response = MistRequests(
            api_token=owner_api_token,
            uri=KEYS_URI,
            params=query_string).get()
        assert_response_ok(response)
        print("List keys with query=", query_string)
        print(response.json()['data'])
        for id in setup_data['tagged']:
            assert_in(id, response.json()['data'])
        print('Success!!!')

    def test_search_implicit_tagkey(self, pretty_print, owner_api_token):
        """Test case for implicit search Keys by tagKey"""
        print(datetime.now().time())
        print("The tagged resources are ", setup_data['tagged'])
        print("Hitting the api:")

        query_string = [('search', 'dev'), ('only', 'id')]
        response = MistRequests(
            api_token=owner_api_token,
            uri=KEYS_URI,
            params=query_string).get()

        assert_response_ok(response)
        print("List keys with query=", query_string)
        print(response.json()['data'])
        for id in setup_data['tagged']:
            assert_in(id, response.json()['data'])
        print('Success!!!')

    def test_search_implicit_tagValue(self, pretty_print, owner_api_token):
        """Test case for implicit search Keys by tagValue"""
        print(datetime.now().time())
        print("The tagged resources are ", setup_data['tagged'])
        print("Hitting the api:")

        query_string = [('search', 'value1'), ('only', 'id')]
        response = MistRequests(
            api_token=owner_api_token,
            uri=KEYS_URI,
            params=query_string).get()

        assert_response_ok(response)
        print("List keys with query=", query_string)
        print(response.json()['data'])
        for id in setup_data['tagged']:
            assert_in(id, response.json()['data'])
        print('Success!!!')

    # def test_untag_and_search_tags(self, pretty_print, owner_api_token):
    #     """Test case for searching keys by tags when no
    #        key is tagged. Should return []
    #     """
    #     print(datetime.now().time())
    #     print("Untagging")
    #     remove_request = setup_data['tag_request'].copy()
    #     remove_request['operations'][0].update({'operation': 'remove'})

    #     request = MistRequests(
    #         api_token=owner_api_token,
    #         uri=TAGS_URI,
    #         json=remove_request)

    #     response = request.post()
    #     assert_response_ok(response)

    #     print("Hitting the api:")

    #     query_string = [('search', 'dev'), ('only', 'id')]
    #     response = MistRequests(
    #         api_token=owner_api_token,
    #         uri=KEYS_URI,
    #         params=query_string).get()

    #     assert_response_ok(response)
    #     print("List keys with search=dev")
    #     print(response.json()['data'])
    #     assert_list_empty(response.json()['data'])


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
    TestSearchTags = pytest.mark.usefixtures('setup')(
        TestSearchTags)
