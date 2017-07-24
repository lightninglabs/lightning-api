#!/usr/local/bin/python
from jinja2 import Environment, PackageLoader, select_autoescape

import json
import re


def json_proto_to_rpc_dict():
    """
    Converts a JSON representation of a proto file as output by protoc-gen-doc
    into a Python dict representing the RPC methods, and returns it.
    """
    # The full structure of a method:
    # {
    #     'description': u'Field comment',
    #     'name': u'SignMessage',
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
    #     'response_type': u'SignMessageResponse'
    # }

    with open('rpc.json') as data_file:
        data = json.load(data_file)

    file_services = data[0]['file_services']
    file_messages = data[0]['file_messages']

    # Structure the data a little nicer for easy lookup
    rpc_messages = {}
    for file_message in file_messages:
        full_name = file_message['message_full_name']
        rpc_message = {
            'full_name': full_name,
            'description': file_message.get('message_description'),
            'extensions': file_message.get('message_extensions'),
            'display_name': file_message['message_name'],  # The standard name we will display
            'fields': [],
        }
        # Keyed by the canonical representation
        rpc_messages[rpc_message['full_name']] = rpc_message

        for field in file_message.get('message_fields'):
            field_name = field['field_name']
            rpc_message['fields'].append({
                'name': field_name,
                'type': field['field_type'],
                'full_type': field['field_full_type'],
                'description': field.get('field_description'),
                'label': field['field_label'],
                'default_value': field['field_default_value'],
            })

    rpc_methods = {}

    # There is only one service currently
    lightning_service = file_services[0]
    for file_method in lightning_service['service_methods']:
        method_name = file_method['method_name']
        method = {
            'name': method_name,
            'description': file_method['method_description'],
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
        method['request_message'] = rpc_messages[request_full_type]
        method['response_message'] = rpc_messages[response_full_type]

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


def generate_slate_docs():
    """
    Given a template, a proto file, and its JSON representation, generates full
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

    # Add the ordering information into the parsed rpc methods
    for method in rpc_methods.itervalues():
        index = ordering[method['name']]
        method['index'] = index

    # Load some example parameters
    example = {
        # Example parameters for a listchannels command
        # NOTE Perhaps these should be grouped by message?
        'pubkey': "02244b8eff01be9f7b4ec1d73ab10fc36da48b01a685ac90ed09a63fe94ec08d0a",
        'channel_point': "2622b779a8acca471a738b0796cd62e4457b79b33265cbfa687aadccc329023a:0",
        'chan_id': "495879744192512",
        'capacity': 1000000,
        'local_balance': 21001,
        'commit_fee': 8688,
        'commit_weight': 724,
        'fee_per_kw': 12000,
        'total_satoshis_received': 21001,
        'num_updates': 9,
        'pending_htlcs': \
        """{
          incoming: true
          amount: 100
          hash_lock:
          'jv2\\232\\372\\200\\357BP\\332\\341\\320\\212\\337_0\\340r\\343t;\\247\\2107\\332\\260\\277\\251 ubK' expiration_height: 1
        }
        """,
    }

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
        example=example,
    ).encode('utf-8')

    # Write the file to the source directory. index.html.md is the default name
    with open('source/index.html.md', "wb") as file_out:
        file_out.write(rendered_docs)


generate_slate_docs()
