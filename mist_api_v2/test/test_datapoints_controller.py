import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']


class TestDatapointsController:
    """DatapointsController integration test stubs"""

    def test_get_datapoints(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_datapoints

        Get datapoints
        """
        query_string = [('query', "'query_example'"),
                        ('tags', "'tags_example'"),
                        ('search', "'search_example'"),
                        ('start', "'start_example'"),
                        ('end', "'end_example'"),
                        ('step', "'step_example'"),
                        ('time', "'time_example'")]
        uri = mist_core.uri + '/api/v2/datapoints' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestDatapointsController):
    attr = getattr(TestDatapointsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestDatapointsController, key, pytest.mark.last(attr))
