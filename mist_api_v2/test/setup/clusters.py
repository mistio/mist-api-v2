import json

from mist.api.auth.methods import create_short_lived_token
from mist.api.auth.methods import inject_vault_credentials_into_request


def setup(app_client):
    add_cloud_request = {
        "name": "example_cloud",
        "provider": "google",
        "credentials": {
            "projectId": "projectId",
            "privateKey": "privateKey",
            "email": "email"
        }
    }
    inject_vault_credentials_into_request(add_cloud_request)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': create_short_lived_token(),
    }
    app_client.open(
        '/api/v2/clouds',
        method='POST',
        headers=headers,
        data=json.dumps(add_cloud_request),
        content_type='application/json')


def teardown(app_client):
    headers = {
        'Authorization': create_short_lived_token(),
    }
    app_client.open(
        '/api/v2/clouds/{cloud}'.format(cloud="example_cloud"),
        method='DELETE',
        headers=headers)
