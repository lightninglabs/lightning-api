#!/usr/bin/env python3
import re
import subprocess


def parse_description(description):
    """
    Parses the description of a request/response field.
    """
    if description is None:
        return None
    return description.lstrip(' /*').lstrip(' /**').replace('\n', ' ')


def parse_method_description(command, description):
    """
    Parses the description of an RPC method.

    Example input:
        /** `command`: `subcommand`
        `subcommand` serves a request and returns a response.
        */

    Example output:
        ('`command`', "`subcommand` serves a request and returns a response.")
    """

    if description is None:
        return None, None

    # Match `command`: `subcommand` or `command`:`subcommand`.
    subcommand = None
    pattern = '(?:{}:.?`)(.*)(?:`)'.format(command)
    match = re.search(pattern, description)
    if match:
        subcommand = match.group(1)
        description = description[match.end():]

    return subcommand, parse_description(description)


def parse_line_number(proto_dir, message_name, files):
    """
    Parses the *.proto files to see on what line number the message appears.
    """

    for file in files:
        with open(proto_dir + '/' + file) as data_file:
            content = data_file.read()

        lines = content.split('\n')
        message_line = 'message ' + message_name + ' {'
        if message_line in lines:
            index = lines.index(message_line)
            return file, index + 1

    return '', -1

def parse_message_params(message):
    """
    Parses the parameters of a gRPC message and returns them as a list.
    """

    params = []
    for param in message['fields']:
        p = {
            'name': param['name'],
            'description': parse_description(param.get('description')),
        }

        if param['label'] == 'repeated':
            p['type'] = 'array ' + param['type']
        else:
            p['type'] = param['type']

        if '.' in param['fullType']:
            p['link'] = param['fullType'].lower().replace('.', '-')

        params.append(p)

    return params


def parse_messages(proto_dir, messages, fileName, packageFiles):
    """
    Parses the different gRPC messages found within the rpc.json file.
    """

    grpc_messages = {}
    for message in messages:
        name = message['fullName']
        package = name.split('.')[0]
        if package not in packageFiles:
            continue

        fileName, line = parse_line_number(proto_dir, message['name'], packageFiles[package])
        params = parse_message_params(message)
        grpc_messages[name] = {
            'name': name,
            'params': params,
            'link': name.lower(),
            'file': fileName,
            'line': line,
        }

    return grpc_messages


def parse_enum_options(enum):
    """ Parses the parameters of a gRPC enum and returns them as a list """
    params = []
    for param in enum['values']:
        params.append({
          'name': param['name'],
          'value': param['number'],
          'description': parse_description(param['description']),
        })
    return params


def parse_enums(enums):
    """ Parses the different gRPC enums found within the rpc.json file """
    grpc_enums = {}
    for enum in enums:
        name = enum['name']
        options = parse_enum_options(enum)
        grpc_enums[name] = {
            'name': name,
            'description': parse_description(enum['description']),
            'options': options,
            'link': name.lower()
        }
    return grpc_enums


def parse_methods(services, messages, fileName, command):
    """
    Parses the different gRPC methods of the different services found within the
    rpc.json file.
    """

    grpc_methods = {}
    grpc_services = {}
    for service in services:
        serviceName = service['name']
        grpc_services[serviceName] = {
            'name': serviceName,
            'index': -1,
            'methods': [],
        }
        for method in service['methods']:
            name = method['name']
            fullName = serviceName + '.' + name
            serviceFullName = service['fullName']

            # Parse the corresponding command and description.
            subcommand, description = parse_method_description(command, method['description'])

            grpc_methods[fullName] = {
                **method,
                'nameJS': name[0].lower() + name[1:],
                'service': serviceName,
                'serviceJS': service['name'][0].lower() + service['name'][1:],
                'fullName': fullName,
                'fileName': fileName,
                'packageName': serviceFullName.replace('.' + service['name'], ''),
                'subcommand': subcommand,
                'description': description,
                'requestMessage': messages[method['requestFullType']],
                'responseMessage': messages[method['responseFullType']],
                'streamingRequest': method['requestStreaming'],
                'streamingResponse': method['responseStreaming'],
            }
            grpc_services[serviceName]['methods'].append(grpc_methods[fullName])

    return grpc_methods, grpc_services


def parse_command_help(command, subcommand):
    """
    Parses the help output from an gRPC method's corresponding lncli command.
    """

    commandParts = subcommand.split(' ')
    help_output = subprocess.check_output([command] + commandParts + ['-h']) \
        .decode('utf-8') \
        .split('\n')

    info = {
        'name': None,
        'usage': None,
        'options': [],
        'description': [],
    }

    section_headers = set(['NAME:', 'USAGE:', 'CATEGORY:', 'DESCRIPTION:', 'OPTIONS:'])

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
                info['name'] = line
            elif section == 'USAGE:':
                info['usage'] = line
            elif section == 'DESCRIPTION:':
                info['description'].append(line)
            elif section == 'OPTIONS:':
                info['options'].append(line)

    if len(info['description']) == 0:
        description = ' '.join(info['name'].split(' ')[3:])
        info['description'].append(description)

    return info
