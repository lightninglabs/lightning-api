```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);{% if method.service == 'WalletUnlocker' %}
> var {{ method.serviceJS }} = new lnrpc.{{ method.service }}('localhost:10009', sslCreds);{% else %}
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var {{ method.serviceJS }} = new lnrpc.{{ method.service }}('localhost:10009', creds);{% endif %}
> var request = {% if method.requestMessage.params|length == 0 %}{}{% else %}{ {% for param in method.requestMessage.params %}
    {{ param.name }}: <{{ param.type }}>, {% endfor %}
  }{% endif %} {% if not method.streamingRequest and not method.streamingResponse %}
{% include 'javascript/simple_rpc.html' %}{% elif not method.streamingRequest and method.streamingResponse %}
{% include 'javascript/streaming_response.html' %}{% else %}
{% include 'javascript/bidirectional.html' %}{% endif %}
{ {% for param in method.responseMessage.params %}
    "{{ param.name }}": <{{ param.type }}>,{% endfor %}
}
```
