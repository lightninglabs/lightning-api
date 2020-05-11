#!/usr/bin/env python3
from parser.grpc import parse_description

import re
import os

def parse_ref(ref):
    """
    Convenience method that removes the "#/definitions/" prefix from the
    reference name to a REST definition.
    """

    ref = ref.replace('#/definitions/', '')
    ref = ref.replace('#/x-stream-definitions/', '')

    # Workaround for nested messages that the Swagger generator doesn't know
    # where to place.
    if ref.startswith('PendingChannelsResponse'):
        ref = 'lnrpc' + ref

    return ref


def parse_definition_params(definition):
    """
    Parses the different parameters of a REST definition found within the
    swagger JSON file and returns them as a list.
    """

    if not definition.get('properties'):
        return []

    params = []
    for def_param_name, def_param in definition['properties'].items():
        p = {'name': def_param_name}

        # Parse the parameter's description.
        if def_param.get('description'):
            p['description'] = parse_description(def_param['description'])
        elif def_param.get('title'):
            p['description'] = parse_description(def_param['title'])

        # Parse the parameter's type.
        param_type = def_param.get('type')
        if param_type is None:
            ref = parse_ref(def_param['$ref'])
            p['type'] = ref
            p['link'] = ref.lower()
        elif param_type == 'array':
            if def_param['items'].get('type'):
                p['type'] = 'array ' + def_param['items']['type']
            elif def_param['items'].get('$ref'):
                ref = parse_ref(def_param['items']['$ref'])
                p['type'] = 'array ' + ref
                p['link'] = ref.lower()
        else:
            param_type = def_param.get('type')
            param_format = def_param.get('format')

            # If the format is defined, we'll use that over the type as it
            # provides more detail.
            if param_format:
                # However, if the parameter is of type string and it's not a
                # base64 encoded byte array, then we'll use the string type
                # directly. We do this to prevent issues when parsing large
                # numbers (int64, uint64) in some languages as they see these
                # types as strings rather than integers.
                if param_type == 'string' and param_format != 'byte':
                    p['type'] = param_type
                else:
                    p['type'] = param_format
            # Otherwise, we only have the type available, so we'll use that.
            else:
                p['type'] = param_type

        params.append(p)

    return params


def parse_enum_options(definition, description):
    enum_options = {}
    for i, option in enumerate(definition['enum']):
        enum_options[option] = {
            'name': option,
            'value': i,
        }

    splits = description.split(' - ')
    pattern = '(\w+): \*\s*(.*)'
    for split in splits:
        match = re.search(pattern, split, re.M | re.S)
        if match:
            enum_options[match.group(1)]['description'] = match.group(2)

    return enum_options


def parse_definitions(definitions):
    """
    Parses the different REST definitions found within the swagger JSON file.
    These definitions include the custom types defined within the protos.
    """

    rest_properties = {}
    rest_enums = {}
    for name, definition in definitions.items():
        # Workaround for nested messages that the Swagger generator doesn't know
        # where to place.
        if name.startswith('PendingChannelsResponse'):
            name = 'lnrpc' + name

        if definition.get('properties'):
            params = parse_definition_params(definition)
            rest_properties[name] = {
                'name': name,
                'params': params,
                'link': name.lower(),
            }

        elif definition.get('enum'):
            desc = ''
            if 'description' in definition:
                desc = parse_description(definition['description'])

            options = parse_enum_options(definition, desc)
            rest_enums[name] = {
                'name': name,
                'options': options.values(),
            }
        else:
            rest_properties[name] = {
                'name': name,
                'params': [],
                'link': name.lower(),
            }

    return rest_properties, rest_enums


def parse_endpoint_request_params(request_properties, definitions):
    """
    Parses the different request parameters of an endpoint found within the
    swagger JSON file and returns them as a list.
    """

    request_params = request_properties.get('parameters')
    if not request_params:
        return []

    if len(request_params) == 1 and request_params[0].get('schema'):
        ref = parse_ref(request_params[0]['schema']['$ref'])
        params = definitions[ref]['params']
        for param in params:
            param['placement'] = 'body'

        return params

    params = []
    for param in request_params:
        p = {'name': param['name'], 'placement': param['in']}

        if param.get('description'):
            p['description'] = parse_description(param['description'])

        # Parse the parameter's type.
        param_type = param.get('type')
        if param_type is None:
            ref = parse_ref(param['schema']['$ref'])
            schema_def = definitions[ref]
            p['type'] = schema_def['name']
            p['link'] = schema_def['link']
        elif param_type == 'integer':
            p['type'] = param['format']
        else:
            p['type'] = param_type

        params.append(p)

    return params


def parse_endpoints(json_endpoints, definitions, ws_enabled):
    """
    Parses the different REST endpoints found within the swagger JSON file and
    returns them as a dictionary, each indexed by its base path.

    For example, the following two endpoints would result in the base path
    "/v1/invoices":
        /v1/invoices
        /v1/invoices/subscribe
    """

    rest_endpoints = {}
    for path, requests in json_endpoints.items():
        # Attempt to retrieve the common path to the endpoint. This will allow
        # us to group different endpoints with the same base path together.
        base_path = path
        match = re.search(r'/{.*}', path)
        if match:
            base_path = path[:match.start()]

        # Parse the different endpoints. Each one should include a set of
        # request and response paramaters.
        endpoints = []
        for request_type, request_properties in requests.items():
            endpoint_request_description = parse_description(request_properties['summary'])

            endpoint_request_params = parse_endpoint_request_params(
                request_properties, definitions)

            response_properties = request_properties['responses']['200']
            if '$ref' in response_properties['schema']:
                rawRef = response_properties['schema']['$ref']
                isStreaming = 'x-stream-definitions' in rawRef
                ref = parse_ref(response_properties['schema']['$ref'])

            if 'properties' in response_properties['schema']:
                isStreaming = True
                ref = parse_ref(response_properties['schema']['properties']['result']['$ref'])

            endpoint_response_params = definitions[ref]['params']

            endpoint = {
                'path': path,
                'type': request_type.upper(),
                'name': request_properties['operationId'],
                'description': endpoint_request_description,
                'requestParams': endpoint_request_params,
                'responseParams': endpoint_response_params,
                'isStreaming': isStreaming,
                'wsEnabled': 'true' in ws_enabled,
                'service': request_properties['tags'][0],
            }

            endpoints.append(endpoint)

        if base_path not in rest_endpoints:
            rest_endpoints[base_path] = []
        for endpoint in endpoints:
            rest_endpoints[base_path].append(endpoint)

    return rest_endpoints
