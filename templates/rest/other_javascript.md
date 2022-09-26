```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('{% filter upper %}{{ component }}{% endfilter %}_DIR/regtest/{{ component }}.macaroon').toString('hex');{% if endpoint.type == 'POST' %}
let requestBody = { {% for param in endpoint.requestParams %}
  {{ param.name }}: <{{ param.type }}>,{% endfor %}
};{% endif %}
let options = {
  url: 'https://localhost:{{ restport }}{{ endpoint.path }}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true,
  headers: {
    'Grpc-Metadata-macaroon': macaroon
  },{% if endpoint.type == 'POST' %}
  form: JSON.stringify(requestBody){% endif %}
};
request.{{ endpoint.type|lower }}(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { {% for param in endpoint.responseParams %}
//      "{{ param.name }}": <{{ param.type }}>, {% endfor %}
//  }
```
