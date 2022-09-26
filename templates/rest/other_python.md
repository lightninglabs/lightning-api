```python
>>> import base64, json, requests
>>> url = 'https://localhost:{{ restport }}{{ endpoint.path }}'
>>> cert_path = '{% filter upper %}{{ component }}{% endfilter %}_DIR/tls.cert'
>>> macaroon = codecs.encode(open('{% filter upper %}{{ component }}{% endfilter %}_DIR/regtest/{{ component }}.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}{% if endpoint.type == 'POST' %}
>>> data = { {% for param in endpoint.requestParams %}
        '{{ param.name }}': {% if param.type == 'byte' %}base64.b64encode(<{{ param.type }}>).decode(){% else %}<{{ param.type }}>{% endif %}, {% endfor %}
    }{% endif %}
>>> r = requests.{{ endpoint.type|lower }}(url, verify=cert_path{% if endpoint.isStreaming %}, stream=True{% endif %}{% if endpoint.type == 'POST' %}, data=json.dumps(data){% endif %}){% if endpoint.isStreaming %}
>>> for raw_response in r.iter_lines():
>>>     json_response = json.loads(raw_response)
>>>     print(json_response){% else %}
>>> print(r.json()){% endif %}
{ {% for param in endpoint.responseParams %}
    "{{ param.name }}": <{{ param.type }}>, {% endfor %}
}
```
