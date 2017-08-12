---
title: LND API Reference

language_tabs:
  - shell
  - python
  - javascript

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:max@lightning.engineering'>Contact Us</a>
  - Powered by <a href='https://github.com/lord/slate'>Slate</a>

includes:

search: true
---

# LND API Reference

Welcome to the API reference documentation for LND, the Lightning Network
Daemon.

This site features API documentation for command line arguments, gRPC in
[Python](//dev.lightning.community/guides/python-grpc/) /
[Javascript](//dev.lightning.community/guides/python-grpc/), and a REST proxy.
It is intended for those who already understand how to work with LND. If this is
your first time or you need a refresher, you may consider perusing our LND
developer site featuring a tutorial, resources and guides at
[dev.lightning.community](//dev.lightning.community).

If you prefer to just read code, the original `rpc.proto` file from which
the gRPC documentation was generated can be found in the [lnd Github
repo](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

Lastly, keep in mind that the code examples will differ slightly based on your
operating system and specific setup. The `LND_HOMEDIR` used in the gRPC examples
is `~/.lnd/` for Linux or `~/Library/Application Support/Lnd/tls.cert` for Mac



# WalletBalance

### Simple RPC


 WalletBalance returns the sum of all confirmed unspent outputs under control by the wallet. This method can be modified by having the request specify only witness outputs should be factored into the final output sum.

```shell


$ lncli walletbalance [command options] [arguments...]

# --witness_only  if only witness outputs should be considered when calculating the wallet's balance
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.WalletBalanceRequest(
        witness_only=<YOUR_PARAM>,
    )
>>> response = stub.WalletBalance(request)
>>> response

{ 
    balance: <int64>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.walletBalance({ 
    witness_only: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('WalletBalance: ' + response);
  })

{ 
    balance: <int64>,
}

```

### gRPC Request: WalletBalanceRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
witness_only | bool | optional | If only witness outputs should be considered when calculating the wallet's balance 




### gRPC Response: WalletBalanceResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
balance | int64 | optional | The balance of the wallet 






# ChannelBalance

### Simple RPC


 ChannelBalance returns the total funds available across all open channels in satoshis.

```shell


$ lncli channelbalance [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ChannelBalanceRequest()
>>> response = stub.ChannelBalance(request)
>>> response

{ 
    balance: <int64>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.channelBalance({}, function(err, response) {
    console.log('ChannelBalance: ' + response);
  })

{ 
    balance: <int64>,
}

```

### gRPC Request: ChannelBalanceRequest 



This request has no parameters.




### gRPC Response: ChannelBalanceResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
balance | int64 | optional | Sum of channels balances denominated in satoshis 






# GetTransactions

### Simple RPC


 GetTransactions returns a list describing all the known transactions relevant to the wallet.

```shell

# List all transactions an address of the wallet was involved in.

$ lncli listchaintxns [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GetTransactionsRequest()
>>> response = stub.GetTransactions(request)
>>> response

{ 
    transactions: <Transaction>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.getTransactions({}, function(err, response) {
    console.log('GetTransactions: ' + response);
  })

{ 
    transactions: <Transaction>,
}

```

### gRPC Request: GetTransactionsRequest 



This request has no parameters.




### gRPC Response: TransactionDetails 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
transactions | Transaction | repeated | The list of transactions relevant to the wallet. 



### Transaction


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
tx_hash | string | optional | The transaction hash 
amount | int64 | optional | The transaction ammount, denominated in satoshis 
num_confirmations | int32 | optional | The number of confirmations 
block_hash | string | optional | The hash of the block this transaction was included in 
block_height | int32 | optional | The height of the block this transaction was included in 
time_stamp | int64 | optional | Timestamp of this transaction 
total_fees | int64 | optional | Fees paid for this transaction 





# SendCoins

### Simple RPC


 SendCoins executes a request to send coins to a particular address. Unlike SendMany, this RPC call only allows creating a single output at a time.

```shell

# Send amt coins in satoshis to the BASE58 encoded bitcoin address addr.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli sendcoins [command options] addr amt

# --addr value  the BASE58 encoded bitcoin address to send coins to on-chain
# --amt value   the number of bitcoin denominated in satoshis to send (default: 0)
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendCoinsRequest(
        addr=<YOUR_PARAM>,
        amount=<YOUR_PARAM>,
    )
>>> response = stub.SendCoins(request)
>>> response

{ 
    txid: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.sendCoins({ 
    addr: <YOUR_PARAM>,
    amount: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('SendCoins: ' + response);
  })

{ 
    txid: <string>,
}

```

### gRPC Request: SendCoinsRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
addr | string | optional | The address to send coins to 
amount | int64 | optional | The amount in satoshis to send 




### gRPC Response: SendCoinsResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
txid | string | optional | The transaction ID of the transaction 






# SubscribeTransactions

### Response-streaming RPC


SubscribeTransactions creates a uni-directional stream from the server to the client in which any newly discovered transactions relevant to the wallet are sent over.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GetTransactionsRequest()
>>> for response in stub.SubscribeTransactions(request):
    # Do something
    print response

{ 
    tx_hash: <string>,
    amount: <int64>,
    num_confirmations: <int32>,
    block_hash: <string>,
    block_height: <int32>,
    time_stamp: <int64>,
    total_fees: <int64>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials);
> var call = lightning.subscribeTransactions({})

> call.on('data', function(message) {
    console.log(message);
  });
> call.on('end', function() {
    // The server has finished sending
    console.log("END");
  });
> call.on('status', function(status) {
    // Process status
    console.log("Current status: " + status);
  });

{ 
    tx_hash: <string>,
    amount: <int64>,
    num_confirmations: <int32>,
    block_hash: <string>,
    block_height: <int32>,
    time_stamp: <int64>,
    total_fees: <int64>,
}

```

### gRPC Request: GetTransactionsRequest 



This request has no parameters.




### gRPC Response: Transaction (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
tx_hash | string | optional | The transaction hash 
amount | int64 | optional | The transaction ammount, denominated in satoshis 
num_confirmations | int32 | optional | The number of confirmations 
block_hash | string | optional | The hash of the block this transaction was included in 
block_height | int32 | optional | The height of the block this transaction was included in 
time_stamp | int64 | optional | Timestamp of this transaction 
total_fees | int64 | optional | Fees paid for this transaction 






# SendMany

### Simple RPC


 SendMany handles a request for a transaction that creates multiple specified outputs in parallel.

```shell

# create and broadcast a transaction paying the specified amount(s) to the passed address(es)
# 'send-json-string' decodes addresses and the amount to send respectively in the following format.
# '{"ExampleAddr": NumCoinsInSatoshis, "SecondAddr": NumCoins}'

$ lncli sendmany send-json-string

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendManyRequest(
        AddrToAmount=<YOUR_PARAM>,
    )
>>> response = stub.SendMany(request)
>>> response

{ 
    txid: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.sendMany({ 
    AddrToAmount: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('SendMany: ' + response);
  })

{ 
    txid: <string>,
}

```

### gRPC Request: SendManyRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
AddrToAmount | AddrToAmountEntry | repeated | The map from addresses to amounts 



### AddrToAmountEntry


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
key | string | optional |  
value | int64 | optional |  



### gRPC Response: SendManyResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
txid | string | optional | The id of the transaction 






# NewAddress

### Simple RPC


 NewAddress creates a new address under control of the local wallet.

```shell

# Generate a wallet new address. Address-types has to be one of:
# - p2wkh:  Push to witness key hash
# - np2wkh: Push to nested witness key hash
# - p2pkh:  Push to public key hash

$ lncli newaddress address-type

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NewAddressRequest(
        type=<YOUR_PARAM>,
    )
>>> response = stub.NewAddress(request)
>>> response

{ 
    address: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.newAddress({ 
    type: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('NewAddress: ' + response);
  })

{ 
    address: <string>,
}

```

### gRPC Request: NewAddressRequest 

`AddressType` has to be one of:  - `p2wkh`: Pay to witness key hash (`WITNESS_PUBKEY_HASH` = 0) - `np2wkh`: Pay to nested witness key hash (`NESTED_PUBKEY_HASH` = 1) - `p2pkh`:  Pay to public key hash (`PUBKEY_HASH` = 2)

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
type | AddressType | optional | The address type 




### gRPC Response: NewAddressResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
address | string | optional | The newly generated wallet address 






# NewWitnessAddress

### Simple RPC


NewWitnessAddress creates a new witness address under control of the local wallet.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NewWitnessAddressRequest()
>>> response = stub.NewWitnessAddress(request)
>>> response

{ 
    address: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.newWitnessAddress({}, function(err, response) {
    console.log('NewWitnessAddress: ' + response);
  })

{ 
    address: <string>,
}

```

### gRPC Request: NewWitnessAddressRequest 



This request has no parameters.




### gRPC Response: NewAddressResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
address | string | optional | The newly generated wallet address 






# SignMessage

### Simple RPC


 SignMessage signs a message with this node's private key. The returned signature string is `zbase32` encoded and pubkey recoverable, meaning that only the message digest and signature are needed for verification.

```shell

# Sign msg with the resident node's private key. Returns a the signature as a zbase32 string.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli signmessage [command options] msg

# --msg value  the message to sign
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SignMessageRequest(
        msg=<YOUR_PARAM>,
    )
>>> response = stub.SignMessage(request)
>>> response

{ 
    signature: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.signMessage({ 
    msg: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('SignMessage: ' + response);
  })

{ 
    signature: <string>,
}

```

### gRPC Request: SignMessageRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
msg | bytes | optional | The message to be signed 




### gRPC Response: SignMessageResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
signature | string | optional | The signature for the given message 






# VerifyMessage

### Simple RPC


 VerifyMessage verifies a signature over a msg. The signature must be zbase32 encoded and signed by an active node in the resident node's channel database. In addition to returning the validity of the signature, VerifyMessage also returns the recovered pubkey from the signature.

```shell

# Verify that the message was signed with a properly-formed signature.
# The signature must be zbase32 encoded and signed with the private key of
# an active node in the resident node's channel database.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli verifymessage [command options] msg signature

# --msg value  the message to verify
# --sig value  the zbase32 encoded signature of the message
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.VerifyMessageRequest(
        msg=<YOUR_PARAM>,
        signature=<YOUR_PARAM>,
    )
>>> response = stub.VerifyMessage(request)
>>> response

{ 
    valid: <bool>,
    pubkey: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.verifyMessage({ 
    msg: <YOUR_PARAM>,
    signature: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('VerifyMessage: ' + response);
  })

{ 
    valid: <bool>,
    pubkey: <string>,
}

```

### gRPC Request: VerifyMessageRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
msg | bytes | optional | The message over which the signature is to be verified 
signature | string | optional | The signature to be verifed over the given message 




### gRPC Response: VerifyMessageResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
valid | bool | optional | Whether the signature was valid over the given message 
pubkey | string | optional | The pubkey recovered from the signature 






# ConnectPeer

### Simple RPC


 ConnectPeer attempts to establish a connection to a remote peer. This is at the networking level, and is used for communication between nodes. This is distinct from establishing a channel with a peer.

```shell


$ lncli connect [command options] <pubkey>@host

# --perm  If set, the daemon will attempt to persistently connect to the target peer.
# If not, the call will be synchronous.
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ConnectPeerRequest(
        addr=<YOUR_PARAM>,
        perm=<YOUR_PARAM>,
    )
>>> response = stub.ConnectPeer(request)
>>> response

{ 
    peer_id: <int32>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.connectPeer({ 
    addr: <YOUR_PARAM>,
    perm: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('ConnectPeer: ' + response);
  })

{ 
    peer_id: <int32>,
}

```

### gRPC Request: ConnectPeerRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
addr | LightningAddress | optional | Lightning address of the peer, in the format `<pubkey>@host` 
perm | bool | optional | If set, the daemon will attempt to persistently connect to the target peer.  Otherwise, the call will be synchronous. 



### LightningAddress


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pubkey | string | optional | The identity pubkey of the Lightning node 
host | string | optional | The network location of the lightning node, e.g. `69.69.69.69:1337` or `localhost:10011` 



### gRPC Response: ConnectPeerResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
peer_id | int32 | optional | The id of the newly connected peer 






# DisconnectPeer

### Simple RPC


 DisconnectPeer attempts to disconnect one peer from another identified by a given pubKey. In the case that we currently have a pending or active channel with the target peer, then this action will be not be allowed.

```shell


$ lncli disconnect [command options] <pubkey>

# --node_key value  The hex-encoded compressed public key of the peer to disconnect from
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.DisconnectPeerRequest(
        pub_key=<YOUR_PARAM>,
    )
>>> response = stub.DisconnectPeer(request)
>>> response
{}
```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.disconnectPeer({ 
    pub_key: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('DisconnectPeer: ' + response);
  })
{}
```

### gRPC Request: DisconnectPeerRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional | The pubkey of the node to disconnect from 




### gRPC Response: DisconnectPeerResponse 



This response is empty.






# ListPeers

### Simple RPC


 ListPeers returns a verbose listing of all currently active peers.

```shell


$ lncli listpeers [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListPeersRequest()
>>> response = stub.ListPeers(request)
>>> response

{ 
    peers: <Peer>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.listPeers({}, function(err, response) {
    console.log('ListPeers: ' + response);
  })

{ 
    peers: <Peer>,
}

```

### gRPC Request: ListPeersRequest 



This request has no parameters.




### gRPC Response: ListPeersResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
peers | Peer | repeated | The list of currently connected peers 



### Peer


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional | The identity pubkey of the peer 
peer_id | int32 | optional | The peer's id from the local point of view 
address | string | optional | Network address of the peer; eg `127.0.0.1:10011` 
bytes_sent | uint64 | optional | Bytes of data transmitted to this peer 
bytes_recv | uint64 | optional | Bytes of data transmitted from this peer 
sat_sent | int64 | optional | Satoshis sent to this peer 
sat_recv | int64 | optional | Satoshis received from this peer 
inbound | bool | optional | A channel is inbound if the counterparty initiated the channel 
ping_time | int64 | optional | Ping time to this peer 





# GetInfo

### Simple RPC


 GetInfo returns general information concerning the lightning node including it's identity pubkey, alias, the chains it is connected to, and information concerning the number of open+pending channels.

```shell


$ lncli getinfo [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GetInfoRequest()
>>> response = stub.GetInfo(request)
>>> response

{ 
    identity_pubkey: <string>,
    alias: <string>,
    num_pending_channels: <uint32>,
    num_active_channels: <uint32>,
    num_peers: <uint32>,
    block_height: <uint32>,
    block_hash: <string>,
    synced_to_chain: <bool>,
    testnet: <bool>,
    chains: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.getInfo({}, function(err, response) {
    console.log('GetInfo: ' + response);
  })

{ 
    identity_pubkey: <string>,
    alias: <string>,
    num_pending_channels: <uint32>,
    num_active_channels: <uint32>,
    num_peers: <uint32>,
    block_height: <uint32>,
    block_hash: <string>,
    synced_to_chain: <bool>,
    testnet: <bool>,
    chains: <string>,
}

```

### gRPC Request: GetInfoRequest 



This request has no parameters.




### gRPC Response: GetInfoResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
identity_pubkey | string | optional | The identity pubkey of the current node. 
alias | string | optional | If applicable, the alias of the current node, e.g. "bob" 
num_pending_channels | uint32 | optional | Number of pending channels 
num_active_channels | uint32 | optional | Number of active channels 
num_peers | uint32 | optional | Number of peers 
block_height | uint32 | optional | The node's current view of the height of the best block 
block_hash | string | optional | The node's current view of the hash of the best block 
synced_to_chain | bool | optional | Whether the wallet's view is synced to the main chain 
testnet | bool | optional | Whether the current node is connected to testnet 
chains | string | repeated | A list of active chains the node is connected to 






# PendingChannels

### Simple RPC


 PendingChannels returns a list of all the channels that are currently considered "pending". A channel is pending if it has finished the funding workflow and is waiting for confirmations for the funding txn, or is in the process of closure, either initiated cooperatively or non-cooperatively.

```shell


$ lncli pendingchannels [command options] [arguments...]

# --open, -o   display the status of new pending channels
# --close, -c  display the status of channels being closed
# --all, -a    display the status of channels in the process of being opened or closed
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PendingChannelRequest()
>>> response = stub.PendingChannels(request)
>>> response

{ 
    total_limbo_balance: <int64>,
    pending_open_channels: <PendingOpenChannel>,
    pending_closing_channels: <ClosedChannel>,
    pending_force_closing_channels: <ForceClosedChannel>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.pendingChannels({}, function(err, response) {
    console.log('PendingChannels: ' + response);
  })

{ 
    total_limbo_balance: <int64>,
    pending_open_channels: <PendingOpenChannel>,
    pending_closing_channels: <ClosedChannel>,
    pending_force_closing_channels: <ForceClosedChannel>,
}

```

### gRPC Request: PendingChannelRequest 



This request has no parameters.




### gRPC Response: PendingChannelResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
total_limbo_balance | int64 | optional | The balance in satoshis encumbered in pending channels 
pending_open_channels | PendingOpenChannel | repeated | Channels pending opening 
pending_closing_channels | ClosedChannel | repeated | Channels pending closing 
pending_force_closing_channels | ForceClosedChannel | repeated | Channels pending force closing 



### PendingOpenChannel


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel | PendingChannel | optional | The pending channel 
confirmation_height | uint32 | optional | The height at which this channel will be confirmed 
blocks_till_open | uint32 | optional | The number of blocks until this channel is open 
commit_fee | int64 | optional | The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart. 
commit_weight | int64 | optional | The weight of the commitment transaction 
fee_per_kw | int64 | optional | The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open. 


### ClosedChannel


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel | PendingChannel | optional | The pending channel to be closed 
closing_txid | string | optional | The transaction id of the closing transaction 


### ForceClosedChannel


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel | PendingChannel | optional | The pending channel to be force closed 
closing_txid | string | optional | The transaction id of the closing transaction 
limbo_balance | int64 | optional | The balance in satoshis encumbered in this pending channel 
maturity_height | uint32 | optional | The height at which funds can be sweeped into the wallet 
blocks_til_maturity | uint32 | optional | Remaining # of blocks until funds can be sweeped into the wallet 





# ListChannels

### Simple RPC


 ListChannels returns a description of all the open channels that this node is a participant in.

```shell


$ lncli listchannels [command options] [arguments...]

# --active_only, -a  only list channels which are currently active
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListChannelsRequest()
>>> response = stub.ListChannels(request)
>>> response

{ 
    channels: <ActiveChannel>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.listChannels({}, function(err, response) {
    console.log('ListChannels: ' + response);
  })

{ 
    channels: <ActiveChannel>,
}

```

### gRPC Request: ListChannelsRequest 



This request has no parameters.




### gRPC Response: ListChannelsResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channels | ActiveChannel | repeated | The list of active channels 



### ActiveChannel


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
active | bool | optional | Whether this channel is active or not 
remote_pubkey | string | optional | The identity pubkey of the remote node 
channel_point | string | optional | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
chan_id | uint64 | optional | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
capacity | int64 | optional | The total amount of funds held in this channel 
local_balance | int64 | optional | This node's current balance in this channel 
remote_balance | int64 | optional | The counterparty's current balance in this channel 
commit_fee | int64 | optional | The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart. 
commit_weight | int64 | optional | The weight of the commitment transaction 
fee_per_kw | int64 | optional | The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open. 
unsettled_balance | int64 | optional | The unsettled balance in this channel 
total_satoshis_sent | int64 | optional | The total number of satoshis we've sent within this channel. 
total_satoshis_received | int64 | optional | The total number of satoshis we've received within this channel. 
num_updates | uint64 | optional | The total number of updates conducted within this channel. 
pending_htlcs | HTLC | repeated | The list of active, uncleared HTLCs currently pending within the channel. 





# OpenChannelSync

### Simple RPC


OpenChannelSync is a synchronous version of the OpenChannel RPC call. This call is meant to be consumed by clients to the REST proxy. As with all other sync calls, all byte slices are intended to be populated as hex encoded strings.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.OpenChannelRequest(
        target_peer_id=<YOUR_PARAM>,
        node_pubkey=<YOUR_PARAM>,
        node_pubkey_string=<YOUR_PARAM>,
        local_funding_amount=<YOUR_PARAM>,
        push_sat=<YOUR_PARAM>,
    )
>>> response = stub.OpenChannelSync(request)
>>> response

{ 
    funding_txid: <bytes>,
    funding_txid_str: <string>,
    output_index: <uint32>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.openChannelSync({ 
    target_peer_id: <YOUR_PARAM>,
    node_pubkey: <YOUR_PARAM>,
    node_pubkey_string: <YOUR_PARAM>,
    local_funding_amount: <YOUR_PARAM>,
    push_sat: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('OpenChannelSync: ' + response);
  })

{ 
    funding_txid: <bytes>,
    funding_txid_str: <string>,
    output_index: <uint32>,
}

```

### gRPC Request: OpenChannelRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
target_peer_id | int32 | optional | The peer_id of the node to open a channel with 
node_pubkey | bytes | optional | The pubkey of the node to open a channel with 
node_pubkey_string | string | optional | The hex encorded pubkey of the node to open a channel with 
local_funding_amount | int64 | optional | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | optional | The number of satoshis to push to the remote side as part of the initial commitment state 




### gRPC Response: ChannelPoint 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
funding_txid | bytes | optional | Txid of the funding transaction 
funding_txid_str | string | optional | Hex-encoded string representing the funding transaction 
output_index | uint32 | optional | The index of the output of the funding transaction 






# OpenChannel

### Response-streaming RPC


 OpenChannel attempts to open a singly funded channel specified in the request to a remote peer.

```shell

# Attempt to open a new channel to an existing peer with the key node-key, optionally blocking until the channel is 'open'. The channel will be initialized with local-amt satoshis local and push-amt satoshis for the remote node. Once the channel is open, a channelPoint (txid:vout) of the funding output is returned. NOTE: peer_id and node_key are mutually exclusive, only one should be used, not both.

$ lncli openchannel [command options] node-key local-amt push-amt

# --peer_id value    the relative id of the peer to open a channel with (default: 0)
# --node_key value   the identity public key of the target peer serialized in compressed format
# --local_amt value  the number of satoshis the wallet should commit to the channel (default: 0)
# --push_amt value   the number of satoshis to push to the remote side as part of the initial commitment state (default: 0)
# --block            block and wait until the channel is fully open
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.OpenChannelRequest(
        target_peer_id=<YOUR_PARAM>,
        node_pubkey=<YOUR_PARAM>,
        node_pubkey_string=<YOUR_PARAM>,
        local_funding_amount=<YOUR_PARAM>,
        push_sat=<YOUR_PARAM>,
    )
>>> for response in stub.OpenChannel(request):
    # Do something
    print response

{ 
    chan_pending: <PendingUpdate>,
    confirmation: <ConfirmationUpdate>,
    chan_open: <ChannelOpenUpdate>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials);
> var call = lightning.openChannel({ 
    target_peer_id: <YOUR_PARAM>,
    node_pubkey: <YOUR_PARAM>,
    node_pubkey_string: <YOUR_PARAM>,
    local_funding_amount: <YOUR_PARAM>,
    push_sat: <YOUR_PARAM>,
  })

> call.on('data', function(message) {
    console.log(message);
  });
> call.on('end', function() {
    // The server has finished sending
    console.log("END");
  });
> call.on('status', function(status) {
    // Process status
    console.log("Current status: " + status);
  });

{ 
    chan_pending: <PendingUpdate>,
    confirmation: <ConfirmationUpdate>,
    chan_open: <ChannelOpenUpdate>,
}

```

### gRPC Request: OpenChannelRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
target_peer_id | int32 | optional | The peer_id of the node to open a channel with 
node_pubkey | bytes | optional | The pubkey of the node to open a channel with 
node_pubkey_string | string | optional | The hex encorded pubkey of the node to open a channel with 
local_funding_amount | int64 | optional | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | optional | The number of satoshis to push to the remote side as part of the initial commitment state 




### gRPC Response: OpenStatusUpdate (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
chan_pending | PendingUpdate | optional |  
confirmation | ConfirmationUpdate | optional |  
chan_open | ChannelOpenUpdate | optional |  



### PendingUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
txid | bytes | optional |  
output_index | uint32 | optional |  


### ConfirmationUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
block_sha | bytes | optional |  
block_height | int32 | optional |  
num_confs_left | uint32 | optional |  


### ChannelOpenUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel_point | ChannelPoint | optional |  





# CloseChannel

### Response-streaming RPC


 CloseChannel attempts to close an active channel identified by its channel outpoint (ChannelPoint). The actions of this method can additionally be augmented to attempt a force close after a timeout period in the case of an inactive peer.

```shell

# Close an existing channel. The channel can be closed either cooperatively, or uncooperatively (forced).

$ lncli closechannel [command options] funding_txid [output_index [time_limit]]

# --funding_txid value  the txid of the channel's funding transaction
# --output_index value  the output index for the funding output of the funding transaction (default: 0)
# --time_limit value    a relative deadline afterwhich the attempt should be abandoned
# --force               after the time limit has passed, attempt an uncooperative closure
# --block               block until the channel is closed
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.CloseChannelRequest(
        channel_point=<YOUR_PARAM>,
        time_limit=<YOUR_PARAM>,
        force=<YOUR_PARAM>,
    )
>>> for response in stub.CloseChannel(request):
    # Do something
    print response

{ 
    close_pending: <PendingUpdate>,
    confirmation: <ConfirmationUpdate>,
    chan_close: <ChannelCloseUpdate>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials);
> var call = lightning.closeChannel({ 
    channel_point: <YOUR_PARAM>,
    time_limit: <YOUR_PARAM>,
    force: <YOUR_PARAM>,
  })

> call.on('data', function(message) {
    console.log(message);
  });
> call.on('end', function() {
    // The server has finished sending
    console.log("END");
  });
> call.on('status', function(status) {
    // Process status
    console.log("Current status: " + status);
  });

{ 
    close_pending: <PendingUpdate>,
    confirmation: <ConfirmationUpdate>,
    chan_close: <ChannelCloseUpdate>,
}

```

### gRPC Request: CloseChannelRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel_point | ChannelPoint | optional | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
time_limit | int64 | optional | a relative deadline afterwhich the attempt should be abandoned 
force | bool | optional | after the time limit has passed, attempt an uncooperative closure 



### ChannelPoint


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
funding_txid | bytes | optional | Txid of the funding transaction 
funding_txid_str | string | optional | Hex-encoded string representing the funding transaction 
output_index | uint32 | optional | The index of the output of the funding transaction 



### gRPC Response: CloseStatusUpdate (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
close_pending | PendingUpdate | optional |  
confirmation | ConfirmationUpdate | optional |  
chan_close | ChannelCloseUpdate | optional |  



### PendingUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
txid | bytes | optional |  
output_index | uint32 | optional |  


### ConfirmationUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
block_sha | bytes | optional |  
block_height | int32 | optional |  
num_confs_left | uint32 | optional |  


### ChannelCloseUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
closing_txid | bytes | optional |  
success | bool | optional |  





# SendPayment

### Bidirectional-streaming RPC


 SendPayment dispatches a bi-directional streaming RPC for sending payments through the Lightning Network. A single RPC invocation creates a persistent bi-directional stream allowing clients to rapidly send payments through the Lightning Network with a single persistent connection.

```shell


$ lncli sendpayment [command options] (destination amount payment_hash | --pay_req=[payment request])

# --dest value, -d value          the compressed identity pubkey of the payment recipient
# --amt value, -a value           number of satoshis to send (default: 0)
# --payment_hash value, -r value  the hash to use within the payment's HTLC
# --debug_send                    use the debug rHash when sending the HTLC
# --pay_req value                 a zbase32-check encoded payment request to fulfill
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
# Define a generator that returns an Iterable of SendRequest objects
>>> def request_generator():
        # Initialization code here
        print("Starting up")
        while True:
            # Params here can be set as arguments to the generator
            request = ln.SendRequest(
                dest=<YOUR_PARAM>,
                dest_string=<YOUR_PARAM>,
                amt=<YOUR_PARAM>,
                payment_hash=<YOUR_PARAM>,
                payment_hash_string=<YOUR_PARAM>,
                payment_request=<YOUR_PARAM>,
            )
            yield request
            # Do things between iterations here
>>> request_iterable = request_generator()
>>> for response in stub.SendPayment(request_iterable):
    # Do something
    print response

{ 
    payment_error: <string>,
    payment_preimage: <bytes>,
    payment_route: <Route>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials);
> var call = lightning.sendPayment({});

> call.on('data', function(message) {
    console.log(message);
  });

  > call.write({ 
    dest: <YOUR_PARAM>,
    dest_string: <YOUR_PARAM>,
    amt: <YOUR_PARAM>,
    payment_hash: <YOUR_PARAM>,
    payment_hash_string: <YOUR_PARAM>,
    payment_request: <YOUR_PARAM>,
  });

{ 
    payment_error: <string>,
    payment_preimage: <bytes>,
    payment_route: <Route>,
}

```

### gRPC Request: SendRequest (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
dest | bytes | optional | The identity pubkey of the payment recipient 
dest_string | string | optional | The hex-encoded identity pubkey of the payment recipient 
amt | int64 | optional | Number of satoshis to send 
payment_hash | bytes | optional | The hash to use within the payment's HTLC 
payment_hash_string | string | optional | The hex-encoded hash to use within the payment's HTLC 
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 




### gRPC Response: SendResponse (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payment_error | string | optional |  
payment_preimage | bytes | optional |  
payment_route | Route | optional |  



### Route
A path through the channel graph which runs over one or more channels in succession. This struct carries all the information required to craft the Sphinx onion packet, and send the payment along the first hop in the path. A route is only selected as valid if all the channels have sufficient capacity to carry the initial payment amount after fees are accounted for.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
total_time_lock | uint32 | optional | The cumulative (final) time lock across the entire route.  This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment. 
total_fees | int64 | optional | The sum of the fees paid at each hop within the final route.  In the case of a one-hop payment, this value will be zero as we don't need to pay a fee it ourself. 
total_amt | int64 | optional | The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees. 
hops | Hop | repeated | Contains details concerning the specific forwarding details at each hop. 





# SendPaymentSync

### Simple RPC


SendPaymentSync is the synchronous non-streaming version of SendPayment. This RPC is intended to be consumed by clients of the REST proxy. Additionally, this RPC expects the destination's public key and the payment hash (if any) to be encoded as hex strings.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendRequest(
        dest=<YOUR_PARAM>,
        dest_string=<YOUR_PARAM>,
        amt=<YOUR_PARAM>,
        payment_hash=<YOUR_PARAM>,
        payment_hash_string=<YOUR_PARAM>,
        payment_request=<YOUR_PARAM>,
    )
>>> response = stub.SendPaymentSync(request)
>>> response

{ 
    payment_error: <string>,
    payment_preimage: <bytes>,
    payment_route: <Route>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.sendPaymentSync({ 
    dest: <YOUR_PARAM>,
    dest_string: <YOUR_PARAM>,
    amt: <YOUR_PARAM>,
    payment_hash: <YOUR_PARAM>,
    payment_hash_string: <YOUR_PARAM>,
    payment_request: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('SendPaymentSync: ' + response);
  })

{ 
    payment_error: <string>,
    payment_preimage: <bytes>,
    payment_route: <Route>,
}

```

### gRPC Request: SendRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
dest | bytes | optional | The identity pubkey of the payment recipient 
dest_string | string | optional | The hex-encoded identity pubkey of the payment recipient 
amt | int64 | optional | Number of satoshis to send 
payment_hash | bytes | optional | The hash to use within the payment's HTLC 
payment_hash_string | string | optional | The hex-encoded hash to use within the payment's HTLC 
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 




### gRPC Response: SendResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payment_error | string | optional |  
payment_preimage | bytes | optional |  
payment_route | Route | optional |  



### Route
A path through the channel graph which runs over one or more channels in succession. This struct carries all the information required to craft the Sphinx onion packet, and send the payment along the first hop in the path. A route is only selected as valid if all the channels have sufficient capacity to carry the initial payment amount after fees are accounted for.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
total_time_lock | uint32 | optional | The cumulative (final) time lock across the entire route.  This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment. 
total_fees | int64 | optional | The sum of the fees paid at each hop within the final route.  In the case of a one-hop payment, this value will be zero as we don't need to pay a fee it ourself. 
total_amt | int64 | optional | The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees. 
hops | Hop | repeated | Contains details concerning the specific forwarding details at each hop. 





# AddInvoice

### Simple RPC


 AddInvoice attempts to add a new invoice to the invoice database. Any duplicated invoices are rejected, therefore all invoices *must* have a unique payment preimage.

```shell

# Add a new invoice, expressing intent for a future payment. The value of the invoice in satoshis and a 32 byte hash preimage are neccesary for the creation

$ lncli addinvoice [command options] value preimage

# --memo value      an optional memo to attach along with the invoice
# --receipt value   an optional cryptographic receipt of payment
# --preimage value  the hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage
# --value value     the value of this invoice in satoshis (default: 0)
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.Invoice(
        memo=<YOUR_PARAM>,
        receipt=<YOUR_PARAM>,
        r_preimage=<YOUR_PARAM>,
        r_hash=<YOUR_PARAM>,
        value=<YOUR_PARAM>,
        settled=<YOUR_PARAM>,
        creation_date=<YOUR_PARAM>,
        settle_date=<YOUR_PARAM>,
        payment_request=<YOUR_PARAM>,
    )
>>> response = stub.AddInvoice(request)
>>> response

{ 
    r_hash: <bytes>,
    payment_request: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.addInvoice({ 
    memo: <YOUR_PARAM>,
    receipt: <YOUR_PARAM>,
    r_preimage: <YOUR_PARAM>,
    r_hash: <YOUR_PARAM>,
    value: <YOUR_PARAM>,
    settled: <YOUR_PARAM>,
    creation_date: <YOUR_PARAM>,
    settle_date: <YOUR_PARAM>,
    payment_request: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('AddInvoice: ' + response);
  })

{ 
    r_hash: <bytes>,
    payment_request: <string>,
}

```

### gRPC Request: Invoice 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional | An optional memo to attach along with the invoice 
receipt | bytes | optional | An optional cryptographic receipt of payment 
r_preimage | bytes | optional | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | optional | The hash of the preimage 
value | int64 | optional | The value of this invoice in satoshis 
settled | bool | optional | Whether this invoice has been fulfilled 
creation_date | int64 | optional | When this invoice was created 
settle_date | int64 | optional | When this invoice was settled 
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 




### gRPC Response: AddInvoiceResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
r_hash | bytes | optional |  
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 






# ListInvoices

### Simple RPC


 ListInvoices returns a list of all the invoices currently stored within the database. Any active debug invoices are ignored.

```shell


$ lncli listinvoices [command options] [arguments...]

# --pending_only  toggles if all invoices should be returned, or only those that are currently unsettled
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListInvoiceRequest(
        pending_only=<YOUR_PARAM>,
    )
>>> response = stub.ListInvoices(request)
>>> response

{ 
    invoices: <Invoice>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.listInvoices({ 
    pending_only: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('ListInvoices: ' + response);
  })

{ 
    invoices: <Invoice>,
}

```

### gRPC Request: ListInvoiceRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pending_only | bool | optional | Toggles if all invoices should be returned, or only those that are currently unsettled 




### gRPC Response: ListInvoiceResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
invoices | Invoice | repeated |  



### Invoice


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional | An optional memo to attach along with the invoice 
receipt | bytes | optional | An optional cryptographic receipt of payment 
r_preimage | bytes | optional | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | optional | The hash of the preimage 
value | int64 | optional | The value of this invoice in satoshis 
settled | bool | optional | Whether this invoice has been fulfilled 
creation_date | int64 | optional | When this invoice was created 
settle_date | int64 | optional | When this invoice was settled 
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 





# LookupInvoice

### Simple RPC


 LookupInvoice attemps to look up an invoice according to its payment hash. The passed payment hash *must* be exactly 32 bytes, if not, an error is returned.

```shell


$ lncli lookupinvoice [command options] rhash

# --rhash value  the 32 byte payment hash of the invoice to query for, the hash should be a hex-encoded string
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PaymentHash(
        r_hash_str=<YOUR_PARAM>,
        r_hash=<YOUR_PARAM>,
    )
>>> response = stub.LookupInvoice(request)
>>> response

{ 
    memo: <string>,
    receipt: <bytes>,
    r_preimage: <bytes>,
    r_hash: <bytes>,
    value: <int64>,
    settled: <bool>,
    creation_date: <int64>,
    settle_date: <int64>,
    payment_request: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.lookupInvoice({ 
    r_hash_str: <YOUR_PARAM>,
    r_hash: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('LookupInvoice: ' + response);
  })

{ 
    memo: <string>,
    receipt: <bytes>,
    r_preimage: <bytes>,
    r_hash: <bytes>,
    value: <int64>,
    settled: <bool>,
    creation_date: <int64>,
    settle_date: <int64>,
    payment_request: <string>,
}

```

### gRPC Request: PaymentHash 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
r_hash_str | string | optional | The hex-encoded payment hash of the invoice to be looked up. The passed payment hash must be exactly 32 bytes, otherwise an error is returned. 
r_hash | bytes | optional | The payment hash of the invoice to be looked up. 




### gRPC Response: Invoice 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional | An optional memo to attach along with the invoice 
receipt | bytes | optional | An optional cryptographic receipt of payment 
r_preimage | bytes | optional | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | optional | The hash of the preimage 
value | int64 | optional | The value of this invoice in satoshis 
settled | bool | optional | Whether this invoice has been fulfilled 
creation_date | int64 | optional | When this invoice was created 
settle_date | int64 | optional | When this invoice was settled 
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 






# SubscribeInvoices

### Response-streaming RPC


SubscribeInvoices returns a uni-directional stream (sever -> client) for notifying the client of newly added/settled invoices.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.InvoiceSubscription()
>>> for response in stub.SubscribeInvoices(request):
    # Do something
    print response

{ 
    memo: <string>,
    receipt: <bytes>,
    r_preimage: <bytes>,
    r_hash: <bytes>,
    value: <int64>,
    settled: <bool>,
    creation_date: <int64>,
    settle_date: <int64>,
    payment_request: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials);
> var call = lightning.subscribeInvoices({})

> call.on('data', function(message) {
    console.log(message);
  });
> call.on('end', function() {
    // The server has finished sending
    console.log("END");
  });
> call.on('status', function(status) {
    // Process status
    console.log("Current status: " + status);
  });

{ 
    memo: <string>,
    receipt: <bytes>,
    r_preimage: <bytes>,
    r_hash: <bytes>,
    value: <int64>,
    settled: <bool>,
    creation_date: <int64>,
    settle_date: <int64>,
    payment_request: <string>,
}

```

### gRPC Request: InvoiceSubscription 



This request has no parameters.




### gRPC Response: Invoice (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional | An optional memo to attach along with the invoice 
receipt | bytes | optional | An optional cryptographic receipt of payment 
r_preimage | bytes | optional | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | optional | The hash of the preimage 
value | int64 | optional | The value of this invoice in satoshis 
settled | bool | optional | Whether this invoice has been fulfilled 
creation_date | int64 | optional | When this invoice was created 
settle_date | int64 | optional | When this invoice was settled 
payment_request | string | optional | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 






# DecodePayReq

### Simple RPC


 DecodePayReq takes an encoded payment request string and attempts to decode it, returning a full description of the conditions encoded within the payment request.

```shell

# Decode the passed payment request revealing the destination, payment hash and value of the payment request

$ lncli decodepayreq [command options] pay_req

# --pay_req value  the zpay32 encoded payment request
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PayReqString(
        pay_req=<YOUR_PARAM>,
    )
>>> response = stub.DecodePayReq(request)
>>> response

{ 
    destination: <string>,
    payment_hash: <string>,
    num_satoshis: <int64>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.decodePayReq({ 
    pay_req: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('DecodePayReq: ' + response);
  })

{ 
    destination: <string>,
    payment_hash: <string>,
    num_satoshis: <int64>,
}

```

### gRPC Request: PayReqString 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pay_req | string | optional | The payment request string to be decoded 




### gRPC Response: PayReq 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
destination | string | optional |  
payment_hash | string | optional |  
num_satoshis | int64 | optional |  






# ListPayments

### Simple RPC


 ListPayments returns a list of all outgoing payments.

```shell


$ lncli listpayments [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListPaymentsRequest()
>>> response = stub.ListPayments(request)
>>> response

{ 
    payments: <Payment>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.listPayments({}, function(err, response) {
    console.log('ListPayments: ' + response);
  })

{ 
    payments: <Payment>,
}

```

### gRPC Request: ListPaymentsRequest 



This request has no parameters.




### gRPC Response: ListPaymentsResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payments | Payment | repeated | The list of payments 



### Payment


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payment_hash | string | optional | The payment hash 
value | int64 | optional | The value of the payment in satoshis 
creation_date | int64 | optional | The date of this payment 
path | string | repeated | The path this payment took 
fee | int64 | optional | The fee paid for this payment in satoshis 





# DeleteAllPayments

### Simple RPC


DeleteAllPayments deletes all outgoing payments from DB.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.DeleteAllPaymentsRequest()
>>> response = stub.DeleteAllPayments(request)
>>> response
{}
```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.deleteAllPayments({}, function(err, response) {
    console.log('DeleteAllPayments: ' + response);
  })
{}
```

### gRPC Request: DeleteAllPaymentsRequest 



This request has no parameters.




### gRPC Response: DeleteAllPaymentsResponse 



This response is empty.






# DescribeGraph

### Simple RPC


 DescribeGraph returns a description of the latest graph state from the point of view of the node. The graph information is partitioned into two components: all the nodes/vertexes, and all the edges that connect the vertexes themselves.  As this is a directed graph, the edges also contain the node directional specific routing policy which includes: the time lock delta, fee information, etc.

```shell

# prints a human readable version of the known channel graph from the PoV of the node

$ lncli describegraph [command options] [arguments...]

# --render  If set, then an image of graph will be generated and displayed. The generated image is stored within the current directory with a file name of 'graph.svg'
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ChannelGraphRequest()
>>> response = stub.DescribeGraph(request)
>>> response

{ 
    nodes: <LightningNode>,
    edges: <ChannelEdge>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.describeGraph({}, function(err, response) {
    console.log('DescribeGraph: ' + response);
  })

{ 
    nodes: <LightningNode>,
    edges: <ChannelEdge>,
}

```

### gRPC Request: ChannelGraphRequest 



This request has no parameters.




### gRPC Response: ChannelGraph 

Returns a new instance of the directed channel graph.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
nodes | LightningNode | repeated | The list of `LightningNode`s in this channel graph 
edges | ChannelEdge | repeated | The list of `ChannelEdge`s in this channel graph 



### LightningNode
An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
last_update | uint32 | optional |  
pub_key | string | optional |  
alias | string | optional |  
addresses | NodeAddress | repeated |  


### ChannelEdge
A fully authenticated channel along with all its unique attributes. Once an authenticated channel announcement has been processed on the network, then a instance of ChannelEdgeInfo encapsulating the channels attributes is stored. The other portions relevant to routing policy of a channel are stored within a ChannelEdgePolicy for each direction of the channel.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel_id | uint64 | optional | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | string | optional |  
last_update | uint32 | optional |  
node1_pub | string | optional |  
node2_pub | string | optional |  
capacity | int64 | optional |  
node1_policy | RoutingPolicy | optional |  
node2_policy | RoutingPolicy | optional |  





# GetChanInfo

### Simple RPC


 GetChanInfo returns the latest authenticated network announcement for the given channel identified by its channel ID: an 8-byte integer which uniquely identifies the location of transaction's funding output within the blockchain.

```shell

# prints out the latest authenticated state for a particular channel

$ lncli getchaninfo [command options] chan_id

# --chan_id value  the 8-byte compact channel ID to query for (default: 0)
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ChanInfoRequest(
        chan_id=<YOUR_PARAM>,
    )
>>> response = stub.GetChanInfo(request)
>>> response

{ 
    channel_id: <uint64>,
    chan_point: <string>,
    last_update: <uint32>,
    node1_pub: <string>,
    node2_pub: <string>,
    capacity: <int64>,
    node1_policy: <RoutingPolicy>,
    node2_policy: <RoutingPolicy>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.getChanInfo({ 
    chan_id: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('GetChanInfo: ' + response);
  })

{ 
    channel_id: <uint64>,
    chan_point: <string>,
    last_update: <uint32>,
    node1_pub: <string>,
    node2_pub: <string>,
    capacity: <int64>,
    node1_policy: <RoutingPolicy>,
    node2_policy: <RoutingPolicy>,
}

```

### gRPC Request: ChanInfoRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
chan_id | uint64 | optional | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 




### gRPC Response: ChannelEdge 

A fully authenticated channel along with all its unique attributes. Once an authenticated channel announcement has been processed on the network, then a instance of ChannelEdgeInfo encapsulating the channels attributes is stored. The other portions relevant to routing policy of a channel are stored within a ChannelEdgePolicy for each direction of the channel.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel_id | uint64 | optional | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | string | optional |  
last_update | uint32 | optional |  
node1_pub | string | optional |  
node2_pub | string | optional |  
capacity | int64 | optional |  
node1_policy | RoutingPolicy | optional |  
node2_policy | RoutingPolicy | optional |  



### RoutingPolicy


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
time_lock_delta | uint32 | optional |  
min_htlc | int64 | optional |  
fee_base_msat | int64 | optional |  
fee_rate_milli_msat | int64 | optional |  


### RoutingPolicy


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
time_lock_delta | uint32 | optional |  
min_htlc | int64 | optional |  
fee_base_msat | int64 | optional |  
fee_rate_milli_msat | int64 | optional |  





# GetNodeInfo

### Simple RPC


 GetNodeInfo returns the latest advertised, aggregated, and authenticated channel information for the specified node identified by its public key.

```shell

# prints out the latest authenticated node state for an advertised node

$ lncli getnodeinfo [command options] [arguments...]

# --pub_key value  the 33-byte hex-encoded compressed public of the target node
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NodeInfoRequest(
        pub_key=<YOUR_PARAM>,
    )
>>> response = stub.GetNodeInfo(request)
>>> response

{ 
    node: <LightningNode>,
    num_channels: <uint32>,
    total_capacity: <int64>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.getNodeInfo({ 
    pub_key: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('GetNodeInfo: ' + response);
  })

{ 
    node: <LightningNode>,
    num_channels: <uint32>,
    total_capacity: <int64>,
}

```

### gRPC Request: NodeInfoRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional | The 33-byte hex-encoded compressed public of the target node 




### gRPC Response: NodeInfo 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
node | LightningNode | optional | An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | uint32 | optional |  
total_capacity | int64 | optional |  



### LightningNode
An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
last_update | uint32 | optional |  
pub_key | string | optional |  
alias | string | optional |  
addresses | NodeAddress | repeated |  





# QueryRoutes

### Simple RPC


 QueryRoutes attempts to query the daemon's Channel Router for a possible route to a target destination capable of carrying a specific amount of satoshis. The retuned route contains the full details required to craft and send an HTLC, also including the necessary information that should be present within the Sphinx packet encapsualted within the HTLC.

```shell

# Queries the channel router for a potential path to the destination that has sufficient flow for the amount including fees

$ lncli queryroutes [command options] dest amt

# --dest value  the 33-byte hex-encoded public key for the payment destination
# --amt value   the amount to send expressed in satoshis (default: 0)
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.QueryRoutesRequest(
        pub_key=<YOUR_PARAM>,
        amt=<YOUR_PARAM>,
    )
>>> response = stub.QueryRoutes(request)
>>> response

{ 
    routes: <Route>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.queryRoutes({ 
    pub_key: <YOUR_PARAM>,
    amt: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('QueryRoutes: ' + response);
  })

{ 
    routes: <Route>,
}

```

### gRPC Request: QueryRoutesRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional | The 33-byte hex-encoded public key for the payment destination 
amt | int64 | optional | The amount to send expressed in satoshis 




### gRPC Response: QueryRoutesResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
routes | Route | repeated |  



### Route
A path through the channel graph which runs over one or more channels in succession. This struct carries all the information required to craft the Sphinx onion packet, and send the payment along the first hop in the path. A route is only selected as valid if all the channels have sufficient capacity to carry the initial payment amount after fees are accounted for.

Field | Type | Label | Description
----- | ---- | ----- | ----------- 
total_time_lock | uint32 | optional | The cumulative (final) time lock across the entire route.  This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment. 
total_fees | int64 | optional | The sum of the fees paid at each hop within the final route.  In the case of a one-hop payment, this value will be zero as we don't need to pay a fee it ourself. 
total_amt | int64 | optional | The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees. 
hops | Hop | repeated | Contains details concerning the specific forwarding details at each hop. 





# GetNetworkInfo

### Simple RPC


 GetNetworkInfo returns some basic stats about the known channel graph from the point of view of the node.

```shell

# returns a set of statistics pertaining to the known channel graph

$ lncli getnetworkinfo [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NetworkInfoRequest()
>>> response = stub.GetNetworkInfo(request)
>>> response

{ 
    graph_diameter: <uint32>,
    avg_out_degree: <double>,
    max_out_degree: <uint32>,
    num_nodes: <uint32>,
    num_channels: <uint32>,
    total_network_capacity: <int64>,
    avg_channel_size: <double>,
    min_channel_size: <int64>,
    max_channel_size: <int64>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.getNetworkInfo({}, function(err, response) {
    console.log('GetNetworkInfo: ' + response);
  })

{ 
    graph_diameter: <uint32>,
    avg_out_degree: <double>,
    max_out_degree: <uint32>,
    num_nodes: <uint32>,
    num_channels: <uint32>,
    total_network_capacity: <int64>,
    avg_channel_size: <double>,
    min_channel_size: <int64>,
    max_channel_size: <int64>,
}

```

### gRPC Request: NetworkInfoRequest 



This request has no parameters.




### gRPC Response: NetworkInfo 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
graph_diameter | uint32 | optional |  
avg_out_degree | double | optional |  
max_out_degree | uint32 | optional |  
num_nodes | uint32 | optional |  
num_channels | uint32 | optional |  
total_network_capacity | int64 | optional |  
avg_channel_size | double | optional |  
min_channel_size | int64 | optional |  
max_channel_size | int64 | optional |  






# StopDaemon

### Simple RPC


 StopDaemon will send a shutdown request to the interrupt handler, triggering a graceful shutdown of the daemon.

```shell

# Gracefully stop all daemon subsystems before stopping the daemon itself. This is equivalent to stopping it using CTRL-C.

$ lncli stop [arguments...]

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.StopRequest()
>>> response = stub.StopDaemon(request)
>>> response
{}
```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.stopDaemon({}, function(err, response) {
    console.log('StopDaemon: ' + response);
  })
{}
```

### gRPC Request: StopRequest 



This request has no parameters.




### gRPC Response: StopResponse 



This response is empty.






# SubscribeChannelGraph

### Response-streaming RPC


SubscribeChannelGraph launches a streaming RPC that allows the caller to receive notifications upon any changes to the channel graph topology from the point of view of the responding node. Events notified include: new nodes coming online, nodes updating their authenticated attributes, new channels being advertised, updates in the routing policy for a directional channel edge, and when channels are closed on-chain.

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GraphTopologySubscription()
>>> for response in stub.SubscribeChannelGraph(request):
    # Do something
    print response

{ 
    node_updates: <NodeUpdate>,
    channel_updates: <ChannelEdgeUpdate>,
    closed_chans: <ClosedChannelUpdate>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials);
> var call = lightning.subscribeChannelGraph({})

> call.on('data', function(message) {
    console.log(message);
  });
> call.on('end', function() {
    // The server has finished sending
    console.log("END");
  });
> call.on('status', function(status) {
    // Process status
    console.log("Current status: " + status);
  });

{ 
    node_updates: <NodeUpdate>,
    channel_updates: <ChannelEdgeUpdate>,
    closed_chans: <ClosedChannelUpdate>,
}

```

### gRPC Request: GraphTopologySubscription 



This request has no parameters.




### gRPC Response: GraphTopologyUpdate (Streaming)



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
node_updates | NodeUpdate | repeated |  
channel_updates | ChannelEdgeUpdate | repeated |  
closed_chans | ClosedChannelUpdate | repeated |  



### NodeUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
addresses | string | repeated |  
identity_key | string | optional |  
global_features | bytes | optional |  
alias | string | optional |  


### ChannelEdgeUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
chan_id | uint64 | optional | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | ChannelPoint | optional |  
capacity | int64 | optional |  
routing_policy | RoutingPolicy | optional |  
advertising_node | string | optional |  
connecting_node | string | optional |  


### ClosedChannelUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
chan_id | uint64 | optional | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
capacity | int64 | optional |  
closed_height | uint32 | optional |  
chan_point | ChannelPoint | optional |  





# SetAlias

### Simple RPC


SetAlias sets the alias for this node; e.g. "alice"

```shell

```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SetAliasRequest(
        new_alias=<YOUR_PARAM>,
    )
>>> response = stub.SetAlias(request)
>>> response
{}
```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.setAlias({ 
    new_alias: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('SetAlias: ' + response);
  })
{}
```

### gRPC Request: SetAliasRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
new_alias | string | optional |  




### gRPC Response: SetAliasResponse 



This response is empty.






# DebugLevel

### Simple RPC


 DebugLevel allows a caller to programmatically set the logging verbosity of lnd. The logging can be targeted according to a coarse daemon-wide logging level, or in a granular fashion to specify the logging for a target sub-system.

```shell

# Logging level for all subsystems {trace, debug, info, warn, error, critical} -- You may also specify <subsystem>=<level>,<subsystem2>=<level>,... to set the log level for individual subsystems -- Use show to list available subsystems

$ lncli debuglevel [command options] [arguments...]

# --show         if true, then the list of available sub-systems will be printed out
# --level value  the level specification to target either a coarse logging level, or granular set of specific sub-systems with logging levels for each
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> cert = open('LND_HOMEDIR/tls.cert').read()
>>> creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.DebugLevelRequest(
        show=<YOUR_PARAM>,
        level_spec=<YOUR_PARAM>,
    )
>>> response = stub.DebugLevel(request)
>>> response

{ 
    sub_systems: <string>,
}

```

```javascript
> var grpc = require('grpc');
> var fs = require('fs');
> var lndCert = fs.readFileSync("LND_HOMEDIR/tls.cert");
> var credentials = grpc.credentials.createSsl(lndCert);
> var lnrpcDescriptor = grpc.load("rpc.proto");
> var lnrpc = lnrpcDescriptor.lnrpc;
> var lightning = new lnrpc.Lightning('localhost:10009', credentials); 
> call = lightning.debugLevel({ 
    show: <YOUR_PARAM>,
    level_spec: <YOUR_PARAM>,
  }, function(err, response) {
    console.log('DebugLevel: ' + response);
  })

{ 
    sub_systems: <string>,
}

```

### gRPC Request: DebugLevelRequest 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
show | bool | optional |  
level_spec | string | optional |  




### gRPC Response: DebugLevelResponse 



Field | Type | Label | Description
----- | ---- | ----- | ----------- 
sub_systems | string | optional |  




