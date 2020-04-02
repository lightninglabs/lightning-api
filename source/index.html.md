---
title: LND gRPC API Reference

language_tabs:
  - shell
  - python
  - javascript

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:hello@lightning.engineering'>Contact Us</a>
  - Powered by <a href='https://github.com/lord/slate'>Slate</a>

search: true
---

# LND gRPC API Reference

Welcome to the gRPC API reference documentation for LND, the Lightning Network
Daemon.

This site features the API documentation for lncli (CLI), [Python](https:///dev.lightning.community/guides/python-grpc/),
and [JavaScript](https://dev.lightning.community/guides/javascript-grpc/) in
order to communicate with a local `lnd` instance through gRPC. It is intended
for those who already understand how to work with LND. If this is your first
time or you need a refresher, you may consider perusing our LND developer site
featuring a tutorial, resources and guides at [dev.lightning.community](https://dev.lightning.community).

The examples to the right assume that the there is a local `lnd` instance
running and listening for gRPC connections on port 10009. `LND_DIR` will be used
as a placeholder to denote the base directory of the `lnd` instance. By default,
this is `~/.lnd` on Linux and `~/Library/Application Support/Lnd` on macOS.

At the time of writing this documentation, two things are needed in order to
make a gRPC request to an `lnd` instance: a TLS/SSL connection and a macaroon
used for RPC authentication. The examples to the right will show how these can
be used in order to make a successful, secure, and authenticated gRPC request.

The original `*.proto` files from which the gRPC documentation was generated
can be found here:

- [`rpc.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto)
- [`autopilotrpc/autopilot.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto)
- [`chainrpc/chainnotifier.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto)
- [`invoicesrpc/invoices.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto)
- [`routerrpc/router.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto)
- [`signrpc/signer.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto)
- [`walletrpc/walletkit.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto)
- [`watchtowerrpc/watchtower.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/watchtowerrpc/watchtower.proto)
- [`wtclientrpc/wtclient.proto`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto)



This is the reference for the **gRPC API**. Alternatively, there is also a [REST
API which is documented here](./rest).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`7e6f3ece239e94f05da1a5d0492ce9767069dbbc`](https://github.com/lightningnetwork/lnd/tree/7e6f3ece239e94f05da1a5d0492ce9767069dbbc).</small>

## Experimental services

The following RPCs/services are currently considered to be experimental. This means
they are subject to change in the future. They also need to be enabled with a
compile-time flag to be active (they are active in the official release binaries).

- Service `ChainNotifier` (file `chainrpc/chainnotifier.proto`)
- Service `Invoices` (file `invoicesrpc/invoices.proto`)
- Service `Signer` (file `signrpc/signer.proto`)
- Service `WalletKit` (file `walletrpc/walletkit.proto`)
- Service `Watchtower` (file `watchtowerrpc/watchtower.proto`)
 


# Autopilot.ModifyStatus


### Simple RPC


ModifyStatus is used to modify the status of the autopilot agent, like enabling or disabling it.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as autopilotrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = autopilotrpc.AutopilotStub(channel)
>>> request = ln.autopilotrpc.ModifyStatusRequest(
        enable=<bool>,
    )
>>> response = stub.ModifyStatus(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var autopilotrpc = grpc.load('autopilotrpc/autopilot.proto').autopilotrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var autopilot = new autopilotrpc.Autopilot('localhost:10009', creds);
> var request = { 
    enable: <bool>, 
  }; 
> autopilot.modifyStatus(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [autopilotrpc.ModifyStatusRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L44)


Parameter | Type | Description
--------- | ---- | ----------- 
enable | bool | Whether the autopilot agent should be enabled or not.  
### gRPC Response: [autopilotrpc.ModifyStatusResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L49)


This response has no parameters.


# Autopilot.QueryScores


### Simple RPC


QueryScores queries all available autopilot heuristics, in addition to any active combination of these heruristics, for the scores they would give to the given nodes.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as autopilotrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = autopilotrpc.AutopilotStub(channel)
>>> request = ln.autopilotrpc.QueryScoresRequest(
        pubkeys=<array string>,
        ignore_local_state=<bool>,
    )
>>> response = stub.QueryScores(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "results": <array HeuristicResult>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var autopilotrpc = grpc.load('autopilotrpc/autopilot.proto').autopilotrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var autopilot = new autopilotrpc.Autopilot('localhost:10009', creds);
> var request = { 
    pubkeys: <array string>, 
    ignore_local_state: <bool>, 
  }; 
> autopilot.queryScores(request, function(err, response) {
    console.log(response);
  })
{ 
    "results": <array HeuristicResult>,
}
```

### gRPC Request: [autopilotrpc.QueryScoresRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L52)


Parameter | Type | Description
--------- | ---- | ----------- 
pubkeys | array string |  
ignore_local_state | bool | If set, we will ignore the local channel state when calculating scores.  
### gRPC Response: [autopilotrpc.QueryScoresResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L59)


Parameter | Type | Description
--------- | ---- | ----------- 
results | array HeuristicResult |   

# Autopilot.SetScores


### Simple RPC


SetScores attempts to set the scores used by the running autopilot agent, if the external scoring heuristic is enabled.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as autopilotrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = autopilotrpc.AutopilotStub(channel)
>>> request = ln.autopilotrpc.SetScoresRequest(
        heuristic=<string>,
        scores=<array ScoresEntry>,
    )
>>> response = stub.SetScores(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var autopilotrpc = grpc.load('autopilotrpc/autopilot.proto').autopilotrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var autopilot = new autopilotrpc.Autopilot('localhost:10009', creds);
> var request = { 
    heuristic: <string>, 
    scores: <array ScoresEntry>, 
  }; 
> autopilot.setScores(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [autopilotrpc.SetScoresRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L68)


Parameter | Type | Description
--------- | ---- | ----------- 
heuristic | string | The name of the heuristic to provide scores to. 
scores | array ScoresEntry | A map from hex-encoded public keys to scores. Scores must be in the range [0.0, 1.0].  
### gRPC Response: [autopilotrpc.SetScoresResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L79)


This response has no parameters.


# Autopilot.Status


### Simple RPC


Status returns whether the daemon's autopilot agent is active.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as autopilotrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = autopilotrpc.AutopilotStub(channel)
>>> request = ln.autopilotrpc.StatusRequest()
>>> response = stub.Status(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "active": <bool>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var autopilotrpc = grpc.load('autopilotrpc/autopilot.proto').autopilotrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var autopilot = new autopilotrpc.Autopilot('localhost:10009', creds);
> var request = {}; 
> autopilot.status(request, function(err, response) {
    console.log(response);
  })
{ 
    "active": <bool>,
}
```

### gRPC Request: [autopilotrpc.StatusRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L36)


This request has no parameters.

### gRPC Response: [autopilotrpc.StatusResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/autopilotrpc/autopilot.proto#L39)


Parameter | Type | Description
--------- | ---- | ----------- 
active | bool | Indicates whether the autopilot is active or not.  

# ChainNotifier.RegisterBlockEpochNtfn


### Response-streaming RPC


RegisterBlockEpochNtfn is a synchronous response-streaming RPC that registers an intent for a client to be notified of blocks in the chain. The stream will return a hash and height tuple of a block for each new/stale block in the chain. It is the client's responsibility to determine whether the tuple returned is for a new or stale block in the chain.  A client can also request a historical backlog of blocks from a particular point. This allows clients to be idempotent by ensuring that they do not missing processing a single block within the chain.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as chainrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = chainrpc.ChainNotifierStub(channel)
>>> request = ln.chainrpc.BlockEpoch(
        hash=<bytes>,
        height=<uint32>,
    )
>>> for response in stub.RegisterBlockEpochNtfn(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "hash": <bytes>,
    "height": <uint32>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var chainrpc = grpc.load('chainrpc/chainnotifier.proto').chainrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var chainNotifier = new chainrpc.ChainNotifier('localhost:10009', creds);
> var request = { 
    hash: <bytes>, 
    height: <uint32>, 
  }; 
> var call = chainNotifier.registerBlockEpochNtfn(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "hash": <bytes>,
    "height": <uint32>,
}
```

### gRPC Request: [chainrpc.BlockEpoch ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto#L136)


Parameter | Type | Description
--------- | ---- | ----------- 
hash | bytes | The hash of the block. 
height | uint32 | The height of the block.  
### gRPC Response: [chainrpc.BlockEpoch (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto#L136)


Parameter | Type | Description
--------- | ---- | ----------- 
hash | bytes | The hash of the block. 
height | uint32 | The height of the block.  

# ChainNotifier.RegisterConfirmationsNtfn


### Response-streaming RPC


RegisterConfirmationsNtfn is a synchronous response-streaming RPC that registers an intent for a client to be notified once a confirmation request has reached its required number of confirmations on-chain.  A client can specify whether the confirmation request should be for a particular transaction by its hash or for an output script by specifying a zero hash.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as chainrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = chainrpc.ChainNotifierStub(channel)
>>> request = ln.chainrpc.ConfRequest(
        txid=<bytes>,
        script=<bytes>,
        num_confs=<uint32>,
        height_hint=<uint32>,
    )
>>> for response in stub.RegisterConfirmationsNtfn(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "conf": <ConfDetails>,
    "reorg": <Reorg>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var chainrpc = grpc.load('chainrpc/chainnotifier.proto').chainrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var chainNotifier = new chainrpc.ChainNotifier('localhost:10009', creds);
> var request = { 
    txid: <bytes>, 
    script: <bytes>, 
    num_confs: <uint32>, 
    height_hint: <uint32>, 
  }; 
> var call = chainNotifier.registerConfirmationsNtfn(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "conf": <ConfDetails>,
    "reorg": <Reorg>,
}
```

### gRPC Request: [chainrpc.ConfRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto#L5)


Parameter | Type | Description
--------- | ---- | ----------- 
txid | bytes | The transaction hash for which we should request a confirmation notification for. If set to a hash of all zeros, then the confirmation notification will be requested for the script instead. 
script | bytes | An output script within a transaction with the hash above which will be used by light clients to match block filters. If the transaction hash is set to a hash of all zeros, then a confirmation notification will be requested for this script instead. 
num_confs | uint32 | The number of desired confirmations the transaction/output script should reach before dispatching a confirmation notification. 
height_hint | uint32 | The earliest height in the chain for which the transaction/output script could have been included in a block. This should in most cases be set to the broadcast height of the transaction/output script.  
### gRPC Response: [chainrpc.ConfEvent (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto#L54)


Parameter | Type | Description
--------- | ---- | ----------- 
conf | ConfDetails | An event that includes the confirmation details of the request (txid/ouput script). 
reorg | Reorg | An event send when the transaction of the request is reorged out of the chain.  

# ChainNotifier.RegisterSpendNtfn


### Response-streaming RPC


RegisterSpendNtfn is a synchronous response-streaming RPC that registers an intent for a client to be notification once a spend request has been spent by a transaction that has confirmed on-chain.  A client can specify whether the spend request should be for a particular outpoint  or for an output script by specifying a zero outpoint.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as chainrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = chainrpc.ChainNotifierStub(channel)
>>> request = ln.chainrpc.SpendRequest(
        outpoint=<Outpoint>,
        script=<bytes>,
        height_hint=<uint32>,
    )
>>> for response in stub.RegisterSpendNtfn(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "spend": <SpendDetails>,
    "reorg": <Reorg>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var chainrpc = grpc.load('chainrpc/chainnotifier.proto').chainrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var chainNotifier = new chainrpc.ChainNotifier('localhost:10009', creds);
> var request = { 
    outpoint: <Outpoint>, 
    script: <bytes>, 
    height_hint: <uint32>, 
  }; 
> var call = chainNotifier.registerSpendNtfn(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "spend": <SpendDetails>,
    "reorg": <Reorg>,
}
```

### gRPC Request: [chainrpc.SpendRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto#L78)


Parameter | Type | Description
--------- | ---- | ----------- 
outpoint | Outpoint | The outpoint for which we should request a spend notification for. If set to a zero outpoint, then the spend notification will be requested for the script instead. 
script | bytes | The output script for the outpoint above. This will be used by light clients to match block filters. If the outpoint is set to a zero outpoint, then a spend notification will be requested for this script instead. 
height_hint | uint32 | The earliest height in the chain for which the outpoint/output script could have been spent. This should in most cases be set to the broadcast height of the outpoint/output script.  
### gRPC Response: [chainrpc.SpendEvent (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/chainrpc/chainnotifier.proto#L120)


Parameter | Type | Description
--------- | ---- | ----------- 
spend | SpendDetails | An event that includes the details of the spending transaction of the request (outpoint/output script). 
reorg | Reorg | An event sent when the spending transaction of the request was reorged out of the chain.  

# Invoices.AddHoldInvoice


### Simple RPC


AddHoldInvoice creates a hold invoice. It ties the invoice to the hash supplied in the request.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as invoicesrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = invoicesrpc.InvoicesStub(channel)
>>> request = ln.invoicesrpc.AddHoldInvoiceRequest(
        memo=<string>,
        hash=<bytes>,
        value=<int64>,
        value_msat=<int64>,
        description_hash=<bytes>,
        expiry=<int64>,
        fallback_addr=<string>,
        cltv_expiry=<uint64>,
        route_hints=<array RouteHint>,
        private=<bool>,
    )
>>> response = stub.AddHoldInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payment_request": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var invoicesrpc = grpc.load('invoicesrpc/invoices.proto').invoicesrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var invoices = new invoicesrpc.Invoices('localhost:10009', creds);
> var request = { 
    memo: <string>, 
    hash: <bytes>, 
    value: <int64>, 
    value_msat: <int64>, 
    description_hash: <bytes>, 
    expiry: <int64>, 
    fallback_addr: <string>, 
    cltv_expiry: <uint64>, 
    route_hints: <array RouteHint>, 
    private: <bool>, 
  }; 
> invoices.addHoldInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
    "payment_request": <string>,
}
```

### gRPC Request: [invoicesrpc.AddHoldInvoiceRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L48)


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
hash | bytes | The hash of the preimage 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels.  
### gRPC Response: [invoicesrpc.AddHoldInvoiceResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L100)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.  

# Invoices.CancelInvoice


### Simple RPC


CancelInvoice cancels a currently open invoice. If the invoice is already canceled, this call will succeed. If the invoice is already settled, it will fail.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as invoicesrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = invoicesrpc.InvoicesStub(channel)
>>> request = ln.invoicesrpc.CancelInvoiceMsg(
        payment_hash=<bytes>,
    )
>>> response = stub.CancelInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var invoicesrpc = grpc.load('invoicesrpc/invoices.proto').invoicesrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var invoices = new invoicesrpc.Invoices('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
  }; 
> invoices.cancelInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [invoicesrpc.CancelInvoiceMsg ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L41)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | Hash corresponding to the (hold) invoice to cancel.  
### gRPC Response: [invoicesrpc.CancelInvoiceResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L45)


This response has no parameters.


# Invoices.SettleInvoice


### Simple RPC


SettleInvoice settles an accepted invoice. If the invoice is already settled, this call will succeed.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as invoicesrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = invoicesrpc.InvoicesStub(channel)
>>> request = ln.invoicesrpc.SettleInvoiceMsg(
        preimage=<bytes>,
    )
>>> response = stub.SettleInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var invoicesrpc = grpc.load('invoicesrpc/invoices.proto').invoicesrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var invoices = new invoicesrpc.Invoices('localhost:10009', creds);
> var request = { 
    preimage: <bytes>, 
  }; 
> invoices.settleInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [invoicesrpc.SettleInvoiceMsg ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L109)


Parameter | Type | Description
--------- | ---- | ----------- 
preimage | bytes | Externally discovered pre-image that should be used to settle the hold / invoice.  
### gRPC Response: [invoicesrpc.SettleInvoiceResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L115)


This response has no parameters.


# Invoices.SubscribeSingleInvoice


### Response-streaming RPC


SubscribeSingleInvoice returns a uni-directional stream (server -> client) to notify the client of state transitions of the specified invoice. Initially the current invoice state is always sent out.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as invoicesrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = invoicesrpc.InvoicesStub(channel)
>>> request = ln.invoicesrpc.SubscribeSingleInvoiceRequest(
        r_hash=<bytes>,
    )
>>> for response in stub.SubscribeSingleInvoice(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "memo": <string>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
    "value_msat": <int64>,
    "settled": <bool>,
    "creation_date": <int64>,
    "settle_date": <int64>,
    "payment_request": <string>,
    "description_hash": <bytes>,
    "expiry": <int64>,
    "fallback_addr": <string>,
    "cltv_expiry": <uint64>,
    "route_hints": <array RouteHint>,
    "private": <bool>,
    "add_index": <uint64>,
    "settle_index": <uint64>,
    "amt_paid": <int64>,
    "amt_paid_sat": <int64>,
    "amt_paid_msat": <int64>,
    "state": <InvoiceState>,
    "htlcs": <array InvoiceHTLC>,
    "features": <array FeaturesEntry>,
    "is_keysend": <bool>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var invoicesrpc = grpc.load('invoicesrpc/invoices.proto').invoicesrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var invoices = new invoicesrpc.Invoices('localhost:10009', creds);
> var request = { 
    r_hash: <bytes>, 
  }; 
> var call = invoices.subscribeSingleInvoice(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "memo": <string>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
    "value_msat": <int64>,
    "settled": <bool>,
    "creation_date": <int64>,
    "settle_date": <int64>,
    "payment_request": <string>,
    "description_hash": <bytes>,
    "expiry": <int64>,
    "fallback_addr": <string>,
    "cltv_expiry": <uint64>,
    "route_hints": <array RouteHint>,
    "private": <bool>,
    "add_index": <uint64>,
    "settle_index": <uint64>,
    "amt_paid": <int64>,
    "amt_paid_sat": <int64>,
    "amt_paid_msat": <int64>,
    "state": <InvoiceState>,
    "htlcs": <array InvoiceHTLC>,
    "features": <array FeaturesEntry>,
    "is_keysend": <bool>,
}
```

### gRPC Request: [invoicesrpc.SubscribeSingleInvoiceRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/invoicesrpc/invoices.proto#L118)


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash | bytes | Hash corresponding to the (hold) invoice to subscribe to.  
### gRPC Response: [lnrpc.Invoice (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2779)


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage. When using REST, this field must be encoded as base64. 
r_hash | bytes | The hash of the preimage. When using REST, this field must be encoded as base64. 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. When using REST, this field must be encoded as base64. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | uint64 | The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | int64 | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | int64 | The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | int64 | The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceState](#invoicestate) | The state the invoice is in. 
htlcs | [array InvoiceHTLC](#invoicehtlc) | List of HTLCs paying to this invoice [EXPERIMENTAL]. 
features | [array FeaturesEntry](#featuresentry) | List of features advertised on the invoice. 
is_keysend | bool | Indicates if this invoice was a spontaneous payment that arrived via keysend [EXPERIMENTAL].  

# Lightning.AbandonChannel


### Simple RPC


AbandonChannel removes all channel state from the database except for a close summary. This method can be used to get rid of permanently unusable channels due to bugs fixed in newer versions of lnd. Only available when in debug builds of lnd.

```shell

# Removes all channel state from the database except for a close
# summary. This method can be used to get rid of permanently unusable
# channels due to bugs fixed in newer versions of lnd.
# Only available when lnd is built in debug mode.
# To view which funding_txids/output_indexes can be used for this command,
# see the channel_point values within the listchannels command output.
# The format for a channel_point is 'funding_txid:output_index'.

$ lncli abandonchannel [command options] funding_txid [output_index]

# --funding_txid value  the txid of the channel's funding transaction
# --output_index value  the output index for the funding output of the funding transaction (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.AbandonChannelRequest(
        channel_point=<ChannelPoint>,
    )
>>> response = stub.AbandonChannel(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    channel_point: <ChannelPoint>, 
  }; 
> lightning.abandonChannel(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.AbandonChannelRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3192)


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) |   
### gRPC Response: [lnrpc.AbandonChannelResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3196)


This response has no parameters.


# Lightning.AddInvoice


### Simple RPC


AddInvoice attempts to add a new invoice to the invoice database. Any duplicated invoices are rejected, therefore all invoices *must* have a unique payment preimage.

```shell

# Add a new invoice, expressing intent for a future payment.
# Invoices without an amount can be created by not supplying any
# parameters or providing an amount of 0. These invoices allow the payee
# to specify the amount of satoshis they wish to send.

$ lncli addinvoice [command options] value preimage

# --memo value              a description of the payment to attach along with the invoice (default="")
# --preimage value          the hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage. If not set, a random preimage will be created.
# --amt value               the amt of satoshis in this invoice (default: 0)
# --description_hash value  SHA-256 hash of the description of the payment. Used if the purpose of payment cannot naturally fit within the memo. If provided this will be used instead of the description(memo) field in the encoded invoice.
# --fallback_addr value     fallback on-chain address that can be used in case the lightning payment fails
# --expiry value            the invoice's expiry time in seconds. If not specified an expiry of 3600 seconds (1 hour) is implied. (default: 0)
# --private                 encode routing hints in the invoice with private channels in order to assist the payer in reaching you
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.Invoice(
        memo=<string>,
        r_preimage=<bytes>,
        r_hash=<bytes>,
        value=<int64>,
        value_msat=<int64>,
        settled=<bool>,
        creation_date=<int64>,
        settle_date=<int64>,
        payment_request=<string>,
        description_hash=<bytes>,
        expiry=<int64>,
        fallback_addr=<string>,
        cltv_expiry=<uint64>,
        route_hints=<array RouteHint>,
        private=<bool>,
        add_index=<uint64>,
        settle_index=<uint64>,
        amt_paid=<int64>,
        amt_paid_sat=<int64>,
        amt_paid_msat=<int64>,
        state=<InvoiceState>,
        htlcs=<array InvoiceHTLC>,
        features=<array FeaturesEntry>,
        is_keysend=<bool>,
    )
>>> response = stub.AddInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "r_hash": <bytes>,
    "payment_request": <string>,
    "add_index": <uint64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    memo: <string>, 
    r_preimage: <bytes>, 
    r_hash: <bytes>, 
    value: <int64>, 
    value_msat: <int64>, 
    settled: <bool>, 
    creation_date: <int64>, 
    settle_date: <int64>, 
    payment_request: <string>, 
    description_hash: <bytes>, 
    expiry: <int64>, 
    fallback_addr: <string>, 
    cltv_expiry: <uint64>, 
    route_hints: <array RouteHint>, 
    private: <bool>, 
    add_index: <uint64>, 
    settle_index: <uint64>, 
    amt_paid: <int64>, 
    amt_paid_sat: <int64>, 
    amt_paid_msat: <int64>, 
    state: <InvoiceState>, 
    htlcs: <array InvoiceHTLC>, 
    features: <array FeaturesEntry>, 
    is_keysend: <bool>, 
  }; 
> lightning.addInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
    "r_hash": <bytes>,
    "payment_request": <string>,
    "add_index": <uint64>,
}
```

### gRPC Request: [lnrpc.Invoice ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2779)


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage. When using REST, this field must be encoded as base64. 
r_hash | bytes | The hash of the preimage. When using REST, this field must be encoded as base64. 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. When using REST, this field must be encoded as base64. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | uint64 | The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | int64 | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | int64 | The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | int64 | The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceState](#invoicestate) | The state the invoice is in. 
htlcs | [array InvoiceHTLC](#invoicehtlc) | List of HTLCs paying to this invoice [EXPERIMENTAL]. 
features | [array FeaturesEntry](#featuresentry) | List of features advertised on the invoice. 
is_keysend | bool | Indicates if this invoice was a spontaneous payment that arrived via keysend [EXPERIMENTAL].  
### gRPC Response: [lnrpc.AddInvoiceResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2962)


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash | bytes |  
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.  

# Lightning.BakeMacaroon


### Simple RPC


BakeMacaroon allows the creation of a new macaroon with custom read and write permissions. No first-party caveats are added since this can be done offline.

```shell

# Bake a new macaroon that grants the provided permissions and
# optionally adds restrictions (timeout, IP address) to it.
# The new macaroon can either be shown on command line in hex serialized
# format or it can be saved directly to a file using the --save_to
# argument.
# A permission is a tuple of an entity and an action, separated by a
# colon. Multiple operations can be added as arguments, for example:
# lncli bakemacaroon info:read invoices:write foo:bar

$ lncli bakemacaroon [command options] [--save_to=] [--timeout=] [--ip_address=] permissions...

# --save_to value     save the created macaroon to this file using the default binary format
# --timeout value     the number of seconds the macaroon will be valid before it times out (default: 0)
# --ip_address value  the IP address the macaroon will be bound to
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.BakeMacaroonRequest(
        permissions=<array MacaroonPermission>,
    )
>>> response = stub.BakeMacaroon(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "macaroon": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    permissions: <array MacaroonPermission>, 
  }; 
> lightning.bakeMacaroon(request, function(err, response) {
    console.log(response);
  })
{ 
    "macaroon": <string>,
}
```

### gRPC Request: [lnrpc.BakeMacaroonRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3479)


Parameter | Type | Description
--------- | ---- | ----------- 
permissions | [array MacaroonPermission](#macaroonpermission) | The list of permissions the new macaroon should grant.  
### gRPC Response: [lnrpc.BakeMacaroonResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3483)


Parameter | Type | Description
--------- | ---- | ----------- 
macaroon | string | The hex encoded macaroon, serialized in binary format.  

# Lightning.ChannelAcceptor


### Bidirectional-streaming RPC


ChannelAcceptor dispatches a bi-directional streaming RPC in which OpenChannel requests are sent to the client and the client responds with a boolean that tells LND whether or not to accept the channel. This allows node operators to specify their own criteria for accepting inbound channels through a single persistent connection.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
# Define a generator that returns an Iterable of lnrpc.ChannelAcceptResponse objects.
>>> def request_generator():
        # Initialization code here.
        while True:
            # Parameters here can be set as arguments to the generator.
            request = ln.lnrpc.ChannelAcceptResponse(
                accept=<bool>,
                pending_chan_id=<bytes>,
            )
            yield request
            # Do things between iterations here.
>>> request_iterable = request_generator()
>>> for response in stub.ChannelAcceptor(request_iterable, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "node_pubkey": <bytes>,
    "chain_hash": <bytes>,
    "pending_chan_id": <bytes>,
    "funding_amt": <uint64>,
    "push_amt": <uint64>,
    "dust_limit": <uint64>,
    "max_value_in_flight": <uint64>,
    "channel_reserve": <uint64>,
    "min_htlc": <uint64>,
    "fee_per_kw": <uint64>,
    "csv_delay": <uint32>,
    "max_accepted_htlcs": <uint32>,
    "channel_flags": <uint32>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    accept: <bool>, 
    pending_chan_id: <bytes>, 
  }; 
> var call = lightning.channelAcceptor({})
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
> call.write(request)

{ 
    "node_pubkey": <bytes>,
    "chain_hash": <bytes>,
    "pending_chan_id": <bytes>,
    "funding_amt": <uint64>,
    "push_amt": <uint64>,
    "dust_limit": <uint64>,
    "max_value_in_flight": <uint64>,
    "channel_reserve": <uint64>,
    "min_htlc": <uint64>,
    "fee_per_kw": <uint64>,
    "csv_delay": <uint32>,
    "max_accepted_htlcs": <uint32>,
    "channel_flags": <uint32>,
}
```

### gRPC Request: [lnrpc.ChannelAcceptResponse (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1102)


Parameter | Type | Description
--------- | ---- | ----------- 
accept | bool | Whether or not the client accepts the channel. 
pending_chan_id | bytes | The pending channel id to which this response applies.  
### gRPC Response: [lnrpc.ChannelAcceptRequest (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1053)


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node that wishes to open an inbound channel. 
chain_hash | bytes | The hash of the genesis block that the proposed channel resides in. 
pending_chan_id | bytes | The pending channel id. 
funding_amt | uint64 | The funding amount in satoshis that initiator wishes to use in the / channel. 
push_amt | uint64 | The push amount of the proposed channel in millisatoshis. 
dust_limit | uint64 | The dust limit of the initiator's commitment tx. 
max_value_in_flight | uint64 | The maximum amount of coins in millisatoshis that can be pending in this / channel. 
channel_reserve | uint64 | The minimum amount of satoshis the initiator requires us to have at all / times. 
min_htlc | uint64 | The smallest HTLC in millisatoshis that the initiator will accept. 
fee_per_kw | uint64 | The initial fee rate that the initiator suggests for both commitment / transactions. 
csv_delay | uint32 | The number of blocks to use for the relative time lock in the pay-to-self output of both commitment transactions. 
max_accepted_htlcs | uint32 | The total number of incoming HTLC's that the initiator will accept. 
channel_flags | uint32 | A bit-field which the initiator uses to specify proposed channel / behavior.  

# Lightning.ChannelBalance


### Simple RPC


ChannelBalance returns the total funds available across all open channels in satoshis.

```shell

# Returns the sum of the total available channel balance across all open channels.

$ lncli channelbalance [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChannelBalanceRequest()
>>> response = stub.ChannelBalance(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "balance": <int64>,
    "pending_open_balance": <int64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.channelBalance(request, function(err, response) {
    console.log(response);
  })
{ 
    "balance": <int64>,
    "pending_open_balance": <int64>,
}
```

### gRPC Request: [lnrpc.ChannelBalanceRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2271)


This request has no parameters.

### gRPC Response: [lnrpc.ChannelBalanceResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2273)


Parameter | Type | Description
--------- | ---- | ----------- 
balance | int64 | Sum of channels balances denominated in satoshis 
pending_open_balance | int64 | Sum of channels pending balances denominated in satoshis  

# Lightning.CloseChannel


### Response-streaming RPC


CloseChannel attempts to close an active channel identified by its channel outpoint (ChannelPoint). The actions of this method can additionally be augmented to attempt a force close after a timeout period in the case of an inactive peer. If a non-force close (cooperative closure) is requested, then the user can specify either a target number of blocks until the closure transaction is confirmed, or a manual fee rate. If neither are specified, then a default lax, block confirmation target is used.

```shell

# Close an existing channel. The channel can be closed either cooperatively,
# or unilaterally (--force).
# A unilateral channel closure means that the latest commitment
# transaction will be broadcast to the network. As a result, any settled
# funds will be time locked for a few blocks before they can be spent.
# In the case of a cooperative closure, one can manually set the fee to
# be used for the closing transaction via either the --conf_target or
# --sat_per_byte arguments. This will be the starting value used during
# fee negotiation. This is optional.
# In the case of a cooperative closure, one can manually set the address
# to deliver funds to upon closure. This is optional, and may only be used
# if an upfront shutdown address has not already been set. If neither are
# set the funds will be delivered to a new wallet address.
# To view which funding_txids/output_indexes can be used for a channel close,
# see the channel_point values within the listchannels command output.
# The format for a channel_point is 'funding_txid:output_index'.

$ lncli closechannel [command options] funding_txid [output_index]

# --funding_txid value   the txid of the channel's funding transaction
# --output_index value   the output index for the funding output of the funding transaction (default: 0)
# --force                attempt an uncooperative closure
# --block                block until the channel is closed
# --conf_target value    (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value   (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
# --delivery_addr value  (optional) an address to deliver funds upon cooperative channel closing, may only be used if an upfront shutdown addresss is notalready set
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.CloseChannelRequest(
        channel_point=<ChannelPoint>,
        force=<bool>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
        delivery_address=<string>,
    )
>>> for response in stub.CloseChannel(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "close_pending": <PendingUpdate>,
    "chan_close": <ChannelCloseUpdate>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    channel_point: <ChannelPoint>, 
    force: <bool>, 
    target_conf: <int32>, 
    sat_per_byte: <int64>, 
    delivery_address: <string>, 
  }; 
> var call = lightning.closeChannel(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "close_pending": <PendingUpdate>,
    "chan_close": <ChannelCloseUpdate>,
}
```

### gRPC Request: [lnrpc.CloseChannelRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1745)


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
force | bool | If true, then the channel will be closed forcibly. This means the / current commitment transaction will be signed and broadcast. 
target_conf | int32 | The target number of blocks that the closure transaction should be / confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / closure transaction. 
delivery_address | string | An optional address to send funds to in the case of a cooperative close. If the channel was opened with an upfront shutdown script and this field is set, the request to close will fail because the channel must pay out to the upfront shutdown addresss.  
### gRPC Response: [lnrpc.CloseStatusUpdate (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1774)


Parameter | Type | Description
--------- | ---- | ----------- 
close_pending | [PendingUpdate](#pendingupdate) |  
chan_close | [ChannelCloseUpdate](#channelcloseupdate) |   

# Lightning.ClosedChannels


### Simple RPC


ClosedChannels returns a description of all the closed channels that this node was a participant in.

```shell

# List all closed channels.

$ lncli closedchannels [command options] [arguments...]

# --cooperative       list channels that were closed cooperatively
# --local_force       list channels that were force-closed by the local node
# --remote_force      list channels that were force-closed by the remote node
# --breach            list channels for which the remote node attempted to broadcast a prior revoked channel state
# --funding_canceled  list channels that were never fully opened
# --abandoned         list channels that were abandoned by the local node
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ClosedChannelsRequest(
        cooperative=<bool>,
        local_force=<bool>,
        remote_force=<bool>,
        breach=<bool>,
        funding_canceled=<bool>,
        abandoned=<bool>,
    )
>>> response = stub.ClosedChannels(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "channels": <array ChannelCloseSummary>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    cooperative: <bool>, 
    local_force: <bool>, 
    remote_force: <bool>, 
    breach: <bool>, 
    funding_canceled: <bool>, 
    abandoned: <bool>, 
  }; 
> lightning.closedChannels(request, function(err, response) {
    console.log(response);
  })
{ 
    "channels": <array ChannelCloseSummary>,
}
```

### gRPC Request: [lnrpc.ClosedChannelsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1550)


Parameter | Type | Description
--------- | ---- | ----------- 
cooperative | bool |  
local_force | bool |  
remote_force | bool |  
breach | bool |  
funding_canceled | bool |  
abandoned | bool |   
### gRPC Response: [lnrpc.ClosedChannelsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1559)


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array ChannelCloseSummary](#channelclosesummary) |   

# Lightning.ConnectPeer


### Simple RPC


ConnectPeer attempts to establish a connection to a remote peer. This is at the networking level, and is used for communication between nodes. This is distinct from establishing a channel with a peer.

```shell

# Connect to a remote lnd peer.

$ lncli connect [command options] <pubkey>@host

# --perm  If set, the daemon will attempt to persistently connect to the target peer.
# If not, the call will be synchronous.
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ConnectPeerRequest(
        addr=<LightningAddress>,
        perm=<bool>,
    )
>>> response = stub.ConnectPeer(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    addr: <LightningAddress>, 
    perm: <bool>, 
  }; 
> lightning.connectPeer(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.ConnectPeerRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1274)


Parameter | Type | Description
--------- | ---- | ----------- 
addr | [LightningAddress](#lightningaddress) | Lightning address of the peer, in the format `<pubkey>@host` 
perm | bool | If set, the daemon will attempt to persistently connect to the target peer. Otherwise, the call will be synchronous.  
### gRPC Response: [lnrpc.ConnectPeerResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1282)


This response has no parameters.


# Lightning.DebugLevel


### Simple RPC


DebugLevel allows a caller to programmatically set the logging verbosity of lnd. The logging can be targeted according to a coarse daemon-wide logging level, or in a granular fashion to specify the logging for a target sub-system.

```shell

# Logging level for all subsystems {trace, debug, info, warn, error, critical, off}
# You may also specify <subsystem>=<level>,<subsystem2>=<level>,... to set the log level for individual subsystems
# Use show to list available subsystems

$ lncli debuglevel [command options] [arguments...]

# --show         if true, then the list of available sub-systems will be printed out
# --level value  the level specification to target either a coarse logging level, or granular set of specific sub-systems with logging levels for each
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.DebugLevelRequest(
        show=<bool>,
        level_spec=<string>,
    )
>>> response = stub.DebugLevel(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "sub_systems": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    show: <bool>, 
    level_spec: <string>, 
  }; 
> lightning.debugLevel(request, function(err, response) {
    console.log(response);
  })
{ 
    "sub_systems": <string>,
}
```

### gRPC Request: [lnrpc.DebugLevelRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3199)


Parameter | Type | Description
--------- | ---- | ----------- 
show | bool |  
level_spec | string |   
### gRPC Response: [lnrpc.DebugLevelResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3203)


Parameter | Type | Description
--------- | ---- | ----------- 
sub_systems | string |   

# Lightning.DecodePayReq


### Simple RPC


DecodePayReq takes an encoded payment request string and attempts to decode it, returning a full description of the conditions encoded within the payment request.

```shell

# Decode the passed payment request revealing the destination, payment hash and value of the payment request

$ lncli decodepayreq [command options] pay_req

# --pay_req value  the bech32 encoded payment request
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.PayReqString(
        pay_req=<string>,
    )
>>> response = stub.DecodePayReq(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "destination": <string>,
    "payment_hash": <string>,
    "num_satoshis": <int64>,
    "timestamp": <int64>,
    "expiry": <int64>,
    "description": <string>,
    "description_hash": <string>,
    "fallback_addr": <string>,
    "cltv_expiry": <int64>,
    "route_hints": <array RouteHint>,
    "payment_addr": <bytes>,
    "num_msat": <int64>,
    "features": <array FeaturesEntry>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pay_req: <string>, 
  }; 
> lightning.decodePayReq(request, function(err, response) {
    console.log(response);
  })
{ 
    "destination": <string>,
    "payment_hash": <string>,
    "num_satoshis": <int64>,
    "timestamp": <int64>,
    "expiry": <int64>,
    "description": <string>,
    "description_hash": <string>,
    "fallback_addr": <string>,
    "cltv_expiry": <int64>,
    "route_hints": <array RouteHint>,
    "payment_addr": <bytes>,
    "num_msat": <int64>,
    "features": <array FeaturesEntry>,
}
```

### gRPC Request: [lnrpc.PayReqString ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3207)


Parameter | Type | Description
--------- | ---- | ----------- 
pay_req | string | The payment request string to be decoded  
### gRPC Response: [lnrpc.PayReq ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3211)


Parameter | Type | Description
--------- | ---- | ----------- 
destination | string |  
payment_hash | string |  
num_satoshis | int64 |  
timestamp | int64 |  
expiry | int64 |  
description | string |  
description_hash | string |  
fallback_addr | string |  
cltv_expiry | int64 |  
route_hints | [array RouteHint](#routehint) |  
payment_addr | bytes |  
num_msat | int64 |  
features | [array FeaturesEntry](#featuresentry) |   

# Lightning.DeleteAllPayments


### Simple RPC


DeleteAllPayments deletes all outgoing payments from DB.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.DeleteAllPaymentsRequest()
>>> response = stub.DeleteAllPayments(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.deleteAllPayments(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.DeleteAllPaymentsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3186)


This request has no parameters.

### gRPC Response: [lnrpc.DeleteAllPaymentsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3189)


This response has no parameters.


# Lightning.DescribeGraph


### Simple RPC


DescribeGraph returns a description of the latest graph state from the point of view of the node. The graph information is partitioned into two components: all the nodes/vertexes, and all the edges that connect the vertexes themselves. As this is a directed graph, the edges also contain the node directional specific routing policy which includes: the time lock delta, fee information, etc.

```shell

# Prints a human readable version of the known channel graph from the PoV of the node

$ lncli describegraph [command options] [arguments...]

# --include_unannounced  If set, unannounced channels will be included in the graph. Unannounced channels are both private channels, and public channels that are not yet announced to the network.
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChannelGraphRequest(
        include_unannounced=<bool>,
    )
>>> response = stub.DescribeGraph(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "nodes": <array LightningNode>,
    "edges": <array ChannelEdge>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    include_unannounced: <bool>, 
  }; 
> lightning.describeGraph(request, function(err, response) {
    console.log(response);
  })
{ 
    "nodes": <array LightningNode>,
    "edges": <array ChannelEdge>,
}
```

### gRPC Request: [lnrpc.ChannelGraphRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2623)


Parameter | Type | Description
--------- | ---- | ----------- 
include_unannounced | bool | Whether unannounced channels are included in the response or not. If set, unannounced channels are included. Unannounced channels are both private channels, and public channels that are not yet announced to the network.  
### gRPC Response: [lnrpc.ChannelGraph ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2633)


Parameter | Type | Description
--------- | ---- | ----------- 
nodes | [array LightningNode](#lightningnode) | The list of `LightningNode`s in this channel graph 
edges | [array ChannelEdge](#channeledge) | The list of `ChannelEdge`s in this channel graph  

# Lightning.DisconnectPeer


### Simple RPC


DisconnectPeer attempts to disconnect one peer from another identified by a given pubKey. In the case that we currently have a pending or active channel with the target peer, then this action will be not be allowed.

```shell

# Disconnect a remote lnd peer identified by public key.

$ lncli disconnect [command options] <pubkey>

# --node_key value  The hex-encoded compressed public key of the peer to disconnect from
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.DisconnectPeerRequest(
        pub_key=<string>,
    )
>>> response = stub.DisconnectPeer(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pub_key: <string>, 
  }; 
> lightning.disconnectPeer(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.DisconnectPeerRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1285)


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The pubkey of the node to disconnect from  
### gRPC Response: [lnrpc.DisconnectPeerResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1289)


This response has no parameters.


# Lightning.EstimateFee


### Simple RPC


EstimateFee asks the chain backend to estimate the fee rate and total fees for a transaction that pays to multiple specified outputs.

```shell

# Get fee estimates for sending a transaction paying the specified amount(s) to the passed address(es).
# The send-json-string' param decodes addresses and the amount to send respectively in the following format:
# '{"ExampleAddr": NumCoinsInSatoshis, "SecondAddr": NumCoins}'

$ lncli estimatefee [command options] send-json-string [--conf_target=N]

# --conf_target value  (optional) the number of blocks that the transaction *should* confirm in (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.EstimateFeeRequest(
        AddrToAmount=<array AddrToAmountEntry>,
        target_conf=<int32>,
    )
>>> response = stub.EstimateFee(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "fee_sat": <int64>,
    "feerate_sat_per_byte": <int64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    AddrToAmount: <array AddrToAmountEntry>, 
    target_conf: <int32>, 
  }; 
> lightning.estimateFee(request, function(err, response) {
    console.log(response);
  })
{ 
    "fee_sat": <int64>,
    "feerate_sat_per_byte": <int64>,
}
```

### gRPC Request: [lnrpc.EstimateFeeRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1149)


Parameter | Type | Description
--------- | ---- | ----------- 
AddrToAmount | [array AddrToAmountEntry](#addrtoamountentry) | The map from addresses to amounts for the transaction. 
target_conf | int32 | The target number of blocks that this transaction should be confirmed / by.  
### gRPC Response: [lnrpc.EstimateFeeResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1158)


Parameter | Type | Description
--------- | ---- | ----------- 
fee_sat | int64 | The total fee in satoshis. 
feerate_sat_per_byte | int64 | The fee rate in satoshi/byte.  

# Lightning.ExportAllChannelBackups


### Simple RPC


ExportAllChannelBackups returns static channel backups for all existing channels known to lnd. A set of regular singular static channel backups for each channel are returned. Additionally, a multi-channel backup is returned as well, which contains a single encrypted blob containing the backups of each channel.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChanBackupExportRequest()
>>> response = stub.ExportAllChannelBackups(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "single_chan_backups": <ChannelBackups>,
    "multi_chan_backup": <MultiChanBackup>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.exportAllChannelBackups(request, function(err, response) {
    console.log(response);
  })
{ 
    "single_chan_backups": <ChannelBackups>,
    "multi_chan_backup": <MultiChanBackup>,
}
```

### gRPC Request: [lnrpc.ChanBackupExportRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3426)


This request has no parameters.

### gRPC Response: [lnrpc.ChanBackupSnapshot ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3428)


Parameter | Type | Description
--------- | ---- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) | The set of new channels that have been added since the last channel backup snapshot was requested. 
multi_chan_backup | [MultiChanBackup](#multichanbackup) | A multi-channel backup that covers all open channels currently known to lnd.  

# Lightning.ExportChannelBackup


### Simple RPC


ExportChannelBackup attempts to return an encrypted static channel backup for the target channel identified by it channel point. The backup is encrypted with a key generated from the aezeed seed of the user. The returned backup can either be restored using the RestoreChannelBackup method once lnd is running, or via the InitWallet and UnlockWallet methods from the WalletUnlocker service.

```shell

# This command allows a user to export a Static Channel Backup (SCB) for
# a selected channel. SCB's are encrypted backups of a channel's initial
# state that are encrypted with a key derived from the seed of a user. In
# the case of partial or complete data loss, the SCB will allow the user
# to reclaim settled funds in the channel at its final state. The
# exported channel backups can be restored at a later time using the
# restorechanbackup command.
# This command will return one of two types of channel backups depending
# on the set of passed arguments:
# * If a target channel point is specified, then a single channel
# backup containing only the information for that channel will be
# returned.
# * If the --all flag is passed, then a multi-channel backup will be
# returned. A multi backup is a single encrypted blob (displayed in
# hex encoding) that contains several channels in a single cipher
# text.
# Both of the backup types can be restored using the restorechanbackup
# command.

$ lncli exportchanbackup [command options] [chan_point] [--all] [--output_file]

# --chan_point value   the target channel to obtain an SCB for
# --all                if specified, then a multi backup of all active channels will be returned
# --output_file value  if specified, then rather than printing a JSON output
# of the static channel backup, a serialized version of
# the backup (either Single or Multi) will be written to
# the target file, this is the same format used by lnd in
# its channels.backup file
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ExportChannelBackupRequest(
        chan_point=<ChannelPoint>,
    )
>>> response = stub.ExportChannelBackup(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "chan_point": <ChannelPoint>,
    "chan_backup": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    chan_point: <ChannelPoint>, 
  }; 
> lightning.exportChannelBackup(request, function(err, response) {
    console.log(response);
  })
{ 
    "chan_point": <ChannelPoint>,
    "chan_backup": <bytes>,
}
```

### gRPC Request: [lnrpc.ExportChannelBackupRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3391)


Parameter | Type | Description
--------- | ---- | ----------- 
chan_point | [ChannelPoint](#channelpoint) | The target channel point to obtain a back up for.  
### gRPC Response: [lnrpc.ChannelBackup ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3396)


Parameter | Type | Description
--------- | ---- | ----------- 
chan_point | [ChannelPoint](#channelpoint) | Identifies the channel that this backup belongs to. 
chan_backup | bytes | Is an encrypted single-chan backup. this can be passed to RestoreChannelBackups, or the WalletUnlocker Init and Unlock methods in order to trigger the recovery protocol. When using REST, this field must be encoded as base64.  

# Lightning.FeeReport


### Simple RPC


FeeReport allows the caller to obtain a report detailing the current fee schedule enforced by the node globally for each channel.

```shell

# Returns the current fee policies of all active channels.
# Fee policies can be updated using the updatechanpolicy command.

$ lncli feereport [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.FeeReportRequest()
>>> response = stub.FeeReport(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "channel_fees": <array ChannelFeeReport>,
    "day_fee_sum": <uint64>,
    "week_fee_sum": <uint64>,
    "month_fee_sum": <uint64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.feeReport(request, function(err, response) {
    console.log(response);
  })
{ 
    "channel_fees": <array ChannelFeeReport>,
    "day_fee_sum": <uint64>,
    "week_fee_sum": <uint64>,
    "month_fee_sum": <uint64>,
}
```

### gRPC Request: [lnrpc.FeeReportRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3253)


This request has no parameters.

### gRPC Response: [lnrpc.FeeReportResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3273)


Parameter | Type | Description
--------- | ---- | ----------- 
channel_fees | [array ChannelFeeReport](#channelfeereport) | An array of channel fee reports which describes the current fee schedule / for each channel. 
day_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected / over the past 24 hrs. 
week_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 week. 
month_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 month.  

# Lightning.ForwardingHistory


### Simple RPC


ForwardingHistory allows the caller to query the htlcswitch for a record of all HTLCs forwarded within the target time range, and integer offset within that time range. If no time-range is specified, then the first chunk of the past 24 hrs of forwarding history are returned.  A list of forwarding events are returned. The size of each forwarding event is 40 bytes, and the max message size able to be returned in gRPC is 4 MiB. As a result each message can only contain 50k entries. Each response has the index offset of the last entry. The index offset can be provided to the request to allow the caller to skip a series of records.

```shell

# Query the HTLC switch's internal forwarding log for all completed
# payment circuits (HTLCs) over a particular time range (--start_time and
# --end_time). The start and end times are meant to be expressed in
# seconds since the Unix epoch. If --start_time isn't provided,
# then 24 hours ago is used.  If --end_time isn't provided,
# then the current time is used.
# The max number of events returned is 50k. The default number is 100,
# callers can use the --max_events param to modify this value.
# Finally, callers can skip a series of events using the --index_offset
# parameter. Each response will contain the offset index of the last
# entry. Using this callers can manually paginate within a time slice.

$ lncli fwdinghistory [command options] start_time [end_time] [index_offset] [max_events]

# --start_time value    the starting time for the query, expressed in seconds since the unix epoch (default: 0)
# --end_time value      the end time for the query, expressed in seconds since the unix epoch (default: 0)
# --index_offset value  the number of events to skip (default: 0)
# --max_events value    the max number of events to return (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ForwardingHistoryRequest(
        start_time=<uint64>,
        end_time=<uint64>,
        index_offset=<uint32>,
        num_max_events=<uint32>,
    )
>>> response = stub.ForwardingHistory(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "forwarding_events": <array ForwardingEvent>,
    "last_offset_index": <uint32>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    start_time: <uint64>, 
    end_time: <uint64>, 
    index_offset: <uint32>, 
    num_max_events: <uint32>, 
  }; 
> lightning.forwardingHistory(request, function(err, response) {
    console.log(response);
  })
{ 
    "forwarding_events": <array ForwardingEvent>,
    "last_offset_index": <uint32>,
}
```

### gRPC Request: [lnrpc.ForwardingHistoryRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3324)


Parameter | Type | Description
--------- | ---- | ----------- 
start_time | uint64 | Start time is the starting point of the forwarding history request. All / records beyond this point will be included, respecting the end time, and / the index offset. 
end_time | uint64 | End time is the end point of the forwarding history request. The / response will carry at most 50k records between the start time and the / end time. The index offset can be used to implement pagination. 
index_offset | uint32 | Index offset is the offset in the time series to start at. As each / response can only contain 50k records, callers can use this to skip / around within a packed time series. 
num_max_events | uint32 | The max number of events to return in the response to this query.  
### gRPC Response: [lnrpc.ForwardingHistoryResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3381)


Parameter | Type | Description
--------- | ---- | ----------- 
forwarding_events | [array ForwardingEvent](#forwardingevent) | A list of forwarding events from the time slice of the time series / specified in the request. 
last_offset_index | uint32 | The index of the last time in the set of returned forwarding events. Can / be used to seek further, pagination style.  

# Lightning.FundingStateStep


### Simple RPC


FundingStateStep is an advanced funding related call that allows the caller to either execute some preparatory steps for a funding workflow, or manually progress a funding workflow. The primary way a funding flow is identified is via its pending channel ID. As an example, this method can be used to specify that we're expecting a funding flow for a particular pending channel ID, for which we need to use specific parameters. Alternatively, this can be used to interactively drive PSBT signing for funding for partially complete funding transactions.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.FundingTransitionMsg(
        shim_register=<FundingShim>,
        shim_cancel=<FundingShimCancel>,
        psbt_verify=<FundingPsbtVerify>,
        psbt_finalize=<FundingPsbtFinalize>,
    )
>>> response = stub.FundingStateStep(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    shim_register: <FundingShim>, 
    shim_cancel: <FundingShimCancel>, 
    psbt_verify: <FundingPsbtVerify>, 
    psbt_finalize: <FundingPsbtFinalize>, 
  }; 
> lightning.fundingStateStep(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.FundingTransitionMsg ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2018)


Parameter | Type | Description
--------- | ---- | ----------- 
shim_register | [FundingShim](#fundingshim) | The funding shim to register. This should be used before any channel funding has began by the remote party, as it is intended as a preparatory step for the full channel funding. 
shim_cancel | [FundingShimCancel](#fundingshimcancel) | Used to cancel an existing registered funding shim. 
psbt_verify | [FundingPsbtVerify](#fundingpsbtverify) | Used to continue a funding flow that was initiated to be executed through a PSBT. This step verifies that the PSBT contains the correct outputs to fund the channel. 
psbt_finalize | [FundingPsbtFinalize](#fundingpsbtfinalize) | Used to continue a funding flow that was initiated to be executed through a PSBT. This step finalizes the funded and signed PSBT, finishes negotiation with the peer and finally publishes the resulting funding transaction.  
### gRPC Response: [lnrpc.FundingStateStepResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2047)


This response has no parameters.


# Lightning.GetChanInfo


### Simple RPC


GetChanInfo returns the latest authenticated network announcement for the given channel identified by its channel ID: an 8-byte integer which uniquely identifies the location of transaction's funding output within the blockchain.

```shell

# Prints out the latest authenticated state for a particular channel

$ lncli getchaninfo [command options] chan_id

# --chan_id value  the 8-byte compact channel ID to query for (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChanInfoRequest(
        chan_id=<uint64>,
    )
>>> response = stub.GetChanInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "channel_id": <uint64>,
    "chan_point": <string>,
    "last_update": <uint32>,
    "node1_pub": <string>,
    "node2_pub": <string>,
    "capacity": <int64>,
    "node1_policy": <RoutingPolicy>,
    "node2_policy": <RoutingPolicy>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    chan_id: <uint64>, 
  }; 
> lightning.getChanInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "channel_id": <uint64>,
    "chan_point": <string>,
    "last_update": <uint32>,
    "node1_pub": <string>,
    "node2_pub": <string>,
    "capacity": <int64>,
    "node1_policy": <RoutingPolicy>,
    "node2_policy": <RoutingPolicy>,
}
```

### gRPC Request: [lnrpc.ChanInfoRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2670)


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.  
### gRPC Response: [lnrpc.ChannelEdge ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2603)


Parameter | Type | Description
--------- | ---- | ----------- 
channel_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | string |  
last_update | uint32 |  
node1_pub | string |  
node2_pub | string |  
capacity | int64 |  
node1_policy | [RoutingPolicy](#routingpolicy) |  
node2_policy | [RoutingPolicy](#routingpolicy) |   

# Lightning.GetInfo


### Simple RPC


GetInfo returns general information concerning the lightning node including it's identity pubkey, alias, the chains it is connected to, and information concerning the number of open+pending channels.

```shell

# Returns basic information related to the active daemon.

$ lncli getinfo [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.GetInfoRequest()
>>> response = stub.GetInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "version": <string>,
    "identity_pubkey": <string>,
    "alias": <string>,
    "color": <string>,
    "num_pending_channels": <uint32>,
    "num_active_channels": <uint32>,
    "num_inactive_channels": <uint32>,
    "num_peers": <uint32>,
    "block_height": <uint32>,
    "block_hash": <string>,
    "best_header_timestamp": <int64>,
    "synced_to_chain": <bool>,
    "synced_to_graph": <bool>,
    "testnet": <bool>,
    "chains": <array Chain>,
    "uris": <array string>,
    "features": <array FeaturesEntry>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.getInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "version": <string>,
    "identity_pubkey": <string>,
    "alias": <string>,
    "color": <string>,
    "num_pending_channels": <uint32>,
    "num_active_channels": <uint32>,
    "num_inactive_channels": <uint32>,
    "num_peers": <uint32>,
    "block_height": <uint32>,
    "block_hash": <string>,
    "best_header_timestamp": <int64>,
    "synced_to_chain": <bool>,
    "synced_to_graph": <bool>,
    "testnet": <bool>,
    "chains": <array Chain>,
    "uris": <array string>,
    "features": <array FeaturesEntry>,
}
```

### gRPC Request: [lnrpc.GetInfoRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1657)


This request has no parameters.

### gRPC Response: [lnrpc.GetInfoResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1659)


Parameter | Type | Description
--------- | ---- | ----------- 
version | string | The version of the LND software that the node is running. 
identity_pubkey | string | The identity pubkey of the current node. 
alias | string | If applicable, the alias of the current node, e.g. "bob" 
color | string | The color of the current node in hex code format 
num_pending_channels | uint32 | Number of pending channels 
num_active_channels | uint32 | Number of active channels 
num_inactive_channels | uint32 | Number of inactive channels 
num_peers | uint32 | Number of peers 
block_height | uint32 | The node's current view of the height of the best block 
block_hash | string | The node's current view of the hash of the best block 
best_header_timestamp | int64 | Timestamp of the block best known to the wallet 
synced_to_chain | bool | Whether the wallet's view is synced to the main chain 
synced_to_graph | bool | Whether we consider ourselves synced with the public channel graph. 
testnet | bool | Whether the current node is connected to testnet. This field is deprecated and the network field should be used instead 
chains | [array Chain](#chain) | A list of active chains the node is connected to 
uris | array string | The URIs of the current node. 
features | [array FeaturesEntry](#featuresentry) | Features that our node has advertised in our init message, node announcements and invoices.  

# Lightning.GetNetworkInfo


### Simple RPC


GetNetworkInfo returns some basic stats about the known channel graph from the point of view of the node.

```shell

# Returns a set of statistics pertaining to the known channel graph

$ lncli getnetworkinfo [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.NetworkInfoRequest()
>>> response = stub.GetNetworkInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "graph_diameter": <uint32>,
    "avg_out_degree": <double>,
    "max_out_degree": <uint32>,
    "num_nodes": <uint32>,
    "num_channels": <uint32>,
    "total_network_capacity": <int64>,
    "avg_channel_size": <double>,
    "min_channel_size": <int64>,
    "max_channel_size": <int64>,
    "median_channel_size_sat": <int64>,
    "num_zombie_chans": <uint64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.getNetworkInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "graph_diameter": <uint32>,
    "avg_out_degree": <double>,
    "max_out_degree": <uint32>,
    "num_nodes": <uint32>,
    "num_channels": <uint32>,
    "total_network_capacity": <int64>,
    "avg_channel_size": <double>,
    "min_channel_size": <int64>,
    "max_channel_size": <int64>,
    "median_channel_size_sat": <int64>,
    "num_zombie_chans": <uint64>,
}
```

### gRPC Request: [lnrpc.NetworkInfoRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2679)


This request has no parameters.

### gRPC Response: [lnrpc.NetworkInfo ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2681)


Parameter | Type | Description
--------- | ---- | ----------- 
graph_diameter | uint32 |  
avg_out_degree | double |  
max_out_degree | uint32 |  
num_nodes | uint32 |  
num_channels | uint32 |  
total_network_capacity | int64 |  
avg_channel_size | double |  
min_channel_size | int64 |  
max_channel_size | int64 |  
median_channel_size_sat | int64 |  
num_zombie_chans | uint64 | The number of edges marked as zombies.  

# Lightning.GetNodeInfo


### Simple RPC


GetNodeInfo returns the latest advertised, aggregated, and authenticated channel information for the specified node identified by its public key.

```shell

# Prints out the latest authenticated node state for an advertised node

$ lncli getnodeinfo [command options] [arguments...]

# --pub_key value     the 33-byte hex-encoded compressed public of the target node
# --include_channels  if true, will return all known channels associated with the node
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.NodeInfoRequest(
        pub_key=<string>,
        include_channels=<bool>,
    )
>>> response = stub.GetNodeInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "node": <LightningNode>,
    "num_channels": <uint32>,
    "total_capacity": <int64>,
    "channels": <array ChannelEdge>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pub_key: <string>, 
    include_channels: <bool>, 
  }; 
> lightning.getNodeInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "node": <LightningNode>,
    "num_channels": <uint32>,
    "total_capacity": <int64>,
    "channels": <array ChannelEdge>,
}
```

### gRPC Request: [lnrpc.NodeInfoRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2539)


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded compressed public of the target node 
include_channels | bool | If true, will include all known channels associated with the node.  
### gRPC Response: [lnrpc.NodeInfo ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2547)


Parameter | Type | Description
--------- | ---- | ----------- 
node | [LightningNode](#lightningnode) | An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | uint32 | The total number of channels for the node. 
total_capacity | int64 | The sum of all channels capacity for the node, denominated in satoshis. 
channels | [array ChannelEdge](#channeledge) | A list of all public channels for the node.  

# Lightning.GetNodeMetrics


### Simple RPC


GetNodeMetrics returns node metrics calculated from the graph. Currently the only supported metric is betweenness centrality of individual nodes.

```shell

# Prints out node metrics calculated from the current graph

$ lncli getnodemetrics [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.NodeMetricsRequest(
        types=<array NodeMetricType>,
    )
>>> response = stub.GetNodeMetrics(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "betweenness_centrality": <array BetweennessCentralityEntry>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    types: <array NodeMetricType>, 
  }; 
> lightning.getNodeMetrics(request, function(err, response) {
    console.log(response);
  })
{ 
    "betweenness_centrality": <array BetweennessCentralityEntry>,
}
```

### gRPC Request: [lnrpc.NodeMetricsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2646)


Parameter | Type | Description
--------- | ---- | ----------- 
types | [array NodeMetricType](#nodemetrictype) | The requested node metrics.  
### gRPC Response: [lnrpc.NodeMetricsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2651)


Parameter | Type | Description
--------- | ---- | ----------- 
betweenness_centrality | [array BetweennessCentralityEntry](#betweennesscentralityentry) | Betweenness centrality is the sum of the ratio of shortest paths that pass through the node for each pair of nodes in the graph (not counting paths starting or ending at this node). Map of node pubkey to betweenness centrality of the node. Normalized values are in the [0,1] closed interval.  

# Lightning.GetTransactions


### Simple RPC


GetTransactions returns a list describing all the known transactions relevant to the wallet.

```shell

# List all transactions an address of the wallet was involved in.

$ lncli listchaintxns [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.GetTransactionsRequest()
>>> response = stub.GetTransactions(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "transactions": <array Transaction>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.getTransactions(request, function(err, response) {
    console.log(response);
  })
{ 
    "transactions": <array Transaction>,
}
```

### gRPC Request: [lnrpc.GetTransactionsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L899)


This request has no parameters.

### gRPC Response: [lnrpc.TransactionDetails ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L901)


Parameter | Type | Description
--------- | ---- | ----------- 
transactions | [array Transaction](#transaction) | The list of transactions relevant to the wallet.  

# Lightning.ListChannels


### Simple RPC


ListChannels returns a description of all the open channels that this node is a participant in.

```shell

# List all open channels.

$ lncli listchannels [command options] [arguments...]

# --active_only    only list channels which are currently active
# --inactive_only  only list channels which are currently inactive
# --public_only    only list channels which are currently public
# --private_only   only list channels which are currently private
# --peer value     (optional) only display channels with a particular peer, accepts 66-byte, hex-encoded pubkeys
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ListChannelsRequest(
        active_only=<bool>,
        inactive_only=<bool>,
        public_only=<bool>,
        private_only=<bool>,
        peer=<bytes>,
    )
>>> response = stub.ListChannels(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "channels": <array Channel>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    active_only: <bool>, 
    inactive_only: <bool>, 
    public_only: <bool>, 
    private_only: <bool>, 
    peer: <bytes>, 
  }; 
> lightning.listChannels(request, function(err, response) {
    console.log(response);
  })
{ 
    "channels": <array Channel>,
}
```

### gRPC Request: [lnrpc.ListChannelsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1469)


Parameter | Type | Description
--------- | ---- | ----------- 
active_only | bool |  
inactive_only | bool |  
public_only | bool |  
private_only | bool |  
peer | bytes | Filters the response for channels with a target peer's pubkey. If peer is empty, all channels will be returned.  
### gRPC Response: [lnrpc.ListChannelsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1481)


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array Channel](#channel) | The list of active channels  

# Lightning.ListInvoices


### Simple RPC


ListInvoices returns a list of all the invoices currently stored within the database. Any active debug invoices are ignored. It has full support for paginated responses, allowing users to query for specific invoices through their add_index. This can be done by using either the first_index_offset or last_index_offset fields included in the response as the index_offset of the next request. By default, the first 100 invoices created will be returned. Backwards pagination is also supported through the Reversed flag.

```shell

# This command enables the retrieval of all invoices currently stored
# within the database. It has full support for paginationed responses,
# allowing users to query for specific invoices through their add_index.
# This can be done by using either the first_index_offset or
# last_index_offset fields included in the response as the index_offset of
# the next request. Backward pagination is enabled by default to receive
# current invoices first. If you wish to paginate forwards, set the
# paginate-forwards flag.  If none of the parameters are specified, then
# the last 100 invoices will be returned.
# For example: if you have 200 invoices, "lncli listinvoices" will return
# the last 100 created. If you wish to retrieve the previous 100, the
# first_offset_index of the response can be used as the index_offset of
# the next listinvoices request.

$ lncli listinvoices [command options] [arguments...]

# --pending_only        toggles if all invoices should be returned, or only those that are currently unsettled
# --index_offset value  the index of an invoice that will be used as either the start or end of a query to determine which invoices should be returned in the response (default: 0)
# --max_invoices value  the max number of invoices to return (default: 0)
# --paginate-forwards   if set, invoices succeeding the index_offset will be returned
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ListInvoiceRequest(
        pending_only=<bool>,
        index_offset=<uint64>,
        num_max_invoices=<uint64>,
        reversed=<bool>,
    )
>>> response = stub.ListInvoices(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "invoices": <array Invoice>,
    "last_index_offset": <uint64>,
    "first_index_offset": <uint64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pending_only: <bool>, 
    index_offset: <uint64>, 
    num_max_invoices: <uint64>, 
    reversed: <bool>, 
  }; 
> lightning.listInvoices(request, function(err, response) {
    console.log(response);
  })
{ 
    "invoices": <array Invoice>,
    "last_index_offset": <uint64>,
    "first_index_offset": <uint64>,
}
```

### gRPC Request: [lnrpc.ListInvoiceRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2996)


Parameter | Type | Description
--------- | ---- | ----------- 
pending_only | bool | If set, only invoices that are not settled and not canceled will be returned in the response. 
index_offset | uint64 | The index of an invoice that will be used as either the start or end of a query to determine which invoices should be returned in the response. 
num_max_invoices | uint64 | The max number of invoices to return in the response to this query. 
reversed | bool | If set, the invoices returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards.  
### gRPC Response: [lnrpc.ListInvoiceResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3018)


Parameter | Type | Description
--------- | ---- | ----------- 
invoices | [array Invoice](#invoice) | A list of invoices from the time slice of the time series specified in the request. 
last_index_offset | uint64 | The index of the last item in the set of returned invoices. This can be used to seek further, pagination style. 
first_index_offset | uint64 | The index of the last item in the set of returned invoices. This can be used to seek backwards, pagination style.  

# Lightning.ListPayments


### Simple RPC


ListPayments returns a list of all outgoing payments.

```shell

# This command enables the retrieval of payments stored in the database. Pagination is supported by the usage of index_offset in combination with the paginate_forwards flag. Reversed pagination is enabled by default to receive current payments first. Pagination can be resumed by using the returned last_index_offset (for forwards order), or first_index_offset (for reversed order) as the offset_index.

$ lncli listpayments [command options] [arguments...]

# --include_incomplete  if set to true, payments still in flight (or failed) will be returned as well, keepingindices for payments the same as without the flag
# --index_offset value  The index of a payment that will be used as either the start (in forwards mode) or end (in reverse mode) of a query to determine which payments should be returned in the response, where the index_offset is excluded. If index_offset is set to zero in reversed mode, the query will end with the last payment made. (default: 0)
# --max_payments value  the max number of payments to return, by default, all completed payments are returned (default: 0)
# --paginate_forwards   if set, payments succeeding the index_offset will be returned, allowing forwards pagination
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ListPaymentsRequest(
        include_incomplete=<bool>,
        index_offset=<uint64>,
        max_payments=<uint64>,
        reversed=<bool>,
    )
>>> response = stub.ListPayments(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payments": <array Payment>,
    "first_index_offset": <uint64>,
    "last_index_offset": <uint64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    include_incomplete: <bool>, 
    index_offset: <uint64>, 
    max_payments: <uint64>, 
    reversed: <bool>, 
  }; 
> lightning.listPayments(request, function(err, response) {
    console.log(response);
  })
{ 
    "payments": <array Payment>,
    "first_index_offset": <uint64>,
    "last_index_offset": <uint64>,
}
```

### gRPC Request: [lnrpc.ListPaymentsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3140)


Parameter | Type | Description
--------- | ---- | ----------- 
include_incomplete | bool | If true, then return payments that have not yet fully completed. This means that pending payments, as well as failed payments will show up if this field is set to true. This flag doesn't change the meaning of the indices, which are tied to individual payments. 
index_offset | uint64 | The index of a payment that will be used as either the start or end of a query to determine which payments should be returned in the response. The index_offset is exclusive. In the case of a zero index_offset, the query will start with the oldest payment when paginating forwards, or will end with the most recent payment when paginating backwards. 
max_payments | uint64 | The maximal number of payments returned in the response to this query. 
reversed | bool | If set, the payments returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards. The order of the returned payments is always oldest first (ascending index order).  
### gRPC Response: [lnrpc.ListPaymentsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3169)


Parameter | Type | Description
--------- | ---- | ----------- 
payments | [array Payment](#payment) | The list of payments 
first_index_offset | uint64 | The index of the first item in the set of returned payments. This can be used as the index_offset to continue seeking backwards in the next request. 
last_index_offset | uint64 | The index of the last item in the set of returned payments. This can be used as the index_offset to continue seeking forwards in the next request.  

# Lightning.ListPeers


### Simple RPC


ListPeers returns a verbose listing of all currently active peers.

```shell

# List all active, currently connected peers.

$ lncli listpeers [command options] [arguments...]

# --list_errors  list a full set of most recent errors for the peer
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ListPeersRequest(
        latest_error=<bool>,
    )
>>> response = stub.ListPeers(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "peers": <array Peer>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    latest_error: <bool>, 
  }; 
> lightning.listPeers(request, function(err, response) {
    console.log(response);
  })
{ 
    "peers": <array Peer>,
}
```

### gRPC Request: [lnrpc.ListPeersRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1629)


Parameter | Type | Description
--------- | ---- | ----------- 
latest_error | bool | If true, only the last error that our peer sent us will be returned with the peer's information, rather than the full set of historic errors we have stored.  
### gRPC Response: [lnrpc.ListPeersResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1637)


Parameter | Type | Description
--------- | ---- | ----------- 
peers | [array Peer](#peer) | The list of currently connected peers  

# Lightning.ListUnspent


### Simple RPC


ListUnspent returns a list of all utxos spendable by the wallet with a number of confirmations between the specified minimum and maximum.

```shell

# For each spendable utxo currently in the wallet, with at least min_confs
# confirmations, and at most max_confs confirmations, lists the txid,
# index, amount, address, address type, scriptPubkey and number of
# confirmations.  Use --min_confs=0 to include unconfirmed coins. To list
# all coins with at least min_confs confirmations, omit the second
# argument or flag '--max_confs'. To list all confirmed and unconfirmed
# coins, no arguments are required. To see only unconfirmed coins, use
# '--unconfirmed_only' with '--min_confs' and '--max_confs' set to zero or
# not present.

$ lncli listunspent [command options] [min-confs [max-confs]] [--unconfirmed_only]

# --min_confs value   the minimum number of confirmations for a utxo (default: 0)
# --max_confs value   the maximum number of confirmations for a utxo (default: 0)
# --unconfirmed_only  when min_confs and max_confs are zero, setting false implicitly overrides max_confs to be MaxInt32, otherwise max_confs remains zero. An error is returned if the value is true and both min_confs and max_confs are non-zero. (default: false)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ListUnspentRequest(
        min_confs=<int32>,
        max_confs=<int32>,
    )
>>> response = stub.ListUnspent(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "utxos": <array Utxo>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    min_confs: <int32>, 
    max_confs: <int32>, 
  }; 
> lightning.listUnspent(request, function(err, response) {
    console.log(response);
  })
{ 
    "utxos": <array Utxo>,
}
```

### gRPC Request: [lnrpc.ListUnspentRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1210)


Parameter | Type | Description
--------- | ---- | ----------- 
min_confs | int32 | The minimum number of confirmations to be included. 
max_confs | int32 | The maximum number of confirmations to be included.  
### gRPC Response: [lnrpc.ListUnspentResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1217)


Parameter | Type | Description
--------- | ---- | ----------- 
utxos | [array Utxo](#utxo) | A list of utxos  

# Lightning.LookupInvoice


### Simple RPC


LookupInvoice attempts to look up an invoice according to its payment hash. The passed payment hash *must* be exactly 32 bytes, if not, an error is returned.

```shell

# Lookup an existing invoice by its payment hash.

$ lncli lookupinvoice [command options] rhash

# --rhash value  the 32 byte payment hash of the invoice to query for, the hash should be a hex-encoded string
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.PaymentHash(
        r_hash_str=<string>,
        r_hash=<bytes>,
    )
>>> response = stub.LookupInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "memo": <string>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
    "value_msat": <int64>,
    "settled": <bool>,
    "creation_date": <int64>,
    "settle_date": <int64>,
    "payment_request": <string>,
    "description_hash": <bytes>,
    "expiry": <int64>,
    "fallback_addr": <string>,
    "cltv_expiry": <uint64>,
    "route_hints": <array RouteHint>,
    "private": <bool>,
    "add_index": <uint64>,
    "settle_index": <uint64>,
    "amt_paid": <int64>,
    "amt_paid_sat": <int64>,
    "amt_paid_msat": <int64>,
    "state": <InvoiceState>,
    "htlcs": <array InvoiceHTLC>,
    "features": <array FeaturesEntry>,
    "is_keysend": <bool>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    r_hash_str: <string>, 
    r_hash: <bytes>, 
  }; 
> lightning.lookupInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
    "memo": <string>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
    "value_msat": <int64>,
    "settled": <bool>,
    "creation_date": <int64>,
    "settle_date": <int64>,
    "payment_request": <string>,
    "description_hash": <bytes>,
    "expiry": <int64>,
    "fallback_addr": <string>,
    "cltv_expiry": <uint64>,
    "route_hints": <array RouteHint>,
    "private": <bool>,
    "add_index": <uint64>,
    "settle_index": <uint64>,
    "amt_paid": <int64>,
    "amt_paid_sat": <int64>,
    "amt_paid_msat": <int64>,
    "state": <InvoiceState>,
    "htlcs": <array InvoiceHTLC>,
    "features": <array FeaturesEntry>,
    "is_keysend": <bool>,
}
```

### gRPC Request: [lnrpc.PaymentHash ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2980)


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash_str | string | The hex-encoded payment hash of the invoice to be looked up. The passed payment hash must be exactly 32 bytes, otherwise an error is returned. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
r_hash | bytes | The payment hash of the invoice to be looked up. When using REST, this field must be encoded as base64.  
### gRPC Response: [lnrpc.Invoice ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2779)


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage. When using REST, this field must be encoded as base64. 
r_hash | bytes | The hash of the preimage. When using REST, this field must be encoded as base64. 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. When using REST, this field must be encoded as base64. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | uint64 | The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | int64 | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | int64 | The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | int64 | The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceState](#invoicestate) | The state the invoice is in. 
htlcs | [array InvoiceHTLC](#invoicehtlc) | List of HTLCs paying to this invoice [EXPERIMENTAL]. 
features | [array FeaturesEntry](#featuresentry) | List of features advertised on the invoice. 
is_keysend | bool | Indicates if this invoice was a spontaneous payment that arrived via keysend [EXPERIMENTAL].  

# Lightning.NewAddress


### Simple RPC


NewAddress creates a new address under control of the local wallet.

```shell

# Generate a wallet new address. Address-types has to be one of:
# - p2wkh:  Pay to witness key hash
# - np2wkh: Pay to nested witness key hash

$ lncli newaddress address-type

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.NewAddressRequest(
        type=<AddressType>,
    )
>>> response = stub.NewAddress(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "address": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    type: <AddressType>, 
  }; 
> lightning.newAddress(request, function(err, response) {
    console.log(response);
  })
{ 
    "address": <string>,
}
```

### gRPC Request: [lnrpc.NewAddressRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1235)


Parameter | Type | Description
--------- | ---- | ----------- 
type | [AddressType](#addresstype) | The address type  
### gRPC Response: [lnrpc.NewAddressResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1239)


Parameter | Type | Description
--------- | ---- | ----------- 
address | string | The newly generated wallet address  

# Lightning.OpenChannel


### Response-streaming RPC


OpenChannel attempts to open a singly funded channel specified in the request to a remote peer. Users are able to specify a target number of blocks that the funding transaction should be confirmed in, or a manual fee rate to us for the funding transaction. If neither are specified, then a lax block confirmation target is used. Each OpenStatusUpdate will return the pending channel ID of the in-progress channel. Depending on the arguments specified in the OpenChannelRequest, this pending channel ID can then be used to manually progress the channel funding flow.

```shell

# Attempt to open a new channel to an existing peer with the key node-key
# optionally blocking until the channel is 'open'.
# One can also connect to a node before opening a new channel to it by
# setting its host:port via the --connect argument. For this to work,
# the node_key must be provided, rather than the peer_id. This is optional.
# The channel will be initialized with local-amt satoshis local and push-amt
# satoshis for the remote node. Note that specifying push-amt means you give that
# amount to the remote node as part of the channel opening. Once the channel is open,
# a channelPoint (txid:vout) of the funding output is returned.
# If the remote peer supports the option upfront shutdown feature bit (query
# listpeers to see their supported feature bits), an address to enforce
# payout of funds on cooperative close can optionally be provided. Note that
# if you set this value, you will not be able to cooperatively close out to
# another address.
# One can manually set the fee to be used for the funding transaction via either
# the --conf_target or --sat_per_byte arguments. This is optional.

$ lncli openchannel [command options] node-key local-amt push-amt

# --node_key value          the identity public key of the target node/peer serialized in compressed format
# --connect value           (optional) the host:port of the target node
# --local_amt value         the number of satoshis the wallet should commit to the channel (default: 0)
# --push_amt value          the number of satoshis to give the remote side as part of the initial commitment state, this is equivalent to first opening a channel and sending the remote party funds, but done all in one step (default: 0)
# --block                   block and wait until the channel is fully open
# --conf_target value       (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value      (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
# --private                 make the channel private, such that it won't be announced to the greater network, and nodes other than the two channel endpoints must be explicitly told about it to be able to route through it
# --min_htlc_msat value     (optional) the minimum value we will require for incoming HTLCs on the channel (default: 0)
# --remote_csv_delay value  (optional) the number of blocks we will require our channel counterparty to wait before accessing its funds in case of unilateral close. If this is not set, we will scale the value according to the channel size (default: 0)
# --min_confs value         (optional) the minimum number of confirmations each one of your outputs used for the funding transaction must satisfy (default: 1)
# --close_address value     (optional) an address to enforce payout of our funds to on cooperative close. Note that if this value is set on channel open, you will *not* be able to cooperatively close to a different address.
# --psbt                    start an interactive mode that initiates funding through a partially signed bitcoin transaction (PSBT), allowing the channel funds to be added and signed from a hardware or other offline device.
# --base_psbt value         when using the interactive PSBT mode to open a new channel, use this base64 encoded PSBT as a base and add the new channel output to it instead of creating a new, empty one.
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.OpenChannelRequest(
        node_pubkey=<bytes>,
        node_pubkey_string=<string>,
        local_funding_amount=<int64>,
        push_sat=<int64>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
        private=<bool>,
        min_htlc_msat=<int64>,
        remote_csv_delay=<uint32>,
        min_confs=<int32>,
        spend_unconfirmed=<bool>,
        close_address=<string>,
        funding_shim=<FundingShim>,
    )
>>> for response in stub.OpenChannel(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "chan_pending": <PendingUpdate>,
    "chan_open": <ChannelOpenUpdate>,
    "psbt_fund": <ReadyForPsbtFunding>,
    "pending_chan_id": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    node_pubkey: <bytes>, 
    node_pubkey_string: <string>, 
    local_funding_amount: <int64>, 
    push_sat: <int64>, 
    target_conf: <int32>, 
    sat_per_byte: <int64>, 
    private: <bool>, 
    min_htlc_msat: <int64>, 
    remote_csv_delay: <uint32>, 
    min_confs: <int32>, 
    spend_unconfirmed: <bool>, 
    close_address: <string>, 
    funding_shim: <FundingShim>, 
  }; 
> var call = lightning.openChannel(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "chan_pending": <PendingUpdate>,
    "chan_open": <ChannelOpenUpdate>,
    "psbt_fund": <ReadyForPsbtFunding>,
    "pending_chan_id": <bytes>,
}
```

### gRPC Request: [lnrpc.OpenChannelRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1808)


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node to open a channel with. When using REST, this field must be encoded as base64. 
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
local_funding_amount | int64 | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | The number of satoshis to push to the remote side as part of the initial / commitment state 
target_conf | int32 | The target number of blocks that the funding transaction should be / confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / funding transaction. 
private | bool | Whether this channel should be private, not announced to the greater / network. 
min_htlc_msat | int64 | The minimum value in millisatoshi we will require for incoming HTLCs on / the channel. 
remote_csv_delay | uint32 | The delay we require on the remote's commitment transaction. If this is / not set, it will be scaled automatically with the channel size. 
min_confs | int32 | The minimum number of confirmations each one of your outputs used for / the funding transaction must satisfy. 
spend_unconfirmed | bool | Whether unconfirmed outputs should be used as inputs for the funding / transaction. 
close_address | string | Close address is an optional address which specifies the address to which funds should be paid out to upon cooperative close. This field may only be set if the peer supports the option upfront feature bit (call listpeers to check). The remote peer will only accept cooperative closes to this address if it is set.  Note: If this value is set on channel creation, you will *not* be able to cooperatively close out to a different address. 
funding_shim | [FundingShim](#fundingshim) | Funding shims are an optional argument that allow the caller to intercept certain funding functionality. For example, a shim can be provided to use a particular key for the commitment key (ideally cold) rather than use one that is generated by the wallet as normal, or signal that signing will be carried out in an interactive manner (PSBT based).  
### gRPC Response: [lnrpc.OpenStatusUpdate (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1877)


Parameter | Type | Description
--------- | ---- | ----------- 
chan_pending | [PendingUpdate](#pendingupdate) | Signals that the channel is now fully negotiated and the funding transaction published. 
chan_open | [ChannelOpenUpdate](#channelopenupdate) | Signals that the channel's funding transaction has now reached the required number of confirmations on chain and can be used. 
psbt_fund | [ReadyForPsbtFunding](#readyforpsbtfunding) | Signals that the funding process has been suspended and the construction of a PSBT that funds the channel PK script is now required. 
pending_chan_id | bytes | The pending channel ID of the created channel. This value may be used to further the funding flow manually via the FundingStateStep method.  

# Lightning.OpenChannelSync


### Simple RPC


OpenChannelSync is a synchronous version of the OpenChannel RPC call. This call is meant to be consumed by clients to the REST proxy. As with all other sync calls, all byte slices are intended to be populated as hex encoded strings.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.OpenChannelRequest(
        node_pubkey=<bytes>,
        node_pubkey_string=<string>,
        local_funding_amount=<int64>,
        push_sat=<int64>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
        private=<bool>,
        min_htlc_msat=<int64>,
        remote_csv_delay=<uint32>,
        min_confs=<int32>,
        spend_unconfirmed=<bool>,
        close_address=<string>,
        funding_shim=<FundingShim>,
    )
>>> response = stub.OpenChannelSync(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "funding_txid_bytes": <bytes>,
    "funding_txid_str": <string>,
    "output_index": <uint32>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    node_pubkey: <bytes>, 
    node_pubkey_string: <string>, 
    local_funding_amount: <int64>, 
    push_sat: <int64>, 
    target_conf: <int32>, 
    sat_per_byte: <int64>, 
    private: <bool>, 
    min_htlc_msat: <int64>, 
    remote_csv_delay: <uint32>, 
    min_confs: <int32>, 
    spend_unconfirmed: <bool>, 
    close_address: <string>, 
    funding_shim: <FundingShim>, 
  }; 
> lightning.openChannelSync(request, function(err, response) {
    console.log(response);
  })
{ 
    "funding_txid_bytes": <bytes>,
    "funding_txid_str": <string>,
    "output_index": <uint32>,
}
```

### gRPC Request: [lnrpc.OpenChannelRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1808)


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node to open a channel with. When using REST, this field must be encoded as base64. 
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
local_funding_amount | int64 | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | The number of satoshis to push to the remote side as part of the initial / commitment state 
target_conf | int32 | The target number of blocks that the funding transaction should be / confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / funding transaction. 
private | bool | Whether this channel should be private, not announced to the greater / network. 
min_htlc_msat | int64 | The minimum value in millisatoshi we will require for incoming HTLCs on / the channel. 
remote_csv_delay | uint32 | The delay we require on the remote's commitment transaction. If this is / not set, it will be scaled automatically with the channel size. 
min_confs | int32 | The minimum number of confirmations each one of your outputs used for / the funding transaction must satisfy. 
spend_unconfirmed | bool | Whether unconfirmed outputs should be used as inputs for the funding / transaction. 
close_address | string | Close address is an optional address which specifies the address to which funds should be paid out to upon cooperative close. This field may only be set if the peer supports the option upfront feature bit (call listpeers to check). The remote peer will only accept cooperative closes to this address if it is set.  Note: If this value is set on channel creation, you will *not* be able to cooperatively close out to a different address. 
funding_shim | [FundingShim](#fundingshim) | Funding shims are an optional argument that allow the caller to intercept certain funding functionality. For example, a shim can be provided to use a particular key for the commitment key (ideally cold) rather than use one that is generated by the wallet as normal, or signal that signing will be carried out in an interactive manner (PSBT based).  
### gRPC Response: [lnrpc.ChannelPoint ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1110)


Parameter | Type | Description
--------- | ---- | ----------- 
funding_txid_bytes | bytes | Txid of the funding transaction. When using REST, this field must be encoded as base64. 
funding_txid_str | string | Hex-encoded string representing the byte-reversed hash of the funding transaction. 
output_index | uint32 | The index of the output of the funding transaction  

# Lightning.PendingChannels


### Simple RPC


PendingChannels returns a list of all the channels that are currently considered "pending". A channel is pending if it has finished the funding workflow and is waiting for confirmations for the funding txn, or is in the process of closure, either initiated cooperatively or non-cooperatively.

```shell

# Display information pertaining to pending channels.

$ lncli pendingchannels [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.PendingChannelsRequest()
>>> response = stub.PendingChannels(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "total_limbo_balance": <int64>,
    "pending_open_channels": <array PendingOpenChannel>,
    "pending_closing_channels": <array ClosedChannel>,
    "pending_force_closing_channels": <array ForceClosedChannel>,
    "waiting_close_channels": <array WaitingCloseChannel>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.pendingChannels(request, function(err, response) {
    console.log(response);
  })
{ 
    "total_limbo_balance": <int64>,
    "pending_open_channels": <array PendingOpenChannel>,
    "pending_closing_channels": <array ClosedChannel>,
    "pending_force_closing_channels": <array ForceClosedChannel>,
    "waiting_close_channels": <array WaitingCloseChannel>,
}
```

### gRPC Request: [lnrpc.PendingChannelsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2074)


This request has no parameters.

### gRPC Response: [lnrpc.PendingChannelsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2076)


Parameter | Type | Description
--------- | ---- | ----------- 
total_limbo_balance | int64 | The balance in satoshis encumbered in pending channels 
pending_open_channels | [array PendingOpenChannel](#pendingopenchannel) | Channels pending opening 
pending_closing_channels | [array ClosedChannel](#closedchannel) | Deprecated: Channels pending closing previously contained cooperatively closed channels with a single confirmation. These channels are now considered closed from the time we see them on chain. 
pending_force_closing_channels | [array ForceClosedChannel](#forceclosedchannel) | Channels pending force closing 
waiting_close_channels | [array WaitingCloseChannel](#waitingclosechannel) | Channels waiting for closing tx to confirm  

# Lightning.QueryRoutes


### Simple RPC


QueryRoutes attempts to query the daemon's Channel Router for a possible route to a target destination capable of carrying a specific amount of satoshis. The returned route contains the full details required to craft and send an HTLC, also including the necessary information that should be present within the Sphinx packet encapsulated within the HTLC.

```shell

# Queries the channel router for a potential path to the destination that has sufficient flow for the amount including fees

$ lncli queryroutes [command options] dest amt

# --dest value               the 33-byte hex-encoded public key for the payment destination
# --amt value                the amount to send expressed in satoshis (default: 0)
# --fee_limit value          maximum fee allowed in satoshis when sending the payment (default: 0)
# --fee_limit_percent value  percentage of the payment's amount used as the maximum fee allowed when sending the payment (default: 0)
# --final_cltv_delta value   (optional) number of blocks the last hop has to reveal the preimage (default: 0)
# --use_mc                   use mission control probabilities
# --cltv_limit value         the maximum time lock that may be used for this payment (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.QueryRoutesRequest(
        pub_key=<string>,
        amt=<int64>,
        amt_msat=<int64>,
        final_cltv_delta=<int32>,
        fee_limit=<FeeLimit>,
        ignored_nodes=<array bytes>,
        ignored_edges=<array EdgeLocator>,
        source_pub_key=<string>,
        use_mission_control=<bool>,
        ignored_pairs=<array NodePair>,
        cltv_limit=<uint32>,
        dest_custom_records=<array DestCustomRecordsEntry>,
        outgoing_chan_id=<uint64>,
        last_hop_pubkey=<bytes>,
        route_hints=<array RouteHint>,
        dest_features=<array FeatureBit>,
    )
>>> response = stub.QueryRoutes(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "routes": <array Route>,
    "success_prob": <double>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pub_key: <string>, 
    amt: <int64>, 
    amt_msat: <int64>, 
    final_cltv_delta: <int32>, 
    fee_limit: <FeeLimit>, 
    ignored_nodes: <array bytes>, 
    ignored_edges: <array EdgeLocator>, 
    source_pub_key: <string>, 
    use_mission_control: <bool>, 
    ignored_pairs: <array NodePair>, 
    cltv_limit: <uint32>, 
    dest_custom_records: <array DestCustomRecordsEntry>, 
    outgoing_chan_id: <uint64>, 
    last_hop_pubkey: <bytes>, 
    route_hints: <array RouteHint>, 
    dest_features: <array FeatureBit>, 
  }; 
> lightning.queryRoutes(request, function(err, response) {
    console.log(response);
  })
{ 
    "routes": <array Route>,
    "success_prob": <double>,
}
```

### gRPC Request: [lnrpc.QueryRoutesRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2281)


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded public key for the payment destination 
amt | int64 | The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive. 
final_cltv_delta | int32 | An optional CLTV delta from the current height that should be used for the timelock of the final hop. Note that unlike SendPayment, QueryRoutes does not add any additional block padding on top of final_ctlv_delta. This padding of a few blocks needs to be added manually or otherwise failures may happen when a block comes in while the payment is in flight. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment. 
ignored_nodes | array bytes | A list of nodes to ignore during path finding. When using REST, these fields must be encoded as base64. 
ignored_edges | [array EdgeLocator](#edgelocator) | Deprecated. A list of edges to ignore during path finding. 
source_pub_key | string | The source node where the request route should originated from. If empty, self is assumed. 
use_mission_control | bool | If set to true, edge probabilities from mission control will be used to get the optimal route. 
ignored_pairs | [array NodePair](#nodepair) | A list of directed node pairs that will be ignored during path finding. 
cltv_limit | uint32 | An optional maximum total time lock for the route. If the source is empty or ourselves, this should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is used as the limit. 
dest_custom_records | [array DestCustomRecordsEntry](#destcustomrecordsentry) | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. If the destination does not support the specified recrods, and error will be returned. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
route_hints | [array RouteHint](#routehint) | Optional route hints to reach the destination through private channels. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  
### gRPC Response: [lnrpc.QueryRoutesResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2416)


Parameter | Type | Description
--------- | ---- | ----------- 
routes | [array Route](#route) | The route that results from the path finding operation. This is still a repeated field to retain backwards compatibility. 
success_prob | double | The success probability of the returned route based on the current mission control state. [EXPERIMENTAL]  

# Lightning.RestoreChannelBackups


### Simple RPC


RestoreChannelBackups accepts a set of singular channel backups, or a single encrypted multi-chan backup and attempts to recover any funds remaining within the channel. If we are able to unpack the backup, then the new channel will be shown under listchannels, as well as pending channels.

```shell

# Allows a user to restore a Static Channel Backup (SCB) that was
# obtained either via the exportchanbackup command, or from lnd's
# automatically manged channels.backup file. This command should be used
# if a user is attempting to restore a channel due to data loss on a
# running node restored with the same seed as the node that created the
# channel. If successful, this command will allows the user to recover
# the settled funds stored in the recovered channels.
# The command will accept backups in one of three forms:
# * A single channel packed SCB, which can be obtained from
# exportchanbackup. This should be passed in hex encoded format.
# * A packed multi-channel SCB, which couples several individual
# static channel backups in single blob.
# * A file path which points to a packed multi-channel backup within a
# file, using the same format that lnd does in its channels.backup
# file.

$ lncli restorechanbackup [command options] [--single_backup] [--multi_backup] [--multi_file=

# --single_backup value  a hex encoded single channel backup obtained from exportchanbackup
# --multi_backup value   a hex encoded multi-channel backup obtained from exportchanbackup
# --multi_file value     the path to a multi-channel back up file
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.RestoreChanBackupRequest(
        chan_backups=<ChannelBackups>,
        multi_chan_backup=<bytes>,
    )
>>> response = stub.RestoreChannelBackups(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    chan_backups: <ChannelBackups>, 
    multi_chan_backup: <bytes>, 
  }; 
> lightning.restoreChannelBackups(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.RestoreChanBackupRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3449)


Parameter | Type | Description
--------- | ---- | ----------- 
chan_backups | [ChannelBackups](#channelbackups) | The channels to restore as a list of channel/backup pairs. 
multi_chan_backup | bytes | The channels to restore in the packed multi backup format. When using REST, this field must be encoded as base64.  
### gRPC Response: [lnrpc.RestoreBackupResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3463)


This response has no parameters.


# Lightning.SendCoins


### Simple RPC


SendCoins executes a request to send coins to a particular address. Unlike SendMany, this RPC call only allows creating a single output at a time. If neither target_conf, or sat_per_byte are set, then the internal wallet will consult its fee model to determine a fee for the default confirmation target.

```shell

# Send amt coins in satoshis to the base58 or bech32 encoded bitcoin address addr.
# Fees used when sending the transaction can be specified via the --conf_target, or
# --sat_per_byte optional flags.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli sendcoins [command options] addr amt

# --addr value          the base58 or bech32 encoded bitcoin address to send coins to on-chain
# --sweepall            if set, then the amount field will be ignored, and all the wallet will attempt to sweep all outputs within the wallet to the target address
# --amt value           the number of bitcoin denominated in satoshis to send (default: 0)
# --conf_target value   (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value  (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.SendCoinsRequest(
        addr=<string>,
        amount=<int64>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
        send_all=<bool>,
    )
>>> response = stub.SendCoins(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "txid": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    addr: <string>, 
    amount: <int64>, 
    target_conf: <int32>, 
    sat_per_byte: <int64>, 
    send_all: <bool>, 
  }; 
> lightning.sendCoins(request, function(err, response) {
    console.log(response);
  })
{ 
    "txid": <string>,
}
```

### gRPC Request: [lnrpc.SendCoinsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1183)


Parameter | Type | Description
--------- | ---- | ----------- 
addr | string | The address to send coins to 
amount | int64 | The amount in satoshis to send 
target_conf | int32 | The target number of blocks that this transaction should be confirmed / by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / transaction. 
send_all | bool | If set, then the amount field will be ignored, and lnd will attempt to send all the coins under control of the internal wallet to the specified address.  
### gRPC Response: [lnrpc.SendCoinsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1205)


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The transaction ID of the transaction  

# Lightning.SendMany


### Simple RPC


SendMany handles a request for a transaction that creates multiple specified outputs in parallel. If neither target_conf, or sat_per_byte are set, then the internal wallet will consult its fee model to determine a fee for the default confirmation target.

```shell

# Create and broadcast a transaction paying the specified amount(s) to the passed address(es).
# The send-json-string' param decodes addresses and the amount to send
# respectively in the following format:
# '{"ExampleAddr": NumCoinsInSatoshis, "SecondAddr": NumCoins}'

$ lncli sendmany [command options] send-json-string [--conf_target=N] [--sat_per_byte=P]

# --conf_target value   (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value  (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.SendManyRequest(
        AddrToAmount=<array AddrToAmountEntry>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
    )
>>> response = stub.SendMany(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "txid": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    AddrToAmount: <array AddrToAmountEntry>, 
    target_conf: <int32>, 
    sat_per_byte: <int64>, 
  }; 
> lightning.sendMany(request, function(err, response) {
    console.log(response);
  })
{ 
    "txid": <string>,
}
```

### gRPC Request: [lnrpc.SendManyRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1166)


Parameter | Type | Description
--------- | ---- | ----------- 
AddrToAmount | [array AddrToAmountEntry](#addrtoamountentry) | The map from addresses to amounts 
target_conf | int32 | The target number of blocks that this transaction should be confirmed / by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / transaction.  
### gRPC Response: [lnrpc.SendManyResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1178)


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The id of the transaction  

# Lightning.SendPayment


### Bidirectional-streaming RPC


Deprecated, use routerrpc.SendPayment. SendPayment dispatches a bi-directional streaming RPC for sending payments through the Lightning Network. A single RPC invocation creates a persistent bi-directional stream allowing clients to rapidly send payments through the Lightning Network with a single persistent connection.

```shell

# Send a payment over Lightning. One can either specify the full
# parameters of the payment, or just use a payment request which encodes
# all the payment details.
# If payment isn't manually specified, then only a payment request needs
# to be passed using the --pay_req argument.
# If the payment *is* manually specified, then all four alternative
# arguments need to be specified in order to complete the payment:
# * --dest=N
# * --amt=A
# * --final_cltv_delta=T
# * --payment_hash=H

$ lncli sendpayment [command options] dest amt payment_hash final_cltv_delta | --pay_req=[payment request]

# --pay_req value                 a zpay32 encoded payment request to fulfill
# --fee_limit value               maximum fee allowed in satoshis when sending the payment (default: 0)
# --fee_limit_percent value       percentage of the payment's amount used as the maximum fee allowed when sending the payment (default: 0)
# --cltv_limit value              the maximum time lock that may be used for this payment (default: 0)
# --last_hop value                pubkey of the last hop (penultimate node in the path) to route through for this payment
# --outgoing_chan_id value        short channel id of the outgoing channel to use for the first hop of the payment (default: 0)
# --force, -f                     will skip payment request confirmation
# --allow_self_payment            allow sending a circular payment to self
# --data value                    attach custom data to the payment. The required format is: <record_id>=<hex_value>,<record_id>=<hex_value>,.. For example: --data 3438382=0a21ff. Custom record ids start from 65536.
# --dest value, -d value          the compressed identity pubkey of the payment recipient
# --amt value, -a value           number of satoshis to send (default: 0)
# --payment_hash value, -r value  the hash to use within the payment's HTLC
# --final_cltv_delta value        the number of blocks the last hop has to reveal the preimage (default: 0)
# --keysend                       will generate a pre-image and encode it in the sphinx packet, a dest must be set [experimental]
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
# Define a generator that returns an Iterable of lnrpc.SendRequest objects.
>>> def request_generator():
        # Initialization code here.
        while True:
            # Parameters here can be set as arguments to the generator.
            request = ln.lnrpc.SendRequest(
                dest=<bytes>,
                dest_string=<string>,
                amt=<int64>,
                amt_msat=<int64>,
                payment_hash=<bytes>,
                payment_hash_string=<string>,
                payment_request=<string>,
                final_cltv_delta=<int32>,
                fee_limit=<FeeLimit>,
                outgoing_chan_id=<uint64>,
                last_hop_pubkey=<bytes>,
                cltv_limit=<uint32>,
                dest_custom_records=<array DestCustomRecordsEntry>,
                allow_self_payment=<bool>,
                dest_features=<array FeatureBit>,
            )
            yield request
            # Do things between iterations here.
>>> request_iterable = request_generator()
>>> for response in stub.SendPayment(request_iterable, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    dest: <bytes>, 
    dest_string: <string>, 
    amt: <int64>, 
    amt_msat: <int64>, 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    payment_request: <string>, 
    final_cltv_delta: <int32>, 
    fee_limit: <FeeLimit>, 
    outgoing_chan_id: <uint64>, 
    last_hop_pubkey: <bytes>, 
    cltv_limit: <uint32>, 
    dest_custom_records: <array DestCustomRecordsEntry>, 
    allow_self_payment: <bool>, 
    dest_features: <array FeatureBit>, 
  }; 
> var call = lightning.sendPayment({})
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
> call.write(request)

{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```

### gRPC Request: [lnrpc.SendRequest (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L927)


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient. When using REST, this field must be encoded as base64. 
dest_string | string | The hex-encoded identity pubkey of the payment recipient. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
amt | int64 | The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive. 
payment_hash | bytes | The hash to use within the payment's HTLC. When using REST, this field must be encoded as base64. 
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
cltv_limit | uint32 | An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced. 
dest_custom_records | [array DestCustomRecordsEntry](#destcustomrecordsentry) | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
allow_self_payment | bool | If set, circular payments to self are permitted. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  
### gRPC Response: [lnrpc.SendResponse (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1027)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |  
payment_hash | bytes |   

# Lightning.SendPaymentSync


### Simple RPC


SendPaymentSync is the synchronous non-streaming version of SendPayment. This RPC is intended to be consumed by clients of the REST proxy. Additionally, this RPC expects the destination's public key and the payment hash (if any) to be encoded as hex strings.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.SendRequest(
        dest=<bytes>,
        dest_string=<string>,
        amt=<int64>,
        amt_msat=<int64>,
        payment_hash=<bytes>,
        payment_hash_string=<string>,
        payment_request=<string>,
        final_cltv_delta=<int32>,
        fee_limit=<FeeLimit>,
        outgoing_chan_id=<uint64>,
        last_hop_pubkey=<bytes>,
        cltv_limit=<uint32>,
        dest_custom_records=<array DestCustomRecordsEntry>,
        allow_self_payment=<bool>,
        dest_features=<array FeatureBit>,
    )
>>> response = stub.SendPaymentSync(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    dest: <bytes>, 
    dest_string: <string>, 
    amt: <int64>, 
    amt_msat: <int64>, 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    payment_request: <string>, 
    final_cltv_delta: <int32>, 
    fee_limit: <FeeLimit>, 
    outgoing_chan_id: <uint64>, 
    last_hop_pubkey: <bytes>, 
    cltv_limit: <uint32>, 
    dest_custom_records: <array DestCustomRecordsEntry>, 
    allow_self_payment: <bool>, 
    dest_features: <array FeatureBit>, 
  }; 
> lightning.sendPaymentSync(request, function(err, response) {
    console.log(response);
  })
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```

### gRPC Request: [lnrpc.SendRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L927)


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient. When using REST, this field must be encoded as base64. 
dest_string | string | The hex-encoded identity pubkey of the payment recipient. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
amt | int64 | The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive. 
payment_hash | bytes | The hash to use within the payment's HTLC. When using REST, this field must be encoded as base64. 
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
cltv_limit | uint32 | An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced. 
dest_custom_records | [array DestCustomRecordsEntry](#destcustomrecordsentry) | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
allow_self_payment | bool | If set, circular payments to self are permitted. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  
### gRPC Response: [lnrpc.SendResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1027)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |  
payment_hash | bytes |   

# Lightning.SendToRoute


### Bidirectional-streaming RPC


SendToRoute is a bi-directional streaming RPC for sending payment through the Lightning Network. This method differs from SendPayment in that it allows users to specify a full route manually. This can be used for things like rebalancing, and atomic swaps.

```shell

# Send a payment over Lightning using a specific route. One must specify
# the route to attempt and the payment hash. This command can even
# be chained with the response to queryroutes or buildroute. This command
# can be used to implement channel rebalancing by crafting a self-route,
# or even atomic swaps using a self-route that crosses multiple chains.
# There are three ways to specify a route:
# * using the --routes parameter to manually specify a JSON encoded
# route in the format of the return value of queryroutes or
# buildroute:
# (lncli sendtoroute --payment_hash=<pay_hash> --routes=<route>)
# * passing the route as a positional argument:
# (lncli sendtoroute --payment_hash=pay_hash <route>)
# * or reading in the route from stdin, which can allow chaining the
# response from queryroutes or buildroute, or even read in a file
# with a pre-computed route:
# (lncli queryroutes --args.. | lncli sendtoroute --payment_hash= -
# notice the '-' at the end, which signals that lncli should read
# the route in from stdin

$ lncli sendtoroute [command options] [arguments...]

# --payment_hash value, --pay_hash value  the hash to use within the payment's HTLC
# --routes value, -r value                a json array string in the format of the response of queryroutes that denotes which routes to use
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
# Define a generator that returns an Iterable of lnrpc.SendToRouteRequest objects.
>>> def request_generator():
        # Initialization code here.
        while True:
            # Parameters here can be set as arguments to the generator.
            request = ln.lnrpc.SendToRouteRequest(
                payment_hash=<bytes>,
                payment_hash_string=<string>,
                route=<Route>,
            )
            yield request
            # Do things between iterations here.
>>> request_iterable = request_generator()
>>> for response in stub.SendToRoute(request_iterable, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    route: <Route>, 
  }; 
> var call = lightning.sendToRoute({})
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
> call.write(request)

{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```

### gRPC Request: [lnrpc.SendToRouteRequest (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1034)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. When using REST, this field must be encoded as base64. 
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
route | [Route](#route) | Route that should be used to attempt to complete the payment.  
### gRPC Response: [lnrpc.SendResponse (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1027)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |  
payment_hash | bytes |   

# Lightning.SendToRouteSync


### Simple RPC


SendToRouteSync is a synchronous version of SendToRoute. It Will block until the payment either fails or succeeds.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.SendToRouteRequest(
        payment_hash=<bytes>,
        payment_hash_string=<string>,
        route=<Route>,
    )
>>> response = stub.SendToRouteSync(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    route: <Route>, 
  }; 
> lightning.sendToRouteSync(request, function(err, response) {
    console.log(response);
  })
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
    "payment_hash": <bytes>,
}
```

### gRPC Request: [lnrpc.SendToRouteRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1034)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. When using REST, this field must be encoded as base64. 
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
route | [Route](#route) | Route that should be used to attempt to complete the payment.  
### gRPC Response: [lnrpc.SendResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1027)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |  
payment_hash | bytes |   

# Lightning.SignMessage


### Simple RPC


SignMessage signs a message with this node's private key. The returned signature string is `zbase32` encoded and pubkey recoverable, meaning that only the message digest and signature are needed for verification.

```shell

# Sign msg with the resident node's private key.
# Returns the signature as a zbase32 string.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli signmessage [command options] msg

# --msg value  the message to sign
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.SignMessageRequest(
        msg=<bytes>,
    )
>>> response = stub.SignMessage(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "signature": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    msg: <bytes>, 
  }; 
> lightning.signMessage(request, function(err, response) {
    console.log(response);
  })
{ 
    "signature": <string>,
}
```

### gRPC Request: [lnrpc.SignMessageRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1244)


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message to be signed. When using REST, this field must be encoded as base64.  
### gRPC Response: [lnrpc.SignMessageResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1251)


Parameter | Type | Description
--------- | ---- | ----------- 
signature | string | The signature for the given message  

# Lightning.StopDaemon


### Simple RPC


StopDaemon will send a shutdown request to the interrupt handler, triggering a graceful shutdown of the daemon.

```shell

# Gracefully stop all daemon subsystems before stopping the daemon itself.
# This is equivalent to stopping it using CTRL-C.

$ lncli stop [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.StopRequest()
>>> response = stub.StopDaemon(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.stopDaemon(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.StopRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2703)


This request has no parameters.

### gRPC Response: [lnrpc.StopResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2705)


This response has no parameters.


# Lightning.SubscribeChannelBackups


### Response-streaming RPC


SubscribeChannelBackups allows a client to sub-subscribe to the most up to date information concerning the state of all channel backups. Each time a new channel is added, we return the new set of channels, along with a multi-chan backup containing the backup info for all channels. Each time a channel is closed, we send a new update, which contains new new chan back ups, but the updated set of encrypted multi-chan backups with the closed channel(s) removed.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChannelBackupSubscription()
>>> for response in stub.SubscribeChannelBackups(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "single_chan_backups": <ChannelBackups>,
    "multi_chan_backup": <MultiChanBackup>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> var call = lightning.subscribeChannelBackups(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "single_chan_backups": <ChannelBackups>,
    "multi_chan_backup": <MultiChanBackup>,
}
```

### gRPC Request: [lnrpc.ChannelBackupSubscription ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3466)


This request has no parameters.

### gRPC Response: [lnrpc.ChanBackupSnapshot (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3428)


Parameter | Type | Description
--------- | ---- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) | The set of new channels that have been added since the last channel backup snapshot was requested. 
multi_chan_backup | [MultiChanBackup](#multichanbackup) | A multi-channel backup that covers all open channels currently known to lnd.  

# Lightning.SubscribeChannelEvents


### Response-streaming RPC


SubscribeChannelEvents creates a uni-directional stream from the server to the client in which any updates relevant to the state of the channels are sent over. Events include new active channels, inactive channels, and closed channels.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChannelEventSubscription()
>>> for response in stub.SubscribeChannelEvents(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "open_channel": <Channel>,
    "closed_channel": <ChannelCloseSummary>,
    "active_channel": <ChannelPoint>,
    "inactive_channel": <ChannelPoint>,
    "pending_open_channel": <PendingUpdate>,
    "type": <UpdateType>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> var call = lightning.subscribeChannelEvents(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "open_channel": <Channel>,
    "closed_channel": <ChannelCloseSummary>,
    "active_channel": <ChannelPoint>,
    "inactive_channel": <ChannelPoint>,
    "pending_open_channel": <PendingUpdate>,
    "type": <UpdateType>,
}
```

### gRPC Request: [lnrpc.ChannelEventSubscription ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2235)


This request has no parameters.

### gRPC Response: [lnrpc.ChannelEventUpdate (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2238)


Parameter | Type | Description
--------- | ---- | ----------- 
open_channel | [Channel](#channel) |  
closed_channel | [ChannelCloseSummary](#channelclosesummary) |  
active_channel | [ChannelPoint](#channelpoint) |  
inactive_channel | [ChannelPoint](#channelpoint) |  
pending_open_channel | [PendingUpdate](#pendingupdate) |  
type | [UpdateType](#updatetype) |   

# Lightning.SubscribeChannelGraph


### Response-streaming RPC


SubscribeChannelGraph launches a streaming RPC that allows the caller to receive notifications upon any changes to the channel graph topology from the point of view of the responding node. Events notified include: new nodes coming online, nodes updating their authenticated attributes, new channels being advertised, updates in the routing policy for a directional channel edge, and when channels are closed on-chain.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.GraphTopologySubscription()
>>> for response in stub.SubscribeChannelGraph(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "node_updates": <array NodeUpdate>,
    "channel_updates": <array ChannelEdgeUpdate>,
    "closed_chans": <array ClosedChannelUpdate>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> var call = lightning.subscribeChannelGraph(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "node_updates": <array NodeUpdate>,
    "channel_updates": <array ChannelEdgeUpdate>,
    "closed_chans": <array ClosedChannelUpdate>,
}
```

### gRPC Request: [lnrpc.GraphTopologySubscription ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2708)


This request has no parameters.

### gRPC Response: [lnrpc.GraphTopologyUpdate (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2710)


Parameter | Type | Description
--------- | ---- | ----------- 
node_updates | [array NodeUpdate](#nodeupdate) |  
channel_updates | [array ChannelEdgeUpdate](#channeledgeupdate) |  
closed_chans | [array ClosedChannelUpdate](#closedchannelupdate) |   

# Lightning.SubscribeInvoices


### Response-streaming RPC


SubscribeInvoices returns a uni-directional stream (server -> client) for notifying the client of newly added/settled invoices. The caller can optionally specify the add_index and/or the settle_index. If the add_index is specified, then we'll first start by sending add invoice events for all invoices with an add_index greater than the specified value. If the settle_index is specified, the next, we'll send out all settle events for invoices with a settle_index greater than the specified value. One or both of these fields can be set. If no fields are set, then we'll only send out the latest add/settle events.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.InvoiceSubscription(
        add_index=<uint64>,
        settle_index=<uint64>,
    )
>>> for response in stub.SubscribeInvoices(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "memo": <string>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
    "value_msat": <int64>,
    "settled": <bool>,
    "creation_date": <int64>,
    "settle_date": <int64>,
    "payment_request": <string>,
    "description_hash": <bytes>,
    "expiry": <int64>,
    "fallback_addr": <string>,
    "cltv_expiry": <uint64>,
    "route_hints": <array RouteHint>,
    "private": <bool>,
    "add_index": <uint64>,
    "settle_index": <uint64>,
    "amt_paid": <int64>,
    "amt_paid_sat": <int64>,
    "amt_paid_msat": <int64>,
    "state": <InvoiceState>,
    "htlcs": <array InvoiceHTLC>,
    "features": <array FeaturesEntry>,
    "is_keysend": <bool>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    add_index: <uint64>, 
    settle_index: <uint64>, 
  }; 
> var call = lightning.subscribeInvoices(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "memo": <string>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
    "value_msat": <int64>,
    "settled": <bool>,
    "creation_date": <int64>,
    "settle_date": <int64>,
    "payment_request": <string>,
    "description_hash": <bytes>,
    "expiry": <int64>,
    "fallback_addr": <string>,
    "cltv_expiry": <uint64>,
    "route_hints": <array RouteHint>,
    "private": <bool>,
    "add_index": <uint64>,
    "settle_index": <uint64>,
    "amt_paid": <int64>,
    "amt_paid_sat": <int64>,
    "amt_paid_msat": <int64>,
    "state": <InvoiceState>,
    "htlcs": <array InvoiceHTLC>,
    "features": <array FeaturesEntry>,
    "is_keysend": <bool>,
}
```

### gRPC Request: [lnrpc.InvoiceSubscription ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3038)


Parameter | Type | Description
--------- | ---- | ----------- 
add_index | uint64 | If specified (non-zero), then we'll first start by sending out notifications for all added indexes with an add_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC. 
settle_index | uint64 | If specified (non-zero), then we'll first start by sending out notifications for all settled indexes with an settle_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC.  
### gRPC Response: [lnrpc.Invoice (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2779)


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage. When using REST, this field must be encoded as base64. 
r_hash | bytes | The hash of the preimage. When using REST, this field must be encoded as base64. 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. When using REST, this field must be encoded as base64. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | uint64 | The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | int64 | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | int64 | The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | int64 | The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceState](#invoicestate) | The state the invoice is in. 
htlcs | [array InvoiceHTLC](#invoicehtlc) | List of HTLCs paying to this invoice [EXPERIMENTAL]. 
features | [array FeaturesEntry](#featuresentry) | List of features advertised on the invoice. 
is_keysend | bool | Indicates if this invoice was a spontaneous payment that arrived via keysend [EXPERIMENTAL].  

# Lightning.SubscribePeerEvents


### Response-streaming RPC


SubscribePeerEvents creates a uni-directional stream from the server to the client in which any events relevant to the state of peers are sent over. Events include peers going online and offline.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.PeerEventSubscription()
>>> for response in stub.SubscribePeerEvents(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "pub_key": <string>,
    "type": <EventType>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> var call = lightning.subscribePeerEvents(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "pub_key": <string>,
    "type": <EventType>,
}
```

### gRPC Request: [lnrpc.PeerEventSubscription ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1642)


This request has no parameters.

### gRPC Response: [lnrpc.PeerEvent (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1645)


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The identity pubkey of the peer. 
type | [EventType](#eventtype) |   

# Lightning.SubscribeTransactions


### Response-streaming RPC


SubscribeTransactions creates a uni-directional stream from the server to the client in which any newly discovered transactions relevant to the wallet are sent over.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.GetTransactionsRequest()
>>> for response in stub.SubscribeTransactions(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "tx_hash": <string>,
    "amount": <int64>,
    "num_confirmations": <int32>,
    "block_hash": <string>,
    "block_height": <int32>,
    "time_stamp": <int64>,
    "total_fees": <int64>,
    "dest_addresses": <array string>,
    "raw_tx_hex": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> var call = lightning.subscribeTransactions(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "tx_hash": <string>,
    "amount": <int64>,
    "num_confirmations": <int32>,
    "block_hash": <string>,
    "block_height": <int32>,
    "time_stamp": <int64>,
    "total_fees": <int64>,
    "dest_addresses": <array string>,
    "raw_tx_hex": <string>,
}
```

### gRPC Request: [lnrpc.GetTransactionsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L899)


This request has no parameters.

### gRPC Response: [lnrpc.Transaction (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L871)


Parameter | Type | Description
--------- | ---- | ----------- 
tx_hash | string | The transaction hash 
amount | int64 | The transaction amount, denominated in satoshis 
num_confirmations | int32 | The number of confirmations 
block_hash | string | The hash of the block this transaction was included in 
block_height | int32 | The height of the block this transaction was included in 
time_stamp | int64 | Timestamp of this transaction 
total_fees | int64 | Fees paid for this transaction 
dest_addresses | array string | Addresses that received funds for this transaction 
raw_tx_hex | string | The raw transaction hex.  

# Lightning.UpdateChannelPolicy


### Simple RPC


UpdateChannelPolicy allows the caller to update the fee schedule and channel policies for all channels globally, or a particular channel.

```shell

# Updates the channel policy for all channels, or just a particular channel
# identified by its channel point. The update will be committed, and
# broadcast to the rest of the network within the next batch.
# Channel points are encoded as: funding_txid:output_index

$ lncli updatechanpolicy [command options] base_fee_msat fee_rate time_lock_delta [--max_htlc_msat=N] [channel_point]

# --base_fee_msat value    the base fee in milli-satoshis that will be charged for each forwarded HTLC, regardless of payment size (default: 0)
# --fee_rate value         the fee rate that will be charged proportionally based on the value of each forwarded HTLC, the lowest possible rate is 0 with a granularity of 0.000001 (millionths)
# --time_lock_delta value  the CLTV delta that will be applied to all forwarded HTLCs (default: 0)
# --min_htlc_msat value    if set, the min HTLC size that will be applied to all forwarded HTLCs. If unset, the min HTLC is left unchanged. (default: 0)
# --max_htlc_msat value    if set, the max HTLC size that will be applied to all forwarded HTLCs. If unset, the max HTLC is left unchanged. (default: 0)
# --chan_point value       The channel whose fee policy should be updated, if nil the policies for all channels will be updated. Takes the form of: txid:output_index
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.PolicyUpdateRequest(
        global=<bool>,
        chan_point=<ChannelPoint>,
        base_fee_msat=<int64>,
        fee_rate=<double>,
        time_lock_delta=<uint32>,
        max_htlc_msat=<uint64>,
        min_htlc_msat=<uint64>,
        min_htlc_msat_specified=<bool>,
    )
>>> response = stub.UpdateChannelPolicy(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    global: <bool>, 
    chan_point: <ChannelPoint>, 
    base_fee_msat: <int64>, 
    fee_rate: <double>, 
    time_lock_delta: <uint32>, 
    max_htlc_msat: <uint64>, 
    min_htlc_msat: <uint64>, 
    min_htlc_msat_specified: <bool>, 
  }; 
> lightning.updateChannelPolicy(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.PolicyUpdateRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3291)


Parameter | Type | Description
--------- | ---- | ----------- 
global | bool | If set, then this update applies to all currently active channels. 
chan_point | [ChannelPoint](#channelpoint) | If set, this update will target a specific channel. 
base_fee_msat | int64 | The base fee charged regardless of the number of milli-satoshis sent. 
fee_rate | double | The effective fee rate in milli-satoshis. The precision of this value / goes up to 6 decimal places, so 1e-6. 
time_lock_delta | uint32 | The required timelock delta for HTLCs forwarded over the channel. 
max_htlc_msat | uint64 | If set, the maximum HTLC size in milli-satoshis. If unset, the maximum / HTLC will be unchanged. 
min_htlc_msat | uint64 | The minimum HTLC size in milli-satoshis. Only applied if / min_htlc_msat_specified is true. 
min_htlc_msat_specified | bool | If true, min_htlc_msat is applied.  
### gRPC Response: [lnrpc.PolicyUpdateResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3321)


This response has no parameters.


# Lightning.VerifyChanBackup


### Simple RPC


VerifyChanBackup allows a caller to verify the integrity of a channel backup snapshot. This method will accept either a packed Single or a packed Multi. Specifying both will result in an error.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.ChanBackupSnapshot(
        single_chan_backups=<ChannelBackups>,
        multi_chan_backup=<MultiChanBackup>,
    )
>>> response = stub.VerifyChanBackup(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    single_chan_backups: <ChannelBackups>, 
    multi_chan_backup: <MultiChanBackup>, 
  }; 
> lightning.verifyChanBackup(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.ChanBackupSnapshot ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3428)


Parameter | Type | Description
--------- | ---- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) | The set of new channels that have been added since the last channel backup snapshot was requested. 
multi_chan_backup | [MultiChanBackup](#multichanbackup) | A multi-channel backup that covers all open channels currently known to lnd.  
### gRPC Response: [lnrpc.VerifyChanBackupResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L3469)


This response has no parameters.


# Lightning.VerifyMessage


### Simple RPC


VerifyMessage verifies a signature over a msg. The signature must be zbase32 encoded and signed by an active node in the resident node's channel database. In addition to returning the validity of the signature, VerifyMessage also returns the recovered pubkey from the signature.

```shell

# Verify that the message was signed with a properly-formed signature
# The signature must be zbase32 encoded and signed with the private key of
# an active node in the resident node's channel database.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli verifymessage [command options] msg signature

# --msg value  the message to verify
# --sig value  the zbase32 encoded signature of the message
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.VerifyMessageRequest(
        msg=<bytes>,
        signature=<string>,
    )
>>> response = stub.VerifyMessage(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "valid": <bool>,
    "pubkey": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    msg: <bytes>, 
    signature: <string>, 
  }; 
> lightning.verifyMessage(request, function(err, response) {
    console.log(response);
  })
{ 
    "valid": <bool>,
    "pubkey": <string>,
}
```

### gRPC Request: [lnrpc.VerifyMessageRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1256)


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message over which the signature is to be verified. When using REST, this field must be encoded as base64. 
signature | string | The signature to be verified over the given message  
### gRPC Response: [lnrpc.VerifyMessageResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L1266)


Parameter | Type | Description
--------- | ---- | ----------- 
valid | bool | Whether the signature was valid over the given message 
pubkey | string | The pubkey recovered from the signature  

# Lightning.WalletBalance


### Simple RPC


WalletBalance returns total unspent outputs(confirmed and unconfirmed), all confirmed unspent outputs and all unconfirmed unspent outputs under control of the wallet.

```shell

# Compute and display the wallet's current balance.

$ lncli walletbalance [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.lnrpc.WalletBalanceRequest()
>>> response = stub.WalletBalance(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "total_balance": <int64>,
    "confirmed_balance": <int64>,
    "unconfirmed_balance": <int64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {}; 
> lightning.walletBalance(request, function(err, response) {
    console.log(response);
  })
{ 
    "total_balance": <int64>,
    "confirmed_balance": <int64>,
    "unconfirmed_balance": <int64>,
}
```

### gRPC Request: [lnrpc.WalletBalanceRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2258)


This request has no parameters.

### gRPC Response: [lnrpc.WalletBalanceResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L2260)


Parameter | Type | Description
--------- | ---- | ----------- 
total_balance | int64 | The balance of the wallet 
confirmed_balance | int64 | The confirmed balance of a wallet(with >= 1 confirmations) 
unconfirmed_balance | int64 | The unconfirmed balance of a wallet(with 0 confirmations)  

# Router.BuildRoute


### Simple RPC


BuildRoute builds a fully specified route based on a list of hop public keys. It retrieves the relevant channel policies from the graph in order to calculate the correct fees and time locks.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.BuildRouteRequest(
        amt_msat=<int64>,
        final_cltv_delta=<int32>,
        outgoing_chan_id=<uint64>,
        hop_pubkeys=<array bytes>,
    )
>>> response = stub.BuildRoute(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "route": <Route>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = { 
    amt_msat: <int64>, 
    final_cltv_delta: <int32>, 
    outgoing_chan_id: <uint64>, 
    hop_pubkeys: <array bytes>, 
  }; 
> router.buildRoute(request, function(err, response) {
    console.log(response);
  })
{ 
    "route": <Route>,
}
```

### gRPC Request: [routerrpc.BuildRouteRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L300)


Parameter | Type | Description
--------- | ---- | ----------- 
amt_msat | int64 | The amount to send expressed in msat. If set to zero, the minimum routable amount is used. 
final_cltv_delta | int32 | CLTV delta from the current height that should be used for the timelock of the final hop 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
hop_pubkeys | array bytes | A list of hops that defines the route. This does not include the source hop pubkey.  
### gRPC Response: [routerrpc.BuildRouteResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L326)


Parameter | Type | Description
--------- | ---- | ----------- 
route | [Route](#route) | Fully specified route that can be used to execute the payment.  

# Router.EstimateRouteFee


### Simple RPC


EstimateRouteFee allows callers to obtain a lower bound w.r.t how much it may cost to send an HTLC to the target end destination.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.RouteFeeRequest(
        dest=<bytes>,
        amt_sat=<int64>,
    )
>>> response = stub.EstimateRouteFee(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "routing_fee_msat": <int64>,
    "time_lock_delay": <int64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = { 
    dest: <bytes>, 
    amt_sat: <int64>, 
  }; 
> router.estimateRouteFee(request, function(err, response) {
    console.log(response);
  })
{ 
    "routing_fee_msat": <int64>,
    "time_lock_delay": <int64>,
}
```

### gRPC Request: [routerrpc.RouteFeeRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L180)


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The destination once wishes to obtain a routing fee quote to. 
amt_sat | int64 | The amount one wishes to send to the target destination.  
### gRPC Response: [routerrpc.RouteFeeResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L192)


Parameter | Type | Description
--------- | ---- | ----------- 
routing_fee_msat | int64 | A lower bound of the estimated fee to the target destination within the network, expressed in milli-satoshis. 
time_lock_delay | int64 | An estimate of the worst case time delay that can occur. Note that callers will still need to factor in the final CLTV delta of the last hop into this value.  

# Router.QueryMissionControl


### Simple RPC


QueryMissionControl exposes the internal mission control state to callers. It is a development feature.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.QueryMissionControlRequest()
>>> response = stub.QueryMissionControl(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "pairs": <array PairHistory>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = {}; 
> router.queryMissionControl(request, function(err, response) {
    console.log(response);
  })
{ 
    "pairs": <array PairHistory>,
}
```

### gRPC Request: [routerrpc.QueryMissionControlRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L229)


This request has no parameters.

### gRPC Response: [routerrpc.QueryMissionControlResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L233)


Parameter | Type | Description
--------- | ---- | ----------- 
pairs | array PairHistory | Node pair-level mission control state.  

# Router.QueryProbability


### Simple RPC


QueryProbability returns the current success probability estimate for a given node pair and amount.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.QueryProbabilityRequest(
        from_node=<bytes>,
        to_node=<bytes>,
        amt_msat=<int64>,
    )
>>> response = stub.QueryProbability(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "probability": <double>,
    "history": <PairData>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = { 
    from_node: <bytes>, 
    to_node: <bytes>, 
    amt_msat: <int64>, 
  }; 
> router.queryProbability(request, function(err, response) {
    console.log(response);
  })
{ 
    "probability": <double>,
    "history": <PairData>,
}
```

### gRPC Request: [routerrpc.QueryProbabilityRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L281)


Parameter | Type | Description
--------- | ---- | ----------- 
from_node | bytes | The source node pubkey of the pair. 
to_node | bytes | The destination node pubkey of the pair. 
amt_msat | int64 | The amount for which to calculate a probability.  
### gRPC Response: [routerrpc.QueryProbabilityResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L292)


Parameter | Type | Description
--------- | ---- | ----------- 
probability | double | The success probability for the requested pair. 
history | PairData | The historical data for the requested pair.  

# Router.ResetMissionControl


### Simple RPC


ResetMissionControl clears all mission control state and starts with a clean slate.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.ResetMissionControlRequest()
>>> response = stub.ResetMissionControl(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = {}; 
> router.resetMissionControl(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [routerrpc.ResetMissionControlRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L223)


This request has no parameters.

### gRPC Response: [routerrpc.ResetMissionControlResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L226)


This response has no parameters.


# Router.SendPayment


### Response-streaming RPC


SendPayment attempts to route a payment described by the passed PaymentRequest to the final destination. The call returns a stream of payment status updates.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.SendPaymentRequest(
        dest=<bytes>,
        amt=<int64>,
        amt_msat=<int64>,
        payment_hash=<bytes>,
        final_cltv_delta=<int32>,
        payment_request=<string>,
        timeout_seconds=<int32>,
        fee_limit_sat=<int64>,
        fee_limit_msat=<int64>,
        outgoing_chan_id=<uint64>,
        last_hop_pubkey=<bytes>,
        cltv_limit=<int32>,
        route_hints=<array RouteHint>,
        dest_custom_records=<array DestCustomRecordsEntry>,
        allow_self_payment=<bool>,
        dest_features=<array FeatureBit>,
    )
>>> for response in stub.SendPayment(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "state": <PaymentState>,
    "preimage": <bytes>,
    "htlcs": <array HTLCAttempt>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = { 
    dest: <bytes>, 
    amt: <int64>, 
    amt_msat: <int64>, 
    payment_hash: <bytes>, 
    final_cltv_delta: <int32>, 
    payment_request: <string>, 
    timeout_seconds: <int32>, 
    fee_limit_sat: <int64>, 
    fee_limit_msat: <int64>, 
    outgoing_chan_id: <uint64>, 
    last_hop_pubkey: <bytes>, 
    cltv_limit: <int32>, 
    route_hints: <array RouteHint>, 
    dest_custom_records: <array DestCustomRecordsEntry>, 
    allow_self_payment: <bool>, 
    dest_features: <array FeatureBit>, 
  }; 
> var call = router.sendPayment(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "state": <PaymentState>,
    "preimage": <bytes>,
    "htlcs": <array HTLCAttempt>,
}
```

### gRPC Request: [routerrpc.SendPaymentRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L9)


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient 
amt | int64 | Number of satoshis to send.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | Number of millisatoshis to send.  The fields amt and amt_msat are mutually exclusive. 
payment_hash | bytes | The hash to use within the payment's HTLC 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. The amount in the payment request may be zero. In that case it is required to set the amt field as well. If no payment request is specified, the following fields are required: dest, amt and payment_hash. 
timeout_seconds | int32 | An upper limit on the amount of time we should spend when attempting to fulfill the payment. This is expressed in seconds. If we cannot make a successful payment within this time frame, an error will be returned. This field must be non-zero. 
fee_limit_sat | int64 | The maximum number of satoshis that will be paid as a fee of the payment. If this field is left to the default value of 0, only zero-fee routes will be considered. This usually means single hop routes connecting directly to the destination. To send the payment without a fee limit, use max int here.  The fields fee_limit_sat and fee_limit_msat are mutually exclusive. 
fee_limit_msat | int64 | The maximum number of millisatoshis that will be paid as a fee of the payment. If this field is left to the default value of 0, only zero-fee routes will be considered. This usually means single hop routes connecting directly to the destination. To send the payment without a fee limit, use max int here.  The fields fee_limit_sat and fee_limit_msat are mutually exclusive. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
cltv_limit | int32 | An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced. 
route_hints | [array RouteHint](#routehint) | Optional route hints to reach the destination through private channels. 
dest_custom_records | array DestCustomRecordsEntry | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
allow_self_payment | bool | If set, circular payments to self are permitted. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  
### gRPC Response: [routerrpc.PaymentStatus (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L163)


Parameter | Type | Description
--------- | ---- | ----------- 
state | PaymentState | Current state the payment is in. 
preimage | bytes | The pre-image of the payment when state is SUCCEEDED. 
htlcs | [array HTLCAttempt](#htlcattempt) | The HTLCs made in attempt to settle the payment.  

# Router.SendToRoute


### Simple RPC


SendToRoute attempts to make a payment via the specified route. This method differs from SendPayment in that it allows users to specify a full route manually. This can be used for things like rebalancing, and atomic swaps.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.SendToRouteRequest(
        payment_hash=<bytes>,
        route=<Route>,
    )
>>> response = stub.SendToRoute(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "preimage": <bytes>,
    "failure": <Failure>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
    route: <Route>, 
  }; 
> router.sendToRoute(request, function(err, response) {
    console.log(response);
  })
{ 
    "preimage": <bytes>,
    "failure": <Failure>,
}
```

### gRPC Request: [routerrpc.SendToRouteRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L207)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. 
route | [Route](#route) | Route that should be used to attempt to complete the payment.  
### gRPC Response: [routerrpc.SendToRouteResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L215)


Parameter | Type | Description
--------- | ---- | ----------- 
preimage | bytes | The preimage obtained by making the payment. 
failure | [Failure](#failure) | The failure message in case the payment failed.  

# Router.SubscribeHtlcEvents


### Response-streaming RPC


SubscribeHtlcEvents creates a uni-directional stream from the server to the client which delivers a stream of htlc events.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.SubscribeHtlcEventsRequest()
>>> for response in stub.SubscribeHtlcEvents(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "incoming_channel_id": <uint64>,
    "outgoing_channel_id": <uint64>,
    "incoming_htlc_id": <uint64>,
    "outgoing_htlc_id": <uint64>,
    "timestamp_ns": <uint64>,
    "event_type": <EventType>,
    "forward_event": <ForwardEvent>,
    "forward_fail_event": <ForwardFailEvent>,
    "settle_event": <SettleEvent>,
    "link_fail_event": <LinkFailEvent>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = {}; 
> var call = router.subscribeHtlcEvents(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "incoming_channel_id": <uint64>,
    "outgoing_channel_id": <uint64>,
    "incoming_htlc_id": <uint64>,
    "outgoing_htlc_id": <uint64>,
    "timestamp_ns": <uint64>,
    "event_type": <EventType>,
    "forward_event": <ForwardEvent>,
    "forward_fail_event": <ForwardFailEvent>,
    "settle_event": <SettleEvent>,
    "link_fail_event": <LinkFailEvent>,
}
```

### gRPC Request: [routerrpc.SubscribeHtlcEventsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L333)


This request has no parameters.

### gRPC Response: [routerrpc.HtlcEvent (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L344)


Parameter | Type | Description
--------- | ---- | ----------- 
incoming_channel_id | uint64 | The short channel id that the incoming htlc arrived at our node on. This value is zero for sends. 
outgoing_channel_id | uint64 | The short channel id that the outgoing htlc left our node on. This value is zero for receives. 
incoming_htlc_id | uint64 | Incoming id is the index of the incoming htlc in the incoming channel. This value is zero for sends. 
outgoing_htlc_id | uint64 | Outgoing id is the index of the outgoing htlc in the outgoing channel. This value is zero for receives. 
timestamp_ns | uint64 | The time in unix nanoseconds that the event occurred. 
event_type | EventType | The event type indicates whether the htlc was part of a send, receive or forward. 
forward_event | ForwardEvent |  
forward_fail_event | ForwardFailEvent |  
settle_event | SettleEvent |  
link_fail_event | LinkFailEvent |   

# Router.TrackPayment


### Response-streaming RPC


TrackPayment returns an update stream for the payment identified by the payment hash.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as routerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = routerrpc.RouterStub(channel)
>>> request = ln.routerrpc.TrackPaymentRequest(
        payment_hash=<bytes>,
    )
>>> for response in stub.TrackPayment(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "state": <PaymentState>,
    "preimage": <bytes>,
    "htlcs": <array HTLCAttempt>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var routerrpc = grpc.load('routerrpc/router.proto').routerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var router = new routerrpc.Router('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
  }; 
> var call = router.trackPayment(request)
> call.on('data', function(response) {
    // A response was received from the server.
    console.log(response);
  });
> call.on('status', function(status) {
    // The current status of the stream.
  });
> call.on('end', function() {
    // The server has closed the stream.
  });
{ 
    "state": <PaymentState>,
    "preimage": <bytes>,
    "htlcs": <array HTLCAttempt>,
}
```

### gRPC Request: [routerrpc.TrackPaymentRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L119)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The hash of the payment to look up.  
### gRPC Response: [routerrpc.PaymentStatus (Streaming)](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/routerrpc/router.proto#L163)


Parameter | Type | Description
--------- | ---- | ----------- 
state | PaymentState | Current state the payment is in. 
preimage | bytes | The pre-image of the payment when state is SUCCEEDED. 
htlcs | [array HTLCAttempt](#htlcattempt) | The HTLCs made in attempt to settle the payment.  

# Signer.ComputeInputScript


### Simple RPC


ComputeInputScript generates a complete InputIndex for the passed transaction with the signature as defined within the passed SignDescriptor. This method should be capable of generating the proper input script for both regular p2wkh output and p2wkh outputs nested within a regular p2sh output.  Note that when using this method to sign inputs belonging to the wallet, the only items of the SignDescriptor that need to be populated are pkScript in the TxOut field, the value in that same field, and finally the input index.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as signrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = signrpc.SignerStub(channel)
>>> request = ln.signrpc.SignReq(
        raw_tx_bytes=<bytes>,
        sign_descs=<array SignDescriptor>,
    )
>>> response = stub.ComputeInputScript(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "input_scripts": <array InputScript>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var signrpc = grpc.load('signrpc/signer.proto').signrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var signer = new signrpc.Signer('localhost:10009', creds);
> var request = { 
    raw_tx_bytes: <bytes>, 
    sign_descs: <array SignDescriptor>, 
  }; 
> signer.computeInputScript(request, function(err, response) {
    console.log(response);
  })
{ 
    "input_scripts": <array InputScript>,
}
```

### gRPC Request: [signrpc.SignReq ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L91)


Parameter | Type | Description
--------- | ---- | ----------- 
raw_tx_bytes | bytes | The raw bytes of the transaction to be signed. 
sign_descs | array SignDescriptor | A set of sign descriptors, for each input to be signed.  
### gRPC Response: [signrpc.InputScriptResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L118)


Parameter | Type | Description
--------- | ---- | ----------- 
input_scripts | array InputScript | The set of fully valid input scripts requested.  

# Signer.DeriveSharedKey


### Simple RPC


DeriveSharedKey returns a shared secret key by performing Diffie-Hellman key derivation between the ephemeral public key in the request and the node's key specified in the key_loc parameter (or the node's identity private key if no key locator is specified): P_shared = privKeyNode * ephemeralPubkey The resulting shared public key is serialized in the compressed format and hashed with sha256, resulting in the final key length of 256bit.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as signrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = signrpc.SignerStub(channel)
>>> request = ln.signrpc.SharedKeyRequest(
        ephemeral_pubkey=<bytes>,
        key_loc=<KeyLocator>,
    )
>>> response = stub.DeriveSharedKey(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "shared_key": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var signrpc = grpc.load('signrpc/signer.proto').signrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var signer = new signrpc.Signer('localhost:10009', creds);
> var request = { 
    ephemeral_pubkey: <bytes>, 
    key_loc: <KeyLocator>, 
  }; 
> signer.deriveSharedKey(request, function(err, response) {
    console.log(response);
  })
{ 
    "shared_key": <bytes>,
}
```

### gRPC Request: [signrpc.SharedKeyRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L155)


Parameter | Type | Description
--------- | ---- | ----------- 
ephemeral_pubkey | bytes | The ephemeral public key to use for the DH key derivation. 
key_loc | KeyLocator | The optional key locator of the local key that should be used. If this parameter is not set then the node's identity private key will be used.  
### gRPC Response: [signrpc.SharedKeyResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L166)


Parameter | Type | Description
--------- | ---- | ----------- 
shared_key | bytes | The shared public key, hashed with sha256.  

# Signer.SignMessage


### Simple RPC


SignMessage signs a message with the key specified in the key locator. The returned signature is fixed-size LN wire format encoded.  The main difference to SignMessage in the main RPC is that a specific key is used to sign the message instead of the node identity private key.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as signrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = signrpc.SignerStub(channel)
>>> request = ln.signrpc.SignMessageReq(
        msg=<bytes>,
        key_loc=<KeyLocator>,
    )
>>> response = stub.SignMessage(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "signature": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var signrpc = grpc.load('signrpc/signer.proto').signrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var signer = new signrpc.Signer('localhost:10009', creds);
> var request = { 
    msg: <bytes>, 
    key_loc: <KeyLocator>, 
  }; 
> signer.signMessage(request, function(err, response) {
    console.log(response);
  })
{ 
    "signature": <bytes>,
}
```

### gRPC Request: [signrpc.SignMessageReq ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L123)


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message to be signed. 
key_loc | KeyLocator | The key locator that identifies which key to use for signing.  
### gRPC Response: [signrpc.SignMessageResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L130)


Parameter | Type | Description
--------- | ---- | ----------- 
signature | bytes | The signature for the given message in the fixed-size LN wire format.  

# Signer.SignOutputRaw


### Simple RPC


SignOutputRaw is a method that can be used to generated a signature for a set of inputs/outputs to a transaction. Each request specifies details concerning how the outputs should be signed, which keys they should be signed with, and also any optional tweaks. The return value is a fixed 64-byte signature (the same format as we use on the wire in Lightning).  If we are  unable to sign using the specified keys, then an error will be returned.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as signrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = signrpc.SignerStub(channel)
>>> request = ln.signrpc.SignReq(
        raw_tx_bytes=<bytes>,
        sign_descs=<array SignDescriptor>,
    )
>>> response = stub.SignOutputRaw(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "raw_sigs": <array bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var signrpc = grpc.load('signrpc/signer.proto').signrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var signer = new signrpc.Signer('localhost:10009', creds);
> var request = { 
    raw_tx_bytes: <bytes>, 
    sign_descs: <array SignDescriptor>, 
  }; 
> signer.signOutputRaw(request, function(err, response) {
    console.log(response);
  })
{ 
    "raw_sigs": <array bytes>,
}
```

### gRPC Request: [signrpc.SignReq ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L91)


Parameter | Type | Description
--------- | ---- | ----------- 
raw_tx_bytes | bytes | The raw bytes of the transaction to be signed. 
sign_descs | array SignDescriptor | A set of sign descriptors, for each input to be signed.  
### gRPC Response: [signrpc.SignResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L99)


Parameter | Type | Description
--------- | ---- | ----------- 
raw_sigs | array bytes | A set of signatures realized in a fixed 64-byte format ordered in ascending input order.  

# Signer.VerifyMessage


### Simple RPC


VerifyMessage verifies a signature over a message using the public key provided. The signature must be fixed-size LN wire format encoded.  The main difference to VerifyMessage in the main RPC is that the public key used to sign the message does not have to be a node known to the network.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as signrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = signrpc.SignerStub(channel)
>>> request = ln.signrpc.VerifyMessageReq(
        msg=<bytes>,
        signature=<bytes>,
        pubkey=<bytes>,
    )
>>> response = stub.VerifyMessage(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "valid": <bool>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var signrpc = grpc.load('signrpc/signer.proto').signrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var signer = new signrpc.Signer('localhost:10009', creds);
> var request = { 
    msg: <bytes>, 
    signature: <bytes>, 
    pubkey: <bytes>, 
  }; 
> signer.verifyMessage(request, function(err, response) {
    console.log(response);
  })
{ 
    "valid": <bool>,
}
```

### gRPC Request: [signrpc.VerifyMessageReq ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L137)


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message over which the signature is to be verified. 
signature | bytes | The fixed-size LN wire encoded signature to be verified over the given message. 
pubkey | bytes | The public key the signature has to be valid for.  
### gRPC Response: [signrpc.VerifyMessageResp ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L150)


Parameter | Type | Description
--------- | ---- | ----------- 
valid | bool | Whether the signature was valid over the given message.  

# WalletKit.BumpFee


### Simple RPC


BumpFee bumps the fee of an arbitrary input within a transaction. This RPC takes a different approach than bitcoind's bumpfee command. lnd has a central batching engine in which inputs with similar fee rates are batched together to save on transaction fees. Due to this, we cannot rely on bumping the fee on a specific transaction, since transactions can change at any point with the addition of new inputs. The list of inputs that currently exist within lnd's central batching engine can be retrieved through the PendingSweeps RPC.  When bumping the fee of an input that currently exists within lnd's central batching engine, a higher fee transaction will be created that replaces the lower fee transaction through the Replace-By-Fee (RBF) policy. If it  This RPC also serves useful when wanting to perform a Child-Pays-For-Parent (CPFP), where the child transaction pays for its parent's fee. This can be done by specifying an outpoint within the low fee transaction that is under the control of the wallet.  The fee preference can be expressed either as a specific fee rate or a delta of blocks in which the output should be swept on-chain within. If a fee preference is not explicitly specified, then an error is returned.  Note that this RPC currently doesn't perform any validation checks on the fee preference being provided. For now, the responsibility of ensuring that the new fee preference is sufficient is delegated to the user.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.BumpFeeRequest(
        outpoint=<OutPoint>,
        target_conf=<uint32>,
        sat_per_byte=<uint32>,
        force=<bool>,
    )
>>> response = stub.BumpFee(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = { 
    outpoint: <OutPoint>, 
    target_conf: <uint32>, 
    sat_per_byte: <uint32>, 
    force: <bool>, 
  }; 
> walletKit.bumpFee(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [walletrpc.BumpFeeRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L224)


Parameter | Type | Description
--------- | ---- | ----------- 
outpoint | [OutPoint](#outpoint) | The input we're attempting to bump the fee of. 
target_conf | uint32 | The target number of blocks that the input should be spent within. 
sat_per_byte | uint32 | The fee rate, expressed in sat/byte, that should be used to spend the input with. 
force | bool | Whether this input must be force-swept. This means that it is swept even if it has a negative yield.  
### gRPC Response: [walletrpc.BumpFeeResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L244)


This response has no parameters.


# WalletKit.DeriveKey


### Simple RPC


DeriveKey attempts to derive an arbitrary key specified by the passed KeyLocator.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.signrpc.KeyLocator(
        key_family=<int32>,
        key_index=<int32>,
    )
>>> response = stub.DeriveKey(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "raw_key_bytes": <bytes>,
    "key_loc": <KeyLocator>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = { 
    key_family: <int32>, 
    key_index: <int32>, 
  }; 
> walletKit.deriveKey(request, function(err, response) {
    console.log(response);
  })
{ 
    "raw_key_bytes": <bytes>,
    "key_loc": <KeyLocator>,
}
```

### gRPC Request: [signrpc.KeyLocator ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L7)


Parameter | Type | Description
--------- | ---- | ----------- 
key_family | int32 | The family of key being identified. 
key_index | int32 | The precise index of the key being identified.  
### gRPC Response: [signrpc.KeyDescriptor ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L15)


Parameter | Type | Description
--------- | ---- | ----------- 
raw_key_bytes | bytes | The raw bytes of the key being identified. Either this or the KeyLocator must be specified. 
key_loc | KeyLocator | The key locator that identifies which key to use for signing. Either this or the raw bytes of the target key must be specified.  

# WalletKit.DeriveNextKey


### Simple RPC


DeriveNextKey attempts to derive the *next* key within the key family (account in BIP43) specified. This method should return the next external child within this branch.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.KeyReq(
        key_finger_print=<int32>,
        key_family=<int32>,
    )
>>> response = stub.DeriveNextKey(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "raw_key_bytes": <bytes>,
    "key_loc": <KeyLocator>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = { 
    key_finger_print: <int32>, 
    key_family: <int32>, 
  }; 
> walletKit.deriveNextKey(request, function(err, response) {
    console.log(response);
  })
{ 
    "raw_key_bytes": <bytes>,
    "key_loc": <KeyLocator>,
}
```

### gRPC Request: [walletrpc.KeyReq ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L10)


Parameter | Type | Description
--------- | ---- | ----------- 
key_finger_print | int32 | Is the key finger print of the root pubkey that this request is targeting. This allows the WalletKit to possibly serve out keys for multiple HD chains via public derivation. 
key_family | int32 | The target key family to derive a key from. In other contexts, this is known as the "account".  
### gRPC Response: [signrpc.KeyDescriptor ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/signrpc/signer.proto#L15)


Parameter | Type | Description
--------- | ---- | ----------- 
raw_key_bytes | bytes | The raw bytes of the key being identified. Either this or the KeyLocator must be specified. 
key_loc | KeyLocator | The key locator that identifies which key to use for signing. Either this or the raw bytes of the target key must be specified.  

# WalletKit.EstimateFee


### Simple RPC


EstimateFee attempts to query the internal fee estimator of the wallet to determine the fee (in sat/kw) to attach to a transaction in order to achieve the confirmation target.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.EstimateFeeRequest(
        conf_target=<int32>,
    )
>>> response = stub.EstimateFee(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "sat_per_kw": <int64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = { 
    conf_target: <int32>, 
  }; 
> walletKit.estimateFee(request, function(err, response) {
    console.log(response);
  })
{ 
    "sat_per_kw": <int64>,
}
```

### gRPC Request: [walletrpc.EstimateFeeRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L71)


Parameter | Type | Description
--------- | ---- | ----------- 
conf_target | int32 | The number of confirmations to shoot for when estimating the fee.  
### gRPC Response: [walletrpc.EstimateFeeResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L77)


Parameter | Type | Description
--------- | ---- | ----------- 
sat_per_kw | int64 | The amount of satoshis per kw that should be used in order to reach the confirmation target in the request.  

# WalletKit.NextAddr


### Simple RPC


NextAddr returns the next unused address within the wallet.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.AddrRequest()
>>> response = stub.NextAddr(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "addr": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = {}; 
> walletKit.nextAddr(request, function(err, response) {
    console.log(response);
  })
{ 
    "addr": <string>,
}
```

### gRPC Request: [walletrpc.AddrRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L25)


This request has no parameters.

### gRPC Response: [walletrpc.AddrResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L28)


Parameter | Type | Description
--------- | ---- | ----------- 
addr | string | The address encoded using a bech32 format.  

# WalletKit.PendingSweeps


### Simple RPC


PendingSweeps returns lists of on-chain outputs that lnd is currently attempting to sweep within its central batching engine. Outputs with similar fee rates are batched together in order to sweep them within a single transaction.  NOTE: Some of the fields within PendingSweepsRequest are not guaranteed to remain supported. This is an advanced API that depends on the internals of the UtxoSweeper, so things may change.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.PendingSweepsRequest()
>>> response = stub.PendingSweeps(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "pending_sweeps": <array PendingSweep>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = {}; 
> walletKit.pendingSweeps(request, function(err, response) {
    console.log(response);
  })
{ 
    "pending_sweeps": <array PendingSweep>,
}
```

### gRPC Request: [walletrpc.PendingSweepsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L214)


This request has no parameters.

### gRPC Response: [walletrpc.PendingSweepsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L217)


Parameter | Type | Description
--------- | ---- | ----------- 
pending_sweeps | array PendingSweep | The set of outputs currently being swept by lnd's central batching engine.  

# WalletKit.PublishTransaction


### Simple RPC


PublishTransaction attempts to publish the passed transaction to the network. Once this returns without an error, the wallet will continually attempt to re-broadcast the transaction on start up, until it enters the chain.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.Transaction(
        tx_hex=<bytes>,
    )
>>> response = stub.PublishTransaction(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "publish_error": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = { 
    tx_hex: <bytes>, 
  }; 
> walletKit.publishTransaction(request, function(err, response) {
    console.log(response);
  })
{ 
    "publish_error": <string>,
}
```

### gRPC Request: [walletrpc.Transaction ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L35)


Parameter | Type | Description
--------- | ---- | ----------- 
tx_hex | bytes | The raw serialized transaction.  
### gRPC Response: [walletrpc.PublishResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L41)


Parameter | Type | Description
--------- | ---- | ----------- 
publish_error | string | If blank, then no error occurred and the transaction was successfully published. If not the empty string, then a string representation of the broadcast error.  TODO(roasbeef): map to a proper enum type  

# WalletKit.SendOutputs


### Simple RPC


SendOutputs is similar to the existing sendmany call in Bitcoind, and allows the caller to create a transaction that sends to several outputs at once. This is ideal when wanting to batch create a set of transactions.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as walletrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = walletrpc.WalletKitStub(channel)
>>> request = ln.walletrpc.SendOutputsRequest(
        sat_per_kw=<int64>,
        outputs=<array TxOut>,
    )
>>> response = stub.SendOutputs(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "raw_tx": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var walletrpc = grpc.load('walletrpc/walletkit.proto').walletrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var walletKit = new walletrpc.WalletKit('localhost:10009', creds);
> var request = { 
    sat_per_kw: <int64>, 
    outputs: <array TxOut>, 
  }; 
> walletKit.sendOutputs(request, function(err, response) {
    console.log(response);
  })
{ 
    "raw_tx": <bytes>,
}
```

### gRPC Request: [walletrpc.SendOutputsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L52)


Parameter | Type | Description
--------- | ---- | ----------- 
sat_per_kw | int64 | The number of satoshis per kilo weight that should be used when crafting this transaction. 
outputs | array TxOut | A slice of the outputs that should be created in the transaction produced.  
### gRPC Response: [walletrpc.SendOutputsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/walletrpc/walletkit.proto#L64)


Parameter | Type | Description
--------- | ---- | ----------- 
raw_tx | bytes | The serialized transaction sent out on the network.  

# WalletUnlocker.ChangePassword


### Simple RPC


ChangePassword changes the password of the encrypted wallet. This will automatically unlock the wallet database if successful.

```shell

# The changepassword command is used to Change lnd's encrypted wallet's
# password. It will automatically unlock the daemon if the password change
# is successful.
# If one did not specify a password for their wallet (running lnd with
# --noseedbackup), one must restart their daemon without
# --noseedbackup and use this command. The "current password" field
# should be left empty.

$ lncli changepassword [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.WalletUnlockerStub(channel)
>>> request = ln.lnrpc.ChangePasswordRequest(
        current_password=<bytes>,
        new_password=<bytes>,
    )
>>> response = stub.ChangePassword(request)
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    current_password: <bytes>, 
    new_password: <bytes>, 
  }; 
> walletUnlocker.changePassword(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.ChangePasswordRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L202)


Parameter | Type | Description
--------- | ---- | ----------- 
current_password | bytes | current_password should be the current valid passphrase used to unlock the daemon. When using REST, this field must be encoded as base64. 
new_password | bytes | new_password should be the new passphrase that will be needed to unlock the daemon. When using REST, this field must be encoded as base64.  
### gRPC Response: [lnrpc.ChangePasswordResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L215)


This response has no parameters.


# WalletUnlocker.GenSeed


### Simple RPC


GenSeed is the first method that should be used to instantiate a new lnd instance. This method allows a caller to generate a new aezeed cipher seed given an optional passphrase. If provided, the passphrase will be necessary to decrypt the cipherseed to expose the internal wallet seed.  Once the cipherseed is obtained and verified by the user, the InitWallet method should be used to commit the newly generated seed, and create the wallet.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.WalletUnlockerStub(channel)
>>> request = ln.lnrpc.GenSeedRequest(
        aezeed_passphrase=<bytes>,
        seed_entropy=<bytes>,
    )
>>> response = stub.GenSeed(request)
>>> print(response)
{ 
    "cipher_seed_mnemonic": <array string>,
    "enciphered_seed": <bytes>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    aezeed_passphrase: <bytes>, 
    seed_entropy: <bytes>, 
  }; 
> walletUnlocker.genSeed(request, function(err, response) {
    console.log(response);
  })
{ 
    "cipher_seed_mnemonic": <array string>,
    "enciphered_seed": <bytes>,
}
```

### gRPC Request: [lnrpc.GenSeedRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L95)


Parameter | Type | Description
--------- | ---- | ----------- 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64. 
seed_entropy | bytes | seed_entropy is an optional 16-bytes generated via CSPRNG. If not specified, then a fresh set of randomness will be used to create the seed. When using REST, this field must be encoded as base64.  
### gRPC Response: [lnrpc.GenSeedResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L110)


Parameter | Type | Description
--------- | ---- | ----------- 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed. 
enciphered_seed | bytes | enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.  

# WalletUnlocker.InitWallet


### Simple RPC


InitWallet is used when lnd is starting up for the first time to fully initialize the daemon and its internal wallet. At the very least a wallet password must be provided. This will be used to encrypt sensitive material on disk.  In the case of a recovery scenario, the user can also specify their aezeed mnemonic and passphrase. If set, then the daemon will use this prior state to initialize its internal wallet.  Alternatively, this can be used along with the GenSeed RPC to obtain a seed, then present it to the user. Once it has been verified by the user, the seed can be fed into this RPC in order to commit the new wallet.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.WalletUnlockerStub(channel)
>>> request = ln.lnrpc.InitWalletRequest(
        wallet_password=<bytes>,
        cipher_seed_mnemonic=<array string>,
        aezeed_passphrase=<bytes>,
        recovery_window=<int32>,
        channel_backups=<ChanBackupSnapshot>,
    )
>>> response = stub.InitWallet(request)
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    wallet_password: <bytes>, 
    cipher_seed_mnemonic: <array string>, 
    aezeed_passphrase: <bytes>, 
    recovery_window: <int32>, 
    channel_backups: <ChanBackupSnapshot>, 
  }; 
> walletUnlocker.initWallet(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.InitWalletRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L127)


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon. When using REST, this field must be encoded as base64. 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed. 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet. 
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) | channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.  
### gRPC Response: [lnrpc.InitWalletResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L169)


This response has no parameters.


# WalletUnlocker.UnlockWallet


### Simple RPC


UnlockWallet is used at startup of lnd to provide a password to unlock the wallet database.

```shell

# The unlock command is used to decrypt lnd's wallet state in order to
# start up. This command MUST be run after booting up lnd before it's
# able to carry out its duties. An exception is if a user is running with
# --noseedbackup, then a default passphrase will be used.

$ lncli unlock [command options] [arguments...]

# --recovery_window value  address lookahead to resume recovery rescan, value should be non-zero --  To recover all funds, this should be greater than the maximum number of consecutive, unused addresses ever generated by the wallet. (default: 0)
# --stdin                  read password from standard input instead of prompting for it. THIS IS CONSIDERED TO BE DANGEROUS if the password is located in a file that can be read by another user. This flag should only be used in combination with some sort of password manager or secrets vault.
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.WalletUnlockerStub(channel)
>>> request = ln.lnrpc.UnlockWalletRequest(
        wallet_password=<bytes>,
        recovery_window=<int32>,
        channel_backups=<ChanBackupSnapshot>,
    )
>>> response = stub.UnlockWallet(request)
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    wallet_password: <bytes>, 
    recovery_window: <int32>, 
    channel_backups: <ChanBackupSnapshot>, 
  }; 
> walletUnlocker.unlockWallet(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [lnrpc.UnlockWalletRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L172)


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly. When using REST, this field must be encoded as base64. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet. 
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) | channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.  
### gRPC Response: [lnrpc.UnlockWalletResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.proto#L199)


This response has no parameters.


# Watchtower.GetInfo


### Simple RPC


lncli: tower info GetInfo returns general information concerning the companion watchtower including its public key and URIs where the server is currently listening for clients.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as watchtowerrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = watchtowerrpc.WatchtowerStub(channel)
>>> request = ln.watchtowerrpc.GetInfoRequest()
>>> response = stub.GetInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "pubkey": <bytes>,
    "listeners": <array string>,
    "uris": <array string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var watchtowerrpc = grpc.load('watchtowerrpc/watchtower.proto').watchtowerrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtower = new watchtowerrpc.Watchtower('localhost:10009', creds);
> var request = {}; 
> watchtower.getInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "pubkey": <bytes>,
    "listeners": <array string>,
    "uris": <array string>,
}
```

### gRPC Request: [watchtowerrpc.GetInfoRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/watchtowerrpc/watchtower.proto#L16)


This request has no parameters.

### gRPC Response: [watchtowerrpc.GetInfoResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/watchtowerrpc/watchtower.proto#L19)


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The public key of the watchtower. 
listeners | array string | The listening addresses of the watchtower. 
uris | array string | The URIs of the watchtower.  

# WatchtowerClient.AddTower


### Simple RPC


AddTower adds a new watchtower reachable at the given address and considers it for new sessions. If the watchtower already exists, then any new addresses included will be considered when dialing it for session negotiations and backups.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as wtclientrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = wtclientrpc.WatchtowerClientStub(channel)
>>> request = ln.wtclientrpc.AddTowerRequest(
        pubkey=<bytes>,
        address=<string>,
    )
>>> response = stub.AddTower(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var wtclientrpc = grpc.load('wtclientrpc/wtclient.proto').wtclientrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtowerClient = new wtclientrpc.WatchtowerClient('localhost:10009', creds);
> var request = { 
    pubkey: <bytes>, 
    address: <string>, 
  }; 
> watchtowerClient.addTower(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [wtclientrpc.AddTowerRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L7)


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower to add. 
address | string | A network address the watchtower is reachable over.  
### gRPC Response: [wtclientrpc.AddTowerResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L15)


This response has no parameters.


# WatchtowerClient.GetTowerInfo


### Simple RPC


GetTowerInfo retrieves information for a registered watchtower.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as wtclientrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = wtclientrpc.WatchtowerClientStub(channel)
>>> request = ln.wtclientrpc.GetTowerInfoRequest(
        pubkey=<bytes>,
        include_sessions=<bool>,
    )
>>> response = stub.GetTowerInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "pubkey": <bytes>,
    "addresses": <array string>,
    "active_session_candidate": <bool>,
    "num_sessions": <uint32>,
    "sessions": <array TowerSession>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var wtclientrpc = grpc.load('wtclientrpc/wtclient.proto').wtclientrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtowerClient = new wtclientrpc.WatchtowerClient('localhost:10009', creds);
> var request = { 
    pubkey: <bytes>, 
    include_sessions: <bool>, 
  }; 
> watchtowerClient.getTowerInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "pubkey": <bytes>,
    "addresses": <array string>,
    "active_session_candidate": <bool>,
    "num_sessions": <uint32>,
    "sessions": <array TowerSession>,
}
```

### gRPC Request: [wtclientrpc.GetTowerInfoRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L33)


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower to retrieve information for. 
include_sessions | bool | Whether we should include sessions with the watchtower in the response.  
### gRPC Response: [wtclientrpc.Tower ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L64)


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower. 
addresses | array string | The list of addresses the watchtower is reachable over. 
active_session_candidate | bool | Whether the watchtower is currently a candidate for new sessions. 
num_sessions | uint32 | The number of sessions that have been negotiated with the watchtower. 
sessions | array TowerSession | The list of sessions that have been negotiated with the watchtower.  

# WatchtowerClient.ListTowers


### Simple RPC


ListTowers returns the list of watchtowers registered with the client.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as wtclientrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = wtclientrpc.WatchtowerClientStub(channel)
>>> request = ln.wtclientrpc.ListTowersRequest(
        include_sessions=<bool>,
    )
>>> response = stub.ListTowers(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "towers": <array Tower>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var wtclientrpc = grpc.load('wtclientrpc/wtclient.proto').wtclientrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtowerClient = new wtclientrpc.WatchtowerClient('localhost:10009', creds);
> var request = { 
    include_sessions: <bool>, 
  }; 
> watchtowerClient.listTowers(request, function(err, response) {
    console.log(response);
  })
{ 
    "towers": <array Tower>,
}
```

### gRPC Request: [wtclientrpc.ListTowersRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L81)


Parameter | Type | Description
--------- | ---- | ----------- 
include_sessions | bool | Whether we should include sessions with the watchtower in the response.  
### gRPC Response: [wtclientrpc.ListTowersResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L86)


Parameter | Type | Description
--------- | ---- | ----------- 
towers | array Tower | The list of watchtowers available for new backups.  

# WatchtowerClient.Policy


### Simple RPC


Policy returns the active watchtower client policy configuration.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as wtclientrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = wtclientrpc.WatchtowerClientStub(channel)
>>> request = ln.wtclientrpc.PolicyRequest()
>>> response = stub.Policy(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "max_updates": <uint32>,
    "sweep_sat_per_byte": <uint32>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var wtclientrpc = grpc.load('wtclientrpc/wtclient.proto').wtclientrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtowerClient = new wtclientrpc.WatchtowerClient('localhost:10009', creds);
> var request = {}; 
> watchtowerClient.policy(request, function(err, response) {
    console.log(response);
  })
{ 
    "max_updates": <uint32>,
    "sweep_sat_per_byte": <uint32>,
}
```

### gRPC Request: [wtclientrpc.PolicyRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L120)


This request has no parameters.

### gRPC Response: [wtclientrpc.PolicyResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L123)


Parameter | Type | Description
--------- | ---- | ----------- 
max_updates | uint32 | The maximum number of updates each session we negotiate with watchtowers should allow. 
sweep_sat_per_byte | uint32 | The fee rate, in satoshis per vbyte, that will be used by watchtowers for justice transactions in response to channel breaches.  

# WatchtowerClient.RemoveTower


### Simple RPC


RemoveTower removes a watchtower from being considered for future session negotiations and from being used for any subsequent backups until it's added again. If an address is provided, then this RPC only serves as a way of removing the address from the watchtower instead.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as wtclientrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = wtclientrpc.WatchtowerClientStub(channel)
>>> request = ln.wtclientrpc.RemoveTowerRequest(
        pubkey=<bytes>,
        address=<string>,
    )
>>> response = stub.RemoveTower(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var wtclientrpc = grpc.load('wtclientrpc/wtclient.proto').wtclientrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtowerClient = new wtclientrpc.WatchtowerClient('localhost:10009', creds);
> var request = { 
    pubkey: <bytes>, 
    address: <string>, 
  }; 
> watchtowerClient.removeTower(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: [wtclientrpc.RemoveTowerRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L18)


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower to remove. 
address | string | If set, then the record for this address will be removed, indicating that is is stale. Otherwise, the watchtower will no longer be used for future session negotiations and backups.  
### gRPC Response: [wtclientrpc.RemoveTowerResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L30)


This response has no parameters.


# WatchtowerClient.Stats


### Simple RPC


Stats returns the in-memory statistics of the client since startup.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as wtclientrpc
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = wtclientrpc.WatchtowerClientStub(channel)
>>> request = ln.wtclientrpc.StatsRequest()
>>> response = stub.Stats(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "num_backups": <uint32>,
    "num_pending_backups": <uint32>,
    "num_failed_backups": <uint32>,
    "num_sessions_acquired": <uint32>,
    "num_sessions_exhausted": <uint32>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var wtclientrpc = grpc.load('wtclientrpc/wtclient.proto').wtclientrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA';
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/data/chain/bitcoin/simnet/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata();
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var watchtowerClient = new wtclientrpc.WatchtowerClient('localhost:10009', creds);
> var request = {}; 
> watchtowerClient.stats(request, function(err, response) {
    console.log(response);
  })
{ 
    "num_backups": <uint32>,
    "num_pending_backups": <uint32>,
    "num_failed_backups": <uint32>,
    "num_sessions_acquired": <uint32>,
    "num_sessions_exhausted": <uint32>,
}
```

### gRPC Request: [wtclientrpc.StatsRequest ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L91)


This request has no parameters.

### gRPC Response: [wtclientrpc.StatsResponse ](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/wtclientrpc/wtclient.proto#L94)


Parameter | Type | Description
--------- | ---- | ----------- 
num_backups | uint32 | The total number of backups made to all active and exhausted watchtower sessions. 
num_pending_backups | uint32 | The total number of backups that are pending to be acknowledged by all active and exhausted watchtower sessions. 
num_failed_backups | uint32 | The total number of backups that all active and exhausted watchtower sessions have failed to acknowledge. 
num_sessions_acquired | uint32 | The total number of new sessions made to watchtowers. 
num_sessions_exhausted | uint32 | The total number of watchtower sessions that have been exhausted.  


# Messages

## lnrpc.AbandonChannelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) |   

## lnrpc.AbandonChannelResponse


This message has no parameters.


## lnrpc.AddInvoiceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash | bytes |  
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.  

## lnrpc.BakeMacaroonRequest


Parameter | Type | Description
--------- | ---- | ----------- 
permissions | [array MacaroonPermission](#macaroonpermission) | The list of permissions the new macaroon should grant.  

## lnrpc.BakeMacaroonResponse


Parameter | Type | Description
--------- | ---- | ----------- 
macaroon | string | The hex encoded macaroon, serialized in binary format.  

## lnrpc.Chain


Parameter | Type | Description
--------- | ---- | ----------- 
chain | string | The blockchain the node is on (eg bitcoin, litecoin) 
network | string | The network the node is on (eg regtest, testnet, mainnet)  

## lnrpc.ChanBackupExportRequest


This message has no parameters.


## lnrpc.ChanBackupSnapshot


Parameter | Type | Description
--------- | ---- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) | The set of new channels that have been added since the last channel backup snapshot was requested. 
multi_chan_backup | [MultiChanBackup](#multichanbackup) | A multi-channel backup that covers all open channels currently known to lnd.  

## lnrpc.ChanInfoRequest


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.  

## lnrpc.ChanPointShim


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | The size of the pre-crafted output to be used as the channel point for this channel funding. 
chan_point | [ChannelPoint](#channelpoint) | The target channel point to refrence in created commitment transactions. 
local_key | [KeyDescriptor](#keydescriptor) | Our local key to use when creating the multi-sig output. 
remote_key | bytes | The key of the remote party to use when creating the multi-sig output. 
pending_chan_id | bytes | If non-zero, then this will be used as the pending channel ID on the wire protocol to initate the funding request. This is an optional field, and should only be set if the responder is already expecting a specific pending channel ID. 
thaw_height | uint32 | This uint32 indicates if this channel is to be considered 'frozen'. A frozen channel does not allow a cooperative channel close by the initiator. The thaw_height is the height that this restriction stops applying to the channel.  

## lnrpc.ChangePasswordRequest


Parameter | Type | Description
--------- | ---- | ----------- 
current_password | bytes | current_password should be the current valid passphrase used to unlock the daemon. When using REST, this field must be encoded as base64. 
new_password | bytes | new_password should be the new passphrase that will be needed to unlock the daemon. When using REST, this field must be encoded as base64.  

## lnrpc.ChangePasswordResponse


This message has no parameters.


## lnrpc.Channel


Parameter | Type | Description
--------- | ---- | ----------- 
active | bool | Whether this channel is active or not 
remote_pubkey | string | The identity pubkey of the remote node 
channel_point | string | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
capacity | int64 | The total amount of funds held in this channel 
local_balance | int64 | This node's current balance in this channel 
remote_balance | int64 | The counterparty's current balance in this channel 
commit_fee | int64 | The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart. 
commit_weight | int64 | The weight of the commitment transaction 
fee_per_kw | int64 | The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open. 
unsettled_balance | int64 | The unsettled balance in this channel 
total_satoshis_sent | int64 | The total number of satoshis we've sent within this channel. 
total_satoshis_received | int64 | The total number of satoshis we've received within this channel. 
num_updates | uint64 | The total number of updates conducted within this channel. 
pending_htlcs | [array HTLC](#htlc) | The list of active, uncleared HTLCs currently pending within the channel. 
csv_delay | uint32 | The CSV delay expressed in relative blocks. If the channel is force closed, we will need to wait for this many blocks before we can regain our funds. 
private | bool | Whether this channel is advertised to the network or not. 
initiator | bool | True if we were the ones that created the channel. 
chan_status_flags | string | A set of flags showing the current state of the channel. 
local_chan_reserve_sat | int64 | The minimum satoshis this node is required to reserve in its balance. 
remote_chan_reserve_sat | int64 | The minimum satoshis the other node is required to reserve in its balance. 
static_remote_key | bool | Deprecated. Use commitment_type. 
commitment_type | [CommitmentType](#commitmenttype) | The commitment type used by this channel. 
lifetime | int64 | The number of seconds that the channel has been monitored by the channel scoring system. Scores are currently not persisted, so this value may be less than the lifetime of the channel [EXPERIMENTAL]. 
uptime | int64 | The number of seconds that the remote peer has been observed as being online by the channel scoring system over the lifetime of the channel [EXPERIMENTAL]. 
close_address | string | Close address is the address that we will enforce payout to on cooperative close if the channel was opened utilizing option upfront shutdown. This value can be set on channel open by setting close_address in an open channel request. If this value is not set, you can still choose a payout address by cooperatively closing with the delivery_address field set. 
push_amount_sat | uint64 | The amount that the initiator of the channel optionally pushed to the remote party on channel open. This amount will be zero if the channel initiator did not push any funds to the remote peer. If the initiator field is true, we pushed this amount to our peer, if it is false, the remote peer pushed this amount to us. 
thaw_height | uint32 | This uint32 indicates if this channel is to be considered 'frozen'. A frozen channel doest not allow a cooperative channel close by the initiator. The thaw_height is the height that this restriction stops applying to the channel. This field is optional, not setting it or using a value of zero will mean the channel has no additional restrictions.  

## lnrpc.ChannelAcceptRequest


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node that wishes to open an inbound channel. 
chain_hash | bytes | The hash of the genesis block that the proposed channel resides in. 
pending_chan_id | bytes | The pending channel id. 
funding_amt | uint64 | The funding amount in satoshis that initiator wishes to use in the / channel. 
push_amt | uint64 | The push amount of the proposed channel in millisatoshis. 
dust_limit | uint64 | The dust limit of the initiator's commitment tx. 
max_value_in_flight | uint64 | The maximum amount of coins in millisatoshis that can be pending in this / channel. 
channel_reserve | uint64 | The minimum amount of satoshis the initiator requires us to have at all / times. 
min_htlc | uint64 | The smallest HTLC in millisatoshis that the initiator will accept. 
fee_per_kw | uint64 | The initial fee rate that the initiator suggests for both commitment / transactions. 
csv_delay | uint32 | The number of blocks to use for the relative time lock in the pay-to-self output of both commitment transactions. 
max_accepted_htlcs | uint32 | The total number of incoming HTLC's that the initiator will accept. 
channel_flags | uint32 | A bit-field which the initiator uses to specify proposed channel / behavior.  

## lnrpc.ChannelAcceptResponse


Parameter | Type | Description
--------- | ---- | ----------- 
accept | bool | Whether or not the client accepts the channel. 
pending_chan_id | bytes | The pending channel id to which this response applies.  

## lnrpc.ChannelBackup


Parameter | Type | Description
--------- | ---- | ----------- 
chan_point | [ChannelPoint](#channelpoint) | Identifies the channel that this backup belongs to. 
chan_backup | bytes | Is an encrypted single-chan backup. this can be passed to RestoreChannelBackups, or the WalletUnlocker Init and Unlock methods in order to trigger the recovery protocol. When using REST, this field must be encoded as base64.  

## lnrpc.ChannelBackupSubscription


This message has no parameters.


## lnrpc.ChannelBackups


Parameter | Type | Description
--------- | ---- | ----------- 
chan_backups | [array ChannelBackup](#channelbackup) | A set of single-chan static channel backups.  

## lnrpc.ChannelBalanceRequest


This message has no parameters.


## lnrpc.ChannelBalanceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
balance | int64 | Sum of channels balances denominated in satoshis 
pending_open_balance | int64 | Sum of channels pending balances denominated in satoshis  

## lnrpc.ChannelCloseSummary


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | string | The outpoint (txid:index) of the funding transaction. 
chan_id | uint64 | The unique channel ID for the channel. 
chain_hash | string | The hash of the genesis block that this channel resides within. 
closing_tx_hash | string | The txid of the transaction which ultimately closed this channel. 
remote_pubkey | string | Public key of the remote peer that we formerly had a channel with. 
capacity | int64 | Total capacity of the channel. 
close_height | uint32 | Height at which the funding transaction was spent. 
settled_balance | int64 | Settled balance at the time of channel closure 
time_locked_balance | int64 | The sum of all the time-locked outputs at the time of channel closure 
close_type | [ClosureType](#closuretype) | Details on how the channel was closed. 
open_initiator | [Initiator](#initiator) | Open initiator is the party that initiated opening the channel. Note that this value may be unknown if the channel was closed before we migrated to store open channel information after close. 
close_initiator | [Initiator](#initiator) | Close initiator indicates which party initiated the close. This value will be unknown for channels that were cooperatively closed before we started tracking cooperative close initiators. Note that this indicates which party initiated a close, and it is possible for both to initiate cooperative or force closes, although only one party's close will be confirmed on chain.  

## lnrpc.ChannelCloseUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
closing_txid | bytes |  
success | bool |   

## lnrpc.ChannelEdge


Parameter | Type | Description
--------- | ---- | ----------- 
channel_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | string |  
last_update | uint32 |  
node1_pub | string |  
node2_pub | string |  
capacity | int64 |  
node1_policy | [RoutingPolicy](#routingpolicy) |  
node2_policy | [RoutingPolicy](#routingpolicy) |   

## lnrpc.ChannelEdgeUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | [ChannelPoint](#channelpoint) |  
capacity | int64 |  
routing_policy | [RoutingPolicy](#routingpolicy) |  
advertising_node | string |  
connecting_node | string |   

## lnrpc.ChannelEventSubscription


This message has no parameters.


## lnrpc.ChannelEventUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
open_channel | [Channel](#channel) |  
closed_channel | [ChannelCloseSummary](#channelclosesummary) |  
active_channel | [ChannelPoint](#channelpoint) |  
inactive_channel | [ChannelPoint](#channelpoint) |  
pending_open_channel | [PendingUpdate](#pendingupdate) |  
type | [UpdateType](#updatetype) |   

## lnrpc.ChannelFeeReport


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The short channel id that this fee report belongs to. 
channel_point | string | The channel that this fee report belongs to. 
base_fee_msat | int64 | The base fee charged regardless of the number of milli-satoshis sent. 
fee_per_mil | int64 | The amount charged per milli-satoshis transferred expressed in / millionths of a satoshi. 
fee_rate | double | The effective fee rate in milli-satoshis. Computed by dividing the / fee_per_mil value by 1 million.  

## lnrpc.ChannelGraph


Parameter | Type | Description
--------- | ---- | ----------- 
nodes | [array LightningNode](#lightningnode) | The list of `LightningNode`s in this channel graph 
edges | [array ChannelEdge](#channeledge) | The list of `ChannelEdge`s in this channel graph  

## lnrpc.ChannelGraphRequest


Parameter | Type | Description
--------- | ---- | ----------- 
include_unannounced | bool | Whether unannounced channels are included in the response or not. If set, unannounced channels are included. Unannounced channels are both private channels, and public channels that are not yet announced to the network.  

## lnrpc.ChannelOpenUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) |   

## lnrpc.ChannelPoint


Parameter | Type | Description
--------- | ---- | ----------- 
funding_txid_bytes | bytes | Txid of the funding transaction. When using REST, this field must be encoded as base64. 
funding_txid_str | string | Hex-encoded string representing the byte-reversed hash of the funding transaction. 
output_index | uint32 | The index of the output of the funding transaction  

## lnrpc.ChannelUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
signature | bytes | The signature that validates the announced data and proves the ownership of node id. 
chain_hash | bytes | The target chain that this channel was opened within. This value should be the genesis hash of the target chain. Along with the short channel ID, this uniquely identifies the channel globally in a blockchain. 
chan_id | uint64 | The unique description of the funding transaction. 
timestamp | uint32 | A timestamp that allows ordering in the case of multiple announcements. We should ignore the message if timestamp is not greater than the last-received. 
message_flags | uint32 | The bitfield that describes whether optional fields are present in this update. Currently, the least-significant bit must be set to 1 if the optional field MaxHtlc is present. 
channel_flags | uint32 | The bitfield that describes additional meta-data concerning how the update is to be interpreted. Currently, the least-significant bit must be set to 0 if the creating node corresponds to the first node in the previously sent channel announcement and 1 otherwise. If the second bit is set, then the channel is set to be disabled. 
time_lock_delta | uint32 | The minimum number of blocks this node requires to be added to the expiry of HTLCs. This is a security parameter determined by the node operator. This value represents the required gap between the time locks of the incoming and outgoing HTLC's set to this node. 
htlc_minimum_msat | uint64 | The minimum HTLC value which will be accepted. 
base_fee | uint32 | The base fee that must be used for incoming HTLC's to this particular channel. This value will be tacked onto the required for a payment independent of the size of the payment. 
fee_rate | uint32 | The fee rate that will be charged per millionth of a satoshi. 
htlc_maximum_msat | uint64 | The maximum HTLC value which will be accepted. 
extra_opaque_data | bytes | The set of data that was appended to this message, some of which we may not actually know how to iterate or parse. By holding onto this data, we ensure that we're able to properly validate the set of signatures that cover these new fields, and ensure we're able to make upgrades to the network in a forwards compatible manner.  

## lnrpc.CloseChannelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
force | bool | If true, then the channel will be closed forcibly. This means the / current commitment transaction will be signed and broadcast. 
target_conf | int32 | The target number of blocks that the closure transaction should be / confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / closure transaction. 
delivery_address | string | An optional address to send funds to in the case of a cooperative close. If the channel was opened with an upfront shutdown script and this field is set, the request to close will fail because the channel must pay out to the upfront shutdown addresss.  

## lnrpc.CloseStatusUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
close_pending | [PendingUpdate](#pendingupdate) |  
chan_close | [ChannelCloseUpdate](#channelcloseupdate) |   

## lnrpc.ClosedChannelUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
capacity | int64 |  
closed_height | uint32 |  
chan_point | [ChannelPoint](#channelpoint) |   

## lnrpc.ClosedChannelsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
cooperative | bool |  
local_force | bool |  
remote_force | bool |  
breach | bool |  
funding_canceled | bool |  
abandoned | bool |   

## lnrpc.ClosedChannelsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array ChannelCloseSummary](#channelclosesummary) |   

## lnrpc.ConfirmationUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
block_sha | bytes |  
block_height | int32 |  
num_confs_left | uint32 |   

## lnrpc.ConnectPeerRequest


Parameter | Type | Description
--------- | ---- | ----------- 
addr | [LightningAddress](#lightningaddress) | Lightning address of the peer, in the format `<pubkey>@host` 
perm | bool | If set, the daemon will attempt to persistently connect to the target peer. Otherwise, the call will be synchronous.  

## lnrpc.ConnectPeerResponse


This message has no parameters.


## lnrpc.DebugLevelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
show | bool |  
level_spec | string |   

## lnrpc.DebugLevelResponse


Parameter | Type | Description
--------- | ---- | ----------- 
sub_systems | string |   

## lnrpc.DeleteAllPaymentsRequest


This message has no parameters.


## lnrpc.DeleteAllPaymentsResponse


This message has no parameters.


## lnrpc.DisconnectPeerRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The pubkey of the node to disconnect from  

## lnrpc.DisconnectPeerResponse


This message has no parameters.


## lnrpc.EdgeLocator


Parameter | Type | Description
--------- | ---- | ----------- 
channel_id | uint64 | The short channel id of this edge. 
direction_reverse | bool | The direction of this edge. If direction_reverse is false, the direction of this edge is from the channel endpoint with the lexicographically smaller pub key to the endpoint with the larger pub key. If direction_reverse is is true, the edge goes the other way.  

## lnrpc.EstimateFeeRequest


Parameter | Type | Description
--------- | ---- | ----------- 
AddrToAmount | [array AddrToAmountEntry](#addrtoamountentry) | The map from addresses to amounts for the transaction. 
target_conf | int32 | The target number of blocks that this transaction should be confirmed / by.  

## lnrpc.EstimateFeeRequest.AddrToAmountEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | string |  
value | int64 |   

## lnrpc.EstimateFeeResponse


Parameter | Type | Description
--------- | ---- | ----------- 
fee_sat | int64 | The total fee in satoshis. 
feerate_sat_per_byte | int64 | The fee rate in satoshi/byte.  

## lnrpc.ExportChannelBackupRequest


Parameter | Type | Description
--------- | ---- | ----------- 
chan_point | [ChannelPoint](#channelpoint) | The target channel point to obtain a back up for.  

## lnrpc.Failure


Parameter | Type | Description
--------- | ---- | ----------- 
code | [FailureCode](#failurecode) | Failure code as defined in the Lightning spec 
channel_update | [ChannelUpdate](#channelupdate) | An optional channel update message. 
htlc_msat | uint64 | A failure type-dependent htlc value. 
onion_sha_256 | bytes | The sha256 sum of the onion payload. 
cltv_expiry | uint32 | A failure type-dependent cltv expiry value. 
flags | uint32 | A failure type-dependent flags value. 
failure_source_index | uint32 | The position in the path of the intermediate or final node that generated the failure message. Position zero is the sender node. 
height | uint32 | A failure type-dependent block height.  

## lnrpc.Feature


Parameter | Type | Description
--------- | ---- | ----------- 
name | string |  
is_required | bool |  
is_known | bool |   

## lnrpc.FeeLimit


Parameter | Type | Description
--------- | ---- | ----------- 
fixed | int64 | The fee limit expressed as a fixed amount of satoshis.  The fields fixed and fixed_msat are mutually exclusive. 
fixed_msat | int64 | The fee limit expressed as a fixed amount of millisatoshis.  The fields fixed and fixed_msat are mutually exclusive. 
percent | int64 | The fee limit expressed as a percentage of the payment amount.  

## lnrpc.FeeReportRequest


This message has no parameters.


## lnrpc.FeeReportResponse


Parameter | Type | Description
--------- | ---- | ----------- 
channel_fees | [array ChannelFeeReport](#channelfeereport) | An array of channel fee reports which describes the current fee schedule / for each channel. 
day_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected / over the past 24 hrs. 
week_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 week. 
month_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 month.  

## lnrpc.FloatMetric


Parameter | Type | Description
--------- | ---- | ----------- 
value | double | Arbitrary float value. 
normalized_value | double | The value normalized to [0,1] or [-1,1].  

## lnrpc.ForwardingEvent


Parameter | Type | Description
--------- | ---- | ----------- 
timestamp | uint64 | Timestamp is the time (unix epoch offset) that this circuit was / completed. 
chan_id_in | uint64 | The incoming channel ID that carried the HTLC that created the circuit. 
chan_id_out | uint64 | The outgoing channel ID that carried the preimage that completed the / circuit. 
amt_in | uint64 | The total amount (in satoshis) of the incoming HTLC that created half / the circuit. 
amt_out | uint64 | The total amount (in satoshis) of the outgoing HTLC that created the / second half of the circuit. 
fee | uint64 | The total fee (in satoshis) that this payment circuit carried. 
fee_msat | uint64 | The total fee (in milli-satoshis) that this payment circuit carried. 
amt_in_msat | uint64 | The total amount (in milli-satoshis) of the incoming HTLC that created / half the circuit. 
amt_out_msat | uint64 | The total amount (in milli-satoshis) of the outgoing HTLC that created / the second half of the circuit.  

## lnrpc.ForwardingHistoryRequest


Parameter | Type | Description
--------- | ---- | ----------- 
start_time | uint64 | Start time is the starting point of the forwarding history request. All / records beyond this point will be included, respecting the end time, and / the index offset. 
end_time | uint64 | End time is the end point of the forwarding history request. The / response will carry at most 50k records between the start time and the / end time. The index offset can be used to implement pagination. 
index_offset | uint32 | Index offset is the offset in the time series to start at. As each / response can only contain 50k records, callers can use this to skip / around within a packed time series. 
num_max_events | uint32 | The max number of events to return in the response to this query.  

## lnrpc.ForwardingHistoryResponse


Parameter | Type | Description
--------- | ---- | ----------- 
forwarding_events | [array ForwardingEvent](#forwardingevent) | A list of forwarding events from the time slice of the time series / specified in the request. 
last_offset_index | uint32 | The index of the last time in the set of returned forwarding events. Can / be used to seek further, pagination style.  

## lnrpc.FundingPsbtFinalize


Parameter | Type | Description
--------- | ---- | ----------- 
signed_psbt | bytes | The funded PSBT that contains all witness data to send the exact channel capacity amount to the PK script returned in the open channel message in a previous step. 
pending_chan_id | bytes | The pending channel ID of the channel to get the PSBT for.  

## lnrpc.FundingPsbtVerify


Parameter | Type | Description
--------- | ---- | ----------- 
funded_psbt | bytes | The funded but not yet signed PSBT that sends the exact channel capacity amount to the PK script returned in the open channel message in a previous step. 
pending_chan_id | bytes | The pending channel ID of the channel to get the PSBT for.  

## lnrpc.FundingShim


Parameter | Type | Description
--------- | ---- | ----------- 
chan_point_shim | [ChanPointShim](#chanpointshim) | A channel shim where the channel point was fully constructed outside of lnd's wallet and the transaction might already be published. 
psbt_shim | [PsbtShim](#psbtshim) | A channel shim that uses a PSBT to fund and sign the channel funding transaction.  

## lnrpc.FundingShimCancel


Parameter | Type | Description
--------- | ---- | ----------- 
pending_chan_id | bytes | The pending channel ID of the channel to cancel the funding shim for.  

## lnrpc.FundingStateStepResp


This message has no parameters.


## lnrpc.FundingTransitionMsg


Parameter | Type | Description
--------- | ---- | ----------- 
shim_register | [FundingShim](#fundingshim) | The funding shim to register. This should be used before any channel funding has began by the remote party, as it is intended as a preparatory step for the full channel funding. 
shim_cancel | [FundingShimCancel](#fundingshimcancel) | Used to cancel an existing registered funding shim. 
psbt_verify | [FundingPsbtVerify](#fundingpsbtverify) | Used to continue a funding flow that was initiated to be executed through a PSBT. This step verifies that the PSBT contains the correct outputs to fund the channel. 
psbt_finalize | [FundingPsbtFinalize](#fundingpsbtfinalize) | Used to continue a funding flow that was initiated to be executed through a PSBT. This step finalizes the funded and signed PSBT, finishes negotiation with the peer and finally publishes the resulting funding transaction.  

## lnrpc.GenSeedRequest


Parameter | Type | Description
--------- | ---- | ----------- 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64. 
seed_entropy | bytes | seed_entropy is an optional 16-bytes generated via CSPRNG. If not specified, then a fresh set of randomness will be used to create the seed. When using REST, this field must be encoded as base64.  

## lnrpc.GenSeedResponse


Parameter | Type | Description
--------- | ---- | ----------- 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed. 
enciphered_seed | bytes | enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.  

## lnrpc.GetInfoRequest


This message has no parameters.


## lnrpc.GetInfoResponse


Parameter | Type | Description
--------- | ---- | ----------- 
version | string | The version of the LND software that the node is running. 
identity_pubkey | string | The identity pubkey of the current node. 
alias | string | If applicable, the alias of the current node, e.g. "bob" 
color | string | The color of the current node in hex code format 
num_pending_channels | uint32 | Number of pending channels 
num_active_channels | uint32 | Number of active channels 
num_inactive_channels | uint32 | Number of inactive channels 
num_peers | uint32 | Number of peers 
block_height | uint32 | The node's current view of the height of the best block 
block_hash | string | The node's current view of the hash of the best block 
best_header_timestamp | int64 | Timestamp of the block best known to the wallet 
synced_to_chain | bool | Whether the wallet's view is synced to the main chain 
synced_to_graph | bool | Whether we consider ourselves synced with the public channel graph. 
testnet | bool | Whether the current node is connected to testnet. This field is deprecated and the network field should be used instead 
chains | [array Chain](#chain) | A list of active chains the node is connected to 
uris | array string | The URIs of the current node. 
features | [array FeaturesEntry](#featuresentry) | Features that our node has advertised in our init message, node announcements and invoices.  

## lnrpc.GetInfoResponse.FeaturesEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint32 |  
value | [Feature](#feature) |   

## lnrpc.GetTransactionsRequest


This message has no parameters.


## lnrpc.GraphTopologySubscription


This message has no parameters.


## lnrpc.GraphTopologyUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
node_updates | [array NodeUpdate](#nodeupdate) |  
channel_updates | [array ChannelEdgeUpdate](#channeledgeupdate) |  
closed_chans | [array ClosedChannelUpdate](#closedchannelupdate) |   

## lnrpc.HTLC


Parameter | Type | Description
--------- | ---- | ----------- 
incoming | bool |  
amount | int64 |  
hash_lock | bytes |  
expiration_height | uint32 |   

## lnrpc.HTLCAttempt


Parameter | Type | Description
--------- | ---- | ----------- 
status | [HTLCStatus](#htlcstatus) | The status of the HTLC. 
route | [Route](#route) | The route taken by this HTLC. 
attempt_time_ns | int64 | The time in UNIX nanoseconds at which this HTLC was sent. 
resolve_time_ns | int64 | The time in UNIX nanoseconds at which this HTLC was settled or failed. This value will not be set if the HTLC is still IN_FLIGHT. 
failure | [Failure](#failure) | Detailed htlc failure info.  

## lnrpc.Hop


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_capacity | int64 |  
amt_to_forward | int64 |  
fee | int64 |  
expiry | uint32 |  
amt_to_forward_msat | int64 |  
fee_msat | int64 |  
pub_key | string | An optional public key of the hop. If the public key is given, the payment can be executed without relying on a copy of the channel graph. 
tlv_payload | bool | If set to true, then this hop will be encoded using the new variable length TLV format. Note that if any custom tlv_records below are specified, then this field MUST be set to true for them to be encoded properly. 
mpp_record | [MPPRecord](#mpprecord) | An optional TLV record tha singals the use of an MPP payment. If present, the receiver will enforce that that the same mpp_record is included in the final hop payload of all non-zero payments in the HTLC set. If empty, a regular single-shot payment is or was attempted. 
custom_records | [array CustomRecordsEntry](#customrecordsentry) | An optional set of key-value TLV records. This is useful within the context of the SendToRoute call as it allows callers to specify arbitrary K-V pairs to drop off at each hop within the onion.  

## lnrpc.Hop.CustomRecordsEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint64 |  
value | bytes |   

## lnrpc.HopHint


Parameter | Type | Description
--------- | ---- | ----------- 
node_id | string | The public key of the node at the start of the channel. 
chan_id | uint64 | The unique identifier of the channel. 
fee_base_msat | uint32 | The base fee of the channel denominated in millisatoshis. 
fee_proportional_millionths | uint32 | The fee rate of the channel for sending one satoshi across it denominated in millionths of a satoshi. 
cltv_expiry_delta | uint32 | The time-lock delta of the channel.  

## lnrpc.InitWalletRequest


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon. When using REST, this field must be encoded as base64. 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed. 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet. 
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) | channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.  

## lnrpc.InitWalletResponse


This message has no parameters.


## lnrpc.Invoice


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage. When using REST, this field must be encoded as base64. 
r_hash | bytes | The hash of the preimage. When using REST, this field must be encoded as base64. 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. When using REST, this field must be encoded as base64. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels. 
add_index | uint64 | The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | uint64 | The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | int64 | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | int64 | The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | int64 | The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceState](#invoicestate) | The state the invoice is in. 
htlcs | [array InvoiceHTLC](#invoicehtlc) | List of HTLCs paying to this invoice [EXPERIMENTAL]. 
features | [array FeaturesEntry](#featuresentry) | List of features advertised on the invoice. 
is_keysend | bool | Indicates if this invoice was a spontaneous payment that arrived via keysend [EXPERIMENTAL].  

## lnrpc.Invoice.FeaturesEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint32 |  
value | [Feature](#feature) |   

## lnrpc.InvoiceHTLC


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | Short channel id over which the htlc was received. 
htlc_index | uint64 | Index identifying the htlc on the channel. 
amt_msat | uint64 | The amount of the htlc in msat. 
accept_height | int32 | Block height at which this htlc was accepted. 
accept_time | int64 | Time at which this htlc was accepted. 
resolve_time | int64 | Time at which this htlc was settled or canceled. 
expiry_height | int32 | Block height at which this htlc expires. 
state | [InvoiceHTLCState](#invoicehtlcstate) | Current state the htlc is in. 
custom_records | [array CustomRecordsEntry](#customrecordsentry) | Custom tlv records. 
mpp_total_amt_msat | uint64 | The total amount of the mpp payment in msat.  

## lnrpc.InvoiceHTLC.CustomRecordsEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint64 |  
value | bytes |   

## lnrpc.InvoiceSubscription


Parameter | Type | Description
--------- | ---- | ----------- 
add_index | uint64 | If specified (non-zero), then we'll first start by sending out notifications for all added indexes with an add_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC. 
settle_index | uint64 | If specified (non-zero), then we'll first start by sending out notifications for all settled indexes with an settle_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC.  

## lnrpc.KeyDescriptor


Parameter | Type | Description
--------- | ---- | ----------- 
raw_key_bytes | bytes | The raw bytes of the key being identified. 
key_loc | [KeyLocator](#keylocator) | The key locator that identifies which key to use for signing.  

## lnrpc.KeyLocator


Parameter | Type | Description
--------- | ---- | ----------- 
key_family | int32 | The family of key being identified. 
key_index | int32 | The precise index of the key being identified.  

## lnrpc.LightningAddress


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | string | The identity pubkey of the Lightning node 
host | string | The network location of the lightning node, e.g. `69.69.69.69:1337` or / `localhost:10011`  

## lnrpc.LightningNode


Parameter | Type | Description
--------- | ---- | ----------- 
last_update | uint32 |  
pub_key | string |  
alias | string |  
addresses | [array NodeAddress](#nodeaddress) |  
color | string |  
features | [array FeaturesEntry](#featuresentry) |   

## lnrpc.LightningNode.FeaturesEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint32 |  
value | [Feature](#feature) |   

## lnrpc.ListChannelsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
active_only | bool |  
inactive_only | bool |  
public_only | bool |  
private_only | bool |  
peer | bytes | Filters the response for channels with a target peer's pubkey. If peer is empty, all channels will be returned.  

## lnrpc.ListChannelsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array Channel](#channel) | The list of active channels  

## lnrpc.ListInvoiceRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pending_only | bool | If set, only invoices that are not settled and not canceled will be returned in the response. 
index_offset | uint64 | The index of an invoice that will be used as either the start or end of a query to determine which invoices should be returned in the response. 
num_max_invoices | uint64 | The max number of invoices to return in the response to this query. 
reversed | bool | If set, the invoices returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards.  

## lnrpc.ListInvoiceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
invoices | [array Invoice](#invoice) | A list of invoices from the time slice of the time series specified in the request. 
last_index_offset | uint64 | The index of the last item in the set of returned invoices. This can be used to seek further, pagination style. 
first_index_offset | uint64 | The index of the last item in the set of returned invoices. This can be used to seek backwards, pagination style.  

## lnrpc.ListPaymentsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
include_incomplete | bool | If true, then return payments that have not yet fully completed. This means that pending payments, as well as failed payments will show up if this field is set to true. This flag doesn't change the meaning of the indices, which are tied to individual payments. 
index_offset | uint64 | The index of a payment that will be used as either the start or end of a query to determine which payments should be returned in the response. The index_offset is exclusive. In the case of a zero index_offset, the query will start with the oldest payment when paginating forwards, or will end with the most recent payment when paginating backwards. 
max_payments | uint64 | The maximal number of payments returned in the response to this query. 
reversed | bool | If set, the payments returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards. The order of the returned payments is always oldest first (ascending index order).  

## lnrpc.ListPaymentsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
payments | [array Payment](#payment) | The list of payments 
first_index_offset | uint64 | The index of the first item in the set of returned payments. This can be used as the index_offset to continue seeking backwards in the next request. 
last_index_offset | uint64 | The index of the last item in the set of returned payments. This can be used as the index_offset to continue seeking forwards in the next request.  

## lnrpc.ListPeersRequest


Parameter | Type | Description
--------- | ---- | ----------- 
latest_error | bool | If true, only the last error that our peer sent us will be returned with the peer's information, rather than the full set of historic errors we have stored.  

## lnrpc.ListPeersResponse


Parameter | Type | Description
--------- | ---- | ----------- 
peers | [array Peer](#peer) | The list of currently connected peers  

## lnrpc.ListUnspentRequest


Parameter | Type | Description
--------- | ---- | ----------- 
min_confs | int32 | The minimum number of confirmations to be included. 
max_confs | int32 | The maximum number of confirmations to be included.  

## lnrpc.ListUnspentResponse


Parameter | Type | Description
--------- | ---- | ----------- 
utxos | [array Utxo](#utxo) | A list of utxos  

## lnrpc.MPPRecord


Parameter | Type | Description
--------- | ---- | ----------- 
payment_addr | bytes | A unique, random identifier used to authenticate the sender as the intended payer of a multi-path payment. The payment_addr must be the same for all subpayments, and match the payment_addr provided in the receiver's invoice. The same payment_addr must be used on all subpayments. 
total_amt_msat | int64 | The total amount in milli-satoshis being sent as part of a larger multi-path payment. The caller is responsible for ensuring subpayments to the same node and payment_hash sum exactly to total_amt_msat. The same total_amt_msat must be used on all subpayments.  

## lnrpc.MacaroonPermission


Parameter | Type | Description
--------- | ---- | ----------- 
entity | string | The entity a permission grants access to. 
action | string | The action that is granted.  

## lnrpc.MultiChanBackup


Parameter | Type | Description
--------- | ---- | ----------- 
chan_points | [array ChannelPoint](#channelpoint) | Is the set of all channels that are included in this multi-channel backup. 
multi_chan_backup | bytes | A single encrypted blob containing all the static channel backups of the channel listed above. This can be stored as a single file or blob, and safely be replaced with any prior/future versions. When using REST, this field must be encoded as base64.  

## lnrpc.NetworkInfo


Parameter | Type | Description
--------- | ---- | ----------- 
graph_diameter | uint32 |  
avg_out_degree | double |  
max_out_degree | uint32 |  
num_nodes | uint32 |  
num_channels | uint32 |  
total_network_capacity | int64 |  
avg_channel_size | double |  
min_channel_size | int64 |  
max_channel_size | int64 |  
median_channel_size_sat | int64 |  
num_zombie_chans | uint64 | The number of edges marked as zombies.  

## lnrpc.NetworkInfoRequest


This message has no parameters.


## lnrpc.NewAddressRequest


Parameter | Type | Description
--------- | ---- | ----------- 
type | [AddressType](#addresstype) | The address type  

## lnrpc.NewAddressResponse


Parameter | Type | Description
--------- | ---- | ----------- 
address | string | The newly generated wallet address  

## lnrpc.NodeAddress


Parameter | Type | Description
--------- | ---- | ----------- 
network | string |  
addr | string |   

## lnrpc.NodeInfo


Parameter | Type | Description
--------- | ---- | ----------- 
node | [LightningNode](#lightningnode) | An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | uint32 | The total number of channels for the node. 
total_capacity | int64 | The sum of all channels capacity for the node, denominated in satoshis. 
channels | [array ChannelEdge](#channeledge) | A list of all public channels for the node.  

## lnrpc.NodeInfoRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded compressed public of the target node 
include_channels | bool | If true, will include all known channels associated with the node.  

## lnrpc.NodeMetricsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
types | [array NodeMetricType](#nodemetrictype) | The requested node metrics.  

## lnrpc.NodeMetricsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
betweenness_centrality | [array BetweennessCentralityEntry](#betweennesscentralityentry) | Betweenness centrality is the sum of the ratio of shortest paths that pass through the node for each pair of nodes in the graph (not counting paths starting or ending at this node). Map of node pubkey to betweenness centrality of the node. Normalized values are in the [0,1] closed interval.  

## lnrpc.NodeMetricsResponse.BetweennessCentralityEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | string |  
value | [FloatMetric](#floatmetric) |   

## lnrpc.NodePair


Parameter | Type | Description
--------- | ---- | ----------- 
from | bytes | The sending node of the pair. When using REST, this field must be encoded as base64. 
to | bytes | The receiving node of the pair. When using REST, this field must be encoded as base64.  

## lnrpc.NodeUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
addresses | array string |  
identity_key | string |  
global_features | bytes |  
alias | string |  
color | string |   

## lnrpc.OpenChannelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node to open a channel with. When using REST, this field must be encoded as base64. 
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
local_funding_amount | int64 | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | The number of satoshis to push to the remote side as part of the initial / commitment state 
target_conf | int32 | The target number of blocks that the funding transaction should be / confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / funding transaction. 
private | bool | Whether this channel should be private, not announced to the greater / network. 
min_htlc_msat | int64 | The minimum value in millisatoshi we will require for incoming HTLCs on / the channel. 
remote_csv_delay | uint32 | The delay we require on the remote's commitment transaction. If this is / not set, it will be scaled automatically with the channel size. 
min_confs | int32 | The minimum number of confirmations each one of your outputs used for / the funding transaction must satisfy. 
spend_unconfirmed | bool | Whether unconfirmed outputs should be used as inputs for the funding / transaction. 
close_address | string | Close address is an optional address which specifies the address to which funds should be paid out to upon cooperative close. This field may only be set if the peer supports the option upfront feature bit (call listpeers to check). The remote peer will only accept cooperative closes to this address if it is set.  Note: If this value is set on channel creation, you will *not* be able to cooperatively close out to a different address. 
funding_shim | [FundingShim](#fundingshim) | Funding shims are an optional argument that allow the caller to intercept certain funding functionality. For example, a shim can be provided to use a particular key for the commitment key (ideally cold) rather than use one that is generated by the wallet as normal, or signal that signing will be carried out in an interactive manner (PSBT based).  

## lnrpc.OpenStatusUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
chan_pending | [PendingUpdate](#pendingupdate) | Signals that the channel is now fully negotiated and the funding transaction published. 
chan_open | [ChannelOpenUpdate](#channelopenupdate) | Signals that the channel's funding transaction has now reached the required number of confirmations on chain and can be used. 
psbt_fund | [ReadyForPsbtFunding](#readyforpsbtfunding) | Signals that the funding process has been suspended and the construction of a PSBT that funds the channel PK script is now required. 
pending_chan_id | bytes | The pending channel ID of the created channel. This value may be used to further the funding flow manually via the FundingStateStep method.  

## lnrpc.OutPoint


Parameter | Type | Description
--------- | ---- | ----------- 
txid_bytes | bytes | Raw bytes representing the transaction id. 
txid_str | string | Reversed, hex-encoded string representing the transaction id. 
output_index | uint32 | The index of the output on the transaction.  

## lnrpc.PayReq


Parameter | Type | Description
--------- | ---- | ----------- 
destination | string |  
payment_hash | string |  
num_satoshis | int64 |  
timestamp | int64 |  
expiry | int64 |  
description | string |  
description_hash | string |  
fallback_addr | string |  
cltv_expiry | int64 |  
route_hints | [array RouteHint](#routehint) |  
payment_addr | bytes |  
num_msat | int64 |  
features | [array FeaturesEntry](#featuresentry) |   

## lnrpc.PayReq.FeaturesEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint32 |  
value | [Feature](#feature) |   

## lnrpc.PayReqString


Parameter | Type | Description
--------- | ---- | ----------- 
pay_req | string | The payment request string to be decoded  

## lnrpc.Payment


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | string | The payment hash 
value | int64 | Deprecated, use value_sat or value_msat. 
creation_date | int64 | Deprecated, use creation_time_ns 
path | array string | The path this payment took. 
fee | int64 | Deprecated, use fee_sat or fee_msat. 
payment_preimage | string | The payment preimage 
value_sat | int64 | The value of the payment in satoshis 
value_msat | int64 | The value of the payment in milli-satoshis 
payment_request | string | The optional payment request being fulfilled. 
status | [PaymentStatus](#paymentstatus) | The status of the payment. 
fee_sat | int64 | The fee paid for this payment in satoshis 
fee_msat | int64 | The fee paid for this payment in milli-satoshis 
creation_time_ns | int64 | The time in UNIX nanoseconds at which the payment was created. 
htlcs | [array HTLCAttempt](#htlcattempt) | The HTLCs made in attempt to settle the payment [EXPERIMENTAL]. 
payment_index | uint64 | The creation index of this payment. Each payment can be uniquely identified by this index, which may not strictly increment by 1 for payments made in older versions of lnd.  

## lnrpc.PaymentHash


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash_str | string | The hex-encoded payment hash of the invoice to be looked up. The passed payment hash must be exactly 32 bytes, otherwise an error is returned. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
r_hash | bytes | The payment hash of the invoice to be looked up. When using REST, this field must be encoded as base64.  

## lnrpc.Peer


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The identity pubkey of the peer 
address | string | Network address of the peer; eg `127.0.0.1:10011` 
bytes_sent | uint64 | Bytes of data transmitted to this peer 
bytes_recv | uint64 | Bytes of data transmitted from this peer 
sat_sent | int64 | Satoshis sent to this peer 
sat_recv | int64 | Satoshis received from this peer 
inbound | bool | A channel is inbound if the counterparty initiated the channel 
ping_time | int64 | Ping time to this peer 
sync_type | [SyncType](#synctype) | The type of sync we are currently performing with this peer. 
features | [array FeaturesEntry](#featuresentry) | Features advertised by the remote peer in their init message. 
errors | [array TimestampedError](#timestampederror) | The latest errors received from our peer with timestamps, limited to the 10 most recent errors. These errors are tracked across peer connections, but are not persisted across lnd restarts. Note that these errors are only stored for peers that we have channels open with, to prevent peers from spamming us with errors at no cost.  

## lnrpc.Peer.FeaturesEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint32 |  
value | [Feature](#feature) |   

## lnrpc.PeerEvent


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The identity pubkey of the peer. 
type | [EventType](#eventtype) |   

## lnrpc.PeerEventSubscription


This message has no parameters.


## lnrpc.PendingChannelsRequest


This message has no parameters.


## lnrpc.PendingChannelsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
total_limbo_balance | int64 | The balance in satoshis encumbered in pending channels 
pending_open_channels | [array PendingOpenChannel](#pendingopenchannel) | Channels pending opening 
pending_closing_channels | [array ClosedChannel](#closedchannel) | Deprecated: Channels pending closing previously contained cooperatively closed channels with a single confirmation. These channels are now considered closed from the time we see them on chain. 
pending_force_closing_channels | [array ForceClosedChannel](#forceclosedchannel) | Channels pending force closing 
waiting_close_channels | [array WaitingCloseChannel](#waitingclosechannel) | Channels waiting for closing tx to confirm  

## lnrpc.PendingChannelsResponse.ClosedChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel to be closed 
closing_txid | string | The transaction id of the closing transaction  

## lnrpc.PendingChannelsResponse.Commitments


Parameter | Type | Description
--------- | ---- | ----------- 
local_txid | string | Hash of the local version of the commitment tx. 
remote_txid | string | Hash of the remote version of the commitment tx. 
remote_pending_txid | string | Hash of the remote pending version of the commitment tx. 
local_commit_fee_sat | uint64 | The amount in satoshis calculated to be paid in fees for the local commitment. 
remote_commit_fee_sat | uint64 | The amount in satoshis calculated to be paid in fees for the remote commitment. 
remote_pending_commit_fee_sat | uint64 | The amount in satoshis calculated to be paid in fees for the remote pending commitment.  

## lnrpc.PendingChannelsResponse.ForceClosedChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel to be force closed 
closing_txid | string | The transaction id of the closing transaction 
limbo_balance | int64 | The balance in satoshis encumbered in this pending channel 
maturity_height | uint32 | The height at which funds can be swept into the wallet 
blocks_til_maturity | int32 | Remaining # of blocks until the commitment output can be swept. Negative values indicate how many blocks have passed since becoming mature. 
recovered_balance | int64 | The total value of funds successfully recovered from this channel 
pending_htlcs | [array PendingHTLC](#pendinghtlc) |  
anchor | [AnchorState](#anchorstate) |   

## lnrpc.PendingChannelsResponse.PendingChannel


Parameter | Type | Description
--------- | ---- | ----------- 
remote_node_pub | string |  
channel_point | string |  
capacity | int64 |  
local_balance | int64 |  
remote_balance | int64 |  
local_chan_reserve_sat | int64 | The minimum satoshis this node is required to reserve in its / balance. 
remote_chan_reserve_sat | int64 | The minimum satoshis the other node is required to reserve in its balance. 
initiator | [Initiator](#initiator) | The party that initiated opening the channel. 
commitment_type | [CommitmentType](#commitmenttype) | The commitment type used by this channel.  

## lnrpc.PendingChannelsResponse.PendingOpenChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel 
confirmation_height | uint32 | The height at which this channel will be confirmed 
commit_fee | int64 | The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart. 
commit_weight | int64 | The weight of the commitment transaction 
fee_per_kw | int64 | The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open.  

## lnrpc.PendingChannelsResponse.WaitingCloseChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel waiting for closing tx to confirm 
limbo_balance | int64 | The balance in satoshis encumbered in this channel 
commitments | [Commitments](#commitments) | A list of valid commitment transactions. Any of these can confirm at this point.  

## lnrpc.PendingHTLC


Parameter | Type | Description
--------- | ---- | ----------- 
incoming | bool | The direction within the channel that the htlc was sent 
amount | int64 | The total value of the htlc 
outpoint | string | The final output to be swept back to the user's wallet 
maturity_height | uint32 | The next block height at which we can spend the current stage 
blocks_til_maturity | int32 | The number of blocks remaining until the current stage can be swept. Negative values indicate how many blocks have passed since becoming mature. 
stage | uint32 | Indicates whether the htlc is in its first or second stage of recovery  

## lnrpc.PendingUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
txid | bytes |  
output_index | uint32 |   

## lnrpc.PolicyUpdateRequest


Parameter | Type | Description
--------- | ---- | ----------- 
global | bool | If set, then this update applies to all currently active channels. 
chan_point | [ChannelPoint](#channelpoint) | If set, this update will target a specific channel. 
base_fee_msat | int64 | The base fee charged regardless of the number of milli-satoshis sent. 
fee_rate | double | The effective fee rate in milli-satoshis. The precision of this value / goes up to 6 decimal places, so 1e-6. 
time_lock_delta | uint32 | The required timelock delta for HTLCs forwarded over the channel. 
max_htlc_msat | uint64 | If set, the maximum HTLC size in milli-satoshis. If unset, the maximum / HTLC will be unchanged. 
min_htlc_msat | uint64 | The minimum HTLC size in milli-satoshis. Only applied if / min_htlc_msat_specified is true. 
min_htlc_msat_specified | bool | If true, min_htlc_msat is applied.  

## lnrpc.PolicyUpdateResponse


This message has no parameters.


## lnrpc.PsbtShim


Parameter | Type | Description
--------- | ---- | ----------- 
pending_chan_id | bytes | A unique identifier of 32 random bytes that will be used as the pending channel ID to identify the PSBT state machine when interacting with it and on the wire protocol to initiate the funding request. 
base_psbt | bytes | An optional base PSBT the new channel output will be added to. If this is non-empty, it must be a binary serialized PSBT.  

## lnrpc.QueryRoutesRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded public key for the payment destination 
amt | int64 | The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive. 
final_cltv_delta | int32 | An optional CLTV delta from the current height that should be used for the timelock of the final hop. Note that unlike SendPayment, QueryRoutes does not add any additional block padding on top of final_ctlv_delta. This padding of a few blocks needs to be added manually or otherwise failures may happen when a block comes in while the payment is in flight. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment. 
ignored_nodes | array bytes | A list of nodes to ignore during path finding. When using REST, these fields must be encoded as base64. 
ignored_edges | [array EdgeLocator](#edgelocator) | Deprecated. A list of edges to ignore during path finding. 
source_pub_key | string | The source node where the request route should originated from. If empty, self is assumed. 
use_mission_control | bool | If set to true, edge probabilities from mission control will be used to get the optimal route. 
ignored_pairs | [array NodePair](#nodepair) | A list of directed node pairs that will be ignored during path finding. 
cltv_limit | uint32 | An optional maximum total time lock for the route. If the source is empty or ourselves, this should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is used as the limit. 
dest_custom_records | [array DestCustomRecordsEntry](#destcustomrecordsentry) | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. If the destination does not support the specified recrods, and error will be returned. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
route_hints | [array RouteHint](#routehint) | Optional route hints to reach the destination through private channels. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  

## lnrpc.QueryRoutesRequest.DestCustomRecordsEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint64 |  
value | bytes |   

## lnrpc.QueryRoutesResponse


Parameter | Type | Description
--------- | ---- | ----------- 
routes | [array Route](#route) | The route that results from the path finding operation. This is still a repeated field to retain backwards compatibility. 
success_prob | double | The success probability of the returned route based on the current mission control state. [EXPERIMENTAL]  

## lnrpc.ReadyForPsbtFunding


Parameter | Type | Description
--------- | ---- | ----------- 
funding_address | string | The P2WSH address of the channel funding multisig address that the below specified amount in satoshis needs to be sent to. 
funding_amount | int64 | The exact amount in satoshis that needs to be sent to the above address to fund the pending channel. 
psbt | bytes | A raw PSBT that contains the pending channel output. If a base PSBT was provided in the PsbtShim, this is the base PSBT with one additional output. If no base PSBT was specified, this is an otherwise empty PSBT with exactly one output.  

## lnrpc.RestoreBackupResponse


This message has no parameters.


## lnrpc.RestoreChanBackupRequest


Parameter | Type | Description
--------- | ---- | ----------- 
chan_backups | [ChannelBackups](#channelbackups) | The channels to restore as a list of channel/backup pairs. 
multi_chan_backup | bytes | The channels to restore in the packed multi backup format. When using REST, this field must be encoded as base64.  

## lnrpc.Route


Parameter | Type | Description
--------- | ---- | ----------- 
total_time_lock | uint32 | The cumulative (final) time lock across the entire route. This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment. 
total_fees | int64 | The sum of the fees paid at each hop within the final route. In the case of a one-hop payment, this value will be zero as we don't need to pay a fee to ourselves. 
total_amt | int64 | The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees. 
hops | [array Hop](#hop) | Contains details concerning the specific forwarding details at each hop. 
total_fees_msat | int64 | The total fees in millisatoshis. 
total_amt_msat | int64 | The total amount in millisatoshis.  

## lnrpc.RouteHint


Parameter | Type | Description
--------- | ---- | ----------- 
hop_hints | [array HopHint](#hophint) | A list of hop hints that when chained together can assist in reaching a specific destination.  

## lnrpc.RoutingPolicy


Parameter | Type | Description
--------- | ---- | ----------- 
time_lock_delta | uint32 |  
min_htlc | int64 |  
fee_base_msat | int64 |  
fee_rate_milli_msat | int64 |  
disabled | bool |  
max_htlc_msat | uint64 |  
last_update | uint32 |   

## lnrpc.SendCoinsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
addr | string | The address to send coins to 
amount | int64 | The amount in satoshis to send 
target_conf | int32 | The target number of blocks that this transaction should be confirmed / by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / transaction. 
send_all | bool | If set, then the amount field will be ignored, and lnd will attempt to send all the coins under control of the internal wallet to the specified address.  

## lnrpc.SendCoinsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The transaction ID of the transaction  

## lnrpc.SendManyRequest


Parameter | Type | Description
--------- | ---- | ----------- 
AddrToAmount | [array AddrToAmountEntry](#addrtoamountentry) | The map from addresses to amounts 
target_conf | int32 | The target number of blocks that this transaction should be confirmed / by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the / transaction.  

## lnrpc.SendManyRequest.AddrToAmountEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | string |  
value | int64 |   

## lnrpc.SendManyResponse


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The id of the transaction  

## lnrpc.SendRequest


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient. When using REST, this field must be encoded as base64. 
dest_string | string | The hex-encoded identity pubkey of the payment recipient. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
amt | int64 | The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive. 
payment_hash | bytes | The hash to use within the payment's HTLC. When using REST, this field must be encoded as base64. 
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
cltv_limit | uint32 | An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced. 
dest_custom_records | [array DestCustomRecordsEntry](#destcustomrecordsentry) | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
allow_self_payment | bool | If set, circular payments to self are permitted. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  

## lnrpc.SendRequest.DestCustomRecordsEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint64 |  
value | bytes |   

## lnrpc.SendResponse


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |  
payment_hash | bytes |   

## lnrpc.SendToRouteRequest


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. When using REST, this field must be encoded as base64. 
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields. 
route | [Route](#route) | Route that should be used to attempt to complete the payment.  

## lnrpc.SignMessageRequest


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message to be signed. When using REST, this field must be encoded as base64.  

## lnrpc.SignMessageResponse


Parameter | Type | Description
--------- | ---- | ----------- 
signature | string | The signature for the given message  

## lnrpc.StopRequest


This message has no parameters.


## lnrpc.StopResponse


This message has no parameters.


## lnrpc.TimestampedError


Parameter | Type | Description
--------- | ---- | ----------- 
timestamp | uint64 | The unix timestamp in seconds when the error occurred. 
error | string | The string representation of the error sent by our peer.  

## lnrpc.Transaction


Parameter | Type | Description
--------- | ---- | ----------- 
tx_hash | string | The transaction hash 
amount | int64 | The transaction amount, denominated in satoshis 
num_confirmations | int32 | The number of confirmations 
block_hash | string | The hash of the block this transaction was included in 
block_height | int32 | The height of the block this transaction was included in 
time_stamp | int64 | Timestamp of this transaction 
total_fees | int64 | Fees paid for this transaction 
dest_addresses | array string | Addresses that received funds for this transaction 
raw_tx_hex | string | The raw transaction hex.  

## lnrpc.TransactionDetails


Parameter | Type | Description
--------- | ---- | ----------- 
transactions | [array Transaction](#transaction) | The list of transactions relevant to the wallet.  

## lnrpc.UnlockWalletRequest


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly. When using REST, this field must be encoded as base64. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet. 
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) | channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.  

## lnrpc.UnlockWalletResponse


This message has no parameters.


## lnrpc.Utxo


Parameter | Type | Description
--------- | ---- | ----------- 
address_type | [AddressType](#addresstype) | The type of address 
address | string | The address 
amount_sat | int64 | The value of the unspent coin in satoshis 
pk_script | string | The pkscript in hex 
outpoint | [OutPoint](#outpoint) | The outpoint in format txid:n 
confirmations | int64 | The number of confirmations for the Utxo  

## lnrpc.VerifyChanBackupResponse


This message has no parameters.


## lnrpc.VerifyMessageRequest


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message over which the signature is to be verified. When using REST, this field must be encoded as base64. 
signature | string | The signature to be verified over the given message  

## lnrpc.VerifyMessageResponse


Parameter | Type | Description
--------- | ---- | ----------- 
valid | bool | Whether the signature was valid over the given message 
pubkey | string | The pubkey recovered from the signature  

## lnrpc.WalletBalanceRequest


This message has no parameters.


## lnrpc.WalletBalanceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
total_balance | int64 | The balance of the wallet 
confirmed_balance | int64 | The confirmed balance of a wallet(with >= 1 confirmations) 
unconfirmed_balance | int64 | The unconfirmed balance of a wallet(with 0 confirmations)  

## autopilotrpc.ModifyStatusRequest


Parameter | Type | Description
--------- | ---- | ----------- 
enable | bool | Whether the autopilot agent should be enabled or not.  

## autopilotrpc.ModifyStatusResponse


This message has no parameters.


## autopilotrpc.QueryScoresRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pubkeys | array string |  
ignore_local_state | bool | If set, we will ignore the local channel state when calculating scores.  

## autopilotrpc.QueryScoresResponse


Parameter | Type | Description
--------- | ---- | ----------- 
results | array HeuristicResult |   

## autopilotrpc.QueryScoresResponse.HeuristicResult


Parameter | Type | Description
--------- | ---- | ----------- 
heuristic | string |  
scores | array ScoresEntry |   

## autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | string |  
value | double |   

## autopilotrpc.SetScoresRequest


Parameter | Type | Description
--------- | ---- | ----------- 
heuristic | string | The name of the heuristic to provide scores to. 
scores | array ScoresEntry | A map from hex-encoded public keys to scores. Scores must be in the range [0.0, 1.0].  

## autopilotrpc.SetScoresRequest.ScoresEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | string |  
value | double |   

## autopilotrpc.SetScoresResponse


This message has no parameters.


## autopilotrpc.StatusRequest


This message has no parameters.


## autopilotrpc.StatusResponse


Parameter | Type | Description
--------- | ---- | ----------- 
active | bool | Indicates whether the autopilot is active or not.  

## chainrpc.BlockEpoch


Parameter | Type | Description
--------- | ---- | ----------- 
hash | bytes | The hash of the block. 
height | uint32 | The height of the block.  

## chainrpc.ConfDetails


Parameter | Type | Description
--------- | ---- | ----------- 
raw_tx | bytes | The raw bytes of the confirmed transaction. 
block_hash | bytes | The hash of the block in which the confirmed transaction was included in. 
block_height | uint32 | The height of the block in which the confirmed transaction was included in. 
tx_index | uint32 | The index of the confirmed transaction within the transaction.  

## chainrpc.ConfEvent


Parameter | Type | Description
--------- | ---- | ----------- 
conf | ConfDetails | An event that includes the confirmation details of the request (txid/ouput script). 
reorg | Reorg | An event send when the transaction of the request is reorged out of the chain.  

## chainrpc.ConfRequest


Parameter | Type | Description
--------- | ---- | ----------- 
txid | bytes | The transaction hash for which we should request a confirmation notification for. If set to a hash of all zeros, then the confirmation notification will be requested for the script instead. 
script | bytes | An output script within a transaction with the hash above which will be used by light clients to match block filters. If the transaction hash is set to a hash of all zeros, then a confirmation notification will be requested for this script instead. 
num_confs | uint32 | The number of desired confirmations the transaction/output script should reach before dispatching a confirmation notification. 
height_hint | uint32 | The earliest height in the chain for which the transaction/output script could have been included in a block. This should in most cases be set to the broadcast height of the transaction/output script.  

## chainrpc.Outpoint


Parameter | Type | Description
--------- | ---- | ----------- 
hash | bytes | The hash of the transaction. 
index | uint32 | The index of the output within the transaction.  

## chainrpc.Reorg


This message has no parameters.


## chainrpc.SpendDetails


Parameter | Type | Description
--------- | ---- | ----------- 
spending_outpoint | Outpoint | The outpoint was that spent. 
raw_spending_tx | bytes | The raw bytes of the spending transaction. 
spending_tx_hash | bytes | The hash of the spending transaction. 
spending_input_index | uint32 | The input of the spending transaction that fulfilled the spend request. 
spending_height | uint32 | The height at which the spending transaction was included in a block.  

## chainrpc.SpendEvent


Parameter | Type | Description
--------- | ---- | ----------- 
spend | SpendDetails | An event that includes the details of the spending transaction of the request (outpoint/output script). 
reorg | Reorg | An event sent when the spending transaction of the request was reorged out of the chain.  

## chainrpc.SpendRequest


Parameter | Type | Description
--------- | ---- | ----------- 
outpoint | Outpoint | The outpoint for which we should request a spend notification for. If set to a zero outpoint, then the spend notification will be requested for the script instead. 
script | bytes | The output script for the outpoint above. This will be used by light clients to match block filters. If the outpoint is set to a zero outpoint, then a spend notification will be requested for this script instead. 
height_hint | uint32 | The earliest height in the chain for which the outpoint/output script could have been spent. This should in most cases be set to the broadcast height of the outpoint/output script.  

## invoicesrpc.AddHoldInvoiceRequest


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
hash | bytes | The hash of the preimage 
value | int64 | The value of this invoice in satoshis  The fields value and value_msat are mutually exclusive. 
value_msat | int64 | The value of this invoice in millisatoshis  The fields value and value_msat are mutually exclusive. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels.  

## invoicesrpc.AddHoldInvoiceResp


Parameter | Type | Description
--------- | ---- | ----------- 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.  

## invoicesrpc.CancelInvoiceMsg


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | Hash corresponding to the (hold) invoice to cancel.  

## invoicesrpc.CancelInvoiceResp


This message has no parameters.


## invoicesrpc.SettleInvoiceMsg


Parameter | Type | Description
--------- | ---- | ----------- 
preimage | bytes | Externally discovered pre-image that should be used to settle the hold / invoice.  

## invoicesrpc.SettleInvoiceResp


This message has no parameters.


## invoicesrpc.SubscribeSingleInvoiceRequest


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash | bytes | Hash corresponding to the (hold) invoice to subscribe to.  

## routerrpc.BuildRouteRequest


Parameter | Type | Description
--------- | ---- | ----------- 
amt_msat | int64 | The amount to send expressed in msat. If set to zero, the minimum routable amount is used. 
final_cltv_delta | int32 | CLTV delta from the current height that should be used for the timelock of the final hop 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
hop_pubkeys | array bytes | A list of hops that defines the route. This does not include the source hop pubkey.  

## routerrpc.BuildRouteResponse


Parameter | Type | Description
--------- | ---- | ----------- 
route | [Route](#route) | Fully specified route that can be used to execute the payment.  

## routerrpc.ForwardEvent


Parameter | Type | Description
--------- | ---- | ----------- 
info | HtlcInfo | Info contains details about the htlc that was forwarded.  

## routerrpc.ForwardFailEvent


This message has no parameters.


## routerrpc.HtlcEvent


Parameter | Type | Description
--------- | ---- | ----------- 
incoming_channel_id | uint64 | The short channel id that the incoming htlc arrived at our node on. This value is zero for sends. 
outgoing_channel_id | uint64 | The short channel id that the outgoing htlc left our node on. This value is zero for receives. 
incoming_htlc_id | uint64 | Incoming id is the index of the incoming htlc in the incoming channel. This value is zero for sends. 
outgoing_htlc_id | uint64 | Outgoing id is the index of the outgoing htlc in the outgoing channel. This value is zero for receives. 
timestamp_ns | uint64 | The time in unix nanoseconds that the event occurred. 
event_type | EventType | The event type indicates whether the htlc was part of a send, receive or forward. 
forward_event | ForwardEvent |  
forward_fail_event | ForwardFailEvent |  
settle_event | SettleEvent |  
link_fail_event | LinkFailEvent |   

## routerrpc.HtlcInfo


Parameter | Type | Description
--------- | ---- | ----------- 
incoming_timelock | uint32 | The timelock on the incoming htlc. 
outgoing_timelock | uint32 | The timelock on the outgoing htlc. 
incoming_amt_msat | uint64 | The amount of the incoming htlc. 
outgoing_amt_msat | uint64 | The amount of the outgoing htlc.  

## routerrpc.LinkFailEvent


Parameter | Type | Description
--------- | ---- | ----------- 
info | HtlcInfo | Info contains details about the htlc that we failed. 
wire_failure | [FailureCode](#failurecode) | FailureCode is the BOLT error code for the failure. 
failure_detail | FailureDetail | FailureDetail provides additional information about the reason for the failure. This detail enriches the information provided by the wire message and may be 'no detail' if the wire message requires no additional metadata. 
failure_string | string | A string representation of the link failure.  

## routerrpc.PairData


Parameter | Type | Description
--------- | ---- | ----------- 
fail_time | int64 | Time of last failure. 
fail_amt_sat | int64 | Lowest amount that failed to forward rounded to whole sats. This may be set to zero if the failure is independent of amount. 
fail_amt_msat | int64 | Lowest amount that failed to forward in millisats. This may be set to zero if the failure is independent of amount. 
success_time | int64 | Time of last success. 
success_amt_sat | int64 | Highest amount that we could successfully forward rounded to whole sats. 
success_amt_msat | int64 | Highest amount that we could successfully forward in millisats.  

## routerrpc.PairHistory


Parameter | Type | Description
--------- | ---- | ----------- 
node_from | bytes | The source node pubkey of the pair. 
node_to | bytes | The destination node pubkey of the pair. 
history | PairData |   

## routerrpc.PaymentStatus


Parameter | Type | Description
--------- | ---- | ----------- 
state | PaymentState | Current state the payment is in. 
preimage | bytes | The pre-image of the payment when state is SUCCEEDED. 
htlcs | [array HTLCAttempt](#htlcattempt) | The HTLCs made in attempt to settle the payment.  

## routerrpc.QueryMissionControlRequest


This message has no parameters.


## routerrpc.QueryMissionControlResponse


Parameter | Type | Description
--------- | ---- | ----------- 
pairs | array PairHistory | Node pair-level mission control state.  

## routerrpc.QueryProbabilityRequest


Parameter | Type | Description
--------- | ---- | ----------- 
from_node | bytes | The source node pubkey of the pair. 
to_node | bytes | The destination node pubkey of the pair. 
amt_msat | int64 | The amount for which to calculate a probability.  

## routerrpc.QueryProbabilityResponse


Parameter | Type | Description
--------- | ---- | ----------- 
probability | double | The success probability for the requested pair. 
history | PairData | The historical data for the requested pair.  

## routerrpc.ResetMissionControlRequest


This message has no parameters.


## routerrpc.ResetMissionControlResponse


This message has no parameters.


## routerrpc.RouteFeeRequest


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The destination once wishes to obtain a routing fee quote to. 
amt_sat | int64 | The amount one wishes to send to the target destination.  

## routerrpc.RouteFeeResponse


Parameter | Type | Description
--------- | ---- | ----------- 
routing_fee_msat | int64 | A lower bound of the estimated fee to the target destination within the network, expressed in milli-satoshis. 
time_lock_delay | int64 | An estimate of the worst case time delay that can occur. Note that callers will still need to factor in the final CLTV delta of the last hop into this value.  

## routerrpc.SendPaymentRequest


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient 
amt | int64 | Number of satoshis to send.  The fields amt and amt_msat are mutually exclusive. 
amt_msat | int64 | Number of millisatoshis to send.  The fields amt and amt_msat are mutually exclusive. 
payment_hash | bytes | The hash to use within the payment's HTLC 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. The amount in the payment request may be zero. In that case it is required to set the amt field as well. If no payment request is specified, the following fields are required: dest, amt and payment_hash. 
timeout_seconds | int32 | An upper limit on the amount of time we should spend when attempting to fulfill the payment. This is expressed in seconds. If we cannot make a successful payment within this time frame, an error will be returned. This field must be non-zero. 
fee_limit_sat | int64 | The maximum number of satoshis that will be paid as a fee of the payment. If this field is left to the default value of 0, only zero-fee routes will be considered. This usually means single hop routes connecting directly to the destination. To send the payment without a fee limit, use max int here.  The fields fee_limit_sat and fee_limit_msat are mutually exclusive. 
fee_limit_msat | int64 | The maximum number of millisatoshis that will be paid as a fee of the payment. If this field is left to the default value of 0, only zero-fee routes will be considered. This usually means single hop routes connecting directly to the destination. To send the payment without a fee limit, use max int here.  The fields fee_limit_sat and fee_limit_msat are mutually exclusive. 
outgoing_chan_id | uint64 | The channel id of the channel that must be taken to the first hop. If zero, any channel may be used. 
last_hop_pubkey | bytes | The pubkey of the last hop of the route. If empty, any hop may be used. 
cltv_limit | int32 | An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced. 
route_hints | [array RouteHint](#routehint) | Optional route hints to reach the destination through private channels. 
dest_custom_records | array DestCustomRecordsEntry | An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64. 
allow_self_payment | bool | If set, circular payments to self are permitted. 
dest_features | [array FeatureBit](#featurebit) | Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.  

## routerrpc.SendPaymentRequest.DestCustomRecordsEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | uint64 |  
value | bytes |   

## routerrpc.SendToRouteRequest


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. 
route | [Route](#route) | Route that should be used to attempt to complete the payment.  

## routerrpc.SendToRouteResponse


Parameter | Type | Description
--------- | ---- | ----------- 
preimage | bytes | The preimage obtained by making the payment. 
failure | [Failure](#failure) | The failure message in case the payment failed.  

## routerrpc.SettleEvent


This message has no parameters.


## routerrpc.SubscribeHtlcEventsRequest


This message has no parameters.


## routerrpc.TrackPaymentRequest


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The hash of the payment to look up.  

## signrpc.InputScript


Parameter | Type | Description
--------- | ---- | ----------- 
witness | array bytes | The serializes witness stack for the specified input. 
sig_script | bytes | The optional sig script for the specified witness that will only be set if the input specified is a nested p2sh witness program.  

## signrpc.InputScriptResp


Parameter | Type | Description
--------- | ---- | ----------- 
input_scripts | array InputScript | The set of fully valid input scripts requested.  

## signrpc.KeyDescriptor


Parameter | Type | Description
--------- | ---- | ----------- 
raw_key_bytes | bytes | The raw bytes of the key being identified. Either this or the KeyLocator must be specified. 
key_loc | KeyLocator | The key locator that identifies which key to use for signing. Either this or the raw bytes of the target key must be specified.  

## signrpc.KeyLocator


Parameter | Type | Description
--------- | ---- | ----------- 
key_family | int32 | The family of key being identified. 
key_index | int32 | The precise index of the key being identified.  

## signrpc.SharedKeyRequest


Parameter | Type | Description
--------- | ---- | ----------- 
ephemeral_pubkey | bytes | The ephemeral public key to use for the DH key derivation. 
key_loc | KeyLocator | The optional key locator of the local key that should be used. If this parameter is not set then the node's identity private key will be used.  

## signrpc.SharedKeyResponse


Parameter | Type | Description
--------- | ---- | ----------- 
shared_key | bytes | The shared public key, hashed with sha256.  

## signrpc.SignDescriptor


Parameter | Type | Description
--------- | ---- | ----------- 
key_desc | KeyDescriptor | A descriptor that precisely describes *which* key to use for signing. This may provide the raw public key directly, or require the Signer to re-derive the key according to the populated derivation path. 
single_tweak | bytes | A scalar value that will be added to the private key corresponding to the above public key to obtain the private key to be used to sign this input. This value is typically derived via the following computation:  derivedKey = privkey + sha256(perCommitmentPoint || pubKey) mod N 
double_tweak | bytes | A private key that will be used in combination with its corresponding private key to derive the private key that is to be used to sign the target input. Within the Lightning protocol, this value is typically the commitment secret from a previously revoked commitment transaction. This value is in combination with two hash values, and the original private key to derive the private key to be used when signing.  k = (privKey*sha256(pubKey || tweakPub) + tweakPriv*sha256(tweakPub || pubKey)) mod N 
witness_script | bytes | The full script required to properly redeem the output.  This field will only be populated if a p2wsh or a p2sh output is being signed. 
output | TxOut | A description of the output being spent. The value and script MUST be provided. 
sighash | uint32 | The target sighash type that should be used when generating the final sighash, and signature. 
input_index | int32 | The target input within the transaction that should be signed.  

## signrpc.SignMessageReq


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message to be signed. 
key_loc | KeyLocator | The key locator that identifies which key to use for signing.  

## signrpc.SignMessageResp


Parameter | Type | Description
--------- | ---- | ----------- 
signature | bytes | The signature for the given message in the fixed-size LN wire format.  

## signrpc.SignReq


Parameter | Type | Description
--------- | ---- | ----------- 
raw_tx_bytes | bytes | The raw bytes of the transaction to be signed. 
sign_descs | array SignDescriptor | A set of sign descriptors, for each input to be signed.  

## signrpc.SignResp


Parameter | Type | Description
--------- | ---- | ----------- 
raw_sigs | array bytes | A set of signatures realized in a fixed 64-byte format ordered in ascending input order.  

## signrpc.TxOut


Parameter | Type | Description
--------- | ---- | ----------- 
value | int64 | The value of the output being spent. 
pk_script | bytes | The script of the output being spent.  

## signrpc.VerifyMessageReq


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message over which the signature is to be verified. 
signature | bytes | The fixed-size LN wire encoded signature to be verified over the given message. 
pubkey | bytes | The public key the signature has to be valid for.  

## signrpc.VerifyMessageResp


Parameter | Type | Description
--------- | ---- | ----------- 
valid | bool | Whether the signature was valid over the given message.  

## walletrpc.AddrRequest


This message has no parameters.


## walletrpc.AddrResponse


Parameter | Type | Description
--------- | ---- | ----------- 
addr | string | The address encoded using a bech32 format.  

## walletrpc.BumpFeeRequest


Parameter | Type | Description
--------- | ---- | ----------- 
outpoint | [OutPoint](#outpoint) | The input we're attempting to bump the fee of. 
target_conf | uint32 | The target number of blocks that the input should be spent within. 
sat_per_byte | uint32 | The fee rate, expressed in sat/byte, that should be used to spend the input with. 
force | bool | Whether this input must be force-swept. This means that it is swept even if it has a negative yield.  

## walletrpc.BumpFeeResponse


This message has no parameters.


## walletrpc.EstimateFeeRequest


Parameter | Type | Description
--------- | ---- | ----------- 
conf_target | int32 | The number of confirmations to shoot for when estimating the fee.  

## walletrpc.EstimateFeeResponse


Parameter | Type | Description
--------- | ---- | ----------- 
sat_per_kw | int64 | The amount of satoshis per kw that should be used in order to reach the confirmation target in the request.  

## walletrpc.KeyReq


Parameter | Type | Description
--------- | ---- | ----------- 
key_finger_print | int32 | Is the key finger print of the root pubkey that this request is targeting. This allows the WalletKit to possibly serve out keys for multiple HD chains via public derivation. 
key_family | int32 | The target key family to derive a key from. In other contexts, this is known as the "account".  

## walletrpc.PendingSweep


Parameter | Type | Description
--------- | ---- | ----------- 
outpoint | [OutPoint](#outpoint) | The outpoint of the output we're attempting to sweep. 
witness_type | WitnessType | The witness type of the output we're attempting to sweep. 
amount_sat | uint32 | The value of the output we're attempting to sweep. 
sat_per_byte | uint32 | The fee rate we'll use to sweep the output. The fee rate is only determined once a sweeping transaction for the output is created, so it's possible for this to be 0 before this. 
broadcast_attempts | uint32 | The number of broadcast attempts we've made to sweep the output. 
next_broadcast_height | uint32 | The next height of the chain at which we'll attempt to broadcast the sweep transaction of the output. 
requested_conf_target | uint32 | The requested confirmation target for this output. 
requested_sat_per_byte | uint32 | The requested fee rate, expressed in sat/byte, for this output. 
force | bool | Whether this input must be force-swept. This means that it is swept even if it has a negative yield.  

## walletrpc.PendingSweepsRequest


This message has no parameters.


## walletrpc.PendingSweepsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
pending_sweeps | array PendingSweep | The set of outputs currently being swept by lnd's central batching engine.  

## walletrpc.PublishResponse


Parameter | Type | Description
--------- | ---- | ----------- 
publish_error | string | If blank, then no error occurred and the transaction was successfully published. If not the empty string, then a string representation of the broadcast error.  TODO(roasbeef): map to a proper enum type  

## walletrpc.SendOutputsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
sat_per_kw | int64 | The number of satoshis per kilo weight that should be used when crafting this transaction. 
outputs | array TxOut | A slice of the outputs that should be created in the transaction produced.  

## walletrpc.SendOutputsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
raw_tx | bytes | The serialized transaction sent out on the network.  

## walletrpc.Transaction


Parameter | Type | Description
--------- | ---- | ----------- 
tx_hex | bytes | The raw serialized transaction.  

## watchtowerrpc.GetInfoRequest


This message has no parameters.


## watchtowerrpc.GetInfoResponse


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The public key of the watchtower. 
listeners | array string | The listening addresses of the watchtower. 
uris | array string | The URIs of the watchtower.  

## wtclientrpc.AddTowerRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower to add. 
address | string | A network address the watchtower is reachable over.  

## wtclientrpc.AddTowerResponse


This message has no parameters.


## wtclientrpc.GetTowerInfoRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower to retrieve information for. 
include_sessions | bool | Whether we should include sessions with the watchtower in the response.  

## wtclientrpc.ListTowersRequest


Parameter | Type | Description
--------- | ---- | ----------- 
include_sessions | bool | Whether we should include sessions with the watchtower in the response.  

## wtclientrpc.ListTowersResponse


Parameter | Type | Description
--------- | ---- | ----------- 
towers | array Tower | The list of watchtowers available for new backups.  

## wtclientrpc.PolicyRequest


This message has no parameters.


## wtclientrpc.PolicyResponse


Parameter | Type | Description
--------- | ---- | ----------- 
max_updates | uint32 | The maximum number of updates each session we negotiate with watchtowers should allow. 
sweep_sat_per_byte | uint32 | The fee rate, in satoshis per vbyte, that will be used by watchtowers for justice transactions in response to channel breaches.  

## wtclientrpc.RemoveTowerRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower to remove. 
address | string | If set, then the record for this address will be removed, indicating that is is stale. Otherwise, the watchtower will no longer be used for future session negotiations and backups.  

## wtclientrpc.RemoveTowerResponse


This message has no parameters.


## wtclientrpc.StatsRequest


This message has no parameters.


## wtclientrpc.StatsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
num_backups | uint32 | The total number of backups made to all active and exhausted watchtower sessions. 
num_pending_backups | uint32 | The total number of backups that are pending to be acknowledged by all active and exhausted watchtower sessions. 
num_failed_backups | uint32 | The total number of backups that all active and exhausted watchtower sessions have failed to acknowledge. 
num_sessions_acquired | uint32 | The total number of new sessions made to watchtowers. 
num_sessions_exhausted | uint32 | The total number of watchtower sessions that have been exhausted.  

## wtclientrpc.Tower


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | bytes | The identifying public key of the watchtower. 
addresses | array string | The list of addresses the watchtower is reachable over. 
active_session_candidate | bool | Whether the watchtower is currently a candidate for new sessions. 
num_sessions | uint32 | The number of sessions that have been negotiated with the watchtower. 
sessions | array TowerSession | The list of sessions that have been negotiated with the watchtower.  

## wtclientrpc.TowerSession


Parameter | Type | Description
--------- | ---- | ----------- 
num_backups | uint32 | The total number of successful backups that have been made to the watchtower session. 
num_pending_backups | uint32 | The total number of backups in the session that are currently pending to be acknowledged by the watchtower. 
max_backups | uint32 | The maximum number of backups allowed by the watchtower session. 
sweep_sat_per_byte | uint32 | The fee rate, in satoshis per vbyte, that will be used by the watchtower for the justice transaction in the event of a channel breach.  
