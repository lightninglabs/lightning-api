#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader, select_autoescape

import json
import re
import subprocess


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


def parse_grpc_messages(messages):
    """
    Parses the different gRPC messages found within the rpc.json file.
    """

    grpc_messages = {}
    for message in messages:
        name = message['name']
        params = parse_grpc_message_params(message)
        grpc_messages[name] = {
            'name': name,
            'params': params,
            'link': name.lower()
        }

    return grpc_messages


def parse_grpc_enum_params(enum):
    """ Parses the parameters of a gRPC enum and returns them as a list """
    params = []
    for param in enum['values']:
        _, description = parse_description(param['description'])
        parsed_param = {
            'name': param['name'],
            'description': description,
            'number': param['number']
        }
        params.append(parsed_param)
    return params


def parse_grpc_enums(enums):
    """ Parses the different gRPC enums found within the rpc.json file """
    grpc_messages = {}
    for enum in enums:
        name = enum['name']
        params = parse_grpc_enum_params(enum)
        grpc_messages[name] = {
            'name': name,
            'description': enum['description'],
            'params': params,
            'link': name.lower()
        }
    return grpc_messages


def parse_grpc_methods(services, messages):
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

            # Parse the corresponding lncli command and description.
            method['lncliCommand'], method['description'] = \
                parse_description(method['description'])

            method['requestMessage'] = messages[method['requestType']]
            method['responseMessage'] = messages[method['responseType']]

            grpc_methods[name] = method

    return grpc_methods


def construct_method_order(filename):
    """
    Reads from a proto file to parse an ordering for gRPC methods.
    """

    proto_lines = open(filename).readlines()

    ordering = {}
    counter = 0
    for line in proto_lines:
        tokenized_line = re.split(' |\(|\)', line.strip())
        if len(tokenized_line) >= 1 and tokenized_line[0] == 'rpc':
            rpc_name = tokenized_line[1]
            ordering[rpc_name] = counter
            counter += 1

    return ordering


def parse_lncli_help(command):
    """
    Parses the help output from an gRPC method's corresponding lncli command.
    """

    help_output = subprocess.check_output(['lncli', command, '-h']) \
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


def parse_out_streaming():
    """
    Parses rpc.proto to see if methods are streaming or not
    This information can't be gleaned from rpc.json since protoc-gen-doc does
    not return this information
    """

    with open('rpc.proto') as data_file:
        lines = data_file.readlines()

    streaming_info = {}

    for line in lines:
        streaming_request = False
        streaming_response = False

        # Ex1: 'rpc SendPayment(stream SendRequest)returns( stream SendResponse )'
        # Ex2: 'rpc SubscribeTransactions (GetTransactionsRequest) returns (stream Transaction)'
        match = re.search(r'(?:rpc )(.*)(?: ?\()(?: ?)(.*)(?:\) ?returns ?\()(?: ?)(.*)\)', line)

        if line.strip()[:len('rpc')] == 'rpc':
            pass

        # If this is a line defining a rpc method
        if match:
            # Ex1: 'SendPayment'
            # Ex2: 'SubscribeTransactions'
            method_name = match.group(1).strip()

            # Ex1: 'stream SendRequest'
            # Ex2: 'GetTransactionsRequest'
            method_request = match.group(2).strip()

            # Ex1: 'stream SendRequest'
            # Ex2: 'stream Transaction'
            method_response = match.group(3).strip()

            # If the response string starts with 'stream'
            if method_response[:len('stream')] == 'stream':
                streaming_response = True

                # If the request string starts with 'stream'
                if method_request[:len('stream')] == 'stream':
                    streaming_request = True

            streaming_info[method_name] = (streaming_request, streaming_response)

    return streaming_info


def render_grpc():
    """
    Given a template, a proto file, and its JSON representation, renders full
    Slate documentation of the `lnd` API.

    Location of
    - proto file: `rpc.proto`
    - proto JSON: `rpc.json`
    - template: `templates/index_template.md`
    - Slate markdown output: `source/index.html.md`
    """

    # Construct the ordering of methods from rpc.proto
    ordering = construct_method_order('rpc.proto')

    # Read the json representation of the proto and construct a Python dict of
    # the methods and messages.
    grpc_json = json.loads(open('rpc.json', 'r').read())['files'][0]
    grpc_messages = parse_grpc_messages(grpc_json['messages'])
    grpc_methods = parse_grpc_methods(grpc_json['services'], grpc_messages)
    grpc_enums = parse_grpc_enums(grpc_json['enums'])

    # Parse out the streaming info from rpc.proto
    streaming_info = parse_out_streaming()

    for _, method in grpc_methods.items():
        # Add the ordering information into the parsed rpc methods
        index = ordering[method['name']]
        method['index'] = index

        # Make calls to lncli -h and populate the method with that information.
        lncli_command = method.get('lncliCommand')
        if lncli_command:
            method['lncliInfo'] = parse_lncli_help(lncli_command)

        method['streamingRequest'], method['streamingResponse'] = \
                streaming_info[method['name']]

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
        enums=grpc_enums,
        methods=methods_list,
        messages=grpc_messages)

    # Write the file to the source directory.
    with open('source/index.html.md', 'w') as f:
        f.write(rendered_docs)
