```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const loaderOptions = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
};
const packageDefinition = protoLoader.loadSync('{{ method.fileName }}', loaderOptions);
const {{ method.packageName }} = grpc.loadPackageDefinition(packageDefinition).{{ method.packageName }};
const {{ method.serviceJS }} = new {{ method.packageName }}.{{ method.service }}('localhost:{{ grpcport }}', grpc.credentials.createInsecure());
let request = {% if method.requestMessage.params|length == 0 %}{}{% else %}{ {% for param in method.requestMessage.params %}
  {{ param.name }}: <{{ param.type }}>, {% endfor %}
};{% endif %}{% if not method.streamingRequest and not method.streamingResponse %}
{% include 'javascript/simple_rpc.html' %}{% elif not method.streamingRequest and method.streamingResponse %}
{% include 'javascript/streaming_response.html' %}{% else %}
{% include 'javascript/bidirectional.html' %}{% endif %}
// Console output:
//  { {% for param in method.responseMessage.params %}
//      "{{ param.name }}": <{{ param.type }}>,{% endfor %}
//  }
```
