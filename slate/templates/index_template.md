---
title: API Reference

language_tabs:
  - shell
  - python

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:max@lightning.engineering'>Contact Us</a>
  - <a href='https://github.com/tripit/slate'>Documentation Powered by Slate</a>

includes:

search: true
---

# Introduction

Welcome to the API documentation for LND, the Lightning Network
Daemon.

This page serves purely as a reference, generally for those who already
understand how to work with LND. If this is your first time, please check out
our [developer site](https://dev.lightning.community) and
[tutorial](https://dev.lightning.community/tutorial).

This site features API documentation for command line arguments, gRPC in Python
and Javscript, and the gRPC REST proxy. The original `rpc.proto` file from which
the gRPC documentation was generated can be found in the [lnd Github
repo](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

{% for method in methods %}

# {{ method.name }}

{{ method.description }}

```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
{% if method.request_message.fields | length == 0 %}
>>> response = stub.{{ method.name }}(ln.{{ method.request_type }}())
{% else %}>>> response = stub.{{ method.name }}(ln.{{ method.request_type }}({% for field in method.request_message.fields %}
        {{ field.name }}=<YOUR_PARAM>,{% endfor %}
    ))
{% endif %}
```

> `response` will be structured similar to this:

```python
{% if method.response_message.fields | length == 0 %}
{}
{% else %}
{ {% for field in method.response_message.fields %}
    {{ field.name }}: <{{ field.type }}>,{% endfor %}
}
{% endif %}
```

### {{ method.request_type }}

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

### {{ method.response_type }}

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
