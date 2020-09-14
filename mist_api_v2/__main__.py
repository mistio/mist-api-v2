#!/usr/bin/env python3

import connexion

from mist_api_v2 import encoder


app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Mist API'},
            pythonic_params=True)
application = app.app


if __name__ == '__main__':
    app.run(port=8080)
