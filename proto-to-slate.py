#!/usr/local/bin/python
from jinja2 import Environment, PackageLoader, select_autoescape
import json


def json_proto_to_rpc_dict():
    with open('rpc-truncated.json') as data_file:
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
            'fields': {}
        }
        # Keyed by the canonical representation
        rpc_messages[rpc_message['full_name']] = rpc_message

        for field in file_message.get('message_fields'):
            field_name = field['field_name']
            rpc_message['fields'][field_name] = {
                'name': field_name,
                'type': field['field_type'],
                'full_type': field['field_full_type'],
                'description': field.get('field_description'),
                'label': field['field_label'],
                'default_value': field['field_default_value'],
            }

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

    return rpc_messages, rpc_methods


def generate_slate_docs():

    rpc_messages, rpc_methods = json_proto_to_rpc_dict()

    # Load from the `templates` dir of the `slate` Python package
    env = Environment(
        loader=PackageLoader('slate', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('index_template.md')

    methods_list = [v for k, v in rpc_methods.iteritems()]

    rendered_docs = template.render(name='Max', methods=methods_list).encode('utf-8')

    # Write the file to the source directory. index.html.md is the default name
    with open('source/index.html.md', "wb") as file_out:
        file_out.write(rendered_docs)


generate_slate_docs()
