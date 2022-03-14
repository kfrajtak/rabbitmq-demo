#!/usr/bin/env python
import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys

app = flask.Flask(__name__)
CORS(app)

# notice there are no dependencies on Dapr - only HTTP GET and POST endpoints are declared

# endpoint called by Dapr when application starts to get the list of topics to subscribe to
# Dapr will create the subcription for your
@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{'pubsubname': 'pubsub',
                      'topic': 'AccountActivatedEvent',  # topic to subscribe to
                      'route': 'account-activated'}]  # see route below
    return jsonify(subscriptions)


# "event" listener - Dapr sidecar will POST data to this endpoint
# when event arrives
@app.route('/account-activated', methods=['POST'])
def topic_subscriber():
    print(request.json, flush=True)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


app.run()
