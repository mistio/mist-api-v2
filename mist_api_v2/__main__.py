#!/usr/bin/env python3
import os
import time
import logging
import jsonpickle
import traceback

import connexion
from flask import g, Response
from werkzeug.exceptions import BadRequest

from mist.api import config
from mist.api import helpers
from mist.api.exceptions import MistError
from mist.api.auth import methods, models
from mist.api.logs import methods as log_methods
from mist.api.users.models import Owner
from mist.api.renderers import json2csv
if config.HAS_RBAC:
    from mist.rbac.tokens import SuperToken

from mist_api_v2 import encoder


if (config.SENTRY_CONFIG.get('API_V2_URL') and
        os.getenv('DRAMATIQ_CONTEXT') is None):
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration
    from mist.api.helpers import get_version_string
    sentry_sdk.init(
        dsn=config.SENTRY_CONFIG['API_V2_URL'],
        integrations=[FlaskIntegration()],
        traces_sample_rate=config.SENTRY_CONFIG['TRACES_SAMPLE_RATE'],
        environment=config.SENTRY_CONFIG['ENVIRONMENT'],
        release=get_version_string(),
    )

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Mist API'},
            pythonic_params=True)
application = app.app

logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)
log = logging.getLogger(__name__)


@application.after_request
def return_csv(response):
    request = connexion.request
    try:
        accept = request.headers['Accept']
        action = application.view_functions[request.endpoint].__name__
    except KeyError:
        return response

    if (accept.endswith('csv') and
        request.method.lower() == 'get' and
        response.status_code == 200 and
            'list_' in action):

        columns = request.args.get('columns') or ''
        columns = columns and columns.split(',') or []
        csv = ',' + json2csv(response.json['data'], columns)
        return Response(csv, mimetype=accept,
                        headers={'Content-disposition':
                                 f'attachment; filename={action}.csv'})
    return response


@application.after_request
def prepare_log(response):
    request = connexion.request
    try:
        request_body = request.json.copy()
    except (AttributeError, BadRequest):
        request_body = {}

    try:
        dry = request_body['dry']
    except (KeyError, TypeError):
        dry = False

    # check if exception occured
    g.exc_flag = (config.LOG_EXCEPTIONS and response.status_code >= 500)

    if ((request.method in ('GET', 'HEAD') or dry is True) and
            g.exc_flag is False):
        return response

    # Find the action from flask's dict mapping endpoints to view functions.
    try:
        action = application.view_functions[request.endpoint].__name__
    except KeyError:
        log.error('Could not find action. Path:%s Method:%s',
                  request.path, request.method)
        return response

    if (action == 'add_cloud' and
            isinstance(request_body.get('credentials'), dict)):
        sensitive_fields = ['secret',
                            'privateKey',
                            'apisecret',
                            'password',
                            'apikey',
                            'token',
                            'tlsKey',
                            'tlsCert', ]
        for field in sensitive_fields:
            if request_body['credentials'].get(field):
                request_body['credentials'][field] = '***CENSORED***'

    log_dict = {
        'event_type': 'request',
        'action': action,
        'request_path': request.path,
        'request_method': request.method,
        'request_ip': request.environ['HTTP_X_REAL_IP'],
        'user_agent': request.user_agent.string,
        'response_code': response.status_code,
        'error': response.status_code >= 400,
        'request_body': request_body,
    }

    session = methods.session_from_request(request)

    if session:
        log_dict['session_id'] = str(session.id)
        try:
            if session.fingerprint:
                log_dict['fingerprint'] = session.fingerprint
            if session.experiment:
                log_dict['experiment'] = session.experiment
            if session.choice:
                log_dict['choice'] = session.choice
        except AttributeError:  # in case of ApiToken
            pass

    # log user
    user = session.get_user(effective=False)
    if user is not None:
        log_dict['user_id'] = user.id
        sudoer = session.get_user()
        if sudoer != user:
            log_dict['sudoer_id'] = sudoer.id
        auth_context = methods.auth_context_from_request(
            request)
        if auth_context.org:
            log_dict['owner_id'] = auth_context.org.id
    else:
        log_dict['user_id'] = None
        log_dict['owner_id'] = None

    if isinstance(session, models.ApiToken):
        if 'dummy' not in session.name:
            log_dict['api_token_id'] = str(session.id)
            log_dict['api_token_name'] = session.name
            log_dict['api_token'] = session.token[:4] + '***CENSORED***'
            log_dict['token_expires'] = models.datetime_to_str(
                session.expires())

    # Log special Token.
    if config.HAS_RBAC and isinstance(session, SuperToken):
        log_dict['setuid'] = True
        log_dict['api_token_id'] = str(session.id)
        log_dict['api_token_name'] = session.name

    # log response body
    response_body = response.json
    if isinstance(response_body, dict):
        if 'jobId' in response_body and 'jobId' not in log_dict:
            log_dict['job_id'] = response_body['jobId']
        if 'job' in response_body and 'job' not in log_dict:
            log_dict['job_'] = response_body['job']
        if 'cloud' in response_body and 'cloud_id' not in log_dict:
            log_dict['cloud_id'] = response_body['cloud']
        if 'machine' in response_body and 'machine_id' not in log_dict:
            log_dict['machine_id'] = response_body['machine']
        if 'machine_uuid' in response_body and 'machine_id' not in log_dict:
            log_dict['machine_id'] = response_body['machine']
        # Match resource type based on the action performed.
        for rtype in ['cloud', 'machine', 'key', 'script', 'tunnel',
                      'stack', 'template', 'schedule', 'volume',
                      'buckets']:
            if rtype in log_dict['action']:
                if 'id' in response_body and '%s_id' % rtype not in log_dict:
                    log_dict['%s_id' % rtype] = response_body['id']
                    break
        if log_dict['action'] == 'update_rule':
            if 'id' in response_body and 'rule_id' not in log_dict:
                log_dict['rule_id'] = response_body['id']
        for key in ('priv', ):
            if key in response_body:
                response_body[key] = '***CENSORED***'
        if 'token' in response_body:
            response_body['token'] = response_body['token'][:4] + \
                '***CENSORED***'
        log_dict['response_body'] = response_body
    else:
        log_dict['response_body'] = response_body

    # save log dict in g namespace
    g.log_dict = log_dict

    return response


