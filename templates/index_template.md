---
title: LND API Reference

language_tabs:
  - shell
  - python
  - javascript

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:max@lightning.engineering'>Contact Us</a>
  - Powered by <a href='https://github.com/lord/slate'>Slate</a>

includes:

search: true
---

# LND API Reference

Welcome to the API reference documentation for LND, the Lightning Network
Daemon.

This site features API documentation for command line arguments, gRPC in
[Python](//dev.lightning.community/guides/python-grpc/) /
[Javascript](//dev.lightning.community/guides/python-grpc/), and a REST proxy.
It is intended for those who already understand how to work with LND. If this is
your first time or you need a refresher, you may consider perusing our LND
developer site featuring a tutorial, resources and guides at
[dev.lightning.community](//dev.lightning.community).

If you prefer to just read code, the original `rpc.proto` file from which
the gRPC documentation was generated can be found in the [lnd Github
repo](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

{% for method in methods %}

# {{ method.name }}
{% if not method.streaming_request and not method.streaming_response %}
### Simple RPC
{% elif not method.streaming_request and method.streaming_response %}
### Response-streaming RPC
{% elif method.streaming_request and not method.streaming_response %}
### Request-streaming RPC
{% elif method.streaming_request and method.streaming_response %}
### Bidirectional-streaming RPC
{% endif %}

{{ method.description }}

```shell
{% if method.lncli_name %}{% for description_line in method.lncli_info.description %}
# {{ description_line }}{% endfor %}

$ {{ method.lncli_info.usage }}
{% for option in method.lncli_info.options %}
# {{ option }}{% endfor %}{% endif %}
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel){% if method.streaming_request %}
{% include 'python/streaming_request.html' %}{% else %}
{% include 'python/simple_request.html' %}{% endif %}{% if method.streaming_response %}
{% include 'python/streaming_response.html' %}{% else %}
{% include 'python/simple_response.html' %}{% endif %}
{% include 'python/response_output.html' %}
```

```javascript
> var grpc = require('grpc');
> var lnrpcDescriptor = grpc.load('rpc.proto');
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', grpc.credentials.createInsecure());
{% if not method.streaming_request and not method.streaming_response %} 
{% include 'javascript/simple_rpc.html' %}{% elif not method.streaming_request and method.streaming_response %}
{% include 'javascript/response_streaming.html' %}{% elif method.streaming_request and not method.streaming_response %}
{% include 'javascript/request_streaming.html' %}{% else %}
{% include 'javascript/bidirectional.html' %}{% endif %}
{% include 'javascript/response_output.html' %}
```

### gRPC Request: {{ method.request_type }} {% if method.streaming_request %}(Streaming){% endif %}

{{ method.request_message.description }}
{% if method.request_message.fields | length == 0 %}
This request has no parameters.
{% else %}
Field | Type | Label | Description
----- | ---- | ----- | ----------- {% for field in method.request_message.fields %}
{{ field.name }} | {{ field.type }} | {{ field.label }} | {{ field.description }} {% endfor %}
{% endif %}

{% for request_field_message in method.request_field_messages %}
### {{ request_field_message.display_name }}
{{ request_field_message.description }}
{% if method.request_message.fields | length == 0 %}
This message has no parameters.
{% else %}
Field | Type | Label | Description
----- | ---- | ----- | ----------- {% for field in request_field_message.fields %}
{{ field.name }} | {{ field.type }} | {{ field.label }} | {{ field.description }} {% endfor %}
{% endif %}
{% endfor %}

### gRPC Response: {{ method.response_type }} {% if method.streaming_response %}(Streaming){% endif %}

{{ method.response_message.description }}
{% if method.response_message.fields | length == 0 %}
This response is empty.
{% else %}
Field | Type | Label | Description
----- | ---- | ----- | ----------- {% for field in method.response_message.fields %}
{{ field.name }} | {{ field.type }} | {{ field.label }} | {{ field.description }} {% endfor %}
{% endif %}

{% for response_field_message in method.response_field_messages %}
### {{ response_field_message.display_name }}
{{ response_field_message.description }}
{% if method.response_message.fields | length == 0 %}
This message has no parameters.
{% else %}
Field | Type | Label | Description
----- | ---- | ----- | ----------- {% for field in response_field_message.fields %}
{{ field.name }} | {{ field.type }} | {{ field.label }} | {{ field.description }} {% endfor %}
{% endif %}
{% endfor %}

{% endfor %}
