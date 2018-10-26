```javascript
> var fs = require('fs');
> var request = require('request');{% if endpoint.service != 'WalletUnlocker' %}
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');{% endif %}{% if endpoint.type == 'POST' %}
> var requestBody = { {% for param in endpoint.requestParams %}
    {{ param.name }}: <{{ param.type }}>,{% endfor %}
  };{% endif %}
> var options = {
    url: 'https://localhost:8080{{ endpoint.path }}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, {% if endpoint.service != 'WalletUnlocker' %}
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },{% endif %}{% if endpoint.type == 'POST' %}
    form: JSON.stringify(requestBody),{% endif %}
  };
> request.{{ endpoint.type|lower }}(options, function(error, response, body) {
    console.log(body);
  });
{ {% for param in endpoint.responseParams %}
    "{{ param.name }}": <{{ param.type }}>, {% endfor %}
}
```
