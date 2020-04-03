---
title: LND REST API Reference

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

# LND REST API Reference

Welcome to the REST API reference documentation for LND, the Lightning Network
Daemon.

This site features the API documentation for Python and JavaScript, along with
barebones examples using `curl`, for HTTP requests. It is intended for those who
already understand how to work with LND. If this is your first time or you need
a refresher, you may consider perusing our LND developer site featuring a
tutorial, resources and guides at [dev.lightning.community](https://dev.lightning.community).

The examples to the right assume that the there is a local `lnd` instance
running and listening for REST connections on port 8080. `LND_DIR` will be used
as a placeholder to denote the base directory of the `lnd` instance. By default,
this is `~/.lnd` on Linux and `~/Library/Application Support/Lnd` on macOS.

At the time of writing this documentation, two things are needed in order to
make an HTTP request to an `lnd` instance: a TLS/SSL connection and a macaroon
used for RPC authentication. The examples to the right will show how these can
be used in order to make a successful, secure, and authenticated HTTP request.

The original `*.swagger.js` files from which the gRPC documentation was generated
can be found here:

- [`rpc.swagger.json`](https://github.com/lightningnetwork/lnd/blob/7e6f3ece239e94f05da1a5d0492ce9767069dbbc/lnrpc/rpc.swagger.json)


NOTE: The `byte` field type must be set as the URL safe base64 encoded string
representation of a raw byte array.


This is the reference for the **REST API**. Alternatively, there is also a [gRPC
API which is documented here](../).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`7e6f3ece239e94f05da1a5d0492ce9767069dbbc`](https://github.com/lightningnetwork/lnd/tree/7e6f3ece239e94f05da1a5d0492ce9767069dbbc).</small>


# /v1/balance/blockchain


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/balance/blockchain 
{ 
    "total_balance": <string>, 
    "confirmed_balance": <string>, 
    "unconfirmed_balance": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/balance/blockchain'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "total_balance": <string>, 
    "confirmed_balance": <string>, 
    "unconfirmed_balance": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/balance/blockchain',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "total_balance": <string>, 
//      "confirmed_balance": <string>, 
//      "unconfirmed_balance": <string>, 
//  }
```

### GET /v1/balance/blockchain
WalletBalance returns total unspent outputs(confirmed and unconfirmed), all confirmed unspent outputs and all unconfirmed unspent outputs under control of the wallet.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
total_balance | string | / The balance of the wallet 
confirmed_balance | string | / The confirmed balance of a wallet(with >= 1 confirmations) 
unconfirmed_balance | string | / The unconfirmed balance of a wallet(with 0 confirmations)  



# /v1/balance/channels


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/balance/channels 
{ 
    "balance": <string>, 
    "pending_open_balance": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/balance/channels'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "balance": <string>, 
    "pending_open_balance": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/balance/channels',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "balance": <string>, 
//      "pending_open_balance": <string>, 
//  }
```

### GET /v1/balance/channels
ChannelBalance returns the total funds available across all open channels in satoshis.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
balance | string | / Sum of channels balances denominated in satoshis 
pending_open_balance | string | / Sum of channels pending balances denominated in satoshis  



# /v1/changepassword


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/changepassword  \
    -d '{ "current_password":<byte>,"new_password":<byte>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/changepassword'
>>> cert_path = 'LND_DIR/tls.cert'
>>> data = { 
        'current_password': base64.b64encode(<byte>).decode(), 
        'new_password': base64.b64encode(<byte>).decode(), 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
let requestBody = { 
    current_password: <byte>,
    new_password: <byte>,
}
let options = {
  url: 'https://localhost:8080/v1/changepassword',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/changepassword
ChangePassword changes the password of the encrypted wallet. This will automatically unlock the wallet database if successful.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
current_password | byte | body | * current_password should be the current valid passphrase used to unlock the daemon. When using REST, this field must be encoded as base64.
new_password | byte | body | * new_password should be the new passphrase that will be needed to unlock the daemon. When using REST, this field must be encoded as base64.

### Response 

This response has no parameters.




# /v1/channels


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels 
{ 
    "channels": <array lnrpcChannel>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "channels": <array lnrpcChannel>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "channels": <array lnrpcChannel>, 
//  }
```

### GET /v1/channels
ListChannels returns a description of all the open channels that this node is a participant in.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
active_only | boolean | query | 
inactive_only | boolean | query | 
public_only | boolean | query | 
private_only | boolean | query | 
peer | string | query | * Filters the response for channels with a target peer's pubkey. If peer is empty, all channels will be returned.

### Response 

Field | Type | Description
----- | ---- | ----------- 
channels | [array lnrpcChannel](#lnrpcchannel) | / The list of active channels  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels  \
    -d '{ "node_pubkey":<byte>,"node_pubkey_string":<string>,"local_funding_amount":<string>,"push_sat":<string>,"target_conf":<int32>,"sat_per_byte":<string>,"private":<boolean>,"min_htlc_msat":<string>,"remote_csv_delay":<int64>,"min_confs":<int32>,"spend_unconfirmed":<boolean>,"close_address":<string>,"funding_shim":<lnrpcFundingShim>, }' 
{ 
    "funding_txid_bytes": <byte>, 
    "funding_txid_str": <string>, 
    "output_index": <int64>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'node_pubkey': base64.b64encode(<byte>).decode(), 
        'node_pubkey_string': <string>, 
        'local_funding_amount': <string>, 
        'push_sat': <string>, 
        'target_conf': <int32>, 
        'sat_per_byte': <string>, 
        'private': <boolean>, 
        'min_htlc_msat': <string>, 
        'remote_csv_delay': <int64>, 
        'min_confs': <int32>, 
        'spend_unconfirmed': <boolean>, 
        'close_address': <string>, 
        'funding_shim': <lnrpcFundingShim>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "funding_txid_bytes": <byte>, 
    "funding_txid_str": <string>, 
    "output_index": <int64>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    node_pubkey: <byte>,
    node_pubkey_string: <string>,
    local_funding_amount: <string>,
    push_sat: <string>,
    target_conf: <int32>,
    sat_per_byte: <string>,
    private: <boolean>,
    min_htlc_msat: <string>,
    remote_csv_delay: <int64>,
    min_confs: <int32>,
    spend_unconfirmed: <boolean>,
    close_address: <string>,
    funding_shim: <lnrpcFundingShim>,
}
let options = {
  url: 'https://localhost:8080/v1/channels',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "funding_txid_bytes": <byte>, 
//      "funding_txid_str": <string>, 
//      "output_index": <int64>, 
//  }
```

### POST /v1/channels
* OpenChannelSync is a synchronous version of the OpenChannel RPC call. This call is meant to be consumed by clients to the REST proxy. As with all other sync calls, all byte slices are intended to be populated as hex encoded strings.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
node_pubkey | byte | body | * The pubkey of the node to open a channel with. When using REST, this field must be encoded as base64.
node_pubkey_string | string | body | * The hex encoded pubkey of the node to open a channel with. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
local_funding_amount | string | body | / The number of satoshis the wallet should commit to the channel
push_sat | string | body | / The number of satoshis to push to the remote side as part of the initial / commitment state
target_conf | int32 | body | / The target number of blocks that the funding transaction should be / confirmed by.
sat_per_byte | string | body | / A manual fee rate set in sat/byte that should be used when crafting the / funding transaction.
private | boolean | body | / Whether this channel should be private, not announced to the greater / network.
min_htlc_msat | string | body | / The minimum value in millisatoshi we will require for incoming HTLCs on / the channel.
remote_csv_delay | int64 | body | / The delay we require on the remote's commitment transaction. If this is / not set, it will be scaled automatically with the channel size.
min_confs | int32 | body | / The minimum number of confirmations each one of your outputs used for / the funding transaction must satisfy.
spend_unconfirmed | boolean | body | / Whether unconfirmed outputs should be used as inputs for the funding / transaction.
close_address | string | body | Close address is an optional address which specifies the address to which funds should be paid out to upon cooperative close. This field may only be set if the peer supports the option upfront feature bit (call listpeers to check). The remote peer will only accept cooperative closes to this address if it is set.  Note: If this value is set on channel creation, you will *not* be able to cooperatively close out to a different address.
funding_shim | [lnrpcFundingShim](#lnrpcfundingshim) | body | * Funding shims are an optional argument that allow the caller to intercept certain funding functionality. For example, a shim can be provided to use a particular key for the commitment key (ideally cold) rather than use one that is generated by the wallet as normal, or signal that signing will be carried out in an interactive manner (PSBT based).

### Response 

Field | Type | Description
----- | ---- | ----------- 
funding_txid_bytes | byte | * Txid of the funding transaction. When using REST, this field must be encoded as base64. 
funding_txid_str | string | * Hex-encoded string representing the byte-reversed hash of the funding transaction. 
output_index | int64 | / The index of the output of the funding transaction  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X DELETE --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index} 
{ 
    "result": <lnrpcCloseStatusUpdate>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.delete(url, headers=headers, verify=cert_path, stream=True)
>>> for raw_response in r.iter_lines():
>>>     json_response = json.loads(raw_response)
>>>     print(json_response)
{ 
    "result": <lnrpcCloseStatusUpdate>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.delete(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <lnrpcCloseStatusUpdate>, 
//      "error": <runtimeStreamError>, 
//  }



// --------------------------
// Example with websockets:
// --------------------------
const WebSocket = require('ws');
const fs = require('fs');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let ws = new WebSocket('wss://localhost:8080/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}?method=DELETE', {
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  headers: {
    'Grpc-Metadata-Macaroon': macaroon,
  },
});
let requestBody = { 
  channel_point.funding_txid_str: <string>,
  channel_point.output_index: <int64>,
  channel_point.funding_txid_bytes: <string>,
  force: <boolean>,
  target_conf: <int32>,
  sat_per_byte: <string>,
  delivery_address: <string>,
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
//  { 
//      "result": <lnrpcCloseStatusUpdate>, 
//      "error": <runtimeStreamError>, 
//  }


```

### DELETE /v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}
CloseChannel attempts to close an active channel identified by its channel outpoint (ChannelPoint). The actions of this method can additionally be augmented to attempt a force close after a timeout period in the case of an inactive peer. If a non-force close (cooperative closure) is requested, then the user can specify either a target number of blocks until the closure transaction is confirmed, or a manual fee rate. If neither are specified, then a default lax, block confirmation target is used.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
channel_point.funding_txid_str | string | path | * Hex-encoded string representing the byte-reversed hash of the funding transaction.
channel_point.output_index | int64 | path | / The index of the output of the funding transaction
channel_point.funding_txid_bytes | string | query | * Txid of the funding transaction. When using REST, this field must be encoded as base64.
force | boolean | query | / If true, then the channel will be closed forcibly. This means the / current commitment transaction will be signed and broadcast.
target_conf | int32 | query | / The target number of blocks that the closure transaction should be / confirmed by.
sat_per_byte | string | query | / A manual fee rate set in sat/byte that should be used when crafting the / closure transaction.
delivery_address | string | query | An optional address to send funds to in the case of a cooperative close. If the channel was opened with an upfront shutdown script and this field is set, the request to close will fail because the channel must pay out to the upfront shutdown addresss.

### Response (streaming)

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcCloseStatusUpdate](#lnrpcclosestatusupdate) |  
error | [runtimeStreamError](#runtimestreamerror) |   



# /v1/channels/abandon


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X DELETE --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index} 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.delete(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.delete(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### DELETE /v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}
AbandonChannel removes all channel state from the database except for a close summary. This method can be used to get rid of permanently unusable channels due to bugs fixed in newer versions of lnd. Only available when in debug builds of lnd.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
channel_point.funding_txid_str | string | path | * Hex-encoded string representing the byte-reversed hash of the funding transaction.
channel_point.output_index | int64 | path | / The index of the output of the funding transaction
channel_point.funding_txid_bytes | string | query | * Txid of the funding transaction. When using REST, this field must be encoded as base64.

### Response 

This response has no parameters.




# /v1/channels/backup


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup 
{ 
    "result": <lnrpcChanBackupSnapshot>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/backup'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "result": <lnrpcChanBackupSnapshot>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels/backup',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <lnrpcChanBackupSnapshot>, 
//      "error": <runtimeStreamError>, 
//  }
```

### GET /v1/channels/backup
* ExportAllChannelBackups returns static channel backups for all existing channels known to lnd. A set of regular singular static channel backups for each channel are returned. Additionally, a multi-channel backup is returned as well, which contains a single encrypted blob containing the backups of each channel.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) |  
error | [runtimeStreamError](#runtimestreamerror) |   



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index} 
{ 
    "chan_point": <lnrpcChannelPoint>, 
    "chan_backup": <byte>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "chan_point": <lnrpcChannelPoint>, 
    "chan_backup": <byte>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "chan_point": <lnrpcChannelPoint>, 
//      "chan_backup": <byte>, 
//  }
```

### GET /v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index}
ExportChannelBackup attempts to return an encrypted static channel backup for the target channel identified by it channel point. The backup is encrypted with a key generated from the aezeed seed of the user. The returned backup can either be restored using the RestoreChannelBackup method once lnd is running, or via the InitWallet and UnlockWallet methods from the WalletUnlocker service.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
chan_point.funding_txid_str | string | path | * Hex-encoded string representing the byte-reversed hash of the funding transaction.
chan_point.output_index | int64 | path | / The index of the output of the funding transaction
chan_point.funding_txid_bytes | string | query | * Txid of the funding transaction. When using REST, this field must be encoded as base64.

### Response 

Field | Type | Description
----- | ---- | ----------- 
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | * Identifies the channel that this backup belongs to. 
chan_backup | byte | * Is an encrypted single-chan backup. this can be passed to RestoreChannelBackups, or the WalletUnlocker Init and Unlock methods in order to trigger the recovery protocol. When using REST, this field must be encoded as base64.  



# /v1/channels/backup/restore


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup/restore  \
    -d '{ "chan_backups":<lnrpcChannelBackups>,"multi_chan_backup":<byte>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/backup/restore'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'chan_backups': <lnrpcChannelBackups>, 
        'multi_chan_backup': base64.b64encode(<byte>).decode(), 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    chan_backups: <lnrpcChannelBackups>,
    multi_chan_backup: <byte>,
}
let options = {
  url: 'https://localhost:8080/v1/channels/backup/restore',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/channels/backup/restore
RestoreChannelBackups accepts a set of singular channel backups, or a single encrypted multi-chan backup and attempts to recover any funds remaining within the channel. If we are able to unpack the backup, then the new channel will be shown under listchannels, as well as pending channels.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
chan_backups | [lnrpcChannelBackups](#lnrpcchannelbackups) | body | * The channels to restore as a list of channel/backup pairs.
multi_chan_backup | byte | body | * The channels to restore in the packed multi backup format. When using REST, this field must be encoded as base64.

### Response 

This response has no parameters.




# /v1/channels/backup/verify


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup/verify  \
    -d '{ "result":<lnrpcChanBackupSnapshot>,"error":<runtimeStreamError>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/backup/verify'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'result': <lnrpcChanBackupSnapshot>, 
        'error': <runtimeStreamError>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    result: <lnrpcChanBackupSnapshot>,
    error: <runtimeStreamError>,
}
let options = {
  url: 'https://localhost:8080/v1/channels/backup/verify',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/channels/backup/verify
* VerifyChanBackup allows a caller to verify the integrity of a channel backup snapshot. This method will accept either a packed Single or a packed Multi. Specifying both will result in an error.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
result | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) | body | 
error | [runtimeStreamError](#runtimestreamerror) | body | 

### Response 

This response has no parameters.




# /v1/channels/closed


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/closed 
{ 
    "channels": <array lnrpcChannelCloseSummary>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/closed'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "channels": <array lnrpcChannelCloseSummary>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels/closed',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "channels": <array lnrpcChannelCloseSummary>, 
//  }
```

### GET /v1/channels/closed
ClosedChannels returns a description of all the closed channels that this node was a participant in.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
cooperative | boolean | query | 
local_force | boolean | query | 
remote_force | boolean | query | 
breach | boolean | query | 
funding_canceled | boolean | query | 
abandoned | boolean | query | 

### Response 

Field | Type | Description
----- | ---- | ----------- 
channels | [array lnrpcChannelCloseSummary](#lnrpcchannelclosesummary) |   



# /v1/channels/pending


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/pending 
{ 
    "total_limbo_balance": <string>, 
    "pending_open_channels": <array PendingChannelsResponsePendingOpenChannel>, 
    "pending_closing_channels": <array PendingChannelsResponseClosedChannel>, 
    "pending_force_closing_channels": <array PendingChannelsResponseForceClosedChannel>, 
    "waiting_close_channels": <array PendingChannelsResponseWaitingCloseChannel>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/pending'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "total_limbo_balance": <string>, 
    "pending_open_channels": <array PendingChannelsResponsePendingOpenChannel>, 
    "pending_closing_channels": <array PendingChannelsResponseClosedChannel>, 
    "pending_force_closing_channels": <array PendingChannelsResponseForceClosedChannel>, 
    "waiting_close_channels": <array PendingChannelsResponseWaitingCloseChannel>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/channels/pending',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "total_limbo_balance": <string>, 
//      "pending_open_channels": <array PendingChannelsResponsePendingOpenChannel>, 
//      "pending_closing_channels": <array PendingChannelsResponseClosedChannel>, 
//      "pending_force_closing_channels": <array PendingChannelsResponseForceClosedChannel>, 
//      "waiting_close_channels": <array PendingChannelsResponseWaitingCloseChannel>, 
//  }
```

### GET /v1/channels/pending
PendingChannels returns a list of all the channels that are currently considered "pending". A channel is pending if it has finished the funding workflow and is waiting for confirmations for the funding txn, or is in the process of closure, either initiated cooperatively or non-cooperatively.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
total_limbo_balance | string | / The balance in satoshis encumbered in pending channels 
pending_open_channels | [array PendingChannelsResponsePendingOpenChannel](#pendingchannelsresponsependingopenchannel) | / Channels pending opening 
pending_closing_channels | [array PendingChannelsResponseClosedChannel](#pendingchannelsresponseclosedchannel) | Deprecated: Channels pending closing previously contained cooperatively closed channels with a single confirmation. These channels are now considered closed from the time we see them on chain. 
pending_force_closing_channels | [array PendingChannelsResponseForceClosedChannel](#pendingchannelsresponseforceclosedchannel) | / Channels pending force closing 
waiting_close_channels | [array PendingChannelsResponseWaitingCloseChannel](#pendingchannelsresponsewaitingclosechannel) | / Channels waiting for closing tx to confirm  



# /v1/channels/transactions


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/transactions  \
    -d '{ "dest":<byte>,"dest_string":<string>,"amt":<string>,"amt_msat":<string>,"payment_hash":<byte>,"payment_hash_string":<string>,"payment_request":<string>,"final_cltv_delta":<int32>,"fee_limit":<lnrpcFeeLimit>,"outgoing_chan_id":<string>,"last_hop_pubkey":<byte>,"cltv_limit":<int64>,"dest_custom_records":<object>,"allow_self_payment":<boolean>,"dest_features":<array lnrpcFeatureBit>, }' 
{ 
    "result": <lnrpcSendResponse>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/transactions'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'dest': base64.b64encode(<byte>).decode(), 
        'dest_string': <string>, 
        'amt': <string>, 
        'amt_msat': <string>, 
        'payment_hash': base64.b64encode(<byte>).decode(), 
        'payment_hash_string': <string>, 
        'payment_request': <string>, 
        'final_cltv_delta': <int32>, 
        'fee_limit': <lnrpcFeeLimit>, 
        'outgoing_chan_id': <string>, 
        'last_hop_pubkey': base64.b64encode(<byte>).decode(), 
        'cltv_limit': <int64>, 
        'dest_custom_records': <object>, 
        'allow_self_payment': <boolean>, 
        'dest_features': <array lnrpcFeatureBit>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "result": <lnrpcSendResponse>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    dest: <byte>,
    dest_string: <string>,
    amt: <string>,
    amt_msat: <string>,
    payment_hash: <byte>,
    payment_hash_string: <string>,
    payment_request: <string>,
    final_cltv_delta: <int32>,
    fee_limit: <lnrpcFeeLimit>,
    outgoing_chan_id: <string>,
    last_hop_pubkey: <byte>,
    cltv_limit: <int64>,
    dest_custom_records: <object>,
    allow_self_payment: <boolean>,
    dest_features: <array lnrpcFeatureBit>,
}
let options = {
  url: 'https://localhost:8080/v1/channels/transactions',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <lnrpcSendResponse>, 
//      "error": <runtimeStreamError>, 
//  }
```

### POST /v1/channels/transactions
* SendPaymentSync is the synchronous non-streaming version of SendPayment. This RPC is intended to be consumed by clients of the REST proxy. Additionally, this RPC expects the destination's public key and the payment hash (if any) to be encoded as hex strings.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
dest | byte | body | * The identity pubkey of the payment recipient. When using REST, this field must be encoded as base64.
dest_string | string | body | * The hex-encoded identity pubkey of the payment recipient. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
amt | string | body | * The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive.
amt_msat | string | body | * The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive.
payment_hash | byte | body | * The hash to use within the payment's HTLC. When using REST, this field must be encoded as base64.
payment_hash_string | string | body | * The hex-encoded hash to use within the payment's HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
payment_request | string | body | * A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
final_cltv_delta | int32 | body | * The CLTV delta from the current height that should be used to set the timelock for the final hop.
fee_limit | [lnrpcFeeLimit](#lnrpcfeelimit) | body | * The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.
outgoing_chan_id | string | body | * The channel id of the channel that must be taken to the first hop. If zero, any channel may be used.
last_hop_pubkey | byte | body | * The pubkey of the last hop of the route. If empty, any hop may be used.
cltv_limit | int64 | body | * An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced.
dest_custom_records | object | body | * An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64.
allow_self_payment | boolean | body | / If set, circular payments to self are permitted.
dest_features | [array lnrpcFeatureBit](#lnrpcfeaturebit) | body | * Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.

### Response 

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcSendResponse](#lnrpcsendresponse) |  
error | [runtimeStreamError](#runtimestreamerror) |   



# /v1/channels/transactions/route


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/transactions/route  \
    -d '{ "payment_hash":<byte>,"payment_hash_string":<string>,"route":<lnrpcRoute>, }' 
{ 
    "result": <lnrpcSendResponse>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/channels/transactions/route'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'payment_hash': base64.b64encode(<byte>).decode(), 
        'payment_hash_string': <string>, 
        'route': <lnrpcRoute>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "result": <lnrpcSendResponse>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    payment_hash: <byte>,
    payment_hash_string: <string>,
    route: <lnrpcRoute>,
}
let options = {
  url: 'https://localhost:8080/v1/channels/transactions/route',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <lnrpcSendResponse>, 
//      "error": <runtimeStreamError>, 
//  }
```

### POST /v1/channels/transactions/route
* SendToRouteSync is a synchronous version of SendToRoute. It Will block until the payment either fails or succeeds.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
payment_hash | byte | body | * The payment hash to use for the HTLC. When using REST, this field must be encoded as base64.
payment_hash_string | string | body | * An optional hex-encoded payment hash to be used for the HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
route | [lnrpcRoute](#lnrpcroute) | body | / Route that should be used to attempt to complete the payment.

### Response 

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcSendResponse](#lnrpcsendresponse) |  
error | [runtimeStreamError](#runtimestreamerror) |   



# /v1/chanpolicy


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/chanpolicy  \
    -d '{ "global":<boolean>,"chan_point":<lnrpcChannelPoint>,"base_fee_msat":<string>,"fee_rate":<double>,"time_lock_delta":<int64>,"max_htlc_msat":<string>,"min_htlc_msat":<string>,"min_htlc_msat_specified":<boolean>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/chanpolicy'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'global': <boolean>, 
        'chan_point': <lnrpcChannelPoint>, 
        'base_fee_msat': <string>, 
        'fee_rate': <double>, 
        'time_lock_delta': <int64>, 
        'max_htlc_msat': <string>, 
        'min_htlc_msat': <string>, 
        'min_htlc_msat_specified': <boolean>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    global: <boolean>,
    chan_point: <lnrpcChannelPoint>,
    base_fee_msat: <string>,
    fee_rate: <double>,
    time_lock_delta: <int64>,
    max_htlc_msat: <string>,
    min_htlc_msat: <string>,
    min_htlc_msat_specified: <boolean>,
}
let options = {
  url: 'https://localhost:8080/v1/chanpolicy',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/chanpolicy
UpdateChannelPolicy allows the caller to update the fee schedule and channel policies for all channels globally, or a particular channel.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
global | boolean | body | / If set, then this update applies to all currently active channels.
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | body | / If set, this update will target a specific channel.
base_fee_msat | string | body | / The base fee charged regardless of the number of milli-satoshis sent.
fee_rate | double | body | / The effective fee rate in milli-satoshis. The precision of this value / goes up to 6 decimal places, so 1e-6.
time_lock_delta | int64 | body | / The required timelock delta for HTLCs forwarded over the channel.
max_htlc_msat | string | body | / If set, the maximum HTLC size in milli-satoshis. If unset, the maximum / HTLC will be unchanged.
min_htlc_msat | string | body | / The minimum HTLC size in milli-satoshis. Only applied if / min_htlc_msat_specified is true.
min_htlc_msat_specified | boolean | body | / If true, min_htlc_msat is applied.

### Response 

This response has no parameters.




# /v1/fees


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/fees 
{ 
    "channel_fees": <array lnrpcChannelFeeReport>, 
    "day_fee_sum": <string>, 
    "week_fee_sum": <string>, 
    "month_fee_sum": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/fees'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "channel_fees": <array lnrpcChannelFeeReport>, 
    "day_fee_sum": <string>, 
    "week_fee_sum": <string>, 
    "month_fee_sum": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/fees',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "channel_fees": <array lnrpcChannelFeeReport>, 
//      "day_fee_sum": <string>, 
//      "week_fee_sum": <string>, 
//      "month_fee_sum": <string>, 
//  }
```

### GET /v1/fees
FeeReport allows the caller to obtain a report detailing the current fee schedule enforced by the node globally for each channel.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
channel_fees | [array lnrpcChannelFeeReport](#lnrpcchannelfeereport) | / An array of channel fee reports which describes the current fee schedule / for each channel. 
day_fee_sum | string | / The total amount of fee revenue (in satoshis) the switch has collected / over the past 24 hrs. 
week_fee_sum | string | / The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 week. 
month_fee_sum | string | / The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 month.  



# /v1/genseed


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/genseed 
{ 
    "cipher_seed_mnemonic": <array string>, 
    "enciphered_seed": <byte>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/genseed'
>>> cert_path = 'LND_DIR/tls.cert'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "cipher_seed_mnemonic": <array string>, 
    "enciphered_seed": <byte>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
let options = {
  url: 'https://localhost:8080/v1/genseed',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "cipher_seed_mnemonic": <array string>, 
//      "enciphered_seed": <byte>, 
//  }
```

### GET /v1/genseed
* GenSeed is the first method that should be used to instantiate a new lnd instance. This method allows a caller to generate a new aezeed cipher seed given an optional passphrase. If provided, the passphrase will be necessary to decrypt the cipherseed to expose the internal wallet seed.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
aezeed_passphrase | string | query | * aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64.
seed_entropy | string | query | * seed_entropy is an optional 16-bytes generated via CSPRNG. If not specified, then a fresh set of randomness will be used to create the seed. When using REST, this field must be encoded as base64.

### Response 

Field | Type | Description
----- | ---- | ----------- 
cipher_seed_mnemonic | array string | * cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed. 
enciphered_seed | byte | * enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.  



# /v1/getinfo


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo 
{ 
    "version": <string>, 
    "identity_pubkey": <string>, 
    "alias": <string>, 
    "color": <string>, 
    "num_pending_channels": <int64>, 
    "num_active_channels": <int64>, 
    "num_inactive_channels": <int64>, 
    "num_peers": <int64>, 
    "block_height": <int64>, 
    "block_hash": <string>, 
    "best_header_timestamp": <string>, 
    "synced_to_chain": <boolean>, 
    "synced_to_graph": <boolean>, 
    "testnet": <boolean>, 
    "chains": <array lnrpcChain>, 
    "uris": <array string>, 
    "features": <object>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/getinfo'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "version": <string>, 
    "identity_pubkey": <string>, 
    "alias": <string>, 
    "color": <string>, 
    "num_pending_channels": <int64>, 
    "num_active_channels": <int64>, 
    "num_inactive_channels": <int64>, 
    "num_peers": <int64>, 
    "block_height": <int64>, 
    "block_hash": <string>, 
    "best_header_timestamp": <string>, 
    "synced_to_chain": <boolean>, 
    "synced_to_graph": <boolean>, 
    "testnet": <boolean>, 
    "chains": <array lnrpcChain>, 
    "uris": <array string>, 
    "features": <object>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/getinfo',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "version": <string>, 
//      "identity_pubkey": <string>, 
//      "alias": <string>, 
//      "color": <string>, 
//      "num_pending_channels": <int64>, 
//      "num_active_channels": <int64>, 
//      "num_inactive_channels": <int64>, 
//      "num_peers": <int64>, 
//      "block_height": <int64>, 
//      "block_hash": <string>, 
//      "best_header_timestamp": <string>, 
//      "synced_to_chain": <boolean>, 
//      "synced_to_graph": <boolean>, 
//      "testnet": <boolean>, 
//      "chains": <array lnrpcChain>, 
//      "uris": <array string>, 
//      "features": <object>, 
//  }
```

### GET /v1/getinfo
GetInfo returns general information concerning the lightning node including it's identity pubkey, alias, the chains it is connected to, and information concerning the number of open+pending channels.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
version | string | / The version of the LND software that the node is running. 
identity_pubkey | string | / The identity pubkey of the current node. 
alias | string | / If applicable, the alias of the current node, e.g. "bob" 
color | string | / The color of the current node in hex code format 
num_pending_channels | int64 | / Number of pending channels 
num_active_channels | int64 | / Number of active channels 
num_inactive_channels | int64 | / Number of inactive channels 
num_peers | int64 | / Number of peers 
block_height | int64 | / The node's current view of the height of the best block 
block_hash | string | / The node's current view of the hash of the best block 
best_header_timestamp | string | / Timestamp of the block best known to the wallet 
synced_to_chain | boolean | / Whether the wallet's view is synced to the main chain 
synced_to_graph | boolean | Whether we consider ourselves synced with the public channel graph. 
testnet | boolean | * Whether the current node is connected to testnet. This field is deprecated and the network field should be used instead 
chains | [array lnrpcChain](#lnrpcchain) | / A list of active chains the node is connected to 
uris | array string | / The URIs of the current node. 
features | object | Features that our node has advertised in our init message, node announcements and invoices.  



# /v1/graph


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph 
{ 
    "nodes": <array lnrpcLightningNode>, 
    "edges": <array lnrpcChannelEdge>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/graph'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "nodes": <array lnrpcLightningNode>, 
    "edges": <array lnrpcChannelEdge>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/graph',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "nodes": <array lnrpcLightningNode>, 
//      "edges": <array lnrpcChannelEdge>, 
//  }
```

### GET /v1/graph
DescribeGraph returns a description of the latest graph state from the point of view of the node. The graph information is partitioned into two components: all the nodes/vertexes, and all the edges that connect the vertexes themselves. As this is a directed graph, the edges also contain the node directional specific routing policy which includes: the time lock delta, fee information, etc.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
include_unannounced | boolean | query | * Whether unannounced channels are included in the response or not. If set, unannounced channels are included. Unannounced channels are both private channels, and public channels that are not yet announced to the network.

### Response 

Field | Type | Description
----- | ---- | ----------- 
nodes | [array lnrpcLightningNode](#lnrpclightningnode) | / The list of `LightningNode`s in this channel graph 
edges | [array lnrpcChannelEdge](#lnrpcchanneledge) | / The list of `ChannelEdge`s in this channel graph  



# /v1/graph/edge


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/edge/{chan_id} 
{ 
    "channel_id": <string>, 
    "chan_point": <string>, 
    "last_update": <int64>, 
    "node1_pub": <string>, 
    "node2_pub": <string>, 
    "capacity": <string>, 
    "node1_policy": <lnrpcRoutingPolicy>, 
    "node2_policy": <lnrpcRoutingPolicy>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/graph/edge/{chan_id}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "channel_id": <string>, 
    "chan_point": <string>, 
    "last_update": <int64>, 
    "node1_pub": <string>, 
    "node2_pub": <string>, 
    "capacity": <string>, 
    "node1_policy": <lnrpcRoutingPolicy>, 
    "node2_policy": <lnrpcRoutingPolicy>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/graph/edge/{chan_id}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "channel_id": <string>, 
//      "chan_point": <string>, 
//      "last_update": <int64>, 
//      "node1_pub": <string>, 
//      "node2_pub": <string>, 
//      "capacity": <string>, 
//      "node1_policy": <lnrpcRoutingPolicy>, 
//      "node2_policy": <lnrpcRoutingPolicy>, 
//  }
```

### GET /v1/graph/edge/{chan_id}
GetChanInfo returns the latest authenticated network announcement for the given channel identified by its channel ID: an 8-byte integer which uniquely identifies the location of transaction's funding output within the blockchain.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
chan_id | string | path | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.

### Response 

Field | Type | Description
----- | ---- | ----------- 
channel_id | string | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | string |  
last_update | int64 |  
node1_pub | string |  
node2_pub | string |  
capacity | string |  
node1_policy | [lnrpcRoutingPolicy](#lnrpcroutingpolicy) |  
node2_policy | [lnrpcRoutingPolicy](#lnrpcroutingpolicy) |   



# /v1/graph/info


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/info 
{ 
    "graph_diameter": <int64>, 
    "avg_out_degree": <double>, 
    "max_out_degree": <int64>, 
    "num_nodes": <int64>, 
    "num_channels": <int64>, 
    "total_network_capacity": <string>, 
    "avg_channel_size": <double>, 
    "min_channel_size": <string>, 
    "max_channel_size": <string>, 
    "median_channel_size_sat": <string>, 
    "num_zombie_chans": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/graph/info'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "graph_diameter": <int64>, 
    "avg_out_degree": <double>, 
    "max_out_degree": <int64>, 
    "num_nodes": <int64>, 
    "num_channels": <int64>, 
    "total_network_capacity": <string>, 
    "avg_channel_size": <double>, 
    "min_channel_size": <string>, 
    "max_channel_size": <string>, 
    "median_channel_size_sat": <string>, 
    "num_zombie_chans": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/graph/info',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "graph_diameter": <int64>, 
//      "avg_out_degree": <double>, 
//      "max_out_degree": <int64>, 
//      "num_nodes": <int64>, 
//      "num_channels": <int64>, 
//      "total_network_capacity": <string>, 
//      "avg_channel_size": <double>, 
//      "min_channel_size": <string>, 
//      "max_channel_size": <string>, 
//      "median_channel_size_sat": <string>, 
//      "num_zombie_chans": <string>, 
//  }
```

### GET /v1/graph/info
GetNetworkInfo returns some basic stats about the known channel graph from the point of view of the node.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
graph_diameter | int64 |  
avg_out_degree | double |  
max_out_degree | int64 |  
num_nodes | int64 |  
num_channels | int64 |  
total_network_capacity | string |  
avg_channel_size | double |  
min_channel_size | string |  
max_channel_size | string |  
median_channel_size_sat | string |  
num_zombie_chans | string | The number of edges marked as zombies.  



# /v1/graph/node


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/node/{pub_key} 
{ 
    "node": <lnrpcLightningNode>, 
    "num_channels": <int64>, 
    "total_capacity": <string>, 
    "channels": <array lnrpcChannelEdge>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/graph/node/{pub_key}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "node": <lnrpcLightningNode>, 
    "num_channels": <int64>, 
    "total_capacity": <string>, 
    "channels": <array lnrpcChannelEdge>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/graph/node/{pub_key}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "node": <lnrpcLightningNode>, 
//      "num_channels": <int64>, 
//      "total_capacity": <string>, 
//      "channels": <array lnrpcChannelEdge>, 
//  }
```

### GET /v1/graph/node/{pub_key}
GetNodeInfo returns the latest advertised, aggregated, and authenticated channel information for the specified node identified by its public key.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pub_key | string | path | / The 33-byte hex-encoded compressed public of the target node
include_channels | boolean | query | / If true, will include all known channels associated with the node.

### Response 

Field | Type | Description
----- | ---- | ----------- 
node | [lnrpcLightningNode](#lnrpclightningnode) | * An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | int64 | / The total number of channels for the node. 
total_capacity | string | / The sum of all channels capacity for the node, denominated in satoshis. 
channels | [array lnrpcChannelEdge](#lnrpcchanneledge) | / A list of all public channels for the node.  



# /v1/graph/nodemetrics


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/nodemetrics 
{ 
    "betweenness_centrality": <object>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/graph/nodemetrics'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "betweenness_centrality": <object>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/graph/nodemetrics',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "betweenness_centrality": <object>, 
//  }
```

### GET /v1/graph/nodemetrics
GetNodeMetrics returns node metrics calculated from the graph. Currently the only supported metric is betweenness centrality of individual nodes.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
types | array | query | / The requested node metrics.

### Response 

Field | Type | Description
----- | ---- | ----------- 
betweenness_centrality | object | * Betweenness centrality is the sum of the ratio of shortest paths that pass through the node for each pair of nodes in the graph (not counting paths starting or ending at this node). Map of node pubkey to betweenness centrality of the node. Normalized values are in the [0,1] closed interval.  



# /v1/graph/routes


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/routes/{pub_key}/{amt} 
{ 
    "routes": <array lnrpcRoute>, 
    "success_prob": <double>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/graph/routes/{pub_key}/{amt}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "routes": <array lnrpcRoute>, 
    "success_prob": <double>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/graph/routes/{pub_key}/{amt}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "routes": <array lnrpcRoute>, 
//      "success_prob": <double>, 
//  }
```

### GET /v1/graph/routes/{pub_key}/{amt}
QueryRoutes attempts to query the daemon's Channel Router for a possible route to a target destination capable of carrying a specific amount of satoshis. The returned route contains the full details required to craft and send an HTLC, also including the necessary information that should be present within the Sphinx packet encapsulated within the HTLC.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pub_key | string | path | / The 33-byte hex-encoded public key for the payment destination
amt | string | path | * The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive.
amt_msat | string | query | * The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive.
final_cltv_delta | int32 | query | * An optional CLTV delta from the current height that should be used for the timelock of the final hop. Note that unlike SendPayment, QueryRoutes does not add any additional block padding on top of final_ctlv_delta. This padding of a few blocks needs to be added manually or otherwise failures may happen when a block comes in while the payment is in flight.
fee_limit.fixed | string | query | * The fee limit expressed as a fixed amount of satoshis.  The fields fixed and fixed_msat are mutually exclusive.
fee_limit.fixed_msat | string | query | * The fee limit expressed as a fixed amount of millisatoshis.  The fields fixed and fixed_msat are mutually exclusive.
fee_limit.percent | string | query | / The fee limit expressed as a percentage of the payment amount.
ignored_nodes | array | query | * A list of nodes to ignore during path finding. When using REST, these fields must be encoded as base64.
source_pub_key | string | query | * The source node where the request route should originated from. If empty, self is assumed.
use_mission_control | boolean | query | * If set to true, edge probabilities from mission control will be used to get the optimal route.
cltv_limit | int64 | query | * An optional maximum total time lock for the route. If the source is empty or ourselves, this should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is used as the limit.
outgoing_chan_id | string | query | * The channel id of the channel that must be taken to the first hop. If zero, any channel may be used.
last_hop_pubkey | string | query | * The pubkey of the last hop of the route. If empty, any hop may be used.
dest_features | array | query | * Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.

### Response 

Field | Type | Description
----- | ---- | ----------- 
routes | [array lnrpcRoute](#lnrpcroute) | * The route that results from the path finding operation. This is still a repeated field to retain backwards compatibility. 
success_prob | double | * The success probability of the returned route based on the current mission control state. [EXPERIMENTAL]  



# /v1/initwallet


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/initwallet  \
    -d '{ "wallet_password":<byte>,"cipher_seed_mnemonic":<array string>,"aezeed_passphrase":<byte>,"recovery_window":<int32>,"channel_backups":<lnrpcChanBackupSnapshot>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/initwallet'
>>> cert_path = 'LND_DIR/tls.cert'
>>> data = { 
        'wallet_password': base64.b64encode(<byte>).decode(), 
        'cipher_seed_mnemonic': <array string>, 
        'aezeed_passphrase': base64.b64encode(<byte>).decode(), 
        'recovery_window': <int32>, 
        'channel_backups': <lnrpcChanBackupSnapshot>, 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
let requestBody = { 
    wallet_password: <byte>,
    cipher_seed_mnemonic: <array string>,
    aezeed_passphrase: <byte>,
    recovery_window: <int32>,
    channel_backups: <lnrpcChanBackupSnapshot>,
}
let options = {
  url: 'https://localhost:8080/v1/initwallet',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/initwallet
* InitWallet is used when lnd is starting up for the first time to fully initialize the daemon and its internal wallet. At the very least a wallet password must be provided. This will be used to encrypt sensitive material on disk.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
wallet_password | byte | body | * wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon. When using REST, this field must be encoded as base64.
cipher_seed_mnemonic | array string | body | * cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed.
aezeed_passphrase | byte | body | * aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64.
recovery_window | int32 | body | * recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) | body | * channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.

### Response 

This response has no parameters.




# /v1/invoice


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoice/{r_hash_str} 
{ 
    "result": <lnrpcInvoice>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/invoice/{r_hash_str}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "result": <lnrpcInvoice>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/invoice/{r_hash_str}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <lnrpcInvoice>, 
//      "error": <runtimeStreamError>, 
//  }
```

### GET /v1/invoice/{r_hash_str}
LookupInvoice attempts to look up an invoice according to its payment hash. The passed payment hash *must* be exactly 32 bytes, if not, an error is returned.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
r_hash_str | string | path | * The hex-encoded payment hash of the invoice to be looked up. The passed payment hash must be exactly 32 bytes, otherwise an error is returned. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
r_hash | string | query | * The payment hash of the invoice to be looked up. When using REST, this field must be encoded as base64.

### Response 

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcInvoice](#lnrpcinvoice) |  
error | [runtimeStreamError](#runtimestreamerror) |   



# /v1/invoices


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoices 
{ 
    "invoices": <array lnrpcInvoice>, 
    "last_index_offset": <string>, 
    "first_index_offset": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/invoices'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "invoices": <array lnrpcInvoice>, 
    "last_index_offset": <string>, 
    "first_index_offset": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/invoices',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "invoices": <array lnrpcInvoice>, 
//      "last_index_offset": <string>, 
//      "first_index_offset": <string>, 
//  }
```

### GET /v1/invoices
ListInvoices returns a list of all the invoices currently stored within the database. Any active debug invoices are ignored. It has full support for paginated responses, allowing users to query for specific invoices through their add_index. This can be done by using either the first_index_offset or last_index_offset fields included in the response as the index_offset of the next request. By default, the first 100 invoices created will be returned. Backwards pagination is also supported through the Reversed flag.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pending_only | boolean | query | * If set, only invoices that are not settled and not canceled will be returned in the response.
index_offset | string | query | * The index of an invoice that will be used as either the start or end of a query to determine which invoices should be returned in the response.
num_max_invoices | string | query | / The max number of invoices to return in the response to this query.
reversed | boolean | query | * If set, the invoices returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards.

### Response 

Field | Type | Description
----- | ---- | ----------- 
invoices | [array lnrpcInvoice](#lnrpcinvoice) | * A list of invoices from the time slice of the time series specified in the request. 
last_index_offset | string | * The index of the last item in the set of returned invoices. This can be used to seek further, pagination style. 
first_index_offset | string | * The index of the last item in the set of returned invoices. This can be used to seek backwards, pagination style.  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoices  \
    -d '{ "result":<lnrpcInvoice>,"error":<runtimeStreamError>, }' 
{ 
    "r_hash": <byte>, 
    "payment_request": <string>, 
    "add_index": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/invoices'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'result': <lnrpcInvoice>, 
        'error': <runtimeStreamError>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "r_hash": <byte>, 
    "payment_request": <string>, 
    "add_index": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    result: <lnrpcInvoice>,
    error: <runtimeStreamError>,
}
let options = {
  url: 'https://localhost:8080/v1/invoices',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "r_hash": <byte>, 
//      "payment_request": <string>, 
//      "add_index": <string>, 
//  }
```

### POST /v1/invoices
AddInvoice attempts to add a new invoice to the invoice database. Any duplicated invoices are rejected, therefore all invoices *must* have a unique payment preimage.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
result | [lnrpcInvoice](#lnrpcinvoice) | body | 
error | [runtimeStreamError](#runtimestreamerror) | body | 

### Response 

Field | Type | Description
----- | ---- | ----------- 
r_hash | byte |  
payment_request | string | * A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
add_index | string | * The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.  



# /v1/invoices/subscribe


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoices/subscribe 
{ 
    "result": <lnrpcInvoice>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/invoices/subscribe'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path, stream=True)
>>> for raw_response in r.iter_lines():
>>>     json_response = json.loads(raw_response)
>>>     print(json_response)
{ 
    "result": <lnrpcInvoice>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/invoices/subscribe',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <lnrpcInvoice>, 
//      "error": <runtimeStreamError>, 
//  }



// --------------------------
// Example with websockets:
// --------------------------
const WebSocket = require('ws');
const fs = require('fs');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let ws = new WebSocket('wss://localhost:8080/v1/invoices/subscribe?method=GET', {
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  headers: {
    'Grpc-Metadata-Macaroon': macaroon,
  },
});
let requestBody = { 
  add_index: <string>,
  settle_index: <string>,
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
//  { 
//      "result": <lnrpcInvoice>, 
//      "error": <runtimeStreamError>, 
//  }


```

### GET /v1/invoices/subscribe
* SubscribeInvoices returns a uni-directional stream (server -> client) for notifying the client of newly added/settled invoices. The caller can optionally specify the add_index and/or the settle_index. If the add_index is specified, then we'll first start by sending add invoice events for all invoices with an add_index greater than the specified value. If the settle_index is specified, the next, we'll send out all settle events for invoices with a settle_index greater than the specified value. One or both of these fields can be set. If no fields are set, then we'll only send out the latest add/settle events.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
add_index | string | query | * If specified (non-zero), then we'll first start by sending out notifications for all added indexes with an add_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC.
settle_index | string | query | * If specified (non-zero), then we'll first start by sending out notifications for all settled indexes with an settle_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC.

### Response (streaming)

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcInvoice](#lnrpcinvoice) |  
error | [runtimeStreamError](#runtimestreamerror) |   



# /v1/macaroon


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/macaroon  \
    -d '{ "permissions":<array lnrpcMacaroonPermission>, }' 
{ 
    "macaroon": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/macaroon'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'permissions': <array lnrpcMacaroonPermission>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "macaroon": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    permissions: <array lnrpcMacaroonPermission>,
}
let options = {
  url: 'https://localhost:8080/v1/macaroon',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "macaroon": <string>, 
//  }
```

### POST /v1/macaroon
BakeMacaroon allows the creation of a new macaroon with custom read and write permissions. No first-party caveats are added since this can be done offline.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
permissions | [array lnrpcMacaroonPermission](#lnrpcmacaroonpermission) | body | / The list of permissions the new macaroon should grant.

### Response 

Field | Type | Description
----- | ---- | ----------- 
macaroon | string | / The hex encoded macaroon, serialized in binary format.  



# /v1/newaddress


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/newaddress 
{ 
    "address": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/newaddress'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "address": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/newaddress',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "address": <string>, 
//  }
```

### GET /v1/newaddress
NewAddress creates a new address under control of the local wallet.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
type | string | query | / The address type.

### Response 

Field | Type | Description
----- | ---- | ----------- 
address | string | / The newly generated wallet address  



# /v1/payments


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/payments 
{ 
    "payments": <array lnrpcPayment>, 
    "first_index_offset": <string>, 
    "last_index_offset": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/payments'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "payments": <array lnrpcPayment>, 
    "first_index_offset": <string>, 
    "last_index_offset": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/payments',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "payments": <array lnrpcPayment>, 
//      "first_index_offset": <string>, 
//      "last_index_offset": <string>, 
//  }
```

### GET /v1/payments
ListPayments returns a list of all outgoing payments.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
include_incomplete | boolean | query | * If true, then return payments that have not yet fully completed. This means that pending payments, as well as failed payments will show up if this field is set to true. This flag doesn't change the meaning of the indices, which are tied to individual payments.
index_offset | string | query | * The index of a payment that will be used as either the start or end of a query to determine which payments should be returned in the response. The index_offset is exclusive. In the case of a zero index_offset, the query will start with the oldest payment when paginating forwards, or will end with the most recent payment when paginating backwards.
max_payments | string | query | / The maximal number of payments returned in the response to this query.
reversed | boolean | query | * If set, the payments returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards. The order of the returned payments is always oldest first (ascending index order).

### Response 

Field | Type | Description
----- | ---- | ----------- 
payments | [array lnrpcPayment](#lnrpcpayment) | / The list of payments 
first_index_offset | string | * The index of the first item in the set of returned payments. This can be used as the index_offset to continue seeking backwards in the next request. 
last_index_offset | string | * The index of the last item in the set of returned payments. This can be used as the index_offset to continue seeking forwards in the next request.  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X DELETE --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/payments 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/payments'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.delete(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/payments',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.delete(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### DELETE /v1/payments
* DeleteAllPayments deletes all outgoing payments from DB.

This request has no parameters.

### Response 

This response has no parameters.




# /v1/payreq


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/payreq/{pay_req} 
{ 
    "destination": <string>, 
    "payment_hash": <string>, 
    "num_satoshis": <string>, 
    "timestamp": <string>, 
    "expiry": <string>, 
    "description": <string>, 
    "description_hash": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array lnrpcRouteHint>, 
    "payment_addr": <byte>, 
    "num_msat": <string>, 
    "features": <object>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/payreq/{pay_req}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "destination": <string>, 
    "payment_hash": <string>, 
    "num_satoshis": <string>, 
    "timestamp": <string>, 
    "expiry": <string>, 
    "description": <string>, 
    "description_hash": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array lnrpcRouteHint>, 
    "payment_addr": <byte>, 
    "num_msat": <string>, 
    "features": <object>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/payreq/{pay_req}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "destination": <string>, 
//      "payment_hash": <string>, 
//      "num_satoshis": <string>, 
//      "timestamp": <string>, 
//      "expiry": <string>, 
//      "description": <string>, 
//      "description_hash": <string>, 
//      "fallback_addr": <string>, 
//      "cltv_expiry": <string>, 
//      "route_hints": <array lnrpcRouteHint>, 
//      "payment_addr": <byte>, 
//      "num_msat": <string>, 
//      "features": <object>, 
//  }
```

### GET /v1/payreq/{pay_req}
DecodePayReq takes an encoded payment request string and attempts to decode it, returning a full description of the conditions encoded within the payment request.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pay_req | string | path | / The payment request string to be decoded

### Response 

Field | Type | Description
----- | ---- | ----------- 
destination | string |  
payment_hash | string |  
num_satoshis | string |  
timestamp | string |  
expiry | string |  
description | string |  
description_hash | string |  
fallback_addr | string |  
cltv_expiry | string |  
route_hints | [array lnrpcRouteHint](#lnrpcroutehint) |  
payment_addr | byte |  
num_msat | string |  
features | object |   



# /v1/peers


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/peers 
{ 
    "peers": <array lnrpcPeer>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/peers'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "peers": <array lnrpcPeer>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/peers',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "peers": <array lnrpcPeer>, 
//  }
```

### GET /v1/peers
ListPeers returns a verbose listing of all currently active peers.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
latest_error | boolean | query | If true, only the last error that our peer sent us will be returned with the peer's information, rather than the full set of historic errors we have stored.

### Response 

Field | Type | Description
----- | ---- | ----------- 
peers | [array lnrpcPeer](#lnrpcpeer) | / The list of currently connected peers  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/peers  \
    -d '{ "addr":<lnrpcLightningAddress>,"perm":<boolean>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/peers'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'addr': <lnrpcLightningAddress>, 
        'perm': <boolean>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    addr: <lnrpcLightningAddress>,
    perm: <boolean>,
}
let options = {
  url: 'https://localhost:8080/v1/peers',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/peers
ConnectPeer attempts to establish a connection to a remote peer. This is at the networking level, and is used for communication between nodes. This is distinct from establishing a channel with a peer.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
addr | [lnrpcLightningAddress](#lnrpclightningaddress) | body | / Lightning address of the peer, in the format `<pubkey>@host`
perm | boolean | body | * If set, the daemon will attempt to persistently connect to the target peer. Otherwise, the call will be synchronous.

### Response 

This response has no parameters.




```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X DELETE --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/peers/{pub_key} 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/peers/{pub_key}'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.delete(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/peers/{pub_key}',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.delete(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### DELETE /v1/peers/{pub_key}
DisconnectPeer attempts to disconnect one peer from another identified by a given pubKey. In the case that we currently have a pending or active channel with the target peer, then this action will be not be allowed.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pub_key | string | path | / The pubkey of the node to disconnect from

### Response 

This response has no parameters.




# /v1/signmessage


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/signmessage  \
    -d '{ "msg":<byte>, }' 
{ 
    "signature": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/signmessage'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'msg': base64.b64encode(<byte>).decode(), 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "signature": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    msg: <byte>,
}
let options = {
  url: 'https://localhost:8080/v1/signmessage',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "signature": <string>, 
//  }
```

### POST /v1/signmessage
SignMessage signs a message with this node's private key. The returned signature string is `zbase32` encoded and pubkey recoverable, meaning that only the message digest and signature are needed for verification.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
msg | byte | body | * The message to be signed. When using REST, this field must be encoded as base64.

### Response 

Field | Type | Description
----- | ---- | ----------- 
signature | string | / The signature for the given message  



# /v1/switch


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/switch  \
    -d '{ "start_time":<string>,"end_time":<string>,"index_offset":<int64>,"num_max_events":<int64>, }' 
{ 
    "forwarding_events": <array lnrpcForwardingEvent>, 
    "last_offset_index": <int64>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/switch'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'start_time': <string>, 
        'end_time': <string>, 
        'index_offset': <int64>, 
        'num_max_events': <int64>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "forwarding_events": <array lnrpcForwardingEvent>, 
    "last_offset_index": <int64>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    start_time: <string>,
    end_time: <string>,
    index_offset: <int64>,
    num_max_events: <int64>,
}
let options = {
  url: 'https://localhost:8080/v1/switch',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "forwarding_events": <array lnrpcForwardingEvent>, 
//      "last_offset_index": <int64>, 
//  }
```

### POST /v1/switch
ForwardingHistory allows the caller to query the htlcswitch for a record of all HTLCs forwarded within the target time range, and integer offset within that time range. If no time-range is specified, then the first chunk of the past 24 hrs of forwarding history are returned.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
start_time | string | body | / Start time is the starting point of the forwarding history request. All / records beyond this point will be included, respecting the end time, and / the index offset.
end_time | string | body | / End time is the end point of the forwarding history request. The / response will carry at most 50k records between the start time and the / end time. The index offset can be used to implement pagination.
index_offset | int64 | body | / Index offset is the offset in the time series to start at. As each / response can only contain 50k records, callers can use this to skip / around within a packed time series.
num_max_events | int64 | body | / The max number of events to return in the response to this query.

### Response 

Field | Type | Description
----- | ---- | ----------- 
forwarding_events | [array lnrpcForwardingEvent](#lnrpcforwardingevent) | / A list of forwarding events from the time slice of the time series / specified in the request. 
last_offset_index | int64 | / The index of the last time in the set of returned forwarding events. Can / be used to seek further, pagination style.  



# /v1/transactions


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/transactions 
{ 
    "transactions": <array lnrpcTransaction>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/transactions'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "transactions": <array lnrpcTransaction>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/transactions',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "transactions": <array lnrpcTransaction>, 
//  }
```

### GET /v1/transactions
GetTransactions returns a list describing all the known transactions relevant to the wallet.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
transactions | [array lnrpcTransaction](#lnrpctransaction) | / The list of transactions relevant to the wallet.  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/transactions  \
    -d '{ "addr":<string>,"amount":<string>,"target_conf":<int32>,"sat_per_byte":<string>,"send_all":<boolean>, }' 
{ 
    "txid": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/transactions'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'addr': <string>, 
        'amount': <string>, 
        'target_conf': <int32>, 
        'sat_per_byte': <string>, 
        'send_all': <boolean>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "txid": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    addr: <string>,
    amount: <string>,
    target_conf: <int32>,
    sat_per_byte: <string>,
    send_all: <boolean>,
}
let options = {
  url: 'https://localhost:8080/v1/transactions',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "txid": <string>, 
//  }
```

### POST /v1/transactions
SendCoins executes a request to send coins to a particular address. Unlike SendMany, this RPC call only allows creating a single output at a time. If neither target_conf, or sat_per_byte are set, then the internal wallet will consult its fee model to determine a fee for the default confirmation target.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
addr | string | body | / The address to send coins to
amount | string | body | / The amount in satoshis to send
target_conf | int32 | body | / The target number of blocks that this transaction should be confirmed / by.
sat_per_byte | string | body | / A manual fee rate set in sat/byte that should be used when crafting the / transaction.
send_all | boolean | body | * If set, then the amount field will be ignored, and lnd will attempt to send all the coins under control of the internal wallet to the specified address.

### Response 

Field | Type | Description
----- | ---- | ----------- 
txid | string | / The transaction ID of the transaction  



# /v1/transactions/fee


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/transactions/fee 
{ 
    "fee_sat": <string>, 
    "feerate_sat_per_byte": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/transactions/fee'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "fee_sat": <string>, 
    "feerate_sat_per_byte": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/transactions/fee',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "fee_sat": <string>, 
//      "feerate_sat_per_byte": <string>, 
//  }
```

### GET /v1/transactions/fee
EstimateFee asks the chain backend to estimate the fee rate and total fees for a transaction that pays to multiple specified outputs.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
target_conf | int32 | query | / The target number of blocks that this transaction should be confirmed / by.

### Response 

Field | Type | Description
----- | ---- | ----------- 
fee_sat | string | / The total fee in satoshis. 
feerate_sat_per_byte | string | / The fee rate in satoshi/byte.  



# /v1/unlockwallet


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/unlockwallet  \
    -d '{ "wallet_password":<byte>,"recovery_window":<int32>,"channel_backups":<lnrpcChanBackupSnapshot>, }' 
{ 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/unlockwallet'
>>> cert_path = 'LND_DIR/tls.cert'
>>> data = { 
        'wallet_password': base64.b64encode(<byte>).decode(), 
        'recovery_window': <int32>, 
        'channel_backups': <lnrpcChanBackupSnapshot>, 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
const fs = require('fs');
const request = require('request');
let requestBody = { 
    wallet_password: <byte>,
    recovery_window: <int32>,
    channel_backups: <lnrpcChanBackupSnapshot>,
}
let options = {
  url: 'https://localhost:8080/v1/unlockwallet',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//  }
```

### POST /v1/unlockwallet
UnlockWallet is used at startup of lnd to provide a password to unlock the wallet database.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
wallet_password | byte | body | * wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly. When using REST, this field must be encoded as base64.
recovery_window | int32 | body | * recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) | body | * channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.

### Response 

This response has no parameters.




# /v1/utxos


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/utxos 
{ 
    "utxos": <array lnrpcUtxo>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/utxos'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> r = requests.get(url, headers=headers, verify=cert_path)
>>> print(r.json())
{ 
    "utxos": <array lnrpcUtxo>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let options = {
  url: 'https://localhost:8080/v1/utxos',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
}
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "utxos": <array lnrpcUtxo>, 
//  }
```

### GET /v1/utxos
ListUnspent returns a list of all utxos spendable by the wallet with a number of confirmations between the specified minimum and maximum.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
min_confs | int32 | query | / The minimum number of confirmations to be included.
max_confs | int32 | query | / The maximum number of confirmations to be included.

### Response 

Field | Type | Description
----- | ---- | ----------- 
utxos | [array lnrpcUtxo](#lnrpcutxo) | / A list of utxos  



# /v1/verifymessage


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/verifymessage  \
    -d '{ "msg":<byte>,"signature":<string>, }' 
{ 
    "valid": <boolean>, 
    "pubkey": <string>, 
}
```
```python
>>> import base64, codecs, json, requests
>>> url = 'https://localhost:8080/v1/verifymessage'
>>> cert_path = 'LND_DIR/tls.cert'
>>> macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
>>> headers = {'Grpc-Metadata-macaroon': macaroon}
>>> data = { 
        'msg': base64.b64encode(<byte>).decode(), 
        'signature': <string>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "valid": <boolean>, 
    "pubkey": <string>, 
}
```
```javascript
const fs = require('fs');
const request = require('request');
const macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
let requestBody = { 
    msg: <byte>,
    signature: <string>,
}
let options = {
  url: 'https://localhost:8080/v1/verifymessage',
  // Work-around for self-signed certificates.
  rejectUnauthorized: false,
  json: true, 
  headers: {
    'Grpc-Metadata-macaroon': macaroon,
  },
  form: JSON.stringify(requestBody),
}
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "valid": <boolean>, 
//      "pubkey": <string>, 
//  }
```

### POST /v1/verifymessage
VerifyMessage verifies a signature over a msg. The signature must be zbase32 encoded and signed by an active node in the resident node's channel database. In addition to returning the validity of the signature, VerifyMessage also returns the recovered pubkey from the signature.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
msg | byte | body | * The message over which the signature is to be verified. When using REST, this field must be encoded as base64.
signature | string | body | / The signature to be verified over the given message

### Response 

Field | Type | Description
----- | ---- | ----------- 
valid | boolean | / Whether the signature was valid over the given message 
pubkey | string | / The pubkey recovered from the signature  




# Definitions

## ChannelCloseSummaryClosureType

This definition has no parameters.


## ChannelEventUpdateUpdateType

This definition has no parameters.


## FailureFailureCode

This definition has no parameters.


## ForceClosedChannelAnchorState

This definition has no parameters.


## HTLCAttemptHTLCStatus

This definition has no parameters.


## InvoiceInvoiceState

This definition has no parameters.


## PaymentPaymentStatus

This definition has no parameters.


## PeerEventEventType

This definition has no parameters.


## PeerSyncType

This definition has no parameters.


## PendingChannelsResponseClosedChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | / The pending channel to be closed
closing_txid | string | / The transaction id of the closing transaction


## PendingChannelsResponseCommitments

Field | Type | Description
----- | ---- | ----------- 
local_txid | string | / Hash of the local version of the commitment tx.
remote_txid | string | / Hash of the remote version of the commitment tx.
remote_pending_txid | string | / Hash of the remote pending version of the commitment tx.
local_commit_fee_sat | string | The amount in satoshis calculated to be paid in fees for the local commitment.
remote_commit_fee_sat | string | The amount in satoshis calculated to be paid in fees for the remote commitment.
remote_pending_commit_fee_sat | string | The amount in satoshis calculated to be paid in fees for the remote pending commitment.


## PendingChannelsResponseForceClosedChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | / The pending channel to be force closed
closing_txid | string | / The transaction id of the closing transaction
limbo_balance | string | / The balance in satoshis encumbered in this pending channel
maturity_height | int64 | / The height at which funds can be swept into the wallet
blocks_til_maturity | int32 | Remaining # of blocks until the commitment output can be swept. Negative values indicate how many blocks have passed since becoming mature.
recovered_balance | string | / The total value of funds successfully recovered from this channel
pending_htlcs | [array lnrpcPendingHTLC](#lnrpcpendinghtlc) | 
anchor | [ForceClosedChannelAnchorState](#forceclosedchannelanchorstate) | 


## PendingChannelsResponsePendingChannel

Field | Type | Description
----- | ---- | ----------- 
remote_node_pub | string | 
channel_point | string | 
capacity | string | 
local_balance | string | 
remote_balance | string | 
local_chan_reserve_sat | string | / The minimum satoshis this node is required to reserve in its / balance.
remote_chan_reserve_sat | string | * The minimum satoshis the other node is required to reserve in its balance.
initiator | [lnrpcInitiator](#lnrpcinitiator) | The party that initiated opening the channel.
commitment_type | [lnrpcCommitmentType](#lnrpccommitmenttype) | / The commitment type used by this channel.


## PendingChannelsResponsePendingOpenChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | / The pending channel
confirmation_height | int64 | / The height at which this channel will be confirmed
commit_fee | string | * The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart.
commit_weight | string | / The weight of the commitment transaction
fee_per_kw | string | * The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open.


## PendingChannelsResponseWaitingCloseChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | / The pending channel waiting for closing tx to confirm
limbo_balance | string | / The balance in satoshis encumbered in this channel
commitments | [PendingChannelsResponseCommitments](#pendingchannelsresponsecommitments) | * A list of valid commitment transactions. Any of these can confirm at this point.


## lnrpcAbandonChannelResponse

This definition has no parameters.


## lnrpcAddInvoiceResponse

Field | Type | Description
----- | ---- | ----------- 
r_hash | byte | 
payment_request | string | * A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
add_index | string | * The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.


## lnrpcAddressType

This definition has no parameters.


## lnrpcBakeMacaroonRequest

Field | Type | Description
----- | ---- | ----------- 
permissions | [array lnrpcMacaroonPermission](#lnrpcmacaroonpermission) | / The list of permissions the new macaroon should grant.


## lnrpcBakeMacaroonResponse

Field | Type | Description
----- | ---- | ----------- 
macaroon | string | / The hex encoded macaroon, serialized in binary format.


## lnrpcChain

Field | Type | Description
----- | ---- | ----------- 
chain | string | / The blockchain the node is on (eg bitcoin, litecoin)
network | string | / The network the node is on (eg regtest, testnet, mainnet)


## lnrpcChanBackupSnapshot

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcChanPointShim

Field | Type | Description
----- | ---- | ----------- 
amt | string | * The size of the pre-crafted output to be used as the channel point for this channel funding.
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | / The target channel point to refrence in created commitment transactions.
local_key | [lnrpcKeyDescriptor](#lnrpckeydescriptor) | / Our local key to use when creating the multi-sig output.
remote_key | byte | / The key of the remote party to use when creating the multi-sig output.
pending_chan_id | byte | * If non-zero, then this will be used as the pending channel ID on the wire protocol to initate the funding request. This is an optional field, and should only be set if the responder is already expecting a specific pending channel ID.
thaw_height | int64 | * This uint32 indicates if this channel is to be considered 'frozen'. A frozen channel does not allow a cooperative channel close by the initiator. The thaw_height is the height that this restriction stops applying to the channel.


## lnrpcChangePasswordRequest

Field | Type | Description
----- | ---- | ----------- 
current_password | byte | * current_password should be the current valid passphrase used to unlock the daemon. When using REST, this field must be encoded as base64.
new_password | byte | * new_password should be the new passphrase that will be needed to unlock the daemon. When using REST, this field must be encoded as base64.


## lnrpcChangePasswordResponse

This definition has no parameters.


## lnrpcChannel

Field | Type | Description
----- | ---- | ----------- 
active | boolean | / Whether this channel is active or not
remote_pubkey | string | / The identity pubkey of the remote node
channel_point | string | * The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction.
chan_id | string | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
capacity | string | / The total amount of funds held in this channel
local_balance | string | / This node's current balance in this channel
remote_balance | string | / The counterparty's current balance in this channel
commit_fee | string | * The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart.
commit_weight | string | / The weight of the commitment transaction
fee_per_kw | string | * The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open.
unsettled_balance | string | / The unsettled balance in this channel
total_satoshis_sent | string | * The total number of satoshis we've sent within this channel.
total_satoshis_received | string | * The total number of satoshis we've received within this channel.
num_updates | string | * The total number of updates conducted within this channel.
pending_htlcs | [array lnrpcHTLC](#lnrpchtlc) | * The list of active, uncleared HTLCs currently pending within the channel.
csv_delay | int64 | * The CSV delay expressed in relative blocks. If the channel is force closed, we will need to wait for this many blocks before we can regain our funds.
private | boolean | / Whether this channel is advertised to the network or not.
initiator | boolean | / True if we were the ones that created the channel.
chan_status_flags | string | / A set of flags showing the current state of the channel.
local_chan_reserve_sat | string | / The minimum satoshis this node is required to reserve in its balance.
remote_chan_reserve_sat | string | * The minimum satoshis the other node is required to reserve in its balance.
static_remote_key | boolean | / Deprecated. Use commitment_type.
commitment_type | [lnrpcCommitmentType](#lnrpccommitmenttype) | / The commitment type used by this channel.
lifetime | string | * The number of seconds that the channel has been monitored by the channel scoring system. Scores are currently not persisted, so this value may be less than the lifetime of the channel [EXPERIMENTAL].
uptime | string | * The number of seconds that the remote peer has been observed as being online by the channel scoring system over the lifetime of the channel [EXPERIMENTAL].
close_address | string | * Close address is the address that we will enforce payout to on cooperative close if the channel was opened utilizing option upfront shutdown. This value can be set on channel open by setting close_address in an open channel request. If this value is not set, you can still choose a payout address by cooperatively closing with the delivery_address field set.
push_amount_sat | string | The amount that the initiator of the channel optionally pushed to the remote party on channel open. This amount will be zero if the channel initiator did not push any funds to the remote peer. If the initiator field is true, we pushed this amount to our peer, if it is false, the remote peer pushed this amount to us.
thaw_height | int64 | * This uint32 indicates if this channel is to be considered 'frozen'. A frozen channel doest not allow a cooperative channel close by the initiator. The thaw_height is the height that this restriction stops applying to the channel. This field is optional, not setting it or using a value of zero will mean the channel has no additional restrictions.


## lnrpcChannelAcceptRequest

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcChannelAcceptRequest](#lnrpcchannelacceptrequest) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcChannelBackup

Field | Type | Description
----- | ---- | ----------- 
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | * Identifies the channel that this backup belongs to.
chan_backup | byte | * Is an encrypted single-chan backup. this can be passed to RestoreChannelBackups, or the WalletUnlocker Init and Unlock methods in order to trigger the recovery protocol. When using REST, this field must be encoded as base64.


## lnrpcChannelBackups

Field | Type | Description
----- | ---- | ----------- 
chan_backups | [array lnrpcChannelBackup](#lnrpcchannelbackup) | * A set of single-chan static channel backups.


## lnrpcChannelBalanceResponse

Field | Type | Description
----- | ---- | ----------- 
balance | string | / Sum of channels balances denominated in satoshis
pending_open_balance | string | / Sum of channels pending balances denominated in satoshis


## lnrpcChannelCloseSummary

Field | Type | Description
----- | ---- | ----------- 
channel_point | string | / The outpoint (txid:index) of the funding transaction.
chan_id | string | /  The unique channel ID for the channel.
chain_hash | string | / The hash of the genesis block that this channel resides within.
closing_tx_hash | string | / The txid of the transaction which ultimately closed this channel.
remote_pubkey | string | / Public key of the remote peer that we formerly had a channel with.
capacity | string | / Total capacity of the channel.
close_height | int64 | / Height at which the funding transaction was spent.
settled_balance | string | / Settled balance at the time of channel closure
time_locked_balance | string | / The sum of all the time-locked outputs at the time of channel closure
close_type | [ChannelCloseSummaryClosureType](#channelclosesummaryclosuretype) | / Details on how the channel was closed.
open_initiator | [lnrpcInitiator](#lnrpcinitiator) | * Open initiator is the party that initiated opening the channel. Note that this value may be unknown if the channel was closed before we migrated to store open channel information after close.
close_initiator | [lnrpcInitiator](#lnrpcinitiator) | * Close initiator indicates which party initiated the close. This value will be unknown for channels that were cooperatively closed before we started tracking cooperative close initiators. Note that this indicates which party initiated a close, and it is possible for both to initiate cooperative or force closes, although only one party's close will be confirmed on chain.


## lnrpcChannelCloseUpdate

Field | Type | Description
----- | ---- | ----------- 
closing_txid | byte | 
success | boolean | 


## lnrpcChannelEdge

Field | Type | Description
----- | ---- | ----------- 
channel_id | string | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
chan_point | string | 
last_update | int64 | 
node1_pub | string | 
node2_pub | string | 
capacity | string | 
node1_policy | [lnrpcRoutingPolicy](#lnrpcroutingpolicy) | 
node2_policy | [lnrpcRoutingPolicy](#lnrpcroutingpolicy) | 


## lnrpcChannelEdgeUpdate

Field | Type | Description
----- | ---- | ----------- 
chan_id | string | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | 
capacity | string | 
routing_policy | [lnrpcRoutingPolicy](#lnrpcroutingpolicy) | 
advertising_node | string | 
connecting_node | string | 


## lnrpcChannelEventUpdate

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcChannelEventUpdate](#lnrpcchanneleventupdate) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcChannelFeeReport

Field | Type | Description
----- | ---- | ----------- 
chan_id | string | / The short channel id that this fee report belongs to.
channel_point | string | / The channel that this fee report belongs to.
base_fee_msat | string | / The base fee charged regardless of the number of milli-satoshis sent.
fee_per_mil | string | / The amount charged per milli-satoshis transferred expressed in / millionths of a satoshi.
fee_rate | double | / The effective fee rate in milli-satoshis. Computed by dividing the / fee_per_mil value by 1 million.


## lnrpcChannelGraph

Field | Type | Description
----- | ---- | ----------- 
nodes | [array lnrpcLightningNode](#lnrpclightningnode) | / The list of `LightningNode`s in this channel graph
edges | [array lnrpcChannelEdge](#lnrpcchanneledge) | / The list of `ChannelEdge`s in this channel graph


## lnrpcChannelOpenUpdate

Field | Type | Description
----- | ---- | ----------- 
channel_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | 


## lnrpcChannelPoint

Field | Type | Description
----- | ---- | ----------- 
funding_txid_bytes | byte | * Txid of the funding transaction. When using REST, this field must be encoded as base64.
funding_txid_str | string | * Hex-encoded string representing the byte-reversed hash of the funding transaction.
output_index | int64 | / The index of the output of the funding transaction


## lnrpcChannelUpdate

Field | Type | Description
----- | ---- | ----------- 
signature | byte | * The signature that validates the announced data and proves the ownership of node id.
chain_hash | byte | * The target chain that this channel was opened within. This value should be the genesis hash of the target chain. Along with the short channel ID, this uniquely identifies the channel globally in a blockchain.
chan_id | string | * The unique description of the funding transaction.
timestamp | int64 | * A timestamp that allows ordering in the case of multiple announcements. We should ignore the message if timestamp is not greater than the last-received.
message_flags | int64 | * The bitfield that describes whether optional fields are present in this update. Currently, the least-significant bit must be set to 1 if the optional field MaxHtlc is present.
channel_flags | int64 | * The bitfield that describes additional meta-data concerning how the update is to be interpreted. Currently, the least-significant bit must be set to 0 if the creating node corresponds to the first node in the previously sent channel announcement and 1 otherwise. If the second bit is set, then the channel is set to be disabled.
time_lock_delta | int64 | * The minimum number of blocks this node requires to be added to the expiry of HTLCs. This is a security parameter determined by the node operator. This value represents the required gap between the time locks of the incoming and outgoing HTLC's set to this node.
htlc_minimum_msat | string | * The minimum HTLC value which will be accepted.
base_fee | int64 | * The base fee that must be used for incoming HTLC's to this particular channel. This value will be tacked onto the required for a payment independent of the size of the payment.
fee_rate | int64 | * The fee rate that will be charged per millionth of a satoshi.
htlc_maximum_msat | string | * The maximum HTLC value which will be accepted.
extra_opaque_data | byte | * The set of data that was appended to this message, some of which we may not actually know how to iterate or parse. By holding onto this data, we ensure that we're able to properly validate the set of signatures that cover these new fields, and ensure we're able to make upgrades to the network in a forwards compatible manner.


## lnrpcCloseStatusUpdate

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcCloseStatusUpdate](#lnrpcclosestatusupdate) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcClosedChannelUpdate

Field | Type | Description
----- | ---- | ----------- 
chan_id | string | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
capacity | string | 
closed_height | int64 | 
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | 


## lnrpcClosedChannelsResponse

Field | Type | Description
----- | ---- | ----------- 
channels | [array lnrpcChannelCloseSummary](#lnrpcchannelclosesummary) | 


## lnrpcCommitmentType

This definition has no parameters.


## lnrpcConnectPeerRequest

Field | Type | Description
----- | ---- | ----------- 
addr | [lnrpcLightningAddress](#lnrpclightningaddress) | / Lightning address of the peer, in the format `<pubkey>@host`
perm | boolean | * If set, the daemon will attempt to persistently connect to the target peer. Otherwise, the call will be synchronous.


## lnrpcConnectPeerResponse

This definition has no parameters.


## lnrpcDebugLevelResponse

Field | Type | Description
----- | ---- | ----------- 
sub_systems | string | 


## lnrpcDeleteAllPaymentsResponse

This definition has no parameters.


## lnrpcDisconnectPeerResponse

This definition has no parameters.


## lnrpcEdgeLocator

Field | Type | Description
----- | ---- | ----------- 
channel_id | string | / The short channel id of this edge.
direction_reverse | boolean | * The direction of this edge. If direction_reverse is false, the direction of this edge is from the channel endpoint with the lexicographically smaller pub key to the endpoint with the larger pub key. If direction_reverse is is true, the edge goes the other way.


## lnrpcEstimateFeeResponse

Field | Type | Description
----- | ---- | ----------- 
fee_sat | string | / The total fee in satoshis.
feerate_sat_per_byte | string | / The fee rate in satoshi/byte.


## lnrpcFailure

Field | Type | Description
----- | ---- | ----------- 
code | [FailureFailureCode](#failurefailurecode) | / Failure code as defined in the Lightning spec
channel_update | [lnrpcChannelUpdate](#lnrpcchannelupdate) | / An optional channel update message.
htlc_msat | string | / A failure type-dependent htlc value.
onion_sha_256 | byte | / The sha256 sum of the onion payload.
cltv_expiry | int64 | / A failure type-dependent cltv expiry value.
flags | int64 | / A failure type-dependent flags value.
failure_source_index | int64 | * The position in the path of the intermediate or final node that generated the failure message. Position zero is the sender node.
height | int64 | / A failure type-dependent block height.


## lnrpcFeature

Field | Type | Description
----- | ---- | ----------- 
name | string | 
is_required | boolean | 
is_known | boolean | 


## lnrpcFeatureBit

This definition has no parameters.


## lnrpcFeeLimit

Field | Type | Description
----- | ---- | ----------- 
fixed | string | * The fee limit expressed as a fixed amount of satoshis.  The fields fixed and fixed_msat are mutually exclusive.
fixed_msat | string | * The fee limit expressed as a fixed amount of millisatoshis.  The fields fixed and fixed_msat are mutually exclusive.
percent | string | / The fee limit expressed as a percentage of the payment amount.


## lnrpcFeeReportResponse

Field | Type | Description
----- | ---- | ----------- 
channel_fees | [array lnrpcChannelFeeReport](#lnrpcchannelfeereport) | / An array of channel fee reports which describes the current fee schedule / for each channel.
day_fee_sum | string | / The total amount of fee revenue (in satoshis) the switch has collected / over the past 24 hrs.
week_fee_sum | string | / The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 week.
month_fee_sum | string | / The total amount of fee revenue (in satoshis) the switch has collected / over the past 1 month.


## lnrpcFloatMetric

Field | Type | Description
----- | ---- | ----------- 
value | double | / Arbitrary float value.
normalized_value | double | / The value normalized to [0,1] or [-1,1].


## lnrpcForwardingEvent

Field | Type | Description
----- | ---- | ----------- 
timestamp | string | / Timestamp is the time (unix epoch offset) that this circuit was / completed.
chan_id_in | string | / The incoming channel ID that carried the HTLC that created the circuit.
chan_id_out | string | / The outgoing channel ID that carried the preimage that completed the / circuit.
amt_in | string | / The total amount (in satoshis) of the incoming HTLC that created half / the circuit.
amt_out | string | / The total amount (in satoshis) of the outgoing HTLC that created the / second half of the circuit.
fee | string | / The total fee (in satoshis) that this payment circuit carried.
fee_msat | string | / The total fee (in milli-satoshis) that this payment circuit carried.
amt_in_msat | string | / The total amount (in milli-satoshis) of the incoming HTLC that created / half the circuit.
amt_out_msat | string | / The total amount (in milli-satoshis) of the outgoing HTLC that created / the second half of the circuit.


## lnrpcForwardingHistoryRequest

Field | Type | Description
----- | ---- | ----------- 
start_time | string | / Start time is the starting point of the forwarding history request. All / records beyond this point will be included, respecting the end time, and / the index offset.
end_time | string | / End time is the end point of the forwarding history request. The / response will carry at most 50k records between the start time and the / end time. The index offset can be used to implement pagination.
index_offset | int64 | / Index offset is the offset in the time series to start at. As each / response can only contain 50k records, callers can use this to skip / around within a packed time series.
num_max_events | int64 | / The max number of events to return in the response to this query.


## lnrpcForwardingHistoryResponse

Field | Type | Description
----- | ---- | ----------- 
forwarding_events | [array lnrpcForwardingEvent](#lnrpcforwardingevent) | / A list of forwarding events from the time slice of the time series / specified in the request.
last_offset_index | int64 | / The index of the last time in the set of returned forwarding events. Can / be used to seek further, pagination style.


## lnrpcFundingPsbtFinalize

Field | Type | Description
----- | ---- | ----------- 
signed_psbt | byte | * The funded PSBT that contains all witness data to send the exact channel capacity amount to the PK script returned in the open channel message in a previous step.
pending_chan_id | byte | / The pending channel ID of the channel to get the PSBT for.


## lnrpcFundingPsbtVerify

Field | Type | Description
----- | ---- | ----------- 
funded_psbt | byte | * The funded but not yet signed PSBT that sends the exact channel capacity amount to the PK script returned in the open channel message in a previous step.
pending_chan_id | byte | / The pending channel ID of the channel to get the PSBT for.


## lnrpcFundingShim

Field | Type | Description
----- | ---- | ----------- 
chan_point_shim | [lnrpcChanPointShim](#lnrpcchanpointshim) | * A channel shim where the channel point was fully constructed outside of lnd's wallet and the transaction might already be published.
psbt_shim | [lnrpcPsbtShim](#lnrpcpsbtshim) | * A channel shim that uses a PSBT to fund and sign the channel funding transaction.


## lnrpcFundingShimCancel

Field | Type | Description
----- | ---- | ----------- 
pending_chan_id | byte | / The pending channel ID of the channel to cancel the funding shim for.


## lnrpcFundingStateStepResp

This definition has no parameters.


## lnrpcGenSeedResponse

Field | Type | Description
----- | ---- | ----------- 
cipher_seed_mnemonic | array string | * cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed.
enciphered_seed | byte | * enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.


## lnrpcGetInfoResponse

Field | Type | Description
----- | ---- | ----------- 
version | string | / The version of the LND software that the node is running.
identity_pubkey | string | / The identity pubkey of the current node.
alias | string | / If applicable, the alias of the current node, e.g. "bob"
color | string | / The color of the current node in hex code format
num_pending_channels | int64 | / Number of pending channels
num_active_channels | int64 | / Number of active channels
num_inactive_channels | int64 | / Number of inactive channels
num_peers | int64 | / Number of peers
block_height | int64 | / The node's current view of the height of the best block
block_hash | string | / The node's current view of the hash of the best block
best_header_timestamp | string | / Timestamp of the block best known to the wallet
synced_to_chain | boolean | / Whether the wallet's view is synced to the main chain
synced_to_graph | boolean | Whether we consider ourselves synced with the public channel graph.
testnet | boolean | * Whether the current node is connected to testnet. This field is deprecated and the network field should be used instead
chains | [array lnrpcChain](#lnrpcchain) | / A list of active chains the node is connected to
uris | array string | / The URIs of the current node.
features | object | Features that our node has advertised in our init message, node announcements and invoices.


## lnrpcGraphTopologyUpdate

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcGraphTopologyUpdate](#lnrpcgraphtopologyupdate) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcHTLC

Field | Type | Description
----- | ---- | ----------- 
incoming | boolean | 
amount | string | 
hash_lock | byte | 
expiration_height | int64 | 


## lnrpcHTLCAttempt

Field | Type | Description
----- | ---- | ----------- 
status | [HTLCAttemptHTLCStatus](#htlcattempthtlcstatus) | / The status of the HTLC.
route | [lnrpcRoute](#lnrpcroute) | / The route taken by this HTLC.
attempt_time_ns | string | / The time in UNIX nanoseconds at which this HTLC was sent.
resolve_time_ns | string | * The time in UNIX nanoseconds at which this HTLC was settled or failed. This value will not be set if the HTLC is still IN_FLIGHT.
failure | [lnrpcFailure](#lnrpcfailure) | Detailed htlc failure info.


## lnrpcHop

Field | Type | Description
----- | ---- | ----------- 
chan_id | string | * The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
chan_capacity | string | 
amt_to_forward | string | 
fee | string | 
expiry | int64 | 
amt_to_forward_msat | string | 
fee_msat | string | 
pub_key | string | * An optional public key of the hop. If the public key is given, the payment can be executed without relying on a copy of the channel graph.
tlv_payload | boolean | * If set to true, then this hop will be encoded using the new variable length TLV format. Note that if any custom tlv_records below are specified, then this field MUST be set to true for them to be encoded properly.
mpp_record | [lnrpcMPPRecord](#lnrpcmpprecord) | * An optional TLV record tha singals the use of an MPP payment. If present, the receiver will enforce that that the same mpp_record is included in the final hop payload of all non-zero payments in the HTLC set. If empty, a regular single-shot payment is or was attempted.
custom_records | object | * An optional set of key-value TLV records. This is useful within the context of the SendToRoute call as it allows callers to specify arbitrary K-V pairs to drop off at each hop within the onion.


## lnrpcHopHint

Field | Type | Description
----- | ---- | ----------- 
node_id | string | / The public key of the node at the start of the channel.
chan_id | string | / The unique identifier of the channel.
fee_base_msat | int64 | / The base fee of the channel denominated in millisatoshis.
fee_proportional_millionths | int64 | * The fee rate of the channel for sending one satoshi across it denominated in millionths of a satoshi.
cltv_expiry_delta | int64 | / The time-lock delta of the channel.


## lnrpcInitWalletRequest

Field | Type | Description
----- | ---- | ----------- 
wallet_password | byte | * wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon. When using REST, this field must be encoded as base64.
cipher_seed_mnemonic | array string | * cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed.
aezeed_passphrase | byte | * aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. When using REST, this field must be encoded as base64.
recovery_window | int32 | * recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) | * channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.


## lnrpcInitWalletResponse

This definition has no parameters.


## lnrpcInitiator

This definition has no parameters.


## lnrpcInvoice

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcInvoice](#lnrpcinvoice) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcInvoiceHTLC

Field | Type | Description
----- | ---- | ----------- 
chan_id | string | / Short channel id over which the htlc was received.
htlc_index | string | / Index identifying the htlc on the channel.
amt_msat | string | / The amount of the htlc in msat.
accept_height | int32 | / Block height at which this htlc was accepted.
accept_time | string | / Time at which this htlc was accepted.
resolve_time | string | / Time at which this htlc was settled or canceled.
expiry_height | int32 | / Block height at which this htlc expires.
state | [lnrpcInvoiceHTLCState](#lnrpcinvoicehtlcstate) | / Current state the htlc is in.
custom_records | object | / Custom tlv records.
mpp_total_amt_msat | string | / The total amount of the mpp payment in msat.


## lnrpcInvoiceHTLCState

This definition has no parameters.


## lnrpcKeyDescriptor

Field | Type | Description
----- | ---- | ----------- 
raw_key_bytes | byte | * The raw bytes of the key being identified.
key_loc | [lnrpcKeyLocator](#lnrpckeylocator) | * The key locator that identifies which key to use for signing.


## lnrpcKeyLocator

Field | Type | Description
----- | ---- | ----------- 
key_family | int32 | / The family of key being identified.
key_index | int32 | / The precise index of the key being identified.


## lnrpcLightningAddress

Field | Type | Description
----- | ---- | ----------- 
pubkey | string | / The identity pubkey of the Lightning node
host | string | / The network location of the lightning node, e.g. `69.69.69.69:1337` or / `localhost:10011`


## lnrpcLightningNode

Field | Type | Description
----- | ---- | ----------- 
last_update | int64 | 
pub_key | string | 
alias | string | 
addresses | [array lnrpcNodeAddress](#lnrpcnodeaddress) | 
color | string | 
features | object | 


## lnrpcListChannelsResponse

Field | Type | Description
----- | ---- | ----------- 
channels | [array lnrpcChannel](#lnrpcchannel) | / The list of active channels


## lnrpcListInvoiceResponse

Field | Type | Description
----- | ---- | ----------- 
invoices | [array lnrpcInvoice](#lnrpcinvoice) | * A list of invoices from the time slice of the time series specified in the request.
last_index_offset | string | * The index of the last item in the set of returned invoices. This can be used to seek further, pagination style.
first_index_offset | string | * The index of the last item in the set of returned invoices. This can be used to seek backwards, pagination style.


## lnrpcListPaymentsResponse

Field | Type | Description
----- | ---- | ----------- 
payments | [array lnrpcPayment](#lnrpcpayment) | / The list of payments
first_index_offset | string | * The index of the first item in the set of returned payments. This can be used as the index_offset to continue seeking backwards in the next request.
last_index_offset | string | * The index of the last item in the set of returned payments. This can be used as the index_offset to continue seeking forwards in the next request.


## lnrpcListPeersResponse

Field | Type | Description
----- | ---- | ----------- 
peers | [array lnrpcPeer](#lnrpcpeer) | / The list of currently connected peers


## lnrpcListUnspentResponse

Field | Type | Description
----- | ---- | ----------- 
utxos | [array lnrpcUtxo](#lnrpcutxo) | / A list of utxos


## lnrpcMPPRecord

Field | Type | Description
----- | ---- | ----------- 
payment_addr | byte | * A unique, random identifier used to authenticate the sender as the intended payer of a multi-path payment. The payment_addr must be the same for all subpayments, and match the payment_addr provided in the receiver's invoice. The same payment_addr must be used on all subpayments.
total_amt_msat | string | * The total amount in milli-satoshis being sent as part of a larger multi-path payment. The caller is responsible for ensuring subpayments to the same node and payment_hash sum exactly to total_amt_msat. The same total_amt_msat must be used on all subpayments.


## lnrpcMacaroonPermission

Field | Type | Description
----- | ---- | ----------- 
entity | string | / The entity a permission grants access to.
action | string | / The action that is granted.


## lnrpcMultiChanBackup

Field | Type | Description
----- | ---- | ----------- 
chan_points | [array lnrpcChannelPoint](#lnrpcchannelpoint) | * Is the set of all channels that are included in this multi-channel backup.
multi_chan_backup | byte | * A single encrypted blob containing all the static channel backups of the channel listed above. This can be stored as a single file or blob, and safely be replaced with any prior/future versions. When using REST, this field must be encoded as base64.


## lnrpcNetworkInfo

Field | Type | Description
----- | ---- | ----------- 
graph_diameter | int64 | 
avg_out_degree | double | 
max_out_degree | int64 | 
num_nodes | int64 | 
num_channels | int64 | 
total_network_capacity | string | 
avg_channel_size | double | 
min_channel_size | string | 
max_channel_size | string | 
median_channel_size_sat | string | 
num_zombie_chans | string | The number of edges marked as zombies.


## lnrpcNewAddressResponse

Field | Type | Description
----- | ---- | ----------- 
address | string | / The newly generated wallet address


## lnrpcNodeAddress

Field | Type | Description
----- | ---- | ----------- 
network | string | 
addr | string | 


## lnrpcNodeInfo

Field | Type | Description
----- | ---- | ----------- 
node | [lnrpcLightningNode](#lnrpclightningnode) | * An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge.
num_channels | int64 | / The total number of channels for the node.
total_capacity | string | / The sum of all channels capacity for the node, denominated in satoshis.
channels | [array lnrpcChannelEdge](#lnrpcchanneledge) | / A list of all public channels for the node.


## lnrpcNodeMetricType

This definition has no parameters.


## lnrpcNodeMetricsResponse

Field | Type | Description
----- | ---- | ----------- 
betweenness_centrality | object | * Betweenness centrality is the sum of the ratio of shortest paths that pass through the node for each pair of nodes in the graph (not counting paths starting or ending at this node). Map of node pubkey to betweenness centrality of the node. Normalized values are in the [0,1] closed interval.


## lnrpcNodePair

Field | Type | Description
----- | ---- | ----------- 
from | byte | * The sending node of the pair. When using REST, this field must be encoded as base64.
to | byte | * The receiving node of the pair. When using REST, this field must be encoded as base64.


## lnrpcNodeUpdate

Field | Type | Description
----- | ---- | ----------- 
addresses | array string | 
identity_key | string | 
global_features | byte | 
alias | string | 
color | string | 


## lnrpcOpenChannelRequest

Field | Type | Description
----- | ---- | ----------- 
node_pubkey | byte | * The pubkey of the node to open a channel with. When using REST, this field must be encoded as base64.
node_pubkey_string | string | * The hex encoded pubkey of the node to open a channel with. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
local_funding_amount | string | / The number of satoshis the wallet should commit to the channel
push_sat | string | / The number of satoshis to push to the remote side as part of the initial / commitment state
target_conf | int32 | / The target number of blocks that the funding transaction should be / confirmed by.
sat_per_byte | string | / A manual fee rate set in sat/byte that should be used when crafting the / funding transaction.
private | boolean | / Whether this channel should be private, not announced to the greater / network.
min_htlc_msat | string | / The minimum value in millisatoshi we will require for incoming HTLCs on / the channel.
remote_csv_delay | int64 | / The delay we require on the remote's commitment transaction. If this is / not set, it will be scaled automatically with the channel size.
min_confs | int32 | / The minimum number of confirmations each one of your outputs used for / the funding transaction must satisfy.
spend_unconfirmed | boolean | / Whether unconfirmed outputs should be used as inputs for the funding / transaction.
close_address | string | Close address is an optional address which specifies the address to which funds should be paid out to upon cooperative close. This field may only be set if the peer supports the option upfront feature bit (call listpeers to check). The remote peer will only accept cooperative closes to this address if it is set.  Note: If this value is set on channel creation, you will *not* be able to cooperatively close out to a different address.
funding_shim | [lnrpcFundingShim](#lnrpcfundingshim) | * Funding shims are an optional argument that allow the caller to intercept certain funding functionality. For example, a shim can be provided to use a particular key for the commitment key (ideally cold) rather than use one that is generated by the wallet as normal, or signal that signing will be carried out in an interactive manner (PSBT based).


## lnrpcOpenStatusUpdate

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcOpenStatusUpdate](#lnrpcopenstatusupdate) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcOutPoint

Field | Type | Description
----- | ---- | ----------- 
txid_bytes | byte | / Raw bytes representing the transaction id.
txid_str | string | / Reversed, hex-encoded string representing the transaction id.
output_index | int64 | / The index of the output on the transaction.


## lnrpcPayReq

Field | Type | Description
----- | ---- | ----------- 
destination | string | 
payment_hash | string | 
num_satoshis | string | 
timestamp | string | 
expiry | string | 
description | string | 
description_hash | string | 
fallback_addr | string | 
cltv_expiry | string | 
route_hints | [array lnrpcRouteHint](#lnrpcroutehint) | 
payment_addr | byte | 
num_msat | string | 
features | object | 


## lnrpcPayment

Field | Type | Description
----- | ---- | ----------- 
payment_hash | string | / The payment hash
value | string | / Deprecated, use value_sat or value_msat.
creation_date | string | / Deprecated, use creation_time_ns
path | array string | / The path this payment took.
fee | string | / Deprecated, use fee_sat or fee_msat.
payment_preimage | string | / The payment preimage
value_sat | string | / The value of the payment in satoshis
value_msat | string | / The value of the payment in milli-satoshis
payment_request | string | / The optional payment request being fulfilled.
status | [PaymentPaymentStatus](#paymentpaymentstatus) | The status of the payment.
fee_sat | string | /  The fee paid for this payment in satoshis
fee_msat | string | /  The fee paid for this payment in milli-satoshis
creation_time_ns | string | / The time in UNIX nanoseconds at which the payment was created.
htlcs | [array lnrpcHTLCAttempt](#lnrpchtlcattempt) | / The HTLCs made in attempt to settle the payment [EXPERIMENTAL].
payment_index | string | * The creation index of this payment. Each payment can be uniquely identified by this index, which may not strictly increment by 1 for payments made in older versions of lnd.


## lnrpcPeer

Field | Type | Description
----- | ---- | ----------- 
pub_key | string | / The identity pubkey of the peer
address | string | / Network address of the peer; eg `127.0.0.1:10011`
bytes_sent | string | / Bytes of data transmitted to this peer
bytes_recv | string | / Bytes of data transmitted from this peer
sat_sent | string | / Satoshis sent to this peer
sat_recv | string | / Satoshis received from this peer
inbound | boolean | / A channel is inbound if the counterparty initiated the channel
ping_time | string | / Ping time to this peer
sync_type | [PeerSyncType](#peersynctype) | The type of sync we are currently performing with this peer.
features | object | / Features advertised by the remote peer in their init message.
errors | [array lnrpcTimestampedError](#lnrpctimestampederror) | The latest errors received from our peer with timestamps, limited to the 10 most recent errors. These errors are tracked across peer connections, but are not persisted across lnd restarts. Note that these errors are only stored for peers that we have channels open with, to prevent peers from spamming us with errors at no cost.


## lnrpcPeerEvent

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcPeerEvent](#lnrpcpeerevent) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcPendingChannelsResponse

Field | Type | Description
----- | ---- | ----------- 
total_limbo_balance | string | / The balance in satoshis encumbered in pending channels
pending_open_channels | [array PendingChannelsResponsePendingOpenChannel](#pendingchannelsresponsependingopenchannel) | / Channels pending opening
pending_closing_channels | [array PendingChannelsResponseClosedChannel](#pendingchannelsresponseclosedchannel) | Deprecated: Channels pending closing previously contained cooperatively closed channels with a single confirmation. These channels are now considered closed from the time we see them on chain.
pending_force_closing_channels | [array PendingChannelsResponseForceClosedChannel](#pendingchannelsresponseforceclosedchannel) | / Channels pending force closing
waiting_close_channels | [array PendingChannelsResponseWaitingCloseChannel](#pendingchannelsresponsewaitingclosechannel) | / Channels waiting for closing tx to confirm


## lnrpcPendingHTLC

Field | Type | Description
----- | ---- | ----------- 
incoming | boolean | / The direction within the channel that the htlc was sent
amount | string | / The total value of the htlc
outpoint | string | / The final output to be swept back to the user's wallet
maturity_height | int64 | / The next block height at which we can spend the current stage
blocks_til_maturity | int32 | * The number of blocks remaining until the current stage can be swept. Negative values indicate how many blocks have passed since becoming mature.
stage | int64 | / Indicates whether the htlc is in its first or second stage of recovery


## lnrpcPendingUpdate

Field | Type | Description
----- | ---- | ----------- 
txid | byte | 
output_index | int64 | 


## lnrpcPolicyUpdateRequest

Field | Type | Description
----- | ---- | ----------- 
global | boolean | / If set, then this update applies to all currently active channels.
chan_point | [lnrpcChannelPoint](#lnrpcchannelpoint) | / If set, this update will target a specific channel.
base_fee_msat | string | / The base fee charged regardless of the number of milli-satoshis sent.
fee_rate | double | / The effective fee rate in milli-satoshis. The precision of this value / goes up to 6 decimal places, so 1e-6.
time_lock_delta | int64 | / The required timelock delta for HTLCs forwarded over the channel.
max_htlc_msat | string | / If set, the maximum HTLC size in milli-satoshis. If unset, the maximum / HTLC will be unchanged.
min_htlc_msat | string | / The minimum HTLC size in milli-satoshis. Only applied if / min_htlc_msat_specified is true.
min_htlc_msat_specified | boolean | / If true, min_htlc_msat is applied.


## lnrpcPolicyUpdateResponse

This definition has no parameters.


## lnrpcPsbtShim

Field | Type | Description
----- | ---- | ----------- 
pending_chan_id | byte | * A unique identifier of 32 random bytes that will be used as the pending channel ID to identify the PSBT state machine when interacting with it and on the wire protocol to initiate the funding request.
base_psbt | byte | * An optional base PSBT the new channel output will be added to. If this is non-empty, it must be a binary serialized PSBT.


## lnrpcQueryRoutesResponse

Field | Type | Description
----- | ---- | ----------- 
routes | [array lnrpcRoute](#lnrpcroute) | * The route that results from the path finding operation. This is still a repeated field to retain backwards compatibility.
success_prob | double | * The success probability of the returned route based on the current mission control state. [EXPERIMENTAL]


## lnrpcReadyForPsbtFunding

Field | Type | Description
----- | ---- | ----------- 
funding_address | string | * The P2WSH address of the channel funding multisig address that the below specified amount in satoshis needs to be sent to.
funding_amount | string | * The exact amount in satoshis that needs to be sent to the above address to fund the pending channel.
psbt | byte | * A raw PSBT that contains the pending channel output. If a base PSBT was provided in the PsbtShim, this is the base PSBT with one additional output. If no base PSBT was specified, this is an otherwise empty PSBT with exactly one output.


## lnrpcRestoreBackupResponse

This definition has no parameters.


## lnrpcRestoreChanBackupRequest

Field | Type | Description
----- | ---- | ----------- 
chan_backups | [lnrpcChannelBackups](#lnrpcchannelbackups) | * The channels to restore as a list of channel/backup pairs.
multi_chan_backup | byte | * The channels to restore in the packed multi backup format. When using REST, this field must be encoded as base64.


## lnrpcRoute

Field | Type | Description
----- | ---- | ----------- 
total_time_lock | int64 | * The cumulative (final) time lock across the entire route. This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment.
total_fees | string | * The sum of the fees paid at each hop within the final route. In the case of a one-hop payment, this value will be zero as we don't need to pay a fee to ourselves.
total_amt | string | * The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees.
hops | [array lnrpcHop](#lnrpchop) | * Contains details concerning the specific forwarding details at each hop.
total_fees_msat | string | * The total fees in millisatoshis.
total_amt_msat | string | * The total amount in millisatoshis.


## lnrpcRouteHint

Field | Type | Description
----- | ---- | ----------- 
hop_hints | [array lnrpcHopHint](#lnrpchophint) | * A list of hop hints that when chained together can assist in reaching a specific destination.


## lnrpcRoutingPolicy

Field | Type | Description
----- | ---- | ----------- 
time_lock_delta | int64 | 
min_htlc | string | 
fee_base_msat | string | 
fee_rate_milli_msat | string | 
disabled | boolean | 
max_htlc_msat | string | 
last_update | int64 | 


## lnrpcSendCoinsRequest

Field | Type | Description
----- | ---- | ----------- 
addr | string | / The address to send coins to
amount | string | / The amount in satoshis to send
target_conf | int32 | / The target number of blocks that this transaction should be confirmed / by.
sat_per_byte | string | / A manual fee rate set in sat/byte that should be used when crafting the / transaction.
send_all | boolean | * If set, then the amount field will be ignored, and lnd will attempt to send all the coins under control of the internal wallet to the specified address.


## lnrpcSendCoinsResponse

Field | Type | Description
----- | ---- | ----------- 
txid | string | / The transaction ID of the transaction


## lnrpcSendManyResponse

Field | Type | Description
----- | ---- | ----------- 
txid | string | / The id of the transaction


## lnrpcSendRequest

Field | Type | Description
----- | ---- | ----------- 
dest | byte | * The identity pubkey of the payment recipient. When using REST, this field must be encoded as base64.
dest_string | string | * The hex-encoded identity pubkey of the payment recipient. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
amt | string | * The amount to send expressed in satoshis.  The fields amt and amt_msat are mutually exclusive.
amt_msat | string | * The amount to send expressed in millisatoshis.  The fields amt and amt_msat are mutually exclusive.
payment_hash | byte | * The hash to use within the payment's HTLC. When using REST, this field must be encoded as base64.
payment_hash_string | string | * The hex-encoded hash to use within the payment's HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
payment_request | string | * A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
final_cltv_delta | int32 | * The CLTV delta from the current height that should be used to set the timelock for the final hop.
fee_limit | [lnrpcFeeLimit](#lnrpcfeelimit) | * The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.
outgoing_chan_id | string | * The channel id of the channel that must be taken to the first hop. If zero, any channel may be used.
last_hop_pubkey | byte | * The pubkey of the last hop of the route. If empty, any hop may be used.
cltv_limit | int64 | * An optional maximum total time lock for the route. This should not exceed lnd's `--max-cltv-expiry` setting. If zero, then the value of `--max-cltv-expiry` is enforced.
dest_custom_records | object | * An optional field that can be used to pass an arbitrary set of TLV records to a peer which understands the new records. This can be used to pass application specific data during the payment attempt. Record types are required to be in the custom range >= 65536. When using REST, the values must be encoded as base64.
allow_self_payment | boolean | / If set, circular payments to self are permitted.
dest_features | [array lnrpcFeatureBit](#lnrpcfeaturebit) | * Features assumed to be supported by the final node. All transitive feature dependencies must also be set properly. For a given feature bit pair, either optional or remote may be set, but not both. If this field is nil or empty, the router will try to load destination features from the graph as a fallback.


## lnrpcSendResponse

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcSendResponse](#lnrpcsendresponse) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcSendToRouteRequest

Field | Type | Description
----- | ---- | ----------- 
payment_hash | byte | * The payment hash to use for the HTLC. When using REST, this field must be encoded as base64.
payment_hash_string | string | * An optional hex-encoded payment hash to be used for the HTLC. Deprecated now that the REST gateway supports base64 encoding of bytes fields.
route | [lnrpcRoute](#lnrpcroute) | / Route that should be used to attempt to complete the payment.


## lnrpcSignMessageRequest

Field | Type | Description
----- | ---- | ----------- 
msg | byte | * The message to be signed. When using REST, this field must be encoded as base64.


## lnrpcSignMessageResponse

Field | Type | Description
----- | ---- | ----------- 
signature | string | / The signature for the given message


## lnrpcStopResponse

This definition has no parameters.


## lnrpcTimestampedError

Field | Type | Description
----- | ---- | ----------- 
timestamp | string | The unix timestamp in seconds when the error occurred.
error | string | The string representation of the error sent by our peer.


## lnrpcTransaction

Field | Type | Description
----- | ---- | ----------- 
result | [lnrpcTransaction](#lnrpctransaction) | 
error | [runtimeStreamError](#runtimestreamerror) | 


## lnrpcTransactionDetails

Field | Type | Description
----- | ---- | ----------- 
transactions | [array lnrpcTransaction](#lnrpctransaction) | / The list of transactions relevant to the wallet.


## lnrpcUnlockWalletRequest

Field | Type | Description
----- | ---- | ----------- 
wallet_password | byte | * wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly. When using REST, this field must be encoded as base64.
recovery_window | int32 | * recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [lnrpcChanBackupSnapshot](#lnrpcchanbackupsnapshot) | * channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.


## lnrpcUnlockWalletResponse

This definition has no parameters.


## lnrpcUtxo

Field | Type | Description
----- | ---- | ----------- 
address_type | [lnrpcAddressType](#lnrpcaddresstype) | / The type of address
address | string | / The address
amount_sat | string | / The value of the unspent coin in satoshis
pk_script | string | / The pkscript in hex
outpoint | [lnrpcOutPoint](#lnrpcoutpoint) | / The outpoint in format txid:n
confirmations | string | / The number of confirmations for the Utxo


## lnrpcVerifyChanBackupResponse

This definition has no parameters.


## lnrpcVerifyMessageRequest

Field | Type | Description
----- | ---- | ----------- 
msg | byte | * The message over which the signature is to be verified. When using REST, this field must be encoded as base64.
signature | string | / The signature to be verified over the given message


## lnrpcVerifyMessageResponse

Field | Type | Description
----- | ---- | ----------- 
valid | boolean | / Whether the signature was valid over the given message
pubkey | string | / The pubkey recovered from the signature


## lnrpcWalletBalanceResponse

Field | Type | Description
----- | ---- | ----------- 
total_balance | string | / The balance of the wallet
confirmed_balance | string | / The confirmed balance of a wallet(with >= 1 confirmations)
unconfirmed_balance | string | / The unconfirmed balance of a wallet(with 0 confirmations)


## protobufAny

Field | Type | Description
----- | ---- | ----------- 
type_url | string | 
value | byte | 


## runtimeStreamError

Field | Type | Description
----- | ---- | ----------- 
grpc_code | int32 | 
http_code | int32 | 
message | string | 
http_status | string | 
details | [array protobufAny](#protobufany) | 

