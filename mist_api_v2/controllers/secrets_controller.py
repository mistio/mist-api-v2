import connexion

from mist_api_v2.models.create_secret_request import CreateSecretRequest  # noqa: E501
from mist_api_v2.models.edit_secret_request import EditSecretRequest  # noqa: E501
from mist_api_v2.models.get_secret_response import GetSecretResponse  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_secrets_response import ListSecretsResponse  # noqa: E501

from mist.api.secrets.models import VaultSecret

from mist.api import config

import mongoengine as me


def create_secret(create_secret_request=None):  # noqa: E501
    """Create secret

    Creates a new secret and returns the secret object. CREATE permission required on secret. # noqa: E501

    :param create_secret_request:
    :type create_secret_request: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        create_secret_request = CreateSecretRequest.from_dict(connexion.request.get_json())  # noqa: E501
    auth_context = connexion.context['token_info']['auth_context']

    name = create_secret_request.name
    secret = create_secret_request.secret

    auth_context.check_perm("secret", "create", None)
    _secret = VaultSecret(name=name, owner=auth_context.owner)
    try:
        _secret.save()
    except me.NotUniqueError as exc:
        return exc.args[0], 409

    try:
        _secret.create_or_update(secret)
    except Exception as exc:
        _secret.delete()
        # FIXME: (probably) throws 500 -- include exceptions in spec
        raise exc

    # Set ownership.
    _secret.assign_to(auth_context.user)

    from mist.api.helpers import trigger_session_update
    trigger_session_update(auth_context.owner.id, ['secrets'])

    if config.HAS_RBAC:
        auth_context.org.mapper.update(
            _secret,
            # callback=async_session_update,
            args=(auth_context.owner.id, ['secrets'], )
        )
    return InlineResponse200(id=_secret.id)


def delete_secret(secret):  # noqa: E501
    """Delete secret

    Delete target secret. DELETE permission required on secret. # noqa: E501

    :param secret:
    :type secret: str

    :rtype: None
    """
    auth_context = connexion.context['token_info']['auth_context']
    secret_id = secret
    try:
        secret = VaultSecret.objects.get(owner=auth_context.owner,
                                         id=secret_id)
    except VaultSecret.DoesNotExist:
        return 'VaultSecret does not exist', 404
    auth_context.check_perm('secret', 'delete', secret_id)
    secret.delete(delete_from_engine=True)

    return 'Deleted secret `%s`' % secret.name, 200


def edit_secret(secret, edit_secret_request=None):  # noqa: E501
    """Edit secret

    Edit/update target secret and return the secret object. UPDATE  permission required on secret.# noqa: E501

    :param secret:
    :type secret: str

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        edit_secret_request = EditSecretRequest.from_dict(connexion.request.get_json())  # noqa: E501
    auth_context = connexion.context['token_info']['auth_context']

    secret_id = secret
    updated_secret = edit_secret_request.secret

    try:
        _secret = VaultSecret.objects.get(owner=auth_context.owner,
                                          id=secret_id)
    except VaultSecret.DoesNotExist:
        return 'VaultSecret does not exist', 404

    auth_context.check_perm("secret", "edit", secret_id)
    _secret.create_or_update(updated_secret)

    return _secret.as_dict()


def get_secret(secret, value=False):  # noqa: E501
    """Get secret

    Read target secret. READ permission required on secret. # noqa: E501

    :param secret:
    :type secret: str
    :param value:
    :type secret: bool

    :rtype: GetSecretResponse
    """
    from mist.api.methods import list_resources
    from mist.api.logs.methods import log_event
    auth_context = connexion.context['token_info']['auth_context']
    secret_dict = {}

    try:
        [secret], total = list_resources(auth_context, 'secret',
                                         search=secret, limit=1)
    except ValueError:
        return 'Secret does not exist', 404

    meta = {
        'kind': 'secret',
        'total': total,
        'returned': 1,
    }

    secret_dict.update(secret.as_dict())

    if value:
        auth_context.check_perm('secret', 'read_value', secret.id)
        log_event(
            auth_context.owner.id, 'request', 'read_value',
            secret_id=secret.id, user_id=auth_context.user.id,
        )
        secret_dict.update(
            {'value': secret.data})

    return GetSecretResponse(secret_dict, meta)


def list_secrets(search=None, sort=None, start=0, limit=100, only=None, deref='auto'):  # noqa: E501
    """List secrets

    List secrets owned by the active org. READ permission required on secret. # noqa: E501
    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int
    :param only: Only return these fields
    :type only: str

    :rtype: ListSecretsResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    from .base import list_resources

    result = list_resources(auth_context, 'secret', search=search,
                            only=only, sort=sort, limit=limit,
                            deref=deref)
    return ListSecretsResponse(data=result['data'], meta=result['meta'])
