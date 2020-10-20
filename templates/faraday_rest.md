# Faraday REST API Reference

Welcome to the gRPC API reference documentation for Faraday.

Faraday is an external service intended to be run in conjunction with the [lnd](https://github.com/lightningnetwork/lnd)
implementation of the [Lightning Network](https://lightning.network). It queries LND for information about its existing
channels and provides channel close recommendations if channels are under-performing.

This site features the API documentation for shell script (CLI), Python and
JavaScript clients in order to communicate with a local `faraday` instance through
gRPC. Currently, this communication is unauthenticated, so exposing this service
to the internet is not recommended.

The original `*.swagger.js` files from which the gRPC documentation was generated
can be found here:

{% for file in files %}- [`{{ file }}`]({{ repoUrl }}/blob/{{ commit }}/{{ rpcdir }}/{{file}})
{% endfor %}

**NOTE**: The `byte` field type must be set as the base64 encoded string
representation of a raw byte array.


This is the reference for the **REST API**. Alternatively, there is also a [gRPC
API which is documented here](#faraday-grpc-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`{{ commit }}`]({{ repoUrl }}/tree/{{ commit }}).</small>

{% for basePath, endpoints in endpoints.items() %}
## {{ basePath }}
{% for endpoint in endpoints %}

{% include 'rest/other_shell.md' %}
{% include 'rest/other_python.md' %}
{% include 'rest/other_javascript.md' %}

{% include 'rest/request.md' %}
{% include 'rest/response.md' %}

{% endfor %}
{% endfor %}

# REST Messages
{% for property in properties %}
{% include 'rest/property.md' %}
{% endfor %}

# REST Enums
{% for enum in enums %}
{% include 'rest/enum.md' %}
{% endfor %}
