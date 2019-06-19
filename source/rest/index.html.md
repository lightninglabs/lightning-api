---
title: LND REST API Reference

language_tabs:
  - shell
  - python
  - javascript

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:max@lightning.engineering'>Contact Us</a>
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

The original `rpc.proto` file from which the gRPC documentation was generated
can be found [here](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

NOTE: The documentation is currently lacking how to receive streaming responses
from streaming endpoints in JavaScript. If you would like to contribute this
change, please take a look at [https://github.com/lightninglabs/lightning-api](https://github.com/lightninglabs/lightning-api).

NOTE: The `byte` field type must be set as the base64 encoded string
representation of a raw byte array.

Alternatively, the gRPC documentation can be found [here](../).


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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/balance/blockchain',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "total_balance": <string>, 
    "confirmed_balance": <string>, 
    "unconfirmed_balance": <string>, 
}
```

### GET /v1/balance/blockchain
WalletBalance returns total unspent outputs(confirmed and unconfirmed), all confirmed unspent outputs and all unconfirmed unspent outputs under control of the wallet.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
total_balance | string | The balance of the wallet 
confirmed_balance | string | The confirmed balance of a wallet(with >= 1 confirmations) 
unconfirmed_balance | string | The unconfirmed balance of a wallet(with 0 confirmations)  



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/balance/channels',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "balance": <string>, 
    "pending_open_balance": <string>, 
}
```

### GET /v1/balance/channels
ChannelBalance returns the total funds available across all open channels in satoshis.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
balance | string | Sum of channels balances denominated in satoshis 
pending_open_balance | string | Sum of channels pending balances denominated in satoshis  



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
> var fs = require('fs');
> var request = require('request');
> var requestBody = { 
    current_password: <byte>,
    new_password: <byte>,
  };
> var options = {
    url: 'https://localhost:8080/v1/changepassword',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/changepassword
ChangePassword changes the password of the encrypted wallet. This will automatically unlock the wallet database if successful.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
current_password | byte | body |  current_password should be the current valid passphrase used to unlock the daemon.
new_password | byte | body |  new_password should be the new passphrase that will be needed to unlock the daemon.

### Response 

This response has no parameters.




# /v1/channels


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels 
{ 
    "channels": <array Channel>, 
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
    "channels": <array Channel>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "channels": <array Channel>, 
}
```

### GET /v1/channels
ListChannels returns a description of all the open channels that this node is a participant in.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
active_only | boolean | query | 
inactive_only | boolean | query | 
public_only | boolean | query | 
private_only | boolean | query | 

### Response 

Field | Type | Description
----- | ---- | ----------- 
channels | [array Channel](#channel) | The list of active channels  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels  \
    -d '{ "node_pubkey":<byte>,"node_pubkey_string":<string>,"local_funding_amount":<string>,"push_sat":<string>,"target_conf":<int32>,"sat_per_byte":<string>,"private":<boolean>,"min_htlc_msat":<string>,"remote_csv_delay":<int64>,"min_confs":<int32>,"spend_unconfirmed":<boolean>, }' 
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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
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
  };
> var options = {
    url: 'https://localhost:8080/v1/channels',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "funding_txid_bytes": <byte>, 
    "funding_txid_str": <string>, 
    "output_index": <int64>, 
}
```

### POST /v1/channels
 OpenChannelSync is a synchronous version of the OpenChannel RPC call. This call is meant to be consumed by clients to the REST proxy. As with all other sync calls, all byte slices are intended to be populated as hex encoded strings.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
node_pubkey | byte | body | The pubkey of the node to open a channel with
node_pubkey_string | string | body | The hex encoded pubkey of the node to open a channel with
local_funding_amount | string | body | The number of satoshis the wallet should commit to the channel
push_sat | string | body | The number of satoshis to push to the remote side as part of the initial commitment state
target_conf | int32 | body | The target number of blocks that the funding transaction should be confirmed by.
sat_per_byte | string | body | A manual fee rate set in sat/byte that should be used when crafting the funding transaction.
private | boolean | body | Whether this channel should be private, not announced to the greater network.
min_htlc_msat | string | body | The minimum value in millisatoshi we will require for incoming HTLCs on the channel.
remote_csv_delay | int64 | body | The delay we require on the remote's commitment transaction. If this is not set, it will be scaled automatically with the channel size.
min_confs | int32 | body | The minimum number of confirmations each one of your outputs used for the funding transaction must satisfy.
spend_unconfirmed | boolean | body | Whether unconfirmed outputs should be used as inputs for the funding transaction.

### Response 

Field | Type | Description
----- | ---- | ----------- 
funding_txid_bytes | byte | Txid of the funding transaction 
funding_txid_str | string | Hex-encoded string representing the funding transaction 
output_index | int64 | The index of the output of the funding transaction  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X DELETE --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index} 
{ 
    "close_pending": <PendingUpdate>, 
    "chan_close": <ChannelCloseUpdate>, 
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
    "close_pending": <PendingUpdate>, 
    "chan_close": <ChannelCloseUpdate>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.delete(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "close_pending": <PendingUpdate>, 
    "chan_close": <ChannelCloseUpdate>, 
}
```

### DELETE /v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}
CloseChannel attempts to close an active channel identified by its channel outpoint (ChannelPoint). The actions of this method can additionally be augmented to attempt a force close after a timeout period in the case of an inactive peer. If a non-force close (cooperative closure) is requested, then the user can specify either a target number of blocks until the closure transaction is confirmed, or a manual fee rate. If neither are specified, then a default lax, block confirmation target is used.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
channel_point.funding_txid_str | string | path | 
channel_point.output_index | int64 | path | 

### Response (streaming)

Field | Type | Description
----- | ---- | ----------- 
close_pending | [PendingUpdate](#pendingupdate) |  
chan_close | [ChannelCloseUpdate](#channelcloseupdate) |   



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.delete(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### DELETE /v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}
AbandonChannel removes all channel state from the database except for a close summary. This method can be used to get rid of permanently unusable channels due to bugs fixed in newer versions of lnd. Only available when in debug builds of lnd.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
channel_point.funding_txid_str | string | path | 
channel_point.output_index | int64 | path | 

### Response 

This response has no parameters.




# /v1/channels/backup


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup 
{ 
    "single_chan_backups": <ChannelBackups>, 
    "multi_chan_backup": <MultiChanBackup>, 
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
    "single_chan_backups": <ChannelBackups>, 
    "multi_chan_backup": <MultiChanBackup>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels/backup',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "single_chan_backups": <ChannelBackups>, 
    "multi_chan_backup": <MultiChanBackup>, 
}
```

### GET /v1/channels/backup
 ExportAllChannelBackups returns static channel backups for all existing channels known to lnd. A set of regular singular static channel backups for each channel are returned. Additionally, a multi-channel backup is returned as well, which contains a single encrypted blob containing the backups of each channel.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) |  The set of new channels that have been added since the last channel backup snapshot was requested. 
multi_chan_backup | [MultiChanBackup](#multichanbackup) |  A multi-channel backup that covers all open channels currently known to lnd.  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index} 
{ 
    "chan_point": <ChannelPoint>, 
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
    "chan_point": <ChannelPoint>, 
    "chan_backup": <byte>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "chan_point": <ChannelPoint>, 
    "chan_backup": <byte>, 
}
```

### GET /v1/channels/backup/{chan_point.funding_txid_str}/{chan_point.output_index}
ExportChannelBackup attempts to return an encrypted static channel backup for the target channel identified by it channel point. The backup is encrypted with a key generated from the aezeed seed of the user. The returned backup can either be restored using the RestoreChannelBackup method once lnd is running, or via the InitWallet and UnlockWallet methods from the WalletUnlocker service.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
chan_point.funding_txid_str | string | path | 
chan_point.output_index | int64 | path | 
chan_point.funding_txid_bytes | string | query | Txid of the funding transaction.

### Response 

Field | Type | Description
----- | ---- | ----------- 
chan_point | [ChannelPoint](#channelpoint) |  Identifies the channel that this backup belongs to. 
chan_backup | byte |  Is an encrypted single-chan backup. this can be passed to RestoreChannelBackups, or the WalletUnlocker Init and Unlock methods in order to trigger the recovery protocol.  



# /v1/channels/backup/restore


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup/restore  \
    -d '{ "chan_backups":<ChannelBackups>,"multi_chan_backup":<byte>, }' 
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
        'chan_backups': <ChannelBackups>, 
        'multi_chan_backup': base64.b64encode(<byte>).decode(), 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    chan_backups: <ChannelBackups>,
    multi_chan_backup: <byte>,
  };
> var options = {
    url: 'https://localhost:8080/v1/channels/backup/restore',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/channels/backup/restore
RestoreChannelBackups accepts a set of singular channel backups, or a single encrypted multi-chan backup and attempts to recover any funds remaining within the channel. If we are able to unpack the backup, then the new channel will be shown under listchannels, as well as pending channels.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
chan_backups | [ChannelBackups](#channelbackups) | body | 
multi_chan_backup | byte | body | 

### Response 

This response has no parameters.




# /v1/channels/backup/verify


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/backup/verify  \
    -d '{ "single_chan_backups":<ChannelBackups>,"multi_chan_backup":<MultiChanBackup>, }' 
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
        'single_chan_backups': <ChannelBackups>, 
        'multi_chan_backup': <MultiChanBackup>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    single_chan_backups: <ChannelBackups>,
    multi_chan_backup: <MultiChanBackup>,
  };
> var options = {
    url: 'https://localhost:8080/v1/channels/backup/verify',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/channels/backup/verify
 VerifyChanBackup allows a caller to verify the integrity of a channel backup snapshot. This method will accept either a packed Single or a packed Multi. Specifying both will result in an error.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) | body |  The set of new channels that have been added since the last channel backup snapshot was requested.
multi_chan_backup | [MultiChanBackup](#multichanbackup) | body |  A multi-channel backup that covers all open channels currently known to lnd.

### Response 

This response has no parameters.




# /v1/channels/closed


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/closed 
{ 
    "channels": <array ChannelCloseSummary>, 
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
    "channels": <array ChannelCloseSummary>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels/closed',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "channels": <array ChannelCloseSummary>, 
}
```

### GET /v1/channels/closed
ClosedChannels returns a description of all the closed channels that  this node was a participant in.

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
channels | [array ChannelCloseSummary](#channelclosesummary) |   



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/channels/pending',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "total_limbo_balance": <string>, 
    "pending_open_channels": <array PendingChannelsResponsePendingOpenChannel>, 
    "pending_closing_channels": <array PendingChannelsResponseClosedChannel>, 
    "pending_force_closing_channels": <array PendingChannelsResponseForceClosedChannel>, 
    "waiting_close_channels": <array PendingChannelsResponseWaitingCloseChannel>, 
}
```

### GET /v1/channels/pending
PendingChannels returns a list of all the channels that are currently considered "pending". A channel is pending if it has finished the funding workflow and is waiting for confirmations for the funding txn, or is in the process of closure, either initiated cooperatively or non-cooperatively.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
total_limbo_balance | string | The balance in satoshis encumbered in pending channels 
pending_open_channels | [array PendingChannelsResponsePendingOpenChannel](#pendingchannelsresponsependingopenchannel) | Channels pending opening 
pending_closing_channels | [array PendingChannelsResponseClosedChannel](#pendingchannelsresponseclosedchannel) | Channels pending closing 
pending_force_closing_channels | [array PendingChannelsResponseForceClosedChannel](#pendingchannelsresponseforceclosedchannel) | Channels pending force closing 
waiting_close_channels | [array PendingChannelsResponseWaitingCloseChannel](#pendingchannelsresponsewaitingclosechannel) | Channels waiting for closing tx to confirm  



# /v1/channels/transactions


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/transactions  \
    -d '{ "dest":<byte>,"dest_string":<string>,"amt":<string>,"payment_hash":<byte>,"payment_hash_string":<string>,"payment_request":<string>,"final_cltv_delta":<int32>,"fee_limit":<FeeLimit>,"outgoing_chan_id":<string>,"cltv_limit":<int64>, }' 
{ 
    "payment_error": <string>, 
    "payment_preimage": <byte>, 
    "payment_route": <Route>, 
    "payment_hash": <byte>, 
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
        'payment_hash': base64.b64encode(<byte>).decode(), 
        'payment_hash_string': <string>, 
        'payment_request': <string>, 
        'final_cltv_delta': <int32>, 
        'fee_limit': <FeeLimit>, 
        'outgoing_chan_id': <string>, 
        'cltv_limit': <int64>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "payment_error": <string>, 
    "payment_preimage": <byte>, 
    "payment_route": <Route>, 
    "payment_hash": <byte>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    dest: <byte>,
    dest_string: <string>,
    amt: <string>,
    payment_hash: <byte>,
    payment_hash_string: <string>,
    payment_request: <string>,
    final_cltv_delta: <int32>,
    fee_limit: <FeeLimit>,
    outgoing_chan_id: <string>,
    cltv_limit: <int64>,
  };
> var options = {
    url: 'https://localhost:8080/v1/channels/transactions',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "payment_error": <string>, 
    "payment_preimage": <byte>, 
    "payment_route": <Route>, 
    "payment_hash": <byte>, 
}
```

### POST /v1/channels/transactions
 SendPaymentSync is the synchronous non-streaming version of SendPayment. This RPC is intended to be consumed by clients of the REST proxy. Additionally, this RPC expects the destination's public key and the payment hash (if any) to be encoded as hex strings.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
dest | byte | body | The identity pubkey of the payment recipient
dest_string | string | body | The hex-encoded identity pubkey of the payment recipient
amt | string | body | Number of satoshis to send.
payment_hash | byte | body | The hash to use within the payment's HTLC
payment_hash_string | string | body | The hex-encoded hash to use within the payment's HTLC
payment_request | string | body |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
final_cltv_delta | int32 | body |  The CLTV delta from the current height that should be used to set the timelock for the final hop.
fee_limit | [FeeLimit](#feelimit) | body |  The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.
outgoing_chan_id | string | body |  The channel id of the channel that must be taken to the first hop. If zero, any channel may be used.
cltv_limit | int64 | body |  An optional maximum total time lock for the route. If zero, there is no maximum enforced.

### Response 

Field | Type | Description
----- | ---- | ----------- 
payment_error | string |  
payment_preimage | byte |  
payment_route | [Route](#route) |  
payment_hash | byte |   



# /v1/channels/transactions/route


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/channels/transactions/route  \
    -d '{ "payment_hash":<byte>,"payment_hash_string":<string>,"route":<Route>, }' 
{ 
    "payment_error": <string>, 
    "payment_preimage": <byte>, 
    "payment_route": <Route>, 
    "payment_hash": <byte>, 
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
        'route': <Route>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "payment_error": <string>, 
    "payment_preimage": <byte>, 
    "payment_route": <Route>, 
    "payment_hash": <byte>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    payment_hash: <byte>,
    payment_hash_string: <string>,
    route: <Route>,
  };
> var options = {
    url: 'https://localhost:8080/v1/channels/transactions/route',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "payment_error": <string>, 
    "payment_preimage": <byte>, 
    "payment_route": <Route>, 
    "payment_hash": <byte>, 
}
```

### POST /v1/channels/transactions/route
 SendToRouteSync is a synchronous version of SendToRoute. It Will block until the payment either fails or succeeds.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
payment_hash | byte | body | The payment hash to use for the HTLC.
payment_hash_string | string | body | An optional hex-encoded payment hash to be used for the HTLC.
route | [Route](#route) | body | Route that should be used to attempt to complete the payment.

### Response 

Field | Type | Description
----- | ---- | ----------- 
payment_error | string |  
payment_preimage | byte |  
payment_route | [Route](#route) |  
payment_hash | byte |   



# /v1/chanpolicy


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/chanpolicy  \
    -d '{ "global":<boolean>,"chan_point":<ChannelPoint>,"base_fee_msat":<string>,"fee_rate":<double>,"time_lock_delta":<int64>, }' 
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
        'chan_point': <ChannelPoint>, 
        'base_fee_msat': <string>, 
        'fee_rate': <double>, 
        'time_lock_delta': <int64>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    global: <boolean>,
    chan_point: <ChannelPoint>,
    base_fee_msat: <string>,
    fee_rate: <double>,
    time_lock_delta: <int64>,
  };
> var options = {
    url: 'https://localhost:8080/v1/chanpolicy',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/chanpolicy
UpdateChannelPolicy allows the caller to update the fee schedule and channel policies for all channels globally, or a particular channel.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
global | boolean | body | If set, then this update applies to all currently active channels.
chan_point | [ChannelPoint](#channelpoint) | body | If set, this update will target a specific channel.
base_fee_msat | string | body | The base fee charged regardless of the number of milli-satoshis sent.
fee_rate | double | body | The effective fee rate in milli-satoshis. The precision of this value goes up to 6 decimal places, so 1e-6.
time_lock_delta | int64 | body | The required timelock delta for HTLCs forwarded over the channel.

### Response 

This response has no parameters.




# /v1/fees


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/fees 
{ 
    "channel_fees": <array ChannelFeeReport>, 
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
    "channel_fees": <array ChannelFeeReport>, 
    "day_fee_sum": <string>, 
    "week_fee_sum": <string>, 
    "month_fee_sum": <string>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/fees',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "channel_fees": <array ChannelFeeReport>, 
    "day_fee_sum": <string>, 
    "week_fee_sum": <string>, 
    "month_fee_sum": <string>, 
}
```

### GET /v1/fees
FeeReport allows the caller to obtain a report detailing the current fee schedule enforced by the node globally for each channel.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
channel_fees | [array ChannelFeeReport](#channelfeereport) | An array of channel fee reports which describes the current fee schedule for each channel. 
day_fee_sum | string | The total amount of fee revenue (in satoshis) the switch has collected over the past 24 hrs. 
week_fee_sum | string | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 week. 
month_fee_sum | string | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 month.  



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
> var fs = require('fs');
> var request = require('request');
> var options = {
    url: 'https://localhost:8080/v1/genseed',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "cipher_seed_mnemonic": <array string>, 
    "enciphered_seed": <byte>, 
}
```

### GET /v1/genseed
 GenSeed is the first method that should be used to instantiate a new lnd instance. This method allows a caller to generate a new aezeed cipher seed given an optional passphrase. If provided, the passphrase will be necessary to decrypt the cipherseed to expose the internal wallet seed.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
aezeed_passphrase | string | query |  aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed.
seed_entropy | string | query |  seed_entropy is an optional 16-bytes generated via CSPRNG. If not specified, then a fresh set of randomness will be used to create the seed.

### Response 

Field | Type | Description
----- | ---- | ----------- 
cipher_seed_mnemonic | array string |  cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed. 
enciphered_seed | byte |  enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.  



# /v1/getinfo


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo 
{ 
    "identity_pubkey": <string>, 
    "alias": <string>, 
    "num_pending_channels": <int64>, 
    "num_active_channels": <int64>, 
    "num_peers": <int64>, 
    "block_height": <int64>, 
    "block_hash": <string>, 
    "synced_to_chain": <boolean>, 
    "testnet": <boolean>, 
    "uris": <array string>, 
    "best_header_timestamp": <string>, 
    "version": <string>, 
    "num_inactive_channels": <int64>, 
    "chains": <array Chain>, 
    "color": <string>, 
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
    "identity_pubkey": <string>, 
    "alias": <string>, 
    "num_pending_channels": <int64>, 
    "num_active_channels": <int64>, 
    "num_peers": <int64>, 
    "block_height": <int64>, 
    "block_hash": <string>, 
    "synced_to_chain": <boolean>, 
    "testnet": <boolean>, 
    "uris": <array string>, 
    "best_header_timestamp": <string>, 
    "version": <string>, 
    "num_inactive_channels": <int64>, 
    "chains": <array Chain>, 
    "color": <string>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/getinfo',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "identity_pubkey": <string>, 
    "alias": <string>, 
    "num_pending_channels": <int64>, 
    "num_active_channels": <int64>, 
    "num_peers": <int64>, 
    "block_height": <int64>, 
    "block_hash": <string>, 
    "synced_to_chain": <boolean>, 
    "testnet": <boolean>, 
    "uris": <array string>, 
    "best_header_timestamp": <string>, 
    "version": <string>, 
    "num_inactive_channels": <int64>, 
    "chains": <array Chain>, 
    "color": <string>, 
}
```

### GET /v1/getinfo
GetInfo returns general information concerning the lightning node including it's identity pubkey, alias, the chains it is connected to, and information concerning the number of open+pending channels.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
identity_pubkey | string | The identity pubkey of the current node. 
alias | string | If applicable, the alias of the current node, e.g. "bob" 
num_pending_channels | int64 | Number of pending channels 
num_active_channels | int64 | Number of active channels 
num_peers | int64 | Number of peers 
block_height | int64 | The node's current view of the height of the best block 
block_hash | string | The node's current view of the hash of the best block 
synced_to_chain | boolean | Whether the wallet's view is synced to the main chain 
testnet | boolean |  Whether the current node is connected to testnet. This field is  deprecated and the network field should be used instead 
uris | array string | The URIs of the current node. 
best_header_timestamp | string | Timestamp of the block best known to the wallet 
version | string | The version of the LND software that the node is running. 
num_inactive_channels | int64 | Number of inactive channels 
chains | [array Chain](#chain) | A list of active chains the node is connected to 
color | string | The color of the current node in hex code format  



# /v1/graph


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph 
{ 
    "nodes": <array LightningNode>, 
    "edges": <array ChannelEdge>, 
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
    "nodes": <array LightningNode>, 
    "edges": <array ChannelEdge>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/graph',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "nodes": <array LightningNode>, 
    "edges": <array ChannelEdge>, 
}
```

### GET /v1/graph
DescribeGraph returns a description of the latest graph state from the point of view of the node. The graph information is partitioned into two components: all the nodes/vertexes, and all the edges that connect the vertexes themselves.  As this is a directed graph, the edges also contain the node directional specific routing policy which includes: the time lock delta, fee information, etc.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
include_unannounced | boolean | query |  Whether unannounced channels are included in the response or not. If set, unannounced channels are included. Unannounced channels are both private channels, and public channels that are not yet announced to the network.

### Response 

Field | Type | Description
----- | ---- | ----------- 
nodes | [array LightningNode](#lightningnode) | The list of `LightningNode`s in this channel graph 
edges | [array ChannelEdge](#channeledge) | The list of `ChannelEdge`s in this channel graph  



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
    "node1_policy": <RoutingPolicy>, 
    "node2_policy": <RoutingPolicy>, 
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
    "node1_policy": <RoutingPolicy>, 
    "node2_policy": <RoutingPolicy>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/graph/edge/{chan_id}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "channel_id": <string>, 
    "chan_point": <string>, 
    "last_update": <int64>, 
    "node1_pub": <string>, 
    "node2_pub": <string>, 
    "capacity": <string>, 
    "node1_policy": <RoutingPolicy>, 
    "node2_policy": <RoutingPolicy>, 
}
```

### GET /v1/graph/edge/{chan_id}
GetChanInfo returns the latest authenticated network announcement for the given channel identified by its channel ID: an 8-byte integer which uniquely identifies the location of transaction's funding output within the blockchain.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
chan_id | string | path | 

### Response 

Field | Type | Description
----- | ---- | ----------- 
channel_id | string |  The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | string |  
last_update | int64 |  
node1_pub | string |  
node2_pub | string |  
capacity | string |  
node1_policy | [RoutingPolicy](#routingpolicy) |  
node2_policy | [RoutingPolicy](#routingpolicy) |   



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
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/graph/info',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
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
}
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



# /v1/graph/node


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/node/{pub_key} 
{ 
    "node": <LightningNode>, 
    "num_channels": <int64>, 
    "total_capacity": <string>, 
    "channels": <array ChannelEdge>, 
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
    "node": <LightningNode>, 
    "num_channels": <int64>, 
    "total_capacity": <string>, 
    "channels": <array ChannelEdge>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/graph/node/{pub_key}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "node": <LightningNode>, 
    "num_channels": <int64>, 
    "total_capacity": <string>, 
    "channels": <array ChannelEdge>, 
}
```

### GET /v1/graph/node/{pub_key}
GetNodeInfo returns the latest advertised, aggregated, and authenticated channel information for the specified node identified by its public key.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pub_key | string | path | 
include_channels | boolean | query | If true, will include all known channels associated with the node.

### Response 

Field | Type | Description
----- | ---- | ----------- 
node | [LightningNode](#lightningnode) |  An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | int64 | The total number of channels for the node. 
total_capacity | string | The sum of all channels capacity for the node, denominated in satoshis. 
channels | [array ChannelEdge](#channeledge) | A list of all public channels for the node.  



# /v1/graph/routes


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/graph/routes/{pub_key}/{amt} 
{ 
    "routes": <array Route>, 
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
    "routes": <array Route>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/graph/routes/{pub_key}/{amt}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "routes": <array Route>, 
}
```

### GET /v1/graph/routes/{pub_key}/{amt}
QueryRoutes attempts to query the daemon's Channel Router for a possible route to a target destination capable of carrying a specific amount of satoshis. The returned route contains the full details required to craft and send an HTLC, also including the necessary information that should be present within the Sphinx packet encapsulated within the HTLC.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pub_key | string | path | 
amt | string | path | 
final_cltv_delta | int32 | query | An optional CLTV delta from the current height that should be used for the timelock of the final hop.
fee_limit.fixed | string | query | The fee limit expressed as a fixed amount of satoshis.
fee_limit.percent | string | query | The fee limit expressed as a percentage of the payment amount.
ignored_nodes | array | query |  A list of nodes to ignore during path finding.
source_pub_key | string | query |  The source node where the request route should originated from. If empty, self is assumed.

### Response 

Field | Type | Description
----- | ---- | ----------- 
routes | [array Route](#route) |   



# /v1/initwallet


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/initwallet  \
    -d '{ "wallet_password":<byte>,"cipher_seed_mnemonic":<array string>,"aezeed_passphrase":<byte>,"recovery_window":<int32>,"channel_backups":<ChanBackupSnapshot>, }' 
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
        'channel_backups': <ChanBackupSnapshot>, 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var requestBody = { 
    wallet_password: <byte>,
    cipher_seed_mnemonic: <array string>,
    aezeed_passphrase: <byte>,
    recovery_window: <int32>,
    channel_backups: <ChanBackupSnapshot>,
  };
> var options = {
    url: 'https://localhost:8080/v1/initwallet',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/initwallet
 InitWallet is used when lnd is starting up for the first time to fully initialize the daemon and its internal wallet. At the very least a wallet password must be provided. This will be used to encrypt sensitive material on disk.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
wallet_password | byte | body |  wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon.
cipher_seed_mnemonic | array string | body |  cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed.
aezeed_passphrase | byte | body |  aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed.
recovery_window | int32 | body |  recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) | body |  channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.

### Response 

This response has no parameters.




# /v1/invoice


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoice/{r_hash_str} 
{ 
    "memo": <string>, 
    "receipt": <byte>, 
    "r_preimage": <byte>, 
    "r_hash": <byte>, 
    "value": <string>, 
    "settled": <boolean>, 
    "creation_date": <string>, 
    "settle_date": <string>, 
    "payment_request": <string>, 
    "description_hash": <byte>, 
    "expiry": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array RouteHint>, 
    "private": <boolean>, 
    "add_index": <string>, 
    "settle_index": <string>, 
    "amt_paid": <string>, 
    "amt_paid_sat": <string>, 
    "amt_paid_msat": <string>, 
    "state": <InvoiceInvoiceState>, 
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
    "memo": <string>, 
    "receipt": <byte>, 
    "r_preimage": <byte>, 
    "r_hash": <byte>, 
    "value": <string>, 
    "settled": <boolean>, 
    "creation_date": <string>, 
    "settle_date": <string>, 
    "payment_request": <string>, 
    "description_hash": <byte>, 
    "expiry": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array RouteHint>, 
    "private": <boolean>, 
    "add_index": <string>, 
    "settle_index": <string>, 
    "amt_paid": <string>, 
    "amt_paid_sat": <string>, 
    "amt_paid_msat": <string>, 
    "state": <InvoiceInvoiceState>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/invoice/{r_hash_str}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "memo": <string>, 
    "receipt": <byte>, 
    "r_preimage": <byte>, 
    "r_hash": <byte>, 
    "value": <string>, 
    "settled": <boolean>, 
    "creation_date": <string>, 
    "settle_date": <string>, 
    "payment_request": <string>, 
    "description_hash": <byte>, 
    "expiry": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array RouteHint>, 
    "private": <boolean>, 
    "add_index": <string>, 
    "settle_index": <string>, 
    "amt_paid": <string>, 
    "amt_paid_sat": <string>, 
    "amt_paid_msat": <string>, 
    "state": <InvoiceInvoiceState>, 
}
```

### GET /v1/invoice/{r_hash_str}
LookupInvoice attempts to look up an invoice according to its payment hash. The passed payment hash *must* be exactly 32 bytes, if not, an error is returned.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
r_hash_str | string | path | 
r_hash | string | query | The payment hash of the invoice to be looked up.

### Response 

Field | Type | Description
----- | ---- | ----------- 
memo | string |  An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
receipt | byte | Deprecated. An optional cryptographic receipt of payment which is not implemented. 
r_preimage | byte |  The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | byte | The hash of the preimage 
value | string | The value of this invoice in satoshis 
settled | boolean | Whether this invoice has been fulfilled 
creation_date | string | When this invoice was created 
settle_date | string | When this invoice was settled 
payment_request | string |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | byte |  Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | string | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | string | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) |  Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | boolean | Whether this invoice should include routing hints for private channels. 
add_index | string |  The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | string |  The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | string | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | string |  The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | string |  The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceInvoiceState](#invoiceinvoicestate) |  The state the invoice is in.  



# /v1/invoices


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoices 
{ 
    "invoices": <array Invoice>, 
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
    "invoices": <array Invoice>, 
    "last_index_offset": <string>, 
    "first_index_offset": <string>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/invoices',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "invoices": <array Invoice>, 
    "last_index_offset": <string>, 
    "first_index_offset": <string>, 
}
```

### GET /v1/invoices
ListInvoices returns a list of all the invoices currently stored within the database. Any active debug invoices are ignored. It has full support for paginated responses, allowing users to query for specific invoices through their add_index. This can be done by using either the first_index_offset or last_index_offset fields included in the response as the index_offset of the next request. By default, the first 100 invoices created will be returned. Backwards pagination is also supported through the Reversed flag.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pending_only | boolean | query | If set, only unsettled invoices will be returned in the response.
index_offset | string | query |  The index of an invoice that will be used as either the start or end of a query to determine which invoices should be returned in the response.
num_max_invoices | string | query | The max number of invoices to return in the response to this query.
reversed | boolean | query |  If set, the invoices returned will result from seeking backwards from the specified index offset. This can be used to paginate backwards.

### Response 

Field | Type | Description
----- | ---- | ----------- 
invoices | [array Invoice](#invoice) |  A list of invoices from the time slice of the time series specified in the request. 
last_index_offset | string |  The index of the last item in the set of returned invoices. This can be used to seek further, pagination style. 
first_index_offset | string |  The index of the last item in the set of returned invoices. This can be used to seek backwards, pagination style.  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoices  \
    -d '{ "memo":<string>,"receipt":<byte>,"r_preimage":<byte>,"r_hash":<byte>,"value":<string>,"settled":<boolean>,"creation_date":<string>,"settle_date":<string>,"payment_request":<string>,"description_hash":<byte>,"expiry":<string>,"fallback_addr":<string>,"cltv_expiry":<string>,"route_hints":<array RouteHint>,"private":<boolean>,"add_index":<string>,"settle_index":<string>,"amt_paid":<string>,"amt_paid_sat":<string>,"amt_paid_msat":<string>,"state":<InvoiceInvoiceState>, }' 
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
        'memo': <string>, 
        'receipt': base64.b64encode(<byte>).decode(), 
        'r_preimage': base64.b64encode(<byte>).decode(), 
        'r_hash': base64.b64encode(<byte>).decode(), 
        'value': <string>, 
        'settled': <boolean>, 
        'creation_date': <string>, 
        'settle_date': <string>, 
        'payment_request': <string>, 
        'description_hash': base64.b64encode(<byte>).decode(), 
        'expiry': <string>, 
        'fallback_addr': <string>, 
        'cltv_expiry': <string>, 
        'route_hints': <array RouteHint>, 
        'private': <boolean>, 
        'add_index': <string>, 
        'settle_index': <string>, 
        'amt_paid': <string>, 
        'amt_paid_sat': <string>, 
        'amt_paid_msat': <string>, 
        'state': <InvoiceInvoiceState>, 
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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    memo: <string>,
    receipt: <byte>,
    r_preimage: <byte>,
    r_hash: <byte>,
    value: <string>,
    settled: <boolean>,
    creation_date: <string>,
    settle_date: <string>,
    payment_request: <string>,
    description_hash: <byte>,
    expiry: <string>,
    fallback_addr: <string>,
    cltv_expiry: <string>,
    route_hints: <array RouteHint>,
    private: <boolean>,
    add_index: <string>,
    settle_index: <string>,
    amt_paid: <string>,
    amt_paid_sat: <string>,
    amt_paid_msat: <string>,
    state: <InvoiceInvoiceState>,
  };
> var options = {
    url: 'https://localhost:8080/v1/invoices',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "r_hash": <byte>, 
    "payment_request": <string>, 
    "add_index": <string>, 
}
```

### POST /v1/invoices
AddInvoice attempts to add a new invoice to the invoice database. Any duplicated invoices are rejected, therefore all invoices *must* have a unique payment preimage.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
memo | string | body |  An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used.
receipt | byte | body | Deprecated. An optional cryptographic receipt of payment which is not implemented.
r_preimage | byte | body |  The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage
r_hash | byte | body | The hash of the preimage
value | string | body | The value of this invoice in satoshis
settled | boolean | body | Whether this invoice has been fulfilled
creation_date | string | body | When this invoice was created
settle_date | string | body | When this invoice was settled
payment_request | string | body |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
description_hash | byte | body |  Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request.
expiry | string | body | Payment request expiry time in seconds. Default is 3600 (1 hour).
fallback_addr | string | body | Fallback on-chain address.
cltv_expiry | string | body | Delta to use for the time-lock of the CLTV extended to the final hop.
route_hints | [array RouteHint](#routehint) | body |  Route hints that can each be individually used to assist in reaching the invoice's destination.
private | boolean | body | Whether this invoice should include routing hints for private channels.
add_index | string | body |  The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.
settle_index | string | body |  The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one.
amt_paid | string | body | Deprecated, use amt_paid_sat or amt_paid_msat.
amt_paid_sat | string | body |  The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well.
amt_paid_msat | string | body |  The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well.
state | [InvoiceInvoiceState](#invoiceinvoicestate) | body |  The state the invoice is in.

### Response 

Field | Type | Description
----- | ---- | ----------- 
r_hash | byte |  
payment_request | string |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
add_index | string |  The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.  



# /v1/invoices/subscribe


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/invoices/subscribe 
{ 
    "memo": <string>, 
    "receipt": <byte>, 
    "r_preimage": <byte>, 
    "r_hash": <byte>, 
    "value": <string>, 
    "settled": <boolean>, 
    "creation_date": <string>, 
    "settle_date": <string>, 
    "payment_request": <string>, 
    "description_hash": <byte>, 
    "expiry": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array RouteHint>, 
    "private": <boolean>, 
    "add_index": <string>, 
    "settle_index": <string>, 
    "amt_paid": <string>, 
    "amt_paid_sat": <string>, 
    "amt_paid_msat": <string>, 
    "state": <InvoiceInvoiceState>, 
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
    "memo": <string>, 
    "receipt": <byte>, 
    "r_preimage": <byte>, 
    "r_hash": <byte>, 
    "value": <string>, 
    "settled": <boolean>, 
    "creation_date": <string>, 
    "settle_date": <string>, 
    "payment_request": <string>, 
    "description_hash": <byte>, 
    "expiry": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array RouteHint>, 
    "private": <boolean>, 
    "add_index": <string>, 
    "settle_index": <string>, 
    "amt_paid": <string>, 
    "amt_paid_sat": <string>, 
    "amt_paid_msat": <string>, 
    "state": <InvoiceInvoiceState>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/invoices/subscribe',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "memo": <string>, 
    "receipt": <byte>, 
    "r_preimage": <byte>, 
    "r_hash": <byte>, 
    "value": <string>, 
    "settled": <boolean>, 
    "creation_date": <string>, 
    "settle_date": <string>, 
    "payment_request": <string>, 
    "description_hash": <byte>, 
    "expiry": <string>, 
    "fallback_addr": <string>, 
    "cltv_expiry": <string>, 
    "route_hints": <array RouteHint>, 
    "private": <boolean>, 
    "add_index": <string>, 
    "settle_index": <string>, 
    "amt_paid": <string>, 
    "amt_paid_sat": <string>, 
    "amt_paid_msat": <string>, 
    "state": <InvoiceInvoiceState>, 
}
```

### GET /v1/invoices/subscribe
 SubscribeInvoices returns a uni-directional stream (server -> client) for notifying the client of newly added/settled invoices. The caller can optionally specify the add_index and/or the settle_index. If the add_index is specified, then we'll first start by sending add invoice events for all invoices with an add_index greater than the specified value.  If the settle_index is specified, the next, we'll send out all settle events for invoices with a settle_index greater than the specified value.  One or both of these fields can be set. If no fields are set, then we'll only send out the latest add/settle events.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
add_index | string | query |  If specified (non-zero), then we'll first start by sending out notifications for all added indexes with an add_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC.
settle_index | string | query |  If specified (non-zero), then we'll first start by sending out notifications for all settled indexes with an settle_index greater than this value. This allows callers to catch up on any events they missed while they weren't connected to the streaming RPC.

### Response (streaming)

Field | Type | Description
----- | ---- | ----------- 
memo | string |  An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
receipt | byte | Deprecated. An optional cryptographic receipt of payment which is not implemented. 
r_preimage | byte |  The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | byte | The hash of the preimage 
value | string | The value of this invoice in satoshis 
settled | boolean | Whether this invoice has been fulfilled 
creation_date | string | When this invoice was created 
settle_date | string | When this invoice was settled 
payment_request | string |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | byte |  Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | string | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | string | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) |  Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | boolean | Whether this invoice should include routing hints for private channels. 
add_index | string |  The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one. 
settle_index | string |  The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one. 
amt_paid | string | Deprecated, use amt_paid_sat or amt_paid_msat. 
amt_paid_sat | string |  The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
amt_paid_msat | string |  The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well. 
state | [InvoiceInvoiceState](#invoiceinvoicestate) |  The state the invoice is in.  



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/newaddress',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "address": <string>, 
}
```

### GET /v1/newaddress
NewAddress creates a new address under control of the local wallet.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
type | string | query | The address type.

### Response 

Field | Type | Description
----- | ---- | ----------- 
address | string | The newly generated wallet address  



# /v1/payments


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/payments 
{ 
    "payments": <array Payment>, 
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
    "payments": <array Payment>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/payments',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "payments": <array Payment>, 
}
```

### GET /v1/payments
ListPayments returns a list of all outgoing payments.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
include_incomplete | boolean | query |  If true, then return payments that have not yet fully completed. This means that pending payments, as well as failed payments will show up if this field is set to True.

### Response 

Field | Type | Description
----- | ---- | ----------- 
payments | [array Payment](#payment) | The list of payments  



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/payments',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.delete(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### DELETE /v1/payments
 DeleteAllPayments deletes all outgoing payments from DB.

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
    "route_hints": <array RouteHint>, 
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
    "route_hints": <array RouteHint>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/payreq/{pay_req}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
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
    "route_hints": <array RouteHint>, 
}
```

### GET /v1/payreq/{pay_req}
DecodePayReq takes an encoded payment request string and attempts to decode it, returning a full description of the conditions encoded within the payment request.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pay_req | string | path | 

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
route_hints | [array RouteHint](#routehint) |   



# /v1/peers


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/peers 
{ 
    "peers": <array Peer>, 
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
    "peers": <array Peer>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/peers',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "peers": <array Peer>, 
}
```

### GET /v1/peers
ListPeers returns a verbose listing of all currently active peers.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
peers | [array Peer](#peer) | The list of currently connected peers  



```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/peers  \
    -d '{ "addr":<LightningAddress>,"perm":<boolean>, }' 
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
        'addr': <LightningAddress>, 
        'perm': <boolean>, 
    }
>>> r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    addr: <LightningAddress>,
    perm: <boolean>,
  };
> var options = {
    url: 'https://localhost:8080/v1/peers',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/peers
ConnectPeer attempts to establish a connection to a remote peer. This is at the networking level, and is used for communication between nodes. This is distinct from establishing a channel with a peer.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
addr | [LightningAddress](#lightningaddress) | body | Lightning address of the peer, in the format `<pubkey>@host`
perm | boolean | body | If set, the daemon will attempt to persistently connect to the target peer.  Otherwise, the call will be synchronous.

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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/peers/{pub_key}',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.delete(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### DELETE /v1/peers/{pub_key}
DisconnectPeer attempts to disconnect one peer from another identified by a given pubKey. In the case that we currently have a pending or active channel with the target peer, then this action will be not be allowed.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
pub_key | string | path | 

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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    msg: <byte>,
  };
> var options = {
    url: 'https://localhost:8080/v1/signmessage',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "signature": <string>, 
}
```

### POST /v1/signmessage
SignMessage signs a message with this node's private key. The returned signature string is `zbase32` encoded and pubkey recoverable, meaning that only the message digest and signature are needed for verification.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
msg | byte | body | The message to be signed

### Response 

Field | Type | Description
----- | ---- | ----------- 
signature | string | The signature for the given message  



# /v1/switch


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/switch  \
    -d '{ "start_time":<string>,"end_time":<string>,"index_offset":<int64>,"num_max_events":<int64>, }' 
{ 
    "forwarding_events": <array ForwardingEvent>, 
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
    "forwarding_events": <array ForwardingEvent>, 
    "last_offset_index": <int64>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    start_time: <string>,
    end_time: <string>,
    index_offset: <int64>,
    num_max_events: <int64>,
  };
> var options = {
    url: 'https://localhost:8080/v1/switch',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "forwarding_events": <array ForwardingEvent>, 
    "last_offset_index": <int64>, 
}
```

### POST /v1/switch
ForwardingHistory allows the caller to query the htlcswitch for a record of all HTLCs forwarded within the target time range, and integer offset within that time range. If no time-range is specified, then the first chunk of the past 24 hrs of forwarding history are returned.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
start_time | string | body | Start time is the starting point of the forwarding history request. All records beyond this point will be included, respecting the end time, and the index offset.
end_time | string | body | End time is the end point of the forwarding history request. The response will carry at most 50k records between the start time and the end time. The index offset can be used to implement pagination.
index_offset | int64 | body | Index offset is the offset in the time series to start at. As each response can only contain 50k records, callers can use this to skip around within a packed time series.
num_max_events | int64 | body | The max number of events to return in the response to this query.

### Response 

Field | Type | Description
----- | ---- | ----------- 
forwarding_events | [array ForwardingEvent](#forwardingevent) | A list of forwarding events from the time slice of the time series specified in the request. 
last_offset_index | int64 | The index of the last time in the set of returned forwarding events. Can be used to seek further, pagination style.  



# /v1/transactions


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/transactions 
{ 
    "transactions": <array Transaction>, 
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
    "transactions": <array Transaction>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/transactions',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "transactions": <array Transaction>, 
}
```

### GET /v1/transactions
GetTransactions returns a list describing all the known transactions relevant to the wallet.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
transactions | [array Transaction](#transaction) | The list of transactions relevant to the wallet.  



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    addr: <string>,
    amount: <string>,
    target_conf: <int32>,
    sat_per_byte: <string>,
    send_all: <boolean>,
  };
> var options = {
    url: 'https://localhost:8080/v1/transactions',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "txid": <string>, 
}
```

### POST /v1/transactions
SendCoins executes a request to send coins to a particular address. Unlike SendMany, this RPC call only allows creating a single output at a time. If neither target_conf, or sat_per_byte are set, then the internal wallet will consult its fee model to determine a fee for the default confirmation target.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
addr | string | body | The address to send coins to
amount | string | body | The amount in satoshis to send
target_conf | int32 | body | The target number of blocks that this transaction should be confirmed by.
sat_per_byte | string | body | A manual fee rate set in sat/byte that should be used when crafting the transaction.
send_all | boolean | body |  If set, then the amount field will be ignored, and lnd will attempt to send all the coins under control of the internal wallet to the specified address.

### Response 

Field | Type | Description
----- | ---- | ----------- 
txid | string | The transaction ID of the transaction  



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/transactions/fee',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "fee_sat": <string>, 
    "feerate_sat_per_byte": <string>, 
}
```

### GET /v1/transactions/fee
EstimateFee asks the chain backend to estimate the fee rate and total fees for a transaction that pays to multiple specified outputs.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
target_conf | int32 | query | The target number of blocks that this transaction should be confirmed by.

### Response 

Field | Type | Description
----- | ---- | ----------- 
fee_sat | string | The total fee in satoshis. 
feerate_sat_per_byte | string | The fee rate in satoshi/byte.  



# /v1/unlockwallet


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X POST --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/unlockwallet  \
    -d '{ "wallet_password":<byte>,"recovery_window":<int32>,"channel_backups":<ChanBackupSnapshot>, }' 
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
        'channel_backups': <ChanBackupSnapshot>, 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var requestBody = { 
    wallet_password: <byte>,
    recovery_window: <int32>,
    channel_backups: <ChanBackupSnapshot>,
  };
> var options = {
    url: 'https://localhost:8080/v1/unlockwallet',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
}
```

### POST /v1/unlockwallet
UnlockWallet is used at startup of lnd to provide a password to unlock the wallet database.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
wallet_password | byte | body |  wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly.
recovery_window | int32 | body |  recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) | body |  channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.

### Response 

This response has no parameters.




# /v1/utxos


```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 $LND_DIR/data/chain/bitcoin/simnet/admin.macaroon)"
$ curl -X GET --cacert $LND_DIR/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/utxos 
{ 
    "utxos": <array Utxo>, 
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
    "utxos": <array Utxo>, 
}
```
```javascript
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var options = {
    url: 'https://localhost:8080/v1/utxos',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
  };
> request.get(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "utxos": <array Utxo>, 
}
```

### GET /v1/utxos
ListUnspent returns a list of all utxos spendable by the wallet with a number of confirmations between the specified minimum and maximum.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
min_confs | int32 | query | The minimum number of confirmations to be included.
max_confs | int32 | query | The maximum number of confirmations to be included.

### Response 

Field | Type | Description
----- | ---- | ----------- 
utxos | [array Utxo](#utxo) | A list of utxos  



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
> var fs = require('fs');
> var request = require('request');
> var macaroon = fs.readFileSync('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon').toString('hex');
> var requestBody = { 
    msg: <byte>,
    signature: <string>,
  };
> var options = {
    url: 'https://localhost:8080/v1/verifymessage',
    // Work-around for self-signed certificates.
    rejectUnauthorized: false,
    json: true, 
    headers: {
      'Grpc-Metadata-macaroon': macaroon,
    },
    form: JSON.stringify(requestBody),
  };
> request.post(options, function(error, response, body) {
    console.log(body);
  });
{ 
    "valid": <boolean>, 
    "pubkey": <string>, 
}
```

### POST /v1/verifymessage
VerifyMessage verifies a signature over a msg. The signature must be zbase32 encoded and signed by an active node in the resident node's channel database. In addition to returning the validity of the signature, VerifyMessage also returns the recovered pubkey from the signature.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
msg | byte | body | The message over which the signature is to be verified
signature | string | body | The signature to be verified over the given message

### Response 

Field | Type | Description
----- | ---- | ----------- 
valid | boolean | Whether the signature was valid over the given message 
pubkey | string | The pubkey recovered from the signature  




# Definitions

## ChannelCloseSummaryClosureType

This definition has no parameters.


## ChannelEventUpdateUpdateType

This definition has no parameters.


## InvoiceInvoiceState

This definition has no parameters.


## PaymentPaymentStatus

This definition has no parameters.


## PeerSyncType

This definition has no parameters.


## PendingChannelsResponseClosedChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | The pending channel to be closed
closing_txid | string | The transaction id of the closing transaction


## PendingChannelsResponseForceClosedChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | The pending channel to be force closed
closing_txid | string | The transaction id of the closing transaction
limbo_balance | string | The balance in satoshis encumbered in this pending channel
maturity_height | int64 | The height at which funds can be swept into the wallet
blocks_til_maturity | int32 | Remaining # of blocks until the commitment output can be swept. Negative values indicate how many blocks have passed since becoming mature.
recovered_balance | string | The total value of funds successfully recovered from this channel
pending_htlcs | [array PendingHTLC](#pendinghtlc) | 


## PendingChannelsResponsePendingChannel

Field | Type | Description
----- | ---- | ----------- 
remote_node_pub | string | 
channel_point | string | 
capacity | string | 
local_balance | string | 
remote_balance | string | 


## PendingChannelsResponsePendingOpenChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | The pending channel
confirmation_height | int64 | The height at which this channel will be confirmed
commit_fee | string |  The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart.
commit_weight | string | The weight of the commitment transaction
fee_per_kw | string |  The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open.


## PendingChannelsResponseWaitingCloseChannel

Field | Type | Description
----- | ---- | ----------- 
channel | [PendingChannelsResponsePendingChannel](#pendingchannelsresponsependingchannel) | The pending channel waiting for closing tx to confirm
limbo_balance | string | The balance in satoshis encumbered in this channel


## AbandonChannelResponse

This definition has no parameters.


## AddInvoiceResponse

Field | Type | Description
----- | ---- | ----------- 
r_hash | byte | 
payment_request | string |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
add_index | string |  The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.


## AddressType

This definition has no parameters.


## Chain

Field | Type | Description
----- | ---- | ----------- 
chain | string | The blockchain the node is on (eg bitcoin, litecoin)
network | string | The network the node is on (eg regtest, testnet, mainnet)


## ChanBackupSnapshot

Field | Type | Description
----- | ---- | ----------- 
single_chan_backups | [ChannelBackups](#channelbackups) |  The set of new channels that have been added since the last channel backup snapshot was requested.
multi_chan_backup | [MultiChanBackup](#multichanbackup) |  A multi-channel backup that covers all open channels currently known to lnd.


## ChangePasswordRequest

Field | Type | Description
----- | ---- | ----------- 
current_password | byte |  current_password should be the current valid passphrase used to unlock the daemon.
new_password | byte |  new_password should be the new passphrase that will be needed to unlock the daemon.


## ChangePasswordResponse

This definition has no parameters.


## Channel

Field | Type | Description
----- | ---- | ----------- 
active | boolean | Whether this channel is active or not
remote_pubkey | string | The identity pubkey of the remote node
channel_point | string |  The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction.
chan_id | string |  The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
capacity | string | The total amount of funds held in this channel
local_balance | string | This node's current balance in this channel
remote_balance | string | The counterparty's current balance in this channel
commit_fee | string |  The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart.
commit_weight | string | The weight of the commitment transaction
fee_per_kw | string |  The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open.
unsettled_balance | string | The unsettled balance in this channel
total_satoshis_sent | string |  The total number of satoshis we've sent within this channel.
total_satoshis_received | string |  The total number of satoshis we've received within this channel.
num_updates | string |  The total number of updates conducted within this channel.
pending_htlcs | [array HTLC](#htlc) |  The list of active, uncleared HTLCs currently pending within the channel.
csv_delay | int64 |  The CSV delay expressed in relative blocks. If the channel is force closed, we will need to wait for this many blocks before we can regain our funds.
private | boolean | Whether this channel is advertised to the network or not.
initiator | boolean | True if we were the ones that created the channel.
chan_status_flags | string | A set of flags showing the current state of the channel.


## ChannelBackup

Field | Type | Description
----- | ---- | ----------- 
chan_point | [ChannelPoint](#channelpoint) |  Identifies the channel that this backup belongs to.
chan_backup | byte |  Is an encrypted single-chan backup. this can be passed to RestoreChannelBackups, or the WalletUnlocker Init and Unlock methods in order to trigger the recovery protocol.


## ChannelBackups

Field | Type | Description
----- | ---- | ----------- 
chan_backups | [array ChannelBackup](#channelbackup) |  A set of single-chan static channel backups.


## ChannelBalanceResponse

Field | Type | Description
----- | ---- | ----------- 
balance | string | Sum of channels balances denominated in satoshis
pending_open_balance | string | Sum of channels pending balances denominated in satoshis


## ChannelCloseSummary

Field | Type | Description
----- | ---- | ----------- 
channel_point | string | The outpoint (txid:index) of the funding transaction.
chan_id | string | The unique channel ID for the channel.
chain_hash | string | The hash of the genesis block that this channel resides within.
closing_tx_hash | string | The txid of the transaction which ultimately closed this channel.
remote_pubkey | string | Public key of the remote peer that we formerly had a channel with.
capacity | string | Total capacity of the channel.
close_height | int64 | Height at which the funding transaction was spent.
settled_balance | string | Settled balance at the time of channel closure
time_locked_balance | string | The sum of all the time-locked outputs at the time of channel closure
close_type | [ChannelCloseSummaryClosureType](#channelclosesummaryclosuretype) | Details on how the channel was closed.


## ChannelCloseUpdate

Field | Type | Description
----- | ---- | ----------- 
closing_txid | byte | 
success | boolean | 


## ChannelEdge

Field | Type | Description
----- | ---- | ----------- 
channel_id | string |  The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
chan_point | string | 
last_update | int64 | 
node1_pub | string | 
node2_pub | string | 
capacity | string | 
node1_policy | [RoutingPolicy](#routingpolicy) | 
node2_policy | [RoutingPolicy](#routingpolicy) | 


## ChannelEdgeUpdate

Field | Type | Description
----- | ---- | ----------- 
chan_id | string |  The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
chan_point | [ChannelPoint](#channelpoint) | 
capacity | string | 
routing_policy | [RoutingPolicy](#routingpolicy) | 
advertising_node | string | 
connecting_node | string | 


## ChannelEventUpdate

Field | Type | Description
----- | ---- | ----------- 
open_channel | [Channel](#channel) | 
closed_channel | [ChannelCloseSummary](#channelclosesummary) | 
active_channel | [ChannelPoint](#channelpoint) | 
inactive_channel | [ChannelPoint](#channelpoint) | 
type | [ChannelEventUpdateUpdateType](#channeleventupdateupdatetype) | 


## ChannelFeeReport

Field | Type | Description
----- | ---- | ----------- 
chan_point | string | The channel that this fee report belongs to.
base_fee_msat | string | The base fee charged regardless of the number of milli-satoshis sent.
fee_per_mil | string | The amount charged per milli-satoshis transferred expressed in millionths of a satoshi.
fee_rate | double | The effective fee rate in milli-satoshis. Computed by dividing the fee_per_mil value by 1 million.


## ChannelGraph

Field | Type | Description
----- | ---- | ----------- 
nodes | [array LightningNode](#lightningnode) | The list of `LightningNode`s in this channel graph
edges | [array ChannelEdge](#channeledge) | The list of `ChannelEdge`s in this channel graph


## ChannelOpenUpdate

Field | Type | Description
----- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) | 


## ChannelPoint

Field | Type | Description
----- | ---- | ----------- 
funding_txid_bytes | byte | Txid of the funding transaction
funding_txid_str | string | Hex-encoded string representing the funding transaction
output_index | int64 | The index of the output of the funding transaction


## CloseStatusUpdate

Field | Type | Description
----- | ---- | ----------- 
close_pending | [PendingUpdate](#pendingupdate) | 
chan_close | [ChannelCloseUpdate](#channelcloseupdate) | 


## ClosedChannelUpdate

Field | Type | Description
----- | ---- | ----------- 
chan_id | string |  The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
capacity | string | 
closed_height | int64 | 
chan_point | [ChannelPoint](#channelpoint) | 


## ClosedChannelsResponse

Field | Type | Description
----- | ---- | ----------- 
channels | [array ChannelCloseSummary](#channelclosesummary) | 


## ConnectPeerRequest

Field | Type | Description
----- | ---- | ----------- 
addr | [LightningAddress](#lightningaddress) | Lightning address of the peer, in the format `<pubkey>@host`
perm | boolean | If set, the daemon will attempt to persistently connect to the target peer.  Otherwise, the call will be synchronous.


## ConnectPeerResponse

This definition has no parameters.


## DebugLevelResponse

Field | Type | Description
----- | ---- | ----------- 
sub_systems | string | 


## DeleteAllPaymentsResponse

This definition has no parameters.


## DisconnectPeerResponse

This definition has no parameters.


## EstimateFeeResponse

Field | Type | Description
----- | ---- | ----------- 
fee_sat | string | The total fee in satoshis.
feerate_sat_per_byte | string | The fee rate in satoshi/byte.


## FeeLimit

Field | Type | Description
----- | ---- | ----------- 
fixed | string | The fee limit expressed as a fixed amount of satoshis.
percent | string | The fee limit expressed as a percentage of the payment amount.


## FeeReportResponse

Field | Type | Description
----- | ---- | ----------- 
channel_fees | [array ChannelFeeReport](#channelfeereport) | An array of channel fee reports which describes the current fee schedule for each channel.
day_fee_sum | string | The total amount of fee revenue (in satoshis) the switch has collected over the past 24 hrs.
week_fee_sum | string | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 week.
month_fee_sum | string | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 month.


## ForwardingEvent

Field | Type | Description
----- | ---- | ----------- 
timestamp | string | Timestamp is the time (unix epoch offset) that this circuit was completed.
chan_id_in | string | The incoming channel ID that carried the HTLC that created the circuit.
chan_id_out | string | The outgoing channel ID that carried the preimage that completed the circuit.
amt_in | string | The total amount (in satoshis) of the incoming HTLC that created half the circuit.
amt_out | string | The total amount (in satoshis) of the outgoing HTLC that created the second half of the circuit.
fee | string | The total fee (in satoshis) that this payment circuit carried.
fee_msat | string | The total fee (in milli-satoshis) that this payment circuit carried.


## ForwardingHistoryRequest

Field | Type | Description
----- | ---- | ----------- 
start_time | string | Start time is the starting point of the forwarding history request. All records beyond this point will be included, respecting the end time, and the index offset.
end_time | string | End time is the end point of the forwarding history request. The response will carry at most 50k records between the start time and the end time. The index offset can be used to implement pagination.
index_offset | int64 | Index offset is the offset in the time series to start at. As each response can only contain 50k records, callers can use this to skip around within a packed time series.
num_max_events | int64 | The max number of events to return in the response to this query.


## ForwardingHistoryResponse

Field | Type | Description
----- | ---- | ----------- 
forwarding_events | [array ForwardingEvent](#forwardingevent) | A list of forwarding events from the time slice of the time series specified in the request.
last_offset_index | int64 | The index of the last time in the set of returned forwarding events. Can be used to seek further, pagination style.


## GenSeedResponse

Field | Type | Description
----- | ---- | ----------- 
cipher_seed_mnemonic | array string |  cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed.
enciphered_seed | byte |  enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.


## GetInfoResponse

Field | Type | Description
----- | ---- | ----------- 
identity_pubkey | string | The identity pubkey of the current node.
alias | string | If applicable, the alias of the current node, e.g. "bob"
num_pending_channels | int64 | Number of pending channels
num_active_channels | int64 | Number of active channels
num_peers | int64 | Number of peers
block_height | int64 | The node's current view of the height of the best block
block_hash | string | The node's current view of the hash of the best block
synced_to_chain | boolean | Whether the wallet's view is synced to the main chain
testnet | boolean |  Whether the current node is connected to testnet. This field is  deprecated and the network field should be used instead
uris | array string | The URIs of the current node.
best_header_timestamp | string | Timestamp of the block best known to the wallet
version | string | The version of the LND software that the node is running.
num_inactive_channels | int64 | Number of inactive channels
chains | [array Chain](#chain) | A list of active chains the node is connected to
color | string | The color of the current node in hex code format


## GraphTopologyUpdate

Field | Type | Description
----- | ---- | ----------- 
node_updates | [array NodeUpdate](#nodeupdate) | 
channel_updates | [array ChannelEdgeUpdate](#channeledgeupdate) | 
closed_chans | [array ClosedChannelUpdate](#closedchannelupdate) | 


## HTLC

Field | Type | Description
----- | ---- | ----------- 
incoming | boolean | 
amount | string | 
hash_lock | byte | 
expiration_height | int64 | 


## Hop

Field | Type | Description
----- | ---- | ----------- 
chan_id | string |  The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.
chan_capacity | string | 
amt_to_forward | string | 
fee | string | 
expiry | int64 | 
amt_to_forward_msat | string | 
fee_msat | string | 
pub_key | string |  An optional public key of the hop. If the public key is given, the payment can be executed without relying on a copy of the channel graph.


## HopHint

Field | Type | Description
----- | ---- | ----------- 
node_id | string | The public key of the node at the start of the channel.
chan_id | string | The unique identifier of the channel.
fee_base_msat | int64 | The base fee of the channel denominated in millisatoshis.
fee_proportional_millionths | int64 |  The fee rate of the channel for sending one satoshi across it denominated in millionths of a satoshi.
cltv_expiry_delta | int64 | The time-lock delta of the channel.


## InitWalletRequest

Field | Type | Description
----- | ---- | ----------- 
wallet_password | byte |  wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon.
cipher_seed_mnemonic | array string |  cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed.
aezeed_passphrase | byte |  aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed.
recovery_window | int32 |  recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) |  channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.


## InitWalletResponse

This definition has no parameters.


## Invoice

Field | Type | Description
----- | ---- | ----------- 
memo | string |  An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used.
receipt | byte | Deprecated. An optional cryptographic receipt of payment which is not implemented.
r_preimage | byte |  The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage
r_hash | byte | The hash of the preimage
value | string | The value of this invoice in satoshis
settled | boolean | Whether this invoice has been fulfilled
creation_date | string | When this invoice was created
settle_date | string | When this invoice was settled
payment_request | string |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
description_hash | byte |  Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request.
expiry | string | Payment request expiry time in seconds. Default is 3600 (1 hour).
fallback_addr | string | Fallback on-chain address.
cltv_expiry | string | Delta to use for the time-lock of the CLTV extended to the final hop.
route_hints | [array RouteHint](#routehint) |  Route hints that can each be individually used to assist in reaching the invoice's destination.
private | boolean | Whether this invoice should include routing hints for private channels.
add_index | string |  The "add" index of this invoice. Each newly created invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all added invoices with an add_index greater than this one.
settle_index | string |  The "settle" index of this invoice. Each newly settled invoice will increment this index making it monotonically increasing. Callers to the SubscribeInvoices call can use this to instantly get notified of all settled invoices with an settle_index greater than this one.
amt_paid | string | Deprecated, use amt_paid_sat or amt_paid_msat.
amt_paid_sat | string |  The amount that was accepted for this invoice, in satoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well.
amt_paid_msat | string |  The amount that was accepted for this invoice, in millisatoshis. This will ONLY be set if this invoice has been settled. We provide this field as if the invoice was created with a zero value, then we need to record what amount was ultimately accepted. Additionally, it's possible that the sender paid MORE that was specified in the original invoice. So we'll record that here as well.
state | [InvoiceInvoiceState](#invoiceinvoicestate) |  The state the invoice is in.


## LightningAddress

Field | Type | Description
----- | ---- | ----------- 
pubkey | string | The identity pubkey of the Lightning node
host | string | The network location of the lightning node, e.g. `69.69.69.69:1337` or `localhost:10011`


## LightningNode

Field | Type | Description
----- | ---- | ----------- 
last_update | int64 | 
pub_key | string | 
alias | string | 
addresses | [array NodeAddress](#nodeaddress) | 
color | string | 


## ListChannelsResponse

Field | Type | Description
----- | ---- | ----------- 
channels | [array Channel](#channel) | The list of active channels


## ListInvoiceResponse

Field | Type | Description
----- | ---- | ----------- 
invoices | [array Invoice](#invoice) |  A list of invoices from the time slice of the time series specified in the request.
last_index_offset | string |  The index of the last item in the set of returned invoices. This can be used to seek further, pagination style.
first_index_offset | string |  The index of the last item in the set of returned invoices. This can be used to seek backwards, pagination style.


## ListPaymentsResponse

Field | Type | Description
----- | ---- | ----------- 
payments | [array Payment](#payment) | The list of payments


## ListPeersResponse

Field | Type | Description
----- | ---- | ----------- 
peers | [array Peer](#peer) | The list of currently connected peers


## ListUnspentResponse

Field | Type | Description
----- | ---- | ----------- 
utxos | [array Utxo](#utxo) | A list of utxos


## MultiChanBackup

Field | Type | Description
----- | ---- | ----------- 
chan_points | [array ChannelPoint](#channelpoint) |  Is the set of all channels that are included in this multi-channel backup.
multi_chan_backup | byte |  A single encrypted blob containing all the static channel backups of the channel listed above. This can be stored as a single file or blob, and safely be replaced with any prior/future versions.


## NetworkInfo

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


## NewAddressResponse

Field | Type | Description
----- | ---- | ----------- 
address | string | The newly generated wallet address


## NodeAddress

Field | Type | Description
----- | ---- | ----------- 
network | string | 
addr | string | 


## NodeInfo

Field | Type | Description
----- | ---- | ----------- 
node | [LightningNode](#lightningnode) |  An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge.
num_channels | int64 | The total number of channels for the node.
total_capacity | string | The sum of all channels capacity for the node, denominated in satoshis.
channels | [array ChannelEdge](#channeledge) | A list of all public channels for the node.


## NodeUpdate

Field | Type | Description
----- | ---- | ----------- 
addresses | array string | 
identity_key | string | 
global_features | byte | 
alias | string | 
color | string | 


## OpenChannelRequest

Field | Type | Description
----- | ---- | ----------- 
node_pubkey | byte | The pubkey of the node to open a channel with
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with
local_funding_amount | string | The number of satoshis the wallet should commit to the channel
push_sat | string | The number of satoshis to push to the remote side as part of the initial commitment state
target_conf | int32 | The target number of blocks that the funding transaction should be confirmed by.
sat_per_byte | string | A manual fee rate set in sat/byte that should be used when crafting the funding transaction.
private | boolean | Whether this channel should be private, not announced to the greater network.
min_htlc_msat | string | The minimum value in millisatoshi we will require for incoming HTLCs on the channel.
remote_csv_delay | int64 | The delay we require on the remote's commitment transaction. If this is not set, it will be scaled automatically with the channel size.
min_confs | int32 | The minimum number of confirmations each one of your outputs used for the funding transaction must satisfy.
spend_unconfirmed | boolean | Whether unconfirmed outputs should be used as inputs for the funding transaction.


## OpenStatusUpdate

Field | Type | Description
----- | ---- | ----------- 
chan_pending | [PendingUpdate](#pendingupdate) | 
chan_open | [ChannelOpenUpdate](#channelopenupdate) | 


## OutPoint

Field | Type | Description
----- | ---- | ----------- 
txid_bytes | byte | Raw bytes representing the transaction id.
txid_str | string | Reversed, hex-encoded string representing the transaction id.
output_index | int64 | The index of the output on the transaction.


## PayReq

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
route_hints | [array RouteHint](#routehint) | 


## Payment

Field | Type | Description
----- | ---- | ----------- 
payment_hash | string | The payment hash
value | string | Deprecated, use value_sat or value_msat.
creation_date | string | The date of this payment
path | array string | The path this payment took
fee | string | The fee paid for this payment in satoshis
payment_preimage | string | The payment preimage
value_sat | string | The value of the payment in satoshis
value_msat | string | The value of the payment in milli-satoshis
payment_request | string | The optional payment request being fulfilled.
status | [PaymentPaymentStatus](#paymentpaymentstatus) | The status of the payment.


## Peer

Field | Type | Description
----- | ---- | ----------- 
pub_key | string | The identity pubkey of the peer
address | string | Network address of the peer; eg `127.0.0.1:10011`
bytes_sent | string | Bytes of data transmitted to this peer
bytes_recv | string | Bytes of data transmitted from this peer
sat_sent | string | Satoshis sent to this peer
sat_recv | string | Satoshis received from this peer
inbound | boolean | A channel is inbound if the counterparty initiated the channel
ping_time | string | Ping time to this peer
sync_type | [PeerSyncType](#peersynctype) | The type of sync we are currently performing with this peer.


## PendingChannelsResponse

Field | Type | Description
----- | ---- | ----------- 
total_limbo_balance | string | The balance in satoshis encumbered in pending channels
pending_open_channels | [array PendingChannelsResponsePendingOpenChannel](#pendingchannelsresponsependingopenchannel) | Channels pending opening
pending_closing_channels | [array PendingChannelsResponseClosedChannel](#pendingchannelsresponseclosedchannel) | Channels pending closing
pending_force_closing_channels | [array PendingChannelsResponseForceClosedChannel](#pendingchannelsresponseforceclosedchannel) | Channels pending force closing
waiting_close_channels | [array PendingChannelsResponseWaitingCloseChannel](#pendingchannelsresponsewaitingclosechannel) | Channels waiting for closing tx to confirm


## PendingHTLC

Field | Type | Description
----- | ---- | ----------- 
incoming | boolean | The direction within the channel that the htlc was sent
amount | string | The total value of the htlc
outpoint | string | The final output to be swept back to the user's wallet
maturity_height | int64 | The next block height at which we can spend the current stage
blocks_til_maturity | int32 |  The number of blocks remaining until the current stage can be swept. Negative values indicate how many blocks have passed since becoming mature.
stage | int64 | Indicates whether the htlc is in its first or second stage of recovery


## PendingUpdate

Field | Type | Description
----- | ---- | ----------- 
txid | byte | 
output_index | int64 | 


## PolicyUpdateRequest

Field | Type | Description
----- | ---- | ----------- 
global | boolean | If set, then this update applies to all currently active channels.
chan_point | [ChannelPoint](#channelpoint) | If set, this update will target a specific channel.
base_fee_msat | string | The base fee charged regardless of the number of milli-satoshis sent.
fee_rate | double | The effective fee rate in milli-satoshis. The precision of this value goes up to 6 decimal places, so 1e-6.
time_lock_delta | int64 | The required timelock delta for HTLCs forwarded over the channel.


## PolicyUpdateResponse

This definition has no parameters.


## QueryRoutesResponse

Field | Type | Description
----- | ---- | ----------- 
routes | [array Route](#route) | 


## RestoreBackupResponse

This definition has no parameters.


## RestoreChanBackupRequest

Field | Type | Description
----- | ---- | ----------- 
chan_backups | [ChannelBackups](#channelbackups) | 
multi_chan_backup | byte | 


## Route

Field | Type | Description
----- | ---- | ----------- 
total_time_lock | int64 |  The cumulative (final) time lock across the entire route.  This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment.
total_fees | string |  The sum of the fees paid at each hop within the final route.  In the case of a one-hop payment, this value will be zero as we don't need to pay a fee to ourselves.
total_amt | string |  The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees.
hops | [array Hop](#hop) |  Contains details concerning the specific forwarding details at each hop.
total_fees_msat | string |  The total fees in millisatoshis.
total_amt_msat | string |  The total amount in millisatoshis.


## RouteHint

Field | Type | Description
----- | ---- | ----------- 
hop_hints | [array HopHint](#hophint) |  A list of hop hints that when chained together can assist in reaching a specific destination.


## RoutingPolicy

Field | Type | Description
----- | ---- | ----------- 
time_lock_delta | int64 | 
min_htlc | string | 
fee_base_msat | string | 
fee_rate_milli_msat | string | 
disabled | boolean | 
max_htlc_msat | string | 


## SendCoinsRequest

Field | Type | Description
----- | ---- | ----------- 
addr | string | The address to send coins to
amount | string | The amount in satoshis to send
target_conf | int32 | The target number of blocks that this transaction should be confirmed by.
sat_per_byte | string | A manual fee rate set in sat/byte that should be used when crafting the transaction.
send_all | boolean |  If set, then the amount field will be ignored, and lnd will attempt to send all the coins under control of the internal wallet to the specified address.


## SendCoinsResponse

Field | Type | Description
----- | ---- | ----------- 
txid | string | The transaction ID of the transaction


## SendManyResponse

Field | Type | Description
----- | ---- | ----------- 
txid | string | The id of the transaction


## SendRequest

Field | Type | Description
----- | ---- | ----------- 
dest | byte | The identity pubkey of the payment recipient
dest_string | string | The hex-encoded identity pubkey of the payment recipient
amt | string | Number of satoshis to send.
payment_hash | byte | The hash to use within the payment's HTLC
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC
payment_request | string |  A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.
final_cltv_delta | int32 |  The CLTV delta from the current height that should be used to set the timelock for the final hop.
fee_limit | [FeeLimit](#feelimit) |  The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.
outgoing_chan_id | string |  The channel id of the channel that must be taken to the first hop. If zero, any channel may be used.
cltv_limit | int64 |  An optional maximum total time lock for the route. If zero, there is no maximum enforced.


## SendResponse

Field | Type | Description
----- | ---- | ----------- 
payment_error | string | 
payment_preimage | byte | 
payment_route | [Route](#route) | 
payment_hash | byte | 


## SendToRouteRequest

Field | Type | Description
----- | ---- | ----------- 
payment_hash | byte | The payment hash to use for the HTLC.
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC.
route | [Route](#route) | Route that should be used to attempt to complete the payment.


## SignMessageRequest

Field | Type | Description
----- | ---- | ----------- 
msg | byte | The message to be signed


## SignMessageResponse

Field | Type | Description
----- | ---- | ----------- 
signature | string | The signature for the given message


## StopResponse

This definition has no parameters.


## Transaction

Field | Type | Description
----- | ---- | ----------- 
tx_hash | string | The transaction hash
amount | string | The transaction amount, denominated in satoshis
num_confirmations | int32 | The number of confirmations
block_hash | string | The hash of the block this transaction was included in
block_height | int32 | The height of the block this transaction was included in
time_stamp | string | Timestamp of this transaction
total_fees | string | Fees paid for this transaction
dest_addresses | array string | Addresses that received funds for this transaction
raw_tx_hex | string | The raw transaction hex.


## TransactionDetails

Field | Type | Description
----- | ---- | ----------- 
transactions | [array Transaction](#transaction) | The list of transactions relevant to the wallet.


## UnlockWalletRequest

Field | Type | Description
----- | ---- | ----------- 
wallet_password | byte |  wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly.
recovery_window | int32 |  recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each individual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.
channel_backups | [ChanBackupSnapshot](#chanbackupsnapshot) |  channel_backups is an optional argument that allows clients to recover the settled funds within a set of channels. This should be populated if the user was unable to close out all channels and sweep funds before partial or total data loss occurred. If specified, then after on-chain recovery of funds, lnd begin to carry out the data loss recovery protocol in order to recover the funds in each channel from a remote force closed transaction.


## UnlockWalletResponse

This definition has no parameters.


## Utxo

Field | Type | Description
----- | ---- | ----------- 
type | [AddressType](#addresstype) | The type of address
address | string | The address
amount_sat | string | The value of the unspent coin in satoshis
pk_script | string | The pkscript in hex
outpoint | [OutPoint](#outpoint) | The outpoint in format txid:n
confirmations | string | The number of confirmations for the Utxo


## VerifyChanBackupResponse

This definition has no parameters.


## VerifyMessageRequest

Field | Type | Description
----- | ---- | ----------- 
msg | byte | The message over which the signature is to be verified
signature | string | The signature to be verified over the given message


## VerifyMessageResponse

Field | Type | Description
----- | ---- | ----------- 
valid | boolean | Whether the signature was valid over the given message
pubkey | string | The pubkey recovered from the signature


## WalletBalanceResponse

Field | Type | Description
----- | ---- | ----------- 
total_balance | string | The balance of the wallet
confirmed_balance | string | The confirmed balance of a wallet(with >= 1 confirmations)
unconfirmed_balance | string | The unconfirmed balance of a wallet(with 0 confirmations)

