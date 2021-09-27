import importlib

import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

try:
    setup_module_name = 'JobsController'.replace('Controller', '').lower()
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{setup_module_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True


class TestJobsController:
    """JobsController integration test stubs"""

    def test_get_job(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_job

        Get job
        """
        uri = mist_core.uri + '/api/v2/jobs/{job_id}'.format(job_id="'job_id_example'") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
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
    TestJobsController = pytest.mark.usefixtures("setup")(TestJobsController)

# Mark delete-related test methods as last to be run
for key in vars(TestJobsController):
    attr = getattr(TestJobsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestJobsController, key, pytest.mark.last(attr))
