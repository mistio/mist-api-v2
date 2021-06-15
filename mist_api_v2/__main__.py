#!/usr/bin/env python3

import connexion

from mist_api_v2 import encoder


app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
mist_api_v2 = app.add_api('openapi.yaml',
                          arguments={'title': 'Mist API'},
                          pythonic_params=True)
application = app.app


@application.before_request
def log_request():
    application.logger.info('Received request!')
    raise Exception
    return


@application.after_request
def after_request_func(response):
    request = connexion.request

    if request.method in ('GET', 'HEAD'):
        return
    import ipdb
    ipdb.set_trace()
    try:
        operation = mist_api_v2.specification.get_operation(
            request.path, request.method.lower())
        operation_id = operation['operationId']
    except KeyError:
        application.logger.error(
            f'Could not find operation id. Path:{request.path} '
            f'Method:{request.method}')
        return response

    log_dict = {
        'event_type': 'request',
        'action': operation_id,
        'request_path': request.path,
        'request_method': request.method,
        'request_ip': request.environ['HTTP_X_REAL_IP'],
        'user_agent': request.user_agent.string,
        'response_code': response.status_code,
        'error': response.status_code >= 400,
    }

    return response

# @application.teardown_request
# def log(exception):
#     import ipdb;ipdb.set_trace()
#     pass

if __name__ == '__main__':
    app.run(port=8080)
