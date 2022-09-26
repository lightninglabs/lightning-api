```python
>>> import codecs, grpc, os
>>> # Generate the following 2 modules by compiling the {{ rpcdir }}/{{ method.fileName }} with the grpcio-tools.
>>> # See https://github.com/lightningnetwork/lnd/blob/master/docs/grpc/python.md for instructions.
>>> import {{ method.stubFileName }}_pb2 as {{ method.packageName }}, {{ method.stubFileName }}_pb2_grpc as {{ method.stubFileName }}stub
>>> macaroon = codecs.encode(open('{% filter upper %}{{ component }}{% endfilter %}_DIR/regtest/{{ component }}.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('{% filter upper %}{{ component }}{% endfilter %}_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:{{ grpcport }}', ssl_creds)
>>> stub = {{ method.stubFileName }}stub.{{ method.service }}Stub(channel){% if method.streamingRequest %}
{% include 'python/streaming_request.html' %}{% else %}
{% include 'python/simple_request.html' %}{% endif %}{% if method.streamingResponse %}
{% include 'python/streaming_response.html' %}{% else %}
{% include 'python/simple_response.html' %}{% endif %}
{ {% for param in method.responseMessage.params %}
    "{{ param.name }}": <{{ param.type }}>,{% endfor %}
}
```
