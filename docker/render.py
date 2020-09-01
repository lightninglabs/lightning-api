#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader, select_autoescape
from parser import grpc, rest
from pathlib import Path
from os.path import relpath

import json
import os
import subprocess

PROTO_DIR = os.environ.get('PROTO_DIR')
EXPERIMENTAL_PACKAGES = os.environ.get('EXPERIMENTAL_PACKAGES')
REPO_URL = os.environ.get('REPO_URL')
COMMIT = os.environ.get('COMMIT')
COMMAND = os.getenv('COMMAND')
COMPONENT = os.getenv('COMPONENT')
WS_ENABLED = os.environ.get('WS_ENABLED')
PROTO_SRC_DIR = os.environ.get('PROTO_SRC_DIR')
APPEND_TO_FILE = os.environ.get('APPEND_TO_FILE')
GRPC_PORT = os.environ.get('GRPC_PORT')
REST_PORT = os.environ.get('REST_PORT')

def render_grpc():
    """
    Given a template and the JSON representation of a set of proto files, renders full
    Slate documentation of the `lnd` API.

    Location of
    - proto JSON: `$PROTO_DIR/generated.json`
    - template: `templates/index_template.md`
    - Slate markdown output: `source/index.html.md`
    """

    # Read the json representation of the proto and construct a Python dict of
    # the methods and messages.
    print('Parsing file ' + PROTO_DIR + '/generated.json')
    grpc_json_files = json.loads(open(PROTO_DIR + '/generated.json', 'r').read())['files']
    grpc_messages = {}
    grpc_methods = {}
    grpc_services = {}
    grpc_enums = {}
    grpc_package_files = {}
    files = []
    experimental = []
    for file in grpc_json_files:
        pkg = file['package']
        if pkg not in grpc_package_files:
            grpc_package_files[pkg] = []

        grpc_package_files[pkg].append(file['name'])
        if pkg in EXPERIMENTAL_PACKAGES:
            experimental.append({
              'package': pkg,
              'file': file['name'],
              'service': file['services'][0]['name']
            })

    for file in grpc_json_files:
        grpc_messages.update(grpc.parse_messages(PROTO_DIR, file['messages'], file['name'], grpc_package_files))

    for file in grpc_json_files:
        files.append(file['name'])
        methods, services = grpc.parse_methods(file['services'], grpc_messages, file['name'], COMMAND)
        grpc_methods.update(methods)
        grpc_services.update(services)
        grpc_enums.update(grpc.parse_enums(file['enums']))

    # Parse the command help for each method.
    for _, service in grpc_services.items():
        for method in service['methods']:
            # Make calls to lncli -h and populate the method with that information.
            subcommand = method.get('subcommand')
            if subcommand:
                method['commandInfo'] = grpc.parse_command_help(COMMAND, subcommand)

    # Sort the services and methods.
    ordering = sorted(grpc_services.keys())
    for _, service in grpc_services.items():
        # Add the ordering information into the parsed rpc methods
        index = ordering.index(service['name'])
        service['index'] = index
        service['methods'].sort(key=lambda m: m['fullName'])

    # Convert the services into a dictionary ordered by index.
    services_list = [v for k, v in grpc_services.items()]
    services_list.sort(key=lambda m: m['index'])

    # Sort all other lists.
    files.sort()
    experimental.sort(key=lambda e: e['service'])

    # Load from the `templates` dir
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template(COMPONENT + '_grpc.md')

    rendered_docs = template.render(
        enums=grpc_enums.values(),
        services=services_list,
        service_methods=grpc_services,
        messages=grpc_messages,
        files=files,
        experimental=experimental,
        repoUrl=REPO_URL,
        commit=COMMIT,
        component=COMPONENT,
        rpcdir=PROTO_SRC_DIR,
        grpcport=GRPC_PORT,
        restport=REST_PORT)

    # Write the file to the source directory.
    with open(APPEND_TO_FILE, 'a+') as f:
        f.write(rendered_docs)

def render_rest():
    """
    Renders the REST documentation from parsing the swagger JSON file.
    """

    definitions = {}
    enums = {}
    endpoints = {}
    files = []

    for path in Path(PROTO_DIR).rglob('*.swagger.json'):
        print('Parsing file ' + str(path))
        files.append(str(path).replace(PROTO_DIR + '/', ''))
        data = json.load(open(path, 'r'))
        file_definitions, file_enums = rest.parse_definitions(data['definitions'])
        definitions.update(file_definitions)
        enums.update(file_enums)

        if 'x-stream-definitions' in data:
            streamDef, _ = rest.parse_definitions(data['x-stream-definitions'])
            definitions.update(streamDef)

        endpoints.update(rest.parse_endpoints(data['paths'], definitions, WS_ENABLED))

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )

    # Convert the definitions into a list ordered by name.
    definitions_list = [v for k, v in definitions.items()]
    definitions_list.sort(key=lambda m: m['name'])

    template = env.get_template(COMPONENT + '_rest.md')
    docs = template.render(
        properties=definitions_list,
        enums=enums.values(),
        endpoints=endpoints,
        files=files,
        repoUrl=REPO_URL,
        commit=COMMIT,
        component=COMPONENT,
        rpcdir=PROTO_SRC_DIR,
        grpcport=GRPC_PORT,
        restport=REST_PORT)

    with open(APPEND_TO_FILE, 'a+') as f:
        f.write(docs)

if __name__ == '__main__':
    render_grpc()
    render_rest()
