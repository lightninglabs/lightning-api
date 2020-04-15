```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.{{ method.service }}Stub(channel){% if method.streamingRequest %}
{% include 'python/streaming_request.html' %}{% else %}
{% include 'python/simple_request.html' %}{% endif %}{% if method.streamingResponse %}
{% include 'python/streaming_response.html' %}{% else %}
{% include 'python/simple_response.html' %}{% endif %}
{ {% for param in method.responseMessage.params %}
    "{{ param.name }}": <{{ param.type }}>,{% endfor %}
}
```
