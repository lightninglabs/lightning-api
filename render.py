#!/usr/local/bin/python
from jinja2 import Environment, PackageLoader, select_autoescape

import json
import re
import subprocess


def parse_out_lncli(description):
    # Example input:
    # /** lncli: `getinfo`
    # GetInfo serves a request.
    # It returns info.
    # */

    # Example output:
    # ('getinfo', "GetInfo serves a request. It returns info.")

    if description is None:
        return None, None

    lncli_name = None
    # Match lncli: `lncli_name` or lncli:`lncli_name`
    match = re.search(r'(?:lncli:.?`)(.*)(?:`)', description)
    if match:
        # Get the lncli_name part between the tick marks
        lncli_name = match.group(1)

        # Remove beginning / trailing spaces
        description = description.strip()

        # Remove the lncli part from the description
        description = description[len(match.group()):]

    # Replace all new lines so that Slate markdown renders correctly
    description = description.replace('\n', ' ').replace('\r', '')

    return lncli_name, description


def json_proto_to_rpc_dict():
    """
    Converts a JSON representation of a proto file as output by protoc-gen-doc
    into a Python dict representing the RPC methods, and returns it.
    """

    # The example full structure of a method:
    # {
    #     'description': u'Field comment',
    #     'name': u'SignMessage',
    #     'lncli_name': 'signmessage',
    #     'lncli_info': {
    #         'usage': u'lncli sendcoins [command options] addr amt',
    #         'description': u'Send amt coins in satoshis to the BASE58 encoded bitcoin address addr. Positional arguments and flags can be used interchangeably but not at the same time!',
    #         'name': u'lncli sendcoins - send bitcoin on-chain to an address',
    #         'options': [
    #             u'--addr value  the BASE58 encoded bitcoin address to send coins to on-chain',
    #             u'--amt value   the number of bitcoin denominated in satoshis to send (default: 0)'
    #         ]
    #     }
    #     'request_full_type': u'lnrpc.SignMessageRequest',
    #     'request_message': {
    #         'description': u'Filler comment',
    #         'display_name': u'SignMessageRequest',
    #         'extensions': [],
    #         'full_name': u'lnrpc.SignMessageRequest',
    #         'fields': [
    #             {
    #                 'default_value': u'',
    #                 'description': u'Field comment',
    #                 'full_type': u'bytes',
    #                 'label': u'optional',
    #                 'name': u'msg',
    #                 'type': u'bytes'
    #             },
    #         ],
    #     },
    #     'request_field_messages': {},
    #     'request_type': u'SignMessageRequest',
    #     'response_full_type': u'lnrpc.SignMessageResponse',
    #     'response_message': {
    #         'description': u'Filler comment',
    #         'display_name': u'SignMessageResponse',
    #         'extensions': [],
    #         'full_name': u'lnrpc.SignMessageResponse',
    #         'fields': [
    #             {
    #                 'default_value': u'',
    #                 'description': u'Field comment',
    #                 'full_type': u'string',
    #                 'label': u'optional',
    #                 'name': u'signature',
    #                 'type': u'string'
    #             },
    #         ],
    #     },
    #     'response_type': u'SignMessageResponse',
    #     'response_field_messages': [{
    #         'description': u'',
    #         'display_name': u'ClosedChannel',
    #         'extensions': [],
    #         'fields': [
    #             {
    #                 'default_value': u'',
    #                 'description': u'',
    #                 'full_type': u'lnrpc.PendingChannelResponse.PendingChannel',
    #                 'label': u'optional',
    #                 'name': u'channel',
    #                 'type': u'PendingChannel'
    #             }, {
    #                 'default_value': u'',
    #                 'description': u'',
    #                 'full_type': u'string',
    #                 'label': u'optional',
    #                 'name': u'closing_txid',
    #                 'type': u'string'
    #             }
    #         ],
    #         'full_name': u'lnrpc.PendingChannelResponse.ClosedChannel'
    #     }, {
    #         # ...
    #     }]
    # }

    with open('rpc.json') as data_file:
        data = json.load(data_file)

    file_services = data[0]['file_services']
    file_messages = data[0]['file_messages']

    # Structure the data a little nicer for easy lookup
    rpc_messages = {}
    for file_message in file_messages:
        full_name = file_message['message_full_name']

        message_lncli_name, message_description = \
            parse_out_lncli(file_message.get('message_description'))
        rpc_message = {
            'full_name': full_name,
            'lncli_name': message_lncli_name,
            'description': message_description,
            'extensions': file_message.get('message_extensions'),
            'display_name': file_message['message_name'],  # The standard name we will display
            'fields': [],
        }
        # Keyed by the canonical representation
        rpc_messages[rpc_message['full_name']] = rpc_message

        for field in file_message.get('message_fields'):
            field_name = field['field_name']
            field_lncli_name, field_description = \
                parse_out_lncli(field.get('field_description'))
            rpc_message['fields'].append({
                'name': field_name,
                'lncli_name': field_lncli_name,
                'type': field['field_type'],
                'full_type': field['field_full_type'],
                'description': field_description,
                'label': field['field_label'],
                'default_value': field['field_default_value'],
            })

    rpc_methods = {}

    # There is only one service currently
    lightning_service = file_services[0]
    for file_method in lightning_service['service_methods']:
        method_name = file_method['method_name']
        method_lncli_name, method_description = \
            parse_out_lncli(file_method['method_description'])
        method = {
            'name': method_name,
            'lncli_name': method_lncli_name,
            'description': method_description,
            'request_type': file_method['method_request_type'],
            'request_full_type': file_method['method_request_full_type'],
            'response_type': file_method['method_response_type'],
            'response_full_type': file_method['method_response_full_type'],
        }
        rpc_methods[method_name] = method

    # Populate methods with references to the associated request and response
    # messages
    for _, method in rpc_methods.iteritems():
        request_full_type = method['request_full_type']
        response_full_type = method['response_full_type']
        request_message = rpc_messages[request_full_type]
        response_message = rpc_messages[response_full_type]
        method['request_message'] = request_message
        method['response_message'] = response_message

        # Populate methods with references to messages referenced in the
        # request and response messages
        request_field_messages = []
        response_field_messages = []
        method['request_field_messages'] = request_field_messages
        method['response_field_messages'] = response_field_messages
        for request_field in request_message['fields']:
            field_message = rpc_messages.get(request_field['full_type'])
            if field_message is not None:
                request_field_messages.append(field_message)
        for response_field in response_message['fields']:
            field_message = rpc_messages.get(response_field['full_type'])
            if field_message is not None:
                response_field_messages.append(field_message)

    return rpc_methods


