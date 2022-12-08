from mongoengine import DoesNotExist
import connexion


def info_from_ApiKeyAuth(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation
    function, if there is one. 'sub' or 'uid' will be set in 'user' parameter
    of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is
        invalid or does not allow access to called API
    :rtype: dict | None
    """
    from mist.api.auth.models import ApiToken, SessionToken
    from mist.api.portal.models import Portal
    from mist.api import config
    if config.HAS_RBAC:
        from mist.rbac.tokens import SuperToken
        from mist.rbac.methods import AuthContext
    else:
        from mist.api.dummy.rbac import AuthContext

    auth_value = api_key.lower()
    auth_context = session = None
    if auth_value.startswith('internal'):
        parts = auth_value.split(' ')
        if len(parts) == 3:
            internal_api_key, session_id = parts[1:]
            if internal_api_key == Portal.get_singleton().internal_api_key:
                try:
                    session_token = SessionToken.objects.get(
                        token=session_id)
                except SessionToken.DoesNotExist:
                    pass
                else:
                    if session_token.is_valid():
                        session_token.internal = True
                        session = session_token
    elif auth_value:
        token_from_request = auth_value
        try:
            api_token = ApiToken.objects.get(
                token=token_from_request
            )
        except DoesNotExist:
            api_token = None
        try:
            if not api_token and config.HAS_RBAC:
                api_token = SuperToken.objects.get(
                    token=token_from_request)
        except DoesNotExist:
            pass
        if api_token and api_token.is_valid():
            session = api_token
        else:
            session = ApiToken()
            session.name = 'dummy_token'
    if session:
        user = session.get_user()
        if user:
            auth_context = AuthContext(user, session)
            return {'uid': user.id, 'user': user, 'auth_context': auth_context}
    return None


def info_from_CookieAuth(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation
    function, if there is one. 'sub' or 'uid' will be set in 'user' parameter
    of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is
        invalid or does not allow access to called API
    :rtype: dict | None
    """
    org = connexion.request.headers.get('X-Org')
    from mist.api.auth.models import SessionToken
    from mist.api import config
    if config.HAS_RBAC:
        from mist.rbac.methods import AuthContext
    else:
        from mist.api.dummy.rbac import AuthContext

    auth_context = session = None
    token_from_request = api_key.lower()
    try:
        session_token = SessionToken.objects.get(
            token=token_from_request
        )
    except DoesNotExist:
        session_token = None
    if session_token and session_token.is_valid():
        session = session_token
    else:
        session = SessionToken()
        session.name = 'dummy_token'
    if session:
        user = session.get_user()
        if user:
            auth_context = AuthContext(user, session, org=org)
            return {'uid': user.id, 'user': user, 'auth_context': auth_context}
    return None