@application.teardown_request
def log_request_to_elastic(exception):
    try:
        log_dict = g.log_dict
    except AttributeError:
        return

    # log original exception
    if isinstance(exception, MistError):
        if exception.orig_exc:
            log_dict['_exc'] = repr(exception.orig_exc)
            log_dict['_exc_type'] = type(exception.orig_exc)
            if exception.orig_traceback:
                log_dict['_traceback'] = exception.orig_traceback
    elif isinstance(exception, Exception):
        log_dict['_exc'] = repr(exception)
        log_dict['_exc_type'] = type(exception)
        log_dict['_traceback'] = traceback.format_exc()

    if log_dict:
        log_methods.log_event(**log_dict)

    # if a bad exception didn't occur then return, else log it to file
    if g.exc_flag is False or exception is None:
        return

    # Publish traceback in rabbitmq, for heka to parse and forward to
    # elastic
    log.info('Bad exception occured, logging to rabbitmq')
    es_dict = log_dict.copy()
    es_dict.pop('_exc_type', '')
    es_dict['time'] = time.time()
    es_dict['traceback'] = es_dict.pop('_traceback', '')
    es_dict['exception'] = es_dict.pop('_exc', '')
    es_dict['type'] = 'exception'
    routing_key = '%s.%s' % (es_dict['owner_id'], es_dict['action'])
    pickler = jsonpickle.pickler.Pickler()
    helpers.amqp_publish('exceptions', routing_key, pickler.flatten(es_dict),
                         ex_type='topic', ex_declare=True,
                         auto_delete=False)

    # log bad exception to file
    log.info('Bad exception occured, logging to file')
    lines = []
    lines.append('Exception: %s' % log_dict.pop('_exc', ''))
    lines.append('Exception type: %s' % log_dict.pop('_exc_type', ''))
    lines.append('Time: %s' % time.strftime('%Y-%m-%d %H:%M %Z'))
    lines += (
        ['%s: %s' % (key, value) for key, value in list(log_dict.items())
            if value and key != '_traceback']
    )
    for key in ('owner', 'user', 'sudoer'):
        id_ = log_dict.get('%s_id' % key)
        if id_:
            try:
                value = Owner.objects.get(id=id_)
                lines.append('%s: %s' % (key, value))
            except Owner.DoesNotExist:
                pass
            except Exception as exc:
                log.error('Error finding user in logged exc: %r', exc)
    lines.append('-' * 10)
    lines.append(log_dict.get('_traceback', ''))
    lines.append('=' * 10)
    msg = '\n'.join(lines) + '\n'
    directory = 'var/log/exceptions'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = '%s/%s' % (directory, int(time.time()))
    with open(filename, 'w+') as f:
        f.write(msg)


if __name__ == '__main__':
    app.run(port=8080)
