import connexion    
import six

from mist_api_v2.models.create_secret_request import CreateSecretRequest  # noqa: E501
from mist_api_v2.models.get_secret_response import GetSecretResponse  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_secrets_response import ListSecretsResponse  # noqa: E501
from mist_api_v2 import util

from mist.api.secrets.models import VaultSecret

from mist.api.exceptions import ConflictError

from mist.api import config

import mongoengine as me


def create_secret(create_secret_request=None):  # noqa: E501
    """Create secret

    Creates a new secret and returns the secret&#39;s id. CREATE permission required on secret. # noqa: E501

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
    except me.NotUniqueError:
        # FIXME: throws 500
        raise ConflictError("The path specified exists on Vault. \
                    Try changing the name of the secret")

    try:
        _secret.ctl.create_or_update_secret(secret)
    except Exception as exc:
        _secret.delete()
        # FIXME: (probably) throws 500 -- include exceptions in spec
        raise exc

    # Set ownership.
    _secret.assign_to(auth_context.user)

    from mist.api.helpers import trigger_session_update
    trigger_session_update(auth_context.owner.id, ['secrets'])

    if config.HAS_RBAC:
        auth_context.owner.mapper.update(
            _secret,
            callback=async_session_update,
            args=(auth_context.owner.id, ['secrets'], )
        )

    return _secret.as_dict()


def delete_secret(secret):  # noqa: E501
    """Delete secret

    Delete target secret # noqa: E501

    :param secret: 
    :type secret: str

    :rtype: None
    """
    from mist.api.secrets.models import VaultSecret
    auth_context = connexion.context['token_info']['auth_context']
    secret_id = secret
    try:
        secret = VaultSecret.objects.get(owner=auth_context.owner,
                                         id=secret_id)
    except VaultSecret.DoesNotExist:
        return 'VaultSecret does not exist', 404
    auth_context.check_perm('secret', 'delete', secret_id)
    secret.ctl.delete_secret()
    secret.delete()

    return 'Deleted secret `%s`' % secret.name, 200


def edit_secret(secret):  # noqa: E501
    """Edit secret

    Edit/update target secret # noqa: E501

    :param secret: 
    :type secret: str

    :rtype: None
    """
    return 'do some magic!'


def get_secret(secret):  # noqa: E501
    """Get secret

    Read target secret # noqa: E501

    :param secret: 
    :type secret: str

    :rtype: GetSecretResponse
    """
    from mist.api.methods import list_resources
    auth_context = connexion.context['token_info']['auth_context']
    secret_id = secret
    try:
        secret = VaultSecret.objects.get(owner=auth_context.owner,
                                         id=secret_id)
    except me.DoesNotExist:
        raise NotFoundError('Secret does not exist')

    auth_context.check_perm("secret", "read", secret_id)

    secret_dict = secret.ctl.read_secret()

    # if key and not secret_dict.get(key, ''):
    #     raise BadRequestError('Secret %s does not have a %s key'
    #                           % (secret.name, key))

    return secret_dict # if not key else {key: secret_dict[key]}


def list_secrets(search=None, sort=None, start=0, limit=100, only=None, cached=True, path=None):  # noqa: E501
    """List secrets

    List secrets owned by the active org. READ permission required on secret. # noqa: E501
    :param cached: Only return cached secrets if set to true
    :type cached: bool
    :param path: Only return secrets under this path
    :type path: str
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
    path = path or '.'
    if path != '.':  # need to apply search based on the name
        if not search:
            search = "name:%s" % path
        else:
            search += " and name:%s" % path

    if cached:
        from mist.api.methods import list_resources
        secrets, total = list_resources(auth_context, 'secret', search=search,
                                    only=only, sort=sort, start=start,
                                    limit=limit)
    else:
        from mist.api.secrets.methods import filter_list_secrets
        # TODO: Reimplement when logic of search, sort etc becomes independent
        # and is not inside list_resources method
        secrets = filter_list_secrets(auth_context, cached=cached, path=path)
        return secrets

    meta = {
        'total_matching': total,
        'total_returned': secrets.count(),
        'sort': sort,
        'start': start
    }

    return ListSecretsResponse([sec.as_dict() for sec in secrets], meta)
