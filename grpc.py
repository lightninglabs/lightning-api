#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader, select_autoescape

import json
import re
import subprocess
import os

PROTO_DIR = os.environ.get('PROTO_DIR')
EXPERIMENTAL_PACKAGES = os.environ.get('EXPERIMENTAL_PACKAGES')
GITHUB_URL = os.environ.get('GITHUB_URL')
COMMIT = os.environ.get('COMMIT')

def parse_description(description):
    """
    Parses the description of an RPC method.

    Example input:
        /** lncli: `getinfo`
        GetInfo serves a request.
        It returns info.
        */

    Example output:
        ('getinfo', "GetInfo serves a request. It returns info.")
    """

    if description is None:
        return None, None

    # Match lncli: `lncli_name` or lncli:`lncli_name`.
    command = None
    match = re.search(r'(?:lncli:.?`)(.*)(?:`)', description)
    if match:
        command = match.group(1)
        description = description[match.end():].strip()

    # Replace all new lines so that Slate markdown renders correctly.
    description = description.replace('\n', ' ').replace('\r', '')

    return command, description


def parse_line_number(message_name, files):
    """
    Parses the *.proto files to see on what line number the message appears.
    """

    for file in files:
        with open(PROTO_DIR + '/' + file) as data_file:
            content = data_file.read()

        lines = content.split('\n')
        message_line = 'message ' + message_name + ' {'
        if message_line in lines:
            index = lines.index(message_line)
            return file, index + 1

    return '', -1

def parse_grpc_message_params(message):
    """
    Parses the parameters of a gRPC message and returns them as a list.
    """

    params = []
    for param in message['fields']:
        _, description = parse_description(param['description'])

        p = {
            'name': param['name'],
            'description': description
        }

        if param['label'] == 'repeated':
            p['type'] = 'array ' + param['type']
        else:
            p['type'] = param['type']

        if param['fullType'].startswith('lnrpc.'):
            p['link'] = param['type'].lower()

        params.append(p)

    return params


def parse_grpc_messages(messages, fileName, packageFiles):
    """
    Parses the different gRPC messages found within the rpc.json file.
    """

    grpc_messages = {}
    for message in messages:
        name = message['fullName']
        package = name.split('.')[0]
        if package not in packageFiles:
            continue

        fileName, line = parse_line_number(message['name'], packageFiles[package])
        params = parse_grpc_message_params(message)
        grpc_messages[name] = {
            'name': name,
            'params': params,
            'link': name.lower(),
            'file': fileName,
            'line': line,
        }

    return grpc_messages


def parse_grpc_methods(services, messages, fileName):
    """
    Parses the different gRPC methods of the different services found within the
    rpc.json file.
    """

    grpc_methods = {}
    for service in services:
        for method in service['methods']:
            # Convert to camelCase format for JavaScript.
            name = method['name']
            method['nameJS'] = name[0].lower() + name[1:]
            method['service'] = service['name']
            method['serviceJS'] = service['name'][0].lower() + \
                service['name'][1:]

            fullName = service['name'] + '.' + name
            method['fullName'] = fullName
            method['fileName'] = fileName

            serviceFullName = service['fullName']
            method['packageName'] = serviceFullName.replace('.' + service['name'], '')

            # Parse the corresponding lncli command and description.
            method['lncliCommand'], method['description'] = \
                parse_description(method['description'])

            method['requestMessage'] = messages[method['requestFullType']]
            method['responseMessage'] = messages[method['responseFullType']]

            method['streamingRequest'] = method['requestStreaming']
            method['streamingResponse'] = method['responseStreaming']

            grpc_methods[fullName] = method

    return grpc_methods


def parse_lncli_help(command):
    """
    Parses the help output from an gRPC method's corresponding lncli command.
    """

    commandParts = command.split(' ')
    help_output = subprocess.check_output(['lncli'] + commandParts + ['-h']) \
        .decode('utf-8') \
        .split('\n')

    lncli_info = {
        'name': None,
        'usage': None,
        'options': [],
        'description': [],
    }

    section_headers = set(
        ['NAME:', 'USAGE:', 'CATEGORY:', 'DESCRIPTION:', 'OPTIONS:'])

    while len(help_output) > 0:
        section = help_output.pop(0).strip()
        if section == '':
            continue

        assert section in section_headers, "Should not have reached a section header"

        while len(help_output) > 0 and help_output[0] not in section_headers:
            line = help_output.pop(0).strip()

            if line == '':
                continue

            if section == 'NAME:':
                lncli_info['name'] = line
            elif section == 'USAGE:':
                lncli_info['usage'] = line
            elif section == 'DESCRIPTION:':
                lncli_info['description'].append(line)
            elif section == 'OPTIONS:':
                lncli_info['options'].append(line)

    if len(lncli_info['description']) == 0:
        description = ' '.join(lncli_info['name'].split(' ')[3:])
        lncli_info['description'].append(description)

    return lncli_info


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
        grpc_messages.update(parse_grpc_messages(file['messages'], file['name'], grpc_package_files))

    for file in grpc_json_files:
        files.append(file['name'])
        grpc_methods.update(parse_grpc_methods(file['services'], grpc_messages, file['name']))

    ordering = sorted(grpc_methods.keys())
    for _, method in grpc_methods.items():
        # Add the ordering information into the parsed rpc methods
        index = ordering.index(method['fullName'])
        method['index'] = index

        # Make calls to lncli -h and populate the method with that information.
        lncli_command = method.get('lncliCommand')
        if lncli_command:
            method['lncliInfo'] = parse_lncli_help(lncli_command)

    # Load from the `templates` dir
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('grpc/index.md')

    # Convert the methods into a dictionary ordered by index.
    methods_list = [v for k, v in grpc_methods.items()]
    methods_list.sort(key=lambda m: m['index'])

    rendered_docs = template.render(
        methods=methods_list,
        messages=grpc_messages,
        files=files,
        experimental=experimental,
        gitHubUrl=GITHUB_URL,
        commit=COMMIT)

    # Write the file to the source directory.
    with open('source/index.html.md', 'w') as f:
        f.write(rendered_docs)
