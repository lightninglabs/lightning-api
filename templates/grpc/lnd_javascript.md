```javascript
const fs = require('fs');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const loaderOptions = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
};
{% if method.fileName == 'lightning.proto' %}const packageDefinition = protoLoader.loadSync('{{ method.fileName }}', loaderOptions);{% endif %}{% if method.fileName != 'lightning.proto' %}const packageDefinition = protoLoader.loadSync(['lightning.proto', '{{ method.fileName }}'], loaderOptions);{% endif %}
const {{ method.packageName }} = grpc.loadPackageDefinition(packageDefinition).{{ method.packageName }};
const macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/regtest/admin.macaroon").toString('hex');
process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
const lndCert = fs.readFileSync('LND_DIR/tls.cert');
const sslCreds = grpc.credentials.createSsl(lndCert);{% if method.service == 'WalletUnlocker' %}
const {{ method.serviceJS }} = new {{ method.packageName }}.{{ method.service }}('localhost:{{ grpcport }}', sslCreds);{% else %}
const macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
  let metadata = new grpc.Metadata();
  metadata.add('macaroon', macaroon);
  callback(null, metadata);
});
let creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
let {{ method.serviceJS }} = new {{ method.packageName }}.{{ method.service }}('localhost:{{ grpcport }}', creds);{% endif %}
let request = {% if method.requestMessage.params|length == 0 %}{};{% else %}{ {% for param in method.requestMessage.params %}
  {{ param.name }}: <{{ param.type }}>, {% endfor %}
};{% endif %} {% if not method.streamingRequest and not method.streamingResponse %}
{% include 'javascript/simple_rpc.html' %}{% elif not method.streamingRequest and method.streamingResponse %}
{% include 'javascript/streaming_response.html' %}{% else %}
{% include 'javascript/bidirectional.html' %}{% endif %}
// Console output:
//  { {% for param in method.responseMessage.params %}
//      "{{ param.name }}": <{{ param.type }}>,{% endfor %}
//  }
```
