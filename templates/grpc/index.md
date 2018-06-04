---
title: LND gRPC API Reference

language_tabs:
  - shell
  - python
  - javascript

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:max@lightning.engineering'>Contact Us</a>
  - Powered by <a href='https://github.com/lord/slate'>Slate</a>

search: true
---

# LND gRPC API Reference

Welcome to the gRPC API reference documentation for LND, the Lightning Network
Daemon.

This site features the API documentation for lncli (CLI), [Python](https:///dev.lightning.community/guides/python-grpc/),
and [JavaScript](https://dev.lightning.community/guides/javascript-grpc/) in
order to communicate with a local `lnd` instance through gRPC. It is intended
for those who already understand how to work with LND. If this is your first
time or you need a refresher, you may consider perusing our LND developer site
featuring a tutorial, resources and guides at [dev.lightning.community](https://dev.lightning.community).

The examples to the right assume that the there is a local `lnd` instance
running and listening for gRPC connections on port 10009. `LND_DIR` will be used
as a placeholder to denote the base directory of the `lnd` instance. By default,
this is `~/.lnd` on Linux and `~/Library/Application Support/Lnd` on macOS.

At the time of writing this documentation, two things are needed in order to
make a gRPC request to an `lnd` instance: a TLS/SSL connection and a macaroon
used for RPC authentication. The examples to the right will show how these can
be used in order to make a successful, secure, and authenticated gRPC request.

The original `rpc.proto` file from which the gRPC documentation was generated
can be found [here](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

Alternatively, the REST documentation can be found [here](./rest).

{% for method in methods %}
# {{ method.name }}

{% if not method.streamingRequest and not method.streamingResponse %}
### Simple RPC
{% elif not method.streamingRequest and method.streamingResponse %}
### Response-streaming RPC
{% elif method.streamingRequest and not method.streamingResponse %}
### Request-streaming RPC
{% elif method.streamingRequest and method.streamingResponse %}
### Bidirectional-streaming RPC
{% endif %}

{{ method.description }}

{% include 'grpc/shell.md' %}
{% include 'grpc/python.md' %}
{% include 'grpc/javascript.md' %}

{% include 'grpc/request.md' %}
{% include 'grpc/response.md' %}
{% endfor %}

# Messages
{% for messageName, message in messages.items() %}
{% include 'grpc/message.md' %}
{% endfor %}
