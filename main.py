import os
from flask import Flask

import requests 

app = Flask(__name__)

ENDPOINT = os.environ['ENDPOINT']

@app.route('/')
def check():
    response = requests.get(ENDPOINT)

    if response.status_code not in [401, 403]:
        return f'Route unprotected; returns: {response.status_code}', 500
    else:
        return 'OK', 200
