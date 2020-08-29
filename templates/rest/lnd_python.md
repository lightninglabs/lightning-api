```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:{{ restport }}{{ endpoint.path }}'
>>> cert_path = 'LND_DIR/tls.cert'{% if endpoint.service != 'WalletUnlocker' %}
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}{% endif %}{% if endpoint.type == 'POST' %}
>>> data = { {% for param in endpoint.requestParams %}
        '{{ param.name }}': {% if param.type == 'byte' %}base64.b64encode(<{{ param.type }}>).decode(){% else %}<{{ param.type }}>{% endif %}, {% endfor %}
    }{% endif %}
>>> r = requests.{{ endpoint.type|lower }}(url{% if endpoint.service != 'WalletUnlocker' %}, headers=headers{% endif %}, verify=cert_path{% if endpoint.isStreaming %}, stream=True{% endif %}{% if endpoint.type == 'POST' %}, data=json.dumps(data){% endif %}){% if endpoint.isStreaming %}
>>> for raw_response in r.iter_lines():
>>>     json_response = json.loads(raw_response)
>>>     print(json_response){% else %}
>>> print(r.json()){% endif %}
{ {% for param in endpoint.responseParams %}
    "{{ param.name }}": <{{ param.type }}>, {% endfor %}
}
```
