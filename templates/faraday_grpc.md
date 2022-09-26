# Faraday gRPC API Reference

Welcome to the gRPC API reference documentation for Faraday.

Faraday is an external service intended to be run in conjunction with the [lnd](https://github.com/lightningnetwork/lnd)
implementation of the [Lightning Network](https://lightning.network). It queries LND for information about its existing
channels and provides channel close recommendations if channels are under-performing.

This site features the documentation for `frcli` (CLI), and the API documentation
for Python and JavaScript clients in order to communicate with a local `faraday`
instance through gRPC.

The examples to the right assume that the there is a local `faraday` instance
running and listening for gRPC connections on port {{ grpcport }}. `FARADAY_DIR`
will be used as a placeholder to denote the base directory of the `faraday`
instance. By default, this is `~/.faraday` on Linux and
`~/Library/Application Support/Faraday` on macOS.

At the time of writing this documentation, two things are needed in order to
make a gRPC request to a `faraday` instance: a TLS/SSL connection and a macaroon
used for RPC authentication. The examples to the right will show how these can
be used in order to make a successful, secure, and authenticated gRPC request.

The original `*.proto` files from which the gRPC documentation was generated
can be found here:

{% for file in files %}- [`{{ file }}`]({{ repoUrl }}/blob/{{ commit }}/{{ rpcdir }}/{{file}})
{% endfor %}


This is the reference for the **gRPC API**. Alternatively, there is also a [REST
API which is documented here](#faraday-rest-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`{{ commit }}`]({{ repoUrl }}/tree/{{ commit }}).</small>

{% for service in services %}
# Service _{{ service.name }}_

{% for method in service_methods[service.name].methods %}
## {{ method.fullName }}

{% if not method.streamingRequest and not method.streamingResponse %}
#### Unary RPC
{% elif not method.streamingRequest and method.streamingResponse %}
#### Server-streaming RPC
{% elif method.streamingRequest and not method.streamingResponse %}
#### Client-streaming RPC
{% elif method.streamingRequest and method.streamingResponse %}
#### Bidirectional-streaming RPC
{% endif %}

{{ method.description }}

{% include 'grpc/shell.md' %}
{% include 'grpc/other_python.md' %}
{% include 'grpc/other_javascript.md' %}

{% include 'grpc/request.md' %}
{% include 'grpc/response.md' %}
{% endfor %}
{% endfor %}

# gRPC Messages
{% for messageName, message in messages.items() %}
{% include 'grpc/message.md' %}
{% endfor %}

# gRPC Enums
{% for enum in enums %}
{% include 'grpc/enum.md' %}
{% endfor %}
