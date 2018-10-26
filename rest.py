#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader, select_autoescape
from grpc import parse_description

import json
import re


def parse_rest_ref(ref):
    """
    Convenience method that removes the "#/definitions/lnrpc" prefix from the
    reference name to a REST definition.
    """

    # It's possible that the name doesn't include the "lnrpc" prefix, so we'll
    # make sure to do it separately.
    ref = ref.replace('#/definitions/', '')
    return ref.replace('lnrpc', '')


def parse_rest_definition_params(definition):
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
            _, p['description'] = parse_description(def_param['description'])
        elif def_param.get('title'):
            _, p['description'] = parse_description(def_param['title'])

        # Parse the parameter's type.
        param_type = def_param.get('type')
        if param_type is None:
            ref = parse_rest_ref(def_param['$ref'])
            p['type'] = ref
            p['link'] = ref.lower()
        elif param_type == 'array':
            if def_param['items'].get('type'):
                p['type'] = 'array ' + def_param['items']['type']
            elif def_param['items'].get('$ref'):
                ref = parse_rest_ref(def_param['items']['$ref'])
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


def parse_rest_definitions(definitions):
    """
    Parses the different REST definitions found within the swagger JSON file.
    These definitions include the custom types defined within the protos.
    """

    rest_definitions = {}
    for name, definition in definitions.items():
        name = name.replace('lnrpc', '')
        params = parse_rest_definition_params(definition)

        rest_definitions[name] = {
            'name': name,
            'params': params,
            'link': name.lower()
        }

    return rest_definitions


def parse_rest_endpoint_request_params(request_properties, definitions):
    """
    Parses the different request parameters of an endpoint found within the
    swagger JSON file and returns them as a list.
    """

    request_params = request_properties.get('parameters')
    if not request_params:
        return []

    if len(request_params) == 1 and request_params[0].get('schema'):
        ref = parse_rest_ref(request_params[0]['schema']['$ref'])
        params = definitions[ref]['params']
        for param in params:
            param['placement'] = 'body'

        return params

    params = []
    for param in request_params:
        p = {'name': param['name'], 'placement': param['in']}

        if param.get('description'):
            _, p['description'] = parse_description(param['description'])

        # Parse the parameter's type.
        param_type = param.get('type')
        if param_type is None:
            ref = parse_rest_ref(param['schema']['$ref'])
            schema_def = definitions[ref]
            p['type'] = schema_def['name']
            p['link'] = schema_def['link']
        elif param_type == 'integer':
            p['type'] = param['format']
        else:
            p['type'] = param_type

        params.append(p)

    return params


def parse_rest_endpoints(json_endpoints, definitions):
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
            _, endpoint_request_description = parse_description(
                request_properties['summary'])

            endpoint_request_params = parse_rest_endpoint_request_params(
                request_properties, definitions)

            response_properties = request_properties['responses']['200']
            ref = parse_rest_ref(response_properties['schema']['$ref'])
            endpoint_response_params = definitions[ref]['params']

            isStreaming = response_properties['description'] == '(streaming responses)'

            endpoint = {
                'path': path,
                'type': request_type.upper(),
                'name': request_properties['operationId'],
                'description': endpoint_request_description,
                'requestParams': endpoint_request_params,
                'responseParams': endpoint_response_params,
                'isStreaming': isStreaming,
                'service': request_properties['tags'][0],
            }

            endpoints.append(endpoint)

        if base_path not in rest_endpoints:
            rest_endpoints[base_path] = []
        for endpoint in endpoints:
            rest_endpoints[base_path].append(endpoint)

    return rest_endpoints


def render_rest():
    """
    Renders the REST documentation from parsing the swagger JSON file.
    """

    data = json.load(open('rpc.swagger.json', 'r'))
    definitions = parse_rest_definitions(data['definitions'])
    endpoints = parse_rest_endpoints(data['paths'], definitions)

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('rest/index.md')
    docs = template.render(
        definitions=definitions.values(),
        endpoints=endpoints)

    with open('source/rest/index.html.md', 'w') as f:
        f.write(docs)