def construct_method_order():
    """
    Reads from rpc.proto to parse an ordering for transactions
    """

    # Construct ordering from rpc.proto
    proto_lines = open('rpc.proto').readlines()

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
    # Example output:
    # {
    #     'usage': u'lncli sendcoins [command options] addr amt',
    #     'description': u'Send amt coins in satoshis to the BASE58 encoded bitcoin address addr. Positional arguments and flags can be used interchangeably but not at the same time!',
    #     'name': u'lncli sendcoins - send bitcoin on-chain to an address',
    #     'options': [
    #         u'--addr value  the BASE58 encoded bitcoin address to send coins to on-chain',
    #         u'--amt value   the number of bitcoin denominated in satoshis to send (default: 0)'
    #     ]
    # }

    subprocess.call(['lncli', command, '-h'])
    help_output = subprocess.check_output(['lncli', command, '-h'])\
        .decode('utf-8')\
        .split('\n')

    lncli_info = {
        'name': None,
        'usage': None,
        'options': [],
        'description': [],
    }
    section_headers = set(['NAME:', 'USAGE:', 'DESCRIPTION:', 'OPTIONS:'])

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

    # Join the description into a single line if it was multiline
    lncli_info['description'] = ' '.join(lncli_info['description'])

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

        # Ex1: '   rpc SendPayment(stream SendRequest)returns( stream SendResponse )'
        # Ex2: '    rpc SubscribeTransactions (GetTransactionsRequest) returns (stream Transaction);'
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


def render():
    """
    Given a template, a proto file, and its JSON representation, renders full
    Slate documentation of the `lnd` API.

    Location of
    - proto file: `rpc.proto`
    - proto JSON: `rpc.json`
    - template: `slate/templates/index_template.md`
    - Slate markdown output: `source/index.html.md`
    """

    # Construct the ordering of methods from rpc.proto
    ordering = construct_method_order()

    # Read the json representation of the proto and construct a Python dict of
    # the methods and messages
    rpc_methods = json_proto_to_rpc_dict()

    # Parse out the streaming info from rpc.proto
    streaming_info = parse_out_streaming()

    for method in rpc_methods.itervalues():
        # Add the ordering information into the parsed rpc methods
        index = ordering[method['name']]
        method['index'] = index

        # Make calls to lncli -h and populate the method with that information
        lncli_name = method.get('lncli_name')
        if lncli_name:
            # method['lncli_info'] = {}
            method['lncli_info'] = parse_lncli_help(lncli_name)

        streaming_request, streaming_response = streaming_info[method['name']]
        method['streaming_request'] = streaming_request
        method['streaming_response'] = streaming_response

    # Load from the `templates` dir of the `slate` Python package
    env = Environment(
        loader=PackageLoader('slate', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('index_template.md')

    # Convert the methods into a dictionary orderedy by index
    methods_list = [v for k, v in rpc_methods.iteritems()]
    methods_list.sort(key=lambda m: m['index'])

    rendered_docs = template.render(
        methods=methods_list,
    ).encode('utf-8')

    # Write the file to the source directory. index.html.md is the default name
    with open('source/index.html.md', "wb") as file_out:
        file_out.write(rendered_docs)


if __name__ == '__main__':
    render()
