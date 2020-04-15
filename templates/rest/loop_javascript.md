```javascript
const request = require('request');{% if endpoint.type == 'POST' %}
let requestBody = { {% for param in endpoint.requestParams %}
  {{ param.name }}: <{{ param.type }}>,{% endfor %}
};{% endif %}
let options = {
  url: 'http://localhost:8080{{ endpoint.path }}',
  json: true{% if endpoint.type == 'POST' %},
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
