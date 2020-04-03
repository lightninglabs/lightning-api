```javascript
const fs = require('fs');
const request = require('request');{% if endpoint.service != 'WalletUnlocker' %}
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');{% endif %}{% if endpoint.type == 'POST' %}
let requestBody = { {% for param in endpoint.requestParams %}
    {{ param.name }}: <{{ param.type }}>,{% endfor %}
}{% endif %}
let options = {
  url: 'https://localhost:8080{{ endpoint.path }}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, {% if endpoint.service != 'WalletUnlocker' %}
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },{% endif %}{% if endpoint.type == 'POST' %}
  form: JSON.stringify(requestBody),{% endif %}
}
request.{{ endpoint.type|lower }}(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { {% for param in endpoint.responseParams %}
//      "{{ param.name }}": <{{ param.type }}>, {% endfor %}
//  }{% if endpoint.isStreaming and endpoint.wsEnabled %}



// --------------------------
// Example with websockets:
// --------------------------
const WebSocket = require('ws');
const fs = require('fs');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let ws = new WebSocket('wss://localhost:8080{{ endpoint.path }}?method={{ endpoint.type }}', {
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  headers: {
    'Grpc-Metadata-Macaroon': macaroon,
  },
});
let requestBody = { {% for param in endpoint.requestParams %}
  {{ param.name }}: <{{ param.type }}>,{% endfor %}
}
ws.on('open', function() {
    ws.send(JSON.stringify(requestBody));
});
ws.on('error', function(err) {
    console.log('Error: ' + err);
});
ws.on('message', function(body) {
    console.log(body);
});
// Console output (repeated for every message in the stream):
//  { {% for param in endpoint.responseParams %}
//      "{{ param.name }}": <{{ param.type }}>, {% endfor %}
//  }

{% endif %}
```
