---
title: LND REST API Reference

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

# LND REST API Reference

Welcome to the REST API reference documentation for LND, the Lightning Network
Daemon.

This site features the API documentation for Python and JavaScript, along with
barebones examples using `curl`, for HTTP requests. It is intended for those who
already understand how to work with LND. If this is your first time or you need
a refresher, you may consider perusing our LND developer site featuring a
tutorial, resources and guides at [dev.lightning.community](https://dev.lightning.community).

The examples to the right assume that the there is a local `lnd` instance
running and listening for REST connections on port 8080. `LND_DIR` will be used
as a placeholder to denote the base directory of the `lnd` instance. By default,
this is `~/.lnd` on Linux and `~/Library/Application Support/Lnd` on macOS.

At the time of writing this documentation, two things are needed in order to
make an HTTP request to an `lnd` instance: a TLS/SSL connection and a macaroon
used for RPC authentication. The examples to the right will show how these can
be used in order to make a successful, secure, and authenticated HTTP request.

The original `rpc.proto` file from which the gRPC documentation was generated
can be found [here](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

NOTE: The documentation is currently lacking how to receive streaming responses
from streaming endpoints in JavaScript. If you would like to contribute this
change, please take a look at [https://github.com/lightninglabs/lightning-api](https://github.com/lightninglabs/lightning-api).

NOTE: The `byte` field type must be set as the base64 encoded string
representation of a raw byte array.

Alternatively, the gRPC documentation can be found [here](../).

{% for basePath, endpoints in endpoints.items() %}
# {{ basePath }}
{% for endpoint in endpoints %}

{% include 'rest/shell.md' %}
{% include 'rest/python.md' %}
{% include 'rest/javascript.md' %}

{% include 'rest/request.md' %}
{% include 'rest/response.md' %}

{% endfor %}
{% endfor %}

# Definitions
{% for definition in definitions %}
{% include 'rest/definitions.md' %}
{% endfor %}
