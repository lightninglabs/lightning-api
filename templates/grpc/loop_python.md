```python
>>> import codecs, grpc, os
>>> # Generate the following 2 modules by compiling the {{ rpcdir }}/{{ method.fileName }} with the grpcio-tools.
>>> # See https://github.com/lightningnetwork/lnd/blob/master/docs/grpc/python.md for instructions.
>>> import {{ method.stubFileName }}_pb2 as {{ method.packageName }}, {{ method.stubFileName }}_pb2_grpc as {{ method.stubFileName }}stub
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = {{ method.stubFileName }}stub.{{ method.service }}Stub(channel){% if method.streamingRequest %}
{% include 'python/streaming_request.html' %}{% else %}
{% include 'python/simple_request.html' %}{% endif %}{% if method.streamingResponse %}
{% include 'python/streaming_response.html' %}{% else %}
{% include 'python/simple_response.html' %}{% endif %}
{ {% for param in method.responseMessage.params %}
    "{{ param.name }}": <{{ param.type }}>,{% endfor %}
}
```
