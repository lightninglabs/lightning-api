#!/usr/bin/env python3
from flask import Flask, request
from hashlib import sha1
from subprocess import call

import hmac
import os

app = Flask(__name__)

RPC_PROTO = '.proto'

def verify_signature(signature, payload):
    """
    Compute the HMAC-SHA1 of the secret token as the key and the payload as the
    message to ensure it matches the given signature.
    """
    key = os.environ['WEBHOOK_SECRET_TOKEN'].encode()
    h = hmac.new(key, payload, sha1)
    sig = 'sha1=' + h.hexdigest()
    return hmac.compare_digest(sig, signature)


def update_and_render():
    call('./docker-update-render.sh', shell=True)


def deploy_updated_docs():
    call('./docker-build-deploy.sh', shell=True)


@app.route('/update', methods=['POST'])
def handle_proto_update():
    """
    Listen for POST requests from GitHub in order to determine when a commit has
    modified the lnrpc or looprpc protobuf definitions.
    """

    github_payload = request.headers.get('X-Hub-Signature')
    if not github_payload:
        return '', 200

    if not verify_signature(github_payload, request.data):
        return '', 200

    data = request.get_json()
    commits = data['commits']
    for commit in commits:
        modified_files = commit['modified']
        for modified_file in modified_files:
            if RPC_PROTO in modified_file:
                update_render_deploy()
                return '', 200

    return '', 200
