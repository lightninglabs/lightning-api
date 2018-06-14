---
title: LND gRPC API Reference

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

The original `rpc.proto` file from which the gRPC documentation was generated
can be found [here](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

Alternatively, the REST documentation can be found [here](./rest).


# GenSeed


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
>>> request = ln.GenSeedRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    aezeed_passphrase: <bytes>, 
    seed_entropy: <bytes>, 
  } 
> walletUnlocker.genSeed(request, function(err, response) {
    console.log(response);
  })
{ 
    "cipher_seed_mnemonic": <array string>,
    "enciphered_seed": <bytes>,
}
```

### gRPC Request: GenSeedRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. 
seed_entropy | bytes | seed_entropy is an optional 16-bytes generated via CSPRNG. If not specified, then a fresh set of randomness will be used to create the seed.  
### gRPC Response: GenSeedResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed. 
enciphered_seed | bytes | enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.  

# InitWallet


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
>>> request = ln.InitWalletRequest(
        wallet_password=<bytes>,
        cipher_seed_mnemonic=<array string>,
        aezeed_passphrase=<bytes>,
        recovery_window=<int32>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    wallet_password: <bytes>, 
    cipher_seed_mnemonic: <array string>, 
    aezeed_passphrase: <bytes>, 
    recovery_window: <int32>, 
  } 
> walletUnlocker.initWallet(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: InitWalletRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon. 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed. 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each invdividual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.  
### gRPC Response: InitWalletResponse 


This response has no parameters.


# UnlockWallet


### Simple RPC


UnlockWallet is used at startup of lnd to provide a password to unlock the wallet database.

```shell

# The unlock command is used to decrypt lnd's wallet state in order to
# start up. This command MUST be run after booting up lnd before it's
# able to carry out its duties. An exception is if a user is running with
# --noencryptwallet, then a default passphrase will be used.

$ lncli unlock [command options] [arguments...]

# --recovery_window value  address lookahead to resume recovery rescan, value should be non-zero --  To recover all funds, this should be greater than the maximum number of consecutive, unused addresses ever generated by the wallet. (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.WalletUnlockerStub(channel)
>>> request = ln.UnlockWalletRequest(
        wallet_password=<bytes>,
        recovery_window=<int32>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    wallet_password: <bytes>, 
    recovery_window: <int32>, 
  } 
> walletUnlocker.unlockWallet(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: UnlockWalletRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each invdividual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.  
### gRPC Response: UnlockWalletResponse 


This response has no parameters.


# ChangePassword


### Simple RPC


ChangePassword changes the password of the encrypted wallet. This will automatically unlock the wallet database if successful.

```shell

# The changepassword command is used to Change lnd's encrypted wallet's
# password. It will automatically unlock the daemon if the password change
# is successful.
# If one did not specify a password for their wallet (running lnd with
# --noencryptwallet), one must restart their daemon without
# --noencryptwallet and use this command. The "current password" field
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
>>> request = ln.ChangePasswordRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var walletUnlocker = new lnrpc.WalletUnlocker('localhost:10009', sslCreds);
> var request = { 
    current_password: <bytes>, 
    new_password: <bytes>, 
  } 
> walletUnlocker.changePassword(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: ChangePasswordRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
current_password | bytes | current_password should be the current valid passphrase used to unlock the daemon. 
new_password | bytes | new_password should be the new passphrase that will be needed to unlock the daemon.  
### gRPC Response: ChangePasswordResponse 


This response has no parameters.


# WalletBalance


### Simple RPC


WalletBalance returns total unspent outputs(confirmed and unconfirmed), all confirmed unspent outputs and all unconfirmed unspent outputs under control of the wallet.

```shell

# Compute and display the wallet's current balance.

$ lncli walletbalance [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.WalletBalanceRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.walletBalance(request, function(err, response) {
    console.log(response);
  })
{ 
    "total_balance": <int64>,
    "confirmed_balance": <int64>,
    "unconfirmed_balance": <int64>,
}
```

### gRPC Request: WalletBalanceRequest 


This request has no parameters.

### gRPC Response: WalletBalanceResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
total_balance | int64 | The balance of the wallet 
confirmed_balance | int64 | The confirmed balance of a wallet(with >= 1 confirmations) 
unconfirmed_balance | int64 | The unconfirmed balance of a wallet(with 0 confirmations)  

# ChannelBalance


### Simple RPC


ChannelBalance returns the total funds available across all open channels in satoshis.

```shell

# Returns the sum of the total available channel balance across all open channels.

$ lncli channelbalance [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ChannelBalanceRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.channelBalance(request, function(err, response) {
    console.log(response);
  })
{ 
    "balance": <int64>,
    "pending_open_balance": <int64>,
}
```

### gRPC Request: ChannelBalanceRequest 


This request has no parameters.

### gRPC Response: ChannelBalanceResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
balance | int64 | Sum of channels balances denominated in satoshis 
pending_open_balance | int64 | Sum of channels pending balances denominated in satoshis  

# GetTransactions


### Simple RPC


GetTransactions returns a list describing all the known transactions relevant to the wallet.

```shell

# List all transactions an address of the wallet was involved in.

$ lncli listchaintxns [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GetTransactionsRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.getTransactions(request, function(err, response) {
    console.log(response);
  })
{ 
    "transactions": <array Transaction>,
}
```

### gRPC Request: GetTransactionsRequest 


This request has no parameters.

### gRPC Response: TransactionDetails 


Parameter | Type | Description
--------- | ---- | ----------- 
transactions | [array Transaction](#transaction) | The list of transactions relevant to the wallet.  

# SendCoins


### Simple RPC


SendCoins executes a request to send coins to a particular address. Unlike SendMany, this RPC call only allows creating a single output at a time. If neither target_conf, or sat_per_byte are set, then the internal wallet will consult its fee model to determine a fee for the default confirmation target.

```shell

# Send amt coins in satoshis to the BASE58 encoded bitcoin address addr.
# Fees used when sending the transaction can be specified via the --conf_target, or
# --sat_per_byte optional flags.
# Positional arguments and flags can be used interchangeably but not at the same time!

$ lncli sendcoins [command options] addr amt

# --addr value          the BASE58 encoded bitcoin address to send coins to on-chain
# --amt value           the number of bitcoin denominated in satoshis to send (default: 0)
# --conf_target value   (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value  (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendCoinsRequest(
        addr=<string>,
        amount=<int64>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
> lightning.sendCoins(request, function(err, response) {
    console.log(response);
  })
{ 
    "txid": <string>,
}
```

### gRPC Request: SendCoinsRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
addr | string | The address to send coins to 
amount | int64 | The amount in satoshis to send 
target_conf | int32 | The target number of blocks that this transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the transaction.  
### gRPC Response: SendCoinsResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The transaction ID of the transaction  

# SubscribeTransactions


### Response-streaming RPC


SubscribeTransactions creates a uni-directional stream from the server to the client in which any newly discovered transactions relevant to the wallet are sent over.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GetTransactionsRequest()
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
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
}
```

### gRPC Request: GetTransactionsRequest 


This request has no parameters.

### gRPC Response: Transaction (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
tx_hash | string | The transaction hash 
amount | int64 | The transaction ammount, denominated in satoshis 
num_confirmations | int32 | The number of confirmations 
block_hash | string | The hash of the block this transaction was included in 
block_height | int32 | The height of the block this transaction was included in 
time_stamp | int64 | Timestamp of this transaction 
total_fees | int64 | Fees paid for this transaction 
dest_addresses | array string | Addresses that received funds for this transaction  

# SendMany


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendManyRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    AddrToAmount: <array AddrToAmountEntry>, 
    target_conf: <int32>, 
    sat_per_byte: <int64>, 
  } 
> lightning.sendMany(request, function(err, response) {
    console.log(response);
  })
{ 
    "txid": <string>,
}
```

### gRPC Request: SendManyRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
AddrToAmount | [array AddrToAmountEntry](#addrtoamountentry) | The map from addresses to amounts 
target_conf | int32 | The target number of blocks that this transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the transaction.  
### gRPC Response: SendManyResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The id of the transaction  

# NewAddress


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NewAddressRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    type: <AddressType>, 
  } 
> lightning.newAddress(request, function(err, response) {
    console.log(response);
  })
{ 
    "address": <string>,
}
```

### gRPC Request: NewAddressRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
type | [AddressType](#addresstype) | The address type  
### gRPC Response: NewAddressResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
address | string | The newly generated wallet address  

# NewWitnessAddress


### Simple RPC


NewWitnessAddress creates a new witness address under control of the local wallet.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NewWitnessAddressRequest()
>>> response = stub.NewWitnessAddress(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "address": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.newWitnessAddress(request, function(err, response) {
    console.log(response);
  })
{ 
    "address": <string>,
}
```

### gRPC Request: NewWitnessAddressRequest 


This request has no parameters.

### gRPC Response: NewAddressResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
address | string | The newly generated wallet address  

# SignMessage


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SignMessageRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    msg: <bytes>, 
  } 
> lightning.signMessage(request, function(err, response) {
    console.log(response);
  })
{ 
    "signature": <string>,
}
```

### gRPC Request: SignMessageRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message to be signed  
### gRPC Response: SignMessageResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
signature | string | The signature for the given message  

# VerifyMessage


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.VerifyMessageRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    msg: <bytes>, 
    signature: <string>, 
  } 
> lightning.verifyMessage(request, function(err, response) {
    console.log(response);
  })
{ 
    "valid": <bool>,
    "pubkey": <string>,
}
```

### gRPC Request: VerifyMessageRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message over which the signature is to be verified 
signature | string | The signature to be verified over the given message  
### gRPC Response: VerifyMessageResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
valid | bool | Whether the signature was valid over the given message 
pubkey | string | The pubkey recovered from the signature  

# ConnectPeer


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ConnectPeerRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    addr: <LightningAddress>, 
    perm: <bool>, 
  } 
> lightning.connectPeer(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: ConnectPeerRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
addr | [LightningAddress](#lightningaddress) | Lightning address of the peer, in the format `<pubkey>@host` 
perm | bool | If set, the daemon will attempt to persistently connect to the target peer.  Otherwise, the call will be synchronous.  
### gRPC Response: ConnectPeerResponse 


This response has no parameters.


# DisconnectPeer


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.DisconnectPeerRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pub_key: <string>, 
  } 
> lightning.disconnectPeer(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: DisconnectPeerRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The pubkey of the node to disconnect from  
### gRPC Response: DisconnectPeerResponse 


This response has no parameters.


# ListPeers


### Simple RPC


ListPeers returns a verbose listing of all currently active peers.

```shell

# List all active, currently connected peers.

$ lncli listpeers [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListPeersRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.listPeers(request, function(err, response) {
    console.log(response);
  })
{ 
    "peers": <array Peer>,
}
```

### gRPC Request: ListPeersRequest 


This request has no parameters.

### gRPC Response: ListPeersResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
peers | [array Peer](#peer) | The list of currently connected peers  

# GetInfo


### Simple RPC


GetInfo returns general information concerning the lightning node including it's identity pubkey, alias, the chains it is connected to, and information concerning the number of open+pending channels.

```shell

# Returns basic information related to the active daemon.

$ lncli getinfo [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GetInfoRequest()
>>> response = stub.GetInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "identity_pubkey": <string>,
    "alias": <string>,
    "num_pending_channels": <uint32>,
    "num_active_channels": <uint32>,
    "num_peers": <uint32>,
    "block_height": <uint32>,
    "block_hash": <string>,
    "synced_to_chain": <bool>,
    "testnet": <bool>,
    "chains": <array string>,
    "uris": <array string>,
    "best_header_timestamp": <int64>,
    "version": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.getInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "identity_pubkey": <string>,
    "alias": <string>,
    "num_pending_channels": <uint32>,
    "num_active_channels": <uint32>,
    "num_peers": <uint32>,
    "block_height": <uint32>,
    "block_hash": <string>,
    "synced_to_chain": <bool>,
    "testnet": <bool>,
    "chains": <array string>,
    "uris": <array string>,
    "best_header_timestamp": <int64>,
    "version": <string>,
}
```

### gRPC Request: GetInfoRequest 


This request has no parameters.

### gRPC Response: GetInfoResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
identity_pubkey | string | The identity pubkey of the current node. 
alias | string | If applicable, the alias of the current node, e.g. "bob" 
num_pending_channels | uint32 | Number of pending channels 
num_active_channels | uint32 | Number of active channels 
num_peers | uint32 | Number of peers 
block_height | uint32 | The node's current view of the height of the best block 
block_hash | string | The node's current view of the hash of the best block 
synced_to_chain | bool | Whether the wallet's view is synced to the main chain 
testnet | bool | Whether the current node is connected to testnet 
chains | array string | A list of active chains the node is connected to 
uris | array string | The URIs of the current node. 
best_header_timestamp | int64 | Timestamp of the block best known to the wallet 
version | string | The version of the LND software that the node is running.  

# PendingChannels


### Simple RPC


PendingChannels returns a list of all the channels that are currently considered "pending". A channel is pending if it has finished the funding workflow and is waiting for confirmations for the funding txn, or is in the process of closure, either initiated cooperatively or non-cooperatively.

```shell

# Display information pertaining to pending channels.

$ lncli pendingchannels [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PendingChannelsRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
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

### gRPC Request: PendingChannelsRequest 


This request has no parameters.

### gRPC Response: PendingChannelsResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
total_limbo_balance | int64 | The balance in satoshis encumbered in pending channels 
pending_open_channels | [array PendingOpenChannel](#pendingopenchannel) | Channels pending opening 
pending_closing_channels | [array ClosedChannel](#closedchannel) | Channels pending closing 
pending_force_closing_channels | [array ForceClosedChannel](#forceclosedchannel) | Channels pending force closing 
waiting_close_channels | [array WaitingCloseChannel](#waitingclosechannel) | Channels waiting for closing tx to confirm  

# ListChannels


### Simple RPC


ListChannels returns a description of all the open channels that this node is a participant in.

```shell

# List all open channels.

$ lncli listchannels [command options] [arguments...]

# --active_only    only list channels which are currently active
# --inactive_only  only list channels which are currently inactive
# --public_only    only list channels which are currently public
# --private_only   only list channels which are currently private
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListChannelsRequest(
        active_only=<bool>,
        inactive_only=<bool>,
        public_only=<bool>,
        private_only=<bool>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
> lightning.listChannels(request, function(err, response) {
    console.log(response);
  })
{ 
    "channels": <array Channel>,
}
```

### gRPC Request: ListChannelsRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
active_only | bool |  
inactive_only | bool |  
public_only | bool |  
private_only | bool |   
### gRPC Response: ListChannelsResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array Channel](#channel) | The list of active channels  

# ClosedChannels


### Simple RPC


ClosedChannels returns a description of all the closed channels that  this node was a participant in.

```shell

# List all closed channels.

$ lncli closedchannels [command options] [arguments...]

# --cooperative       list channels that were closed cooperatively
# --local_force       list channels that were force-closed by the local node
# --remote_force      list channels that were force-closed by the remote node
# --breach            list channels for which the remote node attempted to broadcast a prior revoked channel state
# --funding_canceled  list channels that were never fully opened
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ClosedChannelsRequest(
        cooperative=<bool>,
        local_force=<bool>,
        remote_force=<bool>,
        breach=<bool>,
        funding_canceled=<bool>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
> lightning.closedChannels(request, function(err, response) {
    console.log(response);
  })
{ 
    "channels": <array ChannelCloseSummary>,
}
```

### gRPC Request: ClosedChannelsRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
cooperative | bool |  
local_force | bool |  
remote_force | bool |  
breach | bool |  
funding_canceled | bool |   
### gRPC Response: ClosedChannelsResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array ChannelCloseSummary](#channelclosesummary) |   

# OpenChannelSync


### Simple RPC


OpenChannelSync is a synchronous version of the OpenChannel RPC call. This call is meant to be consumed by clients to the REST proxy. As with all other sync calls, all byte slices are intended to be populated as hex encoded strings.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.OpenChannelRequest(
        node_pubkey=<bytes>,
        node_pubkey_string=<string>,
        local_funding_amount=<int64>,
        push_sat=<int64>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
        private=<bool>,
        min_htlc_msat=<int64>,
        remote_csv_delay=<uint32>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
> lightning.openChannelSync(request, function(err, response) {
    console.log(response);
  })
{ 
    "funding_txid_bytes": <bytes>,
    "funding_txid_str": <string>,
    "output_index": <uint32>,
}
```

### gRPC Request: OpenChannelRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node to open a channel with 
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with 
local_funding_amount | int64 | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | The number of satoshis to push to the remote side as part of the initial commitment state 
target_conf | int32 | The target number of blocks that the funding transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the funding transaction. 
private | bool | Whether this channel should be private, not announced to the greater network. 
min_htlc_msat | int64 | The minimum value in millisatoshi we will require for incoming HTLCs on the channel. 
remote_csv_delay | uint32 | The delay we require on the remote's commitment transaction. If this is not set, it will be scaled automatically with the channel size.  
### gRPC Response: ChannelPoint 


Parameter | Type | Description
--------- | ---- | ----------- 
funding_txid_bytes | bytes | Txid of the funding transaction 
funding_txid_str | string | Hex-encoded string representing the funding transaction 
output_index | uint32 | The index of the output of the funding transaction  

# OpenChannel


### Response-streaming RPC


OpenChannel attempts to open a singly funded channel specified in the request to a remote peer. Users are able to specify a target number of blocks that the funding transaction should be confirmed in, or a manual fee rate to us for the funding transaction. If neither are specified, then a lax block confirmation target is used.

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
# One can manually set the fee to be used for the funding transaction via either
# the --conf_target or --sat_per_byte arguments. This is optional.

$ lncli openchannel [command options] node-key local-amt push-amt

# --node_key value          the identity public key of the target node/peer serialized in compressed format
# --connect value           (optional) the host:port of the target node
# --local_amt value         the number of satoshis the wallet should commit to the channel (default: 0)
# --push_amt value          the number of satoshis to push to the remote side as part of the initial commitment state (default: 0)
# --block                   block and wait until the channel is fully open
# --conf_target value       (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value      (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
# --private                 make the channel private, such that it won't be announced to the greater network, and nodes other than the two channel endpoints must be explicitly told about it to be able to route through it
# --min_htlc_msat value     (optional) the minimum value we will require for incoming HTLCs on the channel (default: 0)
# --remote_csv_delay value  (optional) the number of blocks we will require our channel counterparty to wait before accessing its funds in case of unilateral close. If this is not set, we will scale the value according to the channel size (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.OpenChannelRequest(
        node_pubkey=<bytes>,
        node_pubkey_string=<string>,
        local_funding_amount=<int64>,
        push_sat=<int64>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
        private=<bool>,
        min_htlc_msat=<int64>,
        remote_csv_delay=<uint32>,
    )
>>> for response in stub.OpenChannel(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "chan_pending": <PendingUpdate>,
    "confirmation": <ConfirmationUpdate>,
    "chan_open": <ChannelOpenUpdate>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
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
    "confirmation": <ConfirmationUpdate>,
    "chan_open": <ChannelOpenUpdate>,
}
```

### gRPC Request: OpenChannelRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node to open a channel with 
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with 
local_funding_amount | int64 | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | The number of satoshis to push to the remote side as part of the initial commitment state 
target_conf | int32 | The target number of blocks that the funding transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the funding transaction. 
private | bool | Whether this channel should be private, not announced to the greater network. 
min_htlc_msat | int64 | The minimum value in millisatoshi we will require for incoming HTLCs on the channel. 
remote_csv_delay | uint32 | The delay we require on the remote's commitment transaction. If this is not set, it will be scaled automatically with the channel size.  
### gRPC Response: OpenStatusUpdate (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
chan_pending | [PendingUpdate](#pendingupdate) |  
confirmation | [ConfirmationUpdate](#confirmationupdate) |  
chan_open | [ChannelOpenUpdate](#channelopenupdate) |   

# CloseChannel


### Response-streaming RPC


CloseChannel attempts to close an active channel identified by its channel outpoint (ChannelPoint). The actions of this method can additionally be augmented to attempt a force close after a timeout period in the case of an inactive peer. If a non-force close (cooperative closure) is requested, then the user can specify either a target number of blocks until the closure transaction is confirmed, or a manual fee rate. If neither are specified, then a default lax, block confirmation target is used.

```shell

# Close an existing channel. The channel can be closed either cooperatively,
# or unilaterally (--force).
# A unilateral channel closure means that the latest commitment
# transaction will be broadcast to the network. As a result, any settled
# funds will be time locked for a few blocks before they can be spent.
# In the case of a cooperative closure, One can manually set the fee to
# be used for the closing transaction via either the --conf_target or
# --sat_per_byte arguments. This will be the starting value used during
# fee negotiation. This is optional.
# To view which funding_txids/output_indexes can be used for a channel close,
# see the channel_point values within the listchannels command output.
# The format for a channel_point is 'funding_txid:output_index'.

$ lncli closechannel [command options] funding_txid [output_index [time_limit]]

# --funding_txid value  the txid of the channel's funding transaction
# --output_index value  the output index for the funding output of the funding transaction (default: 0)
# --time_limit value    a relative deadline afterwhich the attempt should be abandoned
# --force               after the time limit has passed, attempt an uncooperative closure
# --block               block until the channel is closed
# --conf_target value   (optional) the number of blocks that the transaction *should* confirm in, will be used for fee estimation (default: 0)
# --sat_per_byte value  (optional) a manual fee expressed in sat/byte that should be used when crafting the transaction (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.CloseChannelRequest(
        channel_point=<ChannelPoint>,
        force=<bool>,
        target_conf=<int32>,
        sat_per_byte=<int64>,
    )
>>> for response in stub.CloseChannel(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "close_pending": <PendingUpdate>,
    "confirmation": <ConfirmationUpdate>,
    "chan_close": <ChannelCloseUpdate>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
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
    "confirmation": <ConfirmationUpdate>,
    "chan_close": <ChannelCloseUpdate>,
}
```

### gRPC Request: CloseChannelRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
force | bool | If true, then the channel will be closed forcibly. This means the current commitment transaction will be signed and broadcast. 
target_conf | int32 | The target number of blocks that the closure transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the closure transaction.  
### gRPC Response: CloseStatusUpdate (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
close_pending | [PendingUpdate](#pendingupdate) |  
confirmation | [ConfirmationUpdate](#confirmationupdate) |  
chan_close | [ChannelCloseUpdate](#channelcloseupdate) |   

# SendPayment


### Bidirectional-streaming RPC


SendPayment dispatches a bi-directional streaming RPC for sending payments through the Lightning Network. A single RPC invocation creates a persistent bi-directional stream allowing clients to rapidly send payments through the Lightning Network with a single persistent connection.

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
# The --debug_send flag is provided for usage *purely* in test
# environments. If specified, then the payment hash isn't required, as
# it'll use the hash of all zeroes. This mode allows one to quickly test
# payment connectivity without having to create an invoice at the
# destination.

$ lncli sendpayment [command options] dest amt payment_hash final_cltv_delta | --pay_req=[payment request]

# --dest value, -d value          the compressed identity pubkey of the payment recipient
# --amt value, -a value           number of satoshis to send (default: 0)
# --fee_limit value               maximum fee allowed in satoshis when sendingthe payment (default: 0)
# --fee_limit_percent value       percentage of the payment's amount used as themaximum fee allowed when sending the payment (default: 0)
# --payment_hash value, -r value  the hash to use within the payment's HTLC
# --debug_send                    use the debug rHash when sending the HTLC
# --pay_req value                 a zpay32 encoded payment request to fulfill
# --final_cltv_delta value        the number of blocks the last hop has to reveal the preimage (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
# Define a generator that returns an Iterable of SendRequest objects.
>>> def request_generator():
        # Initialization code here.
        while True:
            # Parameters here can be set as arguments to the generator.
            request = ln.SendRequest(
                dest=<bytes>,
                dest_string=<string>,
                amt=<int64>,
                payment_hash=<bytes>,
                payment_hash_string=<string>,
                payment_request=<string>,
                final_cltv_delta=<int32>,
                fee_limit=<FeeLimit>,
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    dest: <bytes>, 
    dest_string: <string>, 
    amt: <int64>, 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    payment_request: <string>, 
    final_cltv_delta: <int32>, 
    fee_limit: <FeeLimit>, 
  } 
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
}
```

### gRPC Request: SendRequest (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient 
dest_string | string | The hex-encoded identity pubkey of the payment recipient 
amt | int64 | Number of satoshis to send. 
payment_hash | bytes | The hash to use within the payment's HTLC 
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.  
### gRPC Response: SendResponse (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |   

# SendPaymentSync


### Simple RPC


SendPaymentSync is the synchronous non-streaming version of SendPayment. This RPC is intended to be consumed by clients of the REST proxy. Additionally, this RPC expects the destination's public key and the payment hash (if any) to be encoded as hex strings.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendRequest(
        dest=<bytes>,
        dest_string=<string>,
        amt=<int64>,
        payment_hash=<bytes>,
        payment_hash_string=<string>,
        payment_request=<string>,
        final_cltv_delta=<int32>,
        fee_limit=<FeeLimit>,
    )
>>> response = stub.SendPaymentSync(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    dest: <bytes>, 
    dest_string: <string>, 
    amt: <int64>, 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    payment_request: <string>, 
    final_cltv_delta: <int32>, 
    fee_limit: <FeeLimit>, 
  } 
> lightning.sendPaymentSync(request, function(err, response) {
    console.log(response);
  })
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
}
```

### gRPC Request: SendRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient 
dest_string | string | The hex-encoded identity pubkey of the payment recipient 
amt | int64 | Number of satoshis to send. 
payment_hash | bytes | The hash to use within the payment's HTLC 
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.  
### gRPC Response: SendResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |   

# SendToRoute


### Bidirectional-streaming RPC


SendToRoute is a bi-directional streaming RPC for sending payment through the Lightning Network. This method differs from SendPayment in that it allows users to specify a full route manually. This can be used for things like rebalancing, and atomic swaps.

```shell

# Send a payment over Lightning using a specific route. One must specify
# a list of routes to attempt and the payment hash. This command can even
# be chained with the response to queryroutes. This command can be used
# to implement channel rebalancing by crafting a self-route, or even
# atomic swaps using a self-route that crosses multiple chains.
# There are three ways to specify routes:
# * using the --routes parameter to manually specify a JSON encoded
# set of routes in the format of the return value of queryroutes:
# (lncli sendtoroute --payment_hash=<pay_hash> --routes=<route>)
# * passing the routes as a positional argument:
# (lncli sendtoroute --payment_hash=pay_hash <route>)
# * or reading in the routes from stdin, which can allow chaining the
# response from queryroutes, or even read in a file with a set of
# pre-computed routes:
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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
# Define a generator that returns an Iterable of SendToRouteRequest objects.
>>> def request_generator():
        # Initialization code here.
        while True:
            # Parameters here can be set as arguments to the generator.
            request = ln.SendToRouteRequest(
                payment_hash=<bytes>,
                payment_hash_string=<string>,
                routes=<array Route>,
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    routes: <array Route>, 
  } 
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
}
```

### gRPC Request: SendToRouteRequest (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. 
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC. 
routes | [array Route](#route) | The set of routes that should be used to attempt to complete the payment.  
### gRPC Response: SendResponse (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |   

# SendToRouteSync


### Simple RPC


SendToRouteSync is a synchronous version of SendToRoute. It Will block until the payment either fails or succeeds.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.SendToRouteRequest(
        payment_hash=<bytes>,
        payment_hash_string=<string>,
        routes=<array Route>,
    )
>>> response = stub.SendToRouteSync(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    payment_hash: <bytes>, 
    payment_hash_string: <string>, 
    routes: <array Route>, 
  } 
> lightning.sendToRouteSync(request, function(err, response) {
    console.log(response);
  })
{ 
    "payment_error": <string>,
    "payment_preimage": <bytes>,
    "payment_route": <Route>,
}
```

### gRPC Request: SendToRouteRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. 
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC. 
routes | [array Route](#route) | The set of routes that should be used to attempt to complete the payment.  
### gRPC Response: SendResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |   

# AddInvoice


### Simple RPC


AddInvoice attempts to add a new invoice to the invoice database. Any duplicated invoices are rejected, therefore all invoices *must* have a unique payment preimage.

```shell

# Add a new invoice, expressing intent for a future payment.
# Invoices without an amount can be created by not supplying any
# parameters or providing an amount of 0. These invoices allow the payee
# to specify the amount of satoshis they wish to send.

$ lncli addinvoice [command options] value preimage

# --memo value              a description of the payment to attach along with the invoice (default="")
# --receipt value           an optional cryptographic receipt of payment
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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.Invoice(
        memo=<string>,
        receipt=<bytes>,
        r_preimage=<bytes>,
        r_hash=<bytes>,
        value=<int64>,
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
    )
>>> response = stub.AddInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "r_hash": <bytes>,
    "payment_request": <string>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    memo: <string>, 
    receipt: <bytes>, 
    r_preimage: <bytes>, 
    r_hash: <bytes>, 
    value: <int64>, 
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
  } 
> lightning.addInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
    "r_hash": <bytes>,
    "payment_request": <string>,
}
```

### gRPC Request: Invoice 


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
receipt | bytes | An optional cryptographic receipt of payment 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | The hash of the preimage 
value | int64 | The value of this invoice in satoshis 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels.  
### gRPC Response: AddInvoiceResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash | bytes |  
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.  

# ListInvoices


### Simple RPC


ListInvoices returns a list of all the invoices currently stored within the database. Any active debug invoices are ignored.

```shell

# List all invoices currently stored.

$ lncli listinvoices [command options] [arguments...]

# --pending_only  toggles if all invoices should be returned, or only those that are currently unsettled
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListInvoiceRequest(
        pending_only=<bool>,
    )
>>> response = stub.ListInvoices(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "invoices": <array Invoice>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pending_only: <bool>, 
  } 
> lightning.listInvoices(request, function(err, response) {
    console.log(response);
  })
{ 
    "invoices": <array Invoice>,
}
```

### gRPC Request: ListInvoiceRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
pending_only | bool | Toggles if all invoices should be returned, or only those that are currently unsettled.  
### gRPC Response: ListInvoiceResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
invoices | [array Invoice](#invoice) |   

# LookupInvoice


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PaymentHash(
        r_hash_str=<string>,
        r_hash=<bytes>,
    )
>>> response = stub.LookupInvoice(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "memo": <string>,
    "receipt": <bytes>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    r_hash_str: <string>, 
    r_hash: <bytes>, 
  } 
> lightning.lookupInvoice(request, function(err, response) {
    console.log(response);
  })
{ 
    "memo": <string>,
    "receipt": <bytes>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
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
}
```

### gRPC Request: PaymentHash 


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash_str | string | The hex-encoded payment hash of the invoice to be looked up. The passed payment hash must be exactly 32 bytes, otherwise an error is returned. 
r_hash | bytes | The payment hash of the invoice to be looked up.  
### gRPC Response: Invoice 


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
receipt | bytes | An optional cryptographic receipt of payment 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | The hash of the preimage 
value | int64 | The value of this invoice in satoshis 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels.  

# SubscribeInvoices


### Response-streaming RPC


SubscribeInvoices returns a uni-directional stream (sever -> client) for notifying the client of newly added/settled invoices.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.InvoiceSubscription()
>>> for response in stub.SubscribeInvoices(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "memo": <string>,
    "receipt": <bytes>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
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
    "receipt": <bytes>,
    "r_preimage": <bytes>,
    "r_hash": <bytes>,
    "value": <int64>,
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
}
```

### gRPC Request: InvoiceSubscription 


This request has no parameters.

### gRPC Response: Invoice (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
receipt | bytes | An optional cryptographic receipt of payment 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | The hash of the preimage 
value | int64 | The value of this invoice in satoshis 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels.  

# DecodePayReq


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PayReqString(
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pay_req: <string>, 
  } 
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
}
```

### gRPC Request: PayReqString 


Parameter | Type | Description
--------- | ---- | ----------- 
pay_req | string | The payment request string to be decoded  
### gRPC Response: PayReq 


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

# ListPayments


### Simple RPC


ListPayments returns a list of all outgoing payments.

```shell

# List all outgoing payments.

$ lncli listpayments [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ListPaymentsRequest()
>>> response = stub.ListPayments(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "payments": <array Payment>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.listPayments(request, function(err, response) {
    console.log(response);
  })
{ 
    "payments": <array Payment>,
}
```

### gRPC Request: ListPaymentsRequest 


This request has no parameters.

### gRPC Response: ListPaymentsResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
payments | [array Payment](#payment) | The list of payments  

# DeleteAllPayments


### Simple RPC


DeleteAllPayments deletes all outgoing payments from DB.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.DeleteAllPaymentsRequest()
>>> response = stub.DeleteAllPayments(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.deleteAllPayments(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: DeleteAllPaymentsRequest 


This request has no parameters.

### gRPC Response: DeleteAllPaymentsResponse 


This response has no parameters.


# DescribeGraph


### Simple RPC


DescribeGraph returns a description of the latest graph state from the point of view of the node. The graph information is partitioned into two components: all the nodes/vertexes, and all the edges that connect the vertexes themselves.  As this is a directed graph, the edges also contain the node directional specific routing policy which includes: the time lock delta, fee information, etc.

```shell

# Prints a human readable version of the known channel graph from the PoV of the node

$ lncli describegraph [command options] [arguments...]

# --render  If set, then an image of graph will be generated and displayed. The generated image is stored within the current directory with a file name of 'graph.svg'
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ChannelGraphRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.describeGraph(request, function(err, response) {
    console.log(response);
  })
{ 
    "nodes": <array LightningNode>,
    "edges": <array ChannelEdge>,
}
```

### gRPC Request: ChannelGraphRequest 


This request has no parameters.

### gRPC Response: ChannelGraph 


Parameter | Type | Description
--------- | ---- | ----------- 
nodes | [array LightningNode](#lightningnode) | The list of `LightningNode`s in this channel graph 
edges | [array ChannelEdge](#channeledge) | The list of `ChannelEdge`s in this channel graph  

# GetChanInfo


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ChanInfoRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    chan_id: <uint64>, 
  } 
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

### gRPC Request: ChanInfoRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.  
### gRPC Response: ChannelEdge 


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

# GetNodeInfo


### Simple RPC


GetNodeInfo returns the latest advertised, aggregated, and authenticated channel information for the specified node identified by its public key.

```shell

# Prints out the latest authenticated node state for an advertised node

$ lncli getnodeinfo [command options] [arguments...]

# --pub_key value  the 33-byte hex-encoded compressed public of the target node
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NodeInfoRequest(
        pub_key=<string>,
    )
>>> response = stub.GetNodeInfo(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "node": <LightningNode>,
    "num_channels": <uint32>,
    "total_capacity": <int64>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pub_key: <string>, 
  } 
> lightning.getNodeInfo(request, function(err, response) {
    console.log(response);
  })
{ 
    "node": <LightningNode>,
    "num_channels": <uint32>,
    "total_capacity": <int64>,
}
```

### gRPC Request: NodeInfoRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded compressed public of the target node  
### gRPC Response: NodeInfo 


Parameter | Type | Description
--------- | ---- | ----------- 
node | [LightningNode](#lightningnode) | An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | uint32 |  
total_capacity | int64 |   

# QueryRoutes


### Simple RPC


QueryRoutes attempts to query the daemon's Channel Router for a possible route to a target destination capable of carrying a specific amount of satoshis. The retuned route contains the full details required to craft and send an HTLC, also including the necessary information that should be present within the Sphinx packet encapsulated within the HTLC.

```shell

# Queries the channel router for a potential path to the destination that has sufficient flow for the amount including fees

$ lncli queryroutes [command options] dest amt

# --dest value               the 33-byte hex-encoded public key for the payment destination
# --amt value                the amount to send expressed in satoshis (default: 0)
# --fee_limit value          maximum fee allowed in satoshis when sendingthe payment (default: 0)
# --fee_limit_percent value  percentage of the payment's amount used as themaximum fee allowed when sending the payment (default: 0)
# --num_max_routes value     the max number of routes to be returned (default: 10) (default: 10)
# --final_cltv_delta value   (optional) number of blocks the last hop has to reveal the preimage (default: 0)
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.QueryRoutesRequest(
        pub_key=<string>,
        amt=<int64>,
        num_routes=<int32>,
        final_cltv_delta=<int32>,
        fee_limit=<FeeLimit>,
    )
>>> response = stub.QueryRoutes(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
    "routes": <array Route>,
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    pub_key: <string>, 
    amt: <int64>, 
    num_routes: <int32>, 
    final_cltv_delta: <int32>, 
    fee_limit: <FeeLimit>, 
  } 
> lightning.queryRoutes(request, function(err, response) {
    console.log(response);
  })
{ 
    "routes": <array Route>,
}
```

### gRPC Request: QueryRoutesRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded public key for the payment destination 
amt | int64 | The amount to send expressed in satoshis 
num_routes | int32 | The max number of routes to return. 
final_cltv_delta | int32 | An optional CLTV delta from the current height that should be used for the timelock of the final hop 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.  
### gRPC Response: QueryRoutesResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
routes | [array Route](#route) |   

# GetNetworkInfo


### Simple RPC


GetNetworkInfo returns some basic stats about the known channel graph from the point of view of the node.

```shell

# Returns a set of statistics pertaining to the known channel graph

$ lncli getnetworkinfo [arguments...]

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.NetworkInfoRequest()
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
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
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
}
```

### gRPC Request: NetworkInfoRequest 


This request has no parameters.

### gRPC Response: NetworkInfo 


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

# StopDaemon


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.StopRequest()
>>> response = stub.StopDaemon(request, metadata=[('macaroon'), macaroon)])
>>> print(response)
{ 
}
```
```javascript
> var fs = require('fs');
> var grpc = require('grpc');
> var lnrpc = grpc.load('rpc.proto').lnrpc;
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
> lightning.stopDaemon(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: StopRequest 


This request has no parameters.

### gRPC Response: StopResponse 


This response has no parameters.


# SubscribeChannelGraph


### Response-streaming RPC


SubscribeChannelGraph launches a streaming RPC that allows the caller to receive notifications upon any changes to the channel graph topology from the point of view of the responding node. Events notified include: new nodes coming online, nodes updating their authenticated attributes, new channels being advertised, updates in the routing policy for a directional channel edge, and when channels are closed on-chain.

```shell

```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.GraphTopologySubscription()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
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

### gRPC Request: GraphTopologySubscription 


This request has no parameters.

### gRPC Response: GraphTopologyUpdate (Streaming)


Parameter | Type | Description
--------- | ---- | ----------- 
node_updates | [array NodeUpdate](#nodeupdate) |  
channel_updates | [array ChannelEdgeUpdate](#channeledgeupdate) |  
closed_chans | [array ClosedChannelUpdate](#closedchannelupdate) |   

# DebugLevel


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.DebugLevelRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = { 
    show: <bool>, 
    level_spec: <string>, 
  } 
> lightning.debugLevel(request, function(err, response) {
    console.log(response);
  })
{ 
    "sub_systems": <string>,
}
```

### gRPC Request: DebugLevelRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
show | bool |  
level_spec | string |   
### gRPC Response: DebugLevelResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
sub_systems | string |   

# FeeReport


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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.FeeReportRequest()
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
    metadata.add('macaroon', macaroon);
    callback(null, metadata);
  });
> var creds = grpc.credentials.combineChannelCredentials(sslCreds, macaroonCreds);
> var lightning = new lnrpc.Lightning('localhost:10009', creds);
> var request = {} 
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

### gRPC Request: FeeReportRequest 


This request has no parameters.

### gRPC Response: FeeReportResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
channel_fees | [array ChannelFeeReport](#channelfeereport) | An array of channel fee reports which describes the current fee schedule for each channel. 
day_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected over the past 24 hrs. 
week_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 week. 
month_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 month.  

# UpdateChannelPolicy


### Simple RPC


UpdateChannelPolicy allows the caller to update the fee schedule and channel policies for all channels globally, or a particular channel.

```shell

# Updates the channel policy for all channels, or just a particular channel
# identified by its channel point. The update will be committed, and
# broadcast to the rest of the network within the next batch.
# Channel points are encoded as: funding_txid:output_index

$ lncli updatechanpolicy [command options] base_fee_msat fee_rate time_lock_delta [channel_point]

# --base_fee_msat value    the base fee in milli-satoshis that will be charged for each forwarded HTLC, regardless of payment size (default: 0)
# --fee_rate value         the fee rate that will be charged proportionally based on the value of each forwarded HTLC, the lowest possible rate is 0.000001
# --time_lock_delta value  the CLTV delta that will be applied to all forwarded HTLCs (default: 0)
# --chan_point value       The channel whose fee policy should be updated, if nil the policies for all channels will be updated. Takes the form of: txid:output_index
```
```python
>>> import codecs, grpc, os
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.PolicyUpdateRequest(
        global=<bool>,
        chan_point=<ChannelPoint>,
        base_fee_msat=<int64>,
        fee_rate=<double>,
        time_lock_delta=<uint32>,
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
> lightning.updateChannelPolicy(request, function(err, response) {
    console.log(response);
  })
{ 
}
```

### gRPC Request: PolicyUpdateRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
global | bool | If set, then this update applies to all currently active channels. 
chan_point | [ChannelPoint](#channelpoint) | If set, this update will target a specific channel. 
base_fee_msat | int64 | The base fee charged regardless of the number of milli-satoshis sent. 
fee_rate | double | The effective fee rate in milli-satoshis. The precision of this value goes up to 6 decimal places, so 1e-6. 
time_lock_delta | uint32 | The required timelock delta for HTLCs forwarded over the channel.  
### gRPC Response: PolicyUpdateResponse 


This response has no parameters.


# ForwardingHistory


### Simple RPC


ForwardingHistory allows the caller to query the htlcswitch for a record of all HTLC's forwarded within the target time range, and integer offset within that time range. If no time-range is specified, then the first chunk of the past 24 hrs of forwarding history are returned.  A list of forwarding events are returned. The size of each forwarding event is 40 bytes, and the max message size able to be returned in gRPC is 4 MiB. As a result each message can only contain 50k entries.  Each response has the index offset of the last entry. The index offset can be provided to the request to allow the caller to skip a series of records.

```shell

# Query the HTLC switch's internal forwarding log for all completed
# payment circuits (HTLCs) over a particular time range (--start_time and
# --end_time). The start and end times are meant to be expressed in
# seconds since the Unix epoch. If a start and end time aren't provided,
# then events over the past 24 hours are queried for.
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
>>> macaroon = codecs.encode(open('LND_DIR/admin.macaroon', 'rb').read(), 'hex')
>>> os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
>>> cert = open('LND_DIR/tls.cert', 'rb').read()
>>> ssl_creds = grpc.ssl_channel_credentials(cert)
>>> channel = grpc.secure_channel('localhost:10009', ssl_creds)
>>> stub = lnrpc.LightningStub(channel)
>>> request = ln.ForwardingHistoryRequest(
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
> process.env.GRPC_SSL_CIPHER_SUITES = 'HIGH+ECDSA'
> var lndCert = fs.readFileSync('LND_DIR/tls.cert');
> var sslCreds = grpc.credentials.createSsl(lndCert);
> var macaroonCreds = grpc.credentials.createFromMetadataGenerator(function(args, callback) {
    var macaroon = fs.readFileSync("LND_DIR/admin.macaroon").toString('hex');
    var metadata = new grpc.Metadata()
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
  } 
> lightning.forwardingHistory(request, function(err, response) {
    console.log(response);
  })
{ 
    "forwarding_events": <array ForwardingEvent>,
    "last_offset_index": <uint32>,
}
```

### gRPC Request: ForwardingHistoryRequest 


Parameter | Type | Description
--------- | ---- | ----------- 
start_time | uint64 | Start time is the starting point of the forwarding history request. All records beyond this point will be included, respecting the end time, and the index offset. 
end_time | uint64 | End time is the end point of the forwarding history request. The response will carry at most 50k records between the start time and the end time. The index offset can be used to implement pagination. 
index_offset | uint32 | Index offset is the offset in the time series to start at. As each response can only contain 50k records, callers can use this to skip around within a packed time series. 
num_max_events | uint32 | The max number of events to return in the response to this query.  
### gRPC Response: ForwardingHistoryResponse 


Parameter | Type | Description
--------- | ---- | ----------- 
forwarding_events | [array ForwardingEvent](#forwardingevent) | A list of forwarding events from the time slice of the time series specified in the request. 
last_offset_index | uint32 | The index of the last time in the set of returned forwarding events. Can be used to seek further, pagination style.  


# Messages

## AddInvoiceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash | bytes |  
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient.  

## ChanInfoRequest


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel.  

## ChangePasswordRequest


Parameter | Type | Description
--------- | ---- | ----------- 
current_password | bytes | current_password should be the current valid passphrase used to unlock the daemon. 
new_password | bytes | new_password should be the new passphrase that will be needed to unlock the daemon.  

## ChangePasswordResponse


This message has no parameters.


## Channel


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
csv_delay | uint32 | The CSV delay expressed in relative blocks. If the channel is force closed, we'll need to wait for this many blocks before we can regain our funds. 
private | bool | Whether this channel is advertised to the network or not  

## ChannelBalanceRequest


This message has no parameters.


## ChannelBalanceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
balance | int64 | Sum of channels balances denominated in satoshis 
pending_open_balance | int64 | Sum of channels pending balances denominated in satoshis  

## ChannelCloseSummary


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

## ChannelCloseUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
closing_txid | bytes |  
success | bool |   

## ChannelEdge


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

## ChannelEdgeUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_point | [ChannelPoint](#channelpoint) |  
capacity | int64 |  
routing_policy | [RoutingPolicy](#routingpolicy) |  
advertising_node | string |  
connecting_node | string |   

## ChannelFeeReport


Parameter | Type | Description
--------- | ---- | ----------- 
chan_point | string | The channel that this fee report belongs to. 
base_fee_msat | int64 | The base fee charged regardless of the number of milli-satoshis sent. 
fee_per_mil | int64 | The amount charged per milli-satoshis transferred expressed in millionths of a satoshi. 
fee_rate | double | The effective fee rate in milli-satoshis. Computed by dividing the fee_per_mil value by 1 million.  

## ChannelGraph


Parameter | Type | Description
--------- | ---- | ----------- 
nodes | [array LightningNode](#lightningnode) | The list of `LightningNode`s in this channel graph 
edges | [array ChannelEdge](#channeledge) | The list of `ChannelEdge`s in this channel graph  

## ChannelGraphRequest


This message has no parameters.


## ChannelOpenUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) |   

## ChannelPoint


Parameter | Type | Description
--------- | ---- | ----------- 
funding_txid_bytes | bytes | Txid of the funding transaction 
funding_txid_str | string | Hex-encoded string representing the funding transaction 
output_index | uint32 | The index of the output of the funding transaction  

## CloseChannelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
channel_point | [ChannelPoint](#channelpoint) | The outpoint (txid:index) of the funding transaction. With this value, Bob will be able to generate a signature for Alice's version of the commitment transaction. 
force | bool | If true, then the channel will be closed forcibly. This means the current commitment transaction will be signed and broadcast. 
target_conf | int32 | The target number of blocks that the closure transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the closure transaction.  

## CloseStatusUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
close_pending | [PendingUpdate](#pendingupdate) |  
confirmation | [ConfirmationUpdate](#confirmationupdate) |  
chan_close | [ChannelCloseUpdate](#channelcloseupdate) |   

## ClosedChannelUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
capacity | int64 |  
closed_height | uint32 |  
chan_point | [ChannelPoint](#channelpoint) |   

## ClosedChannelsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
cooperative | bool |  
local_force | bool |  
remote_force | bool |  
breach | bool |  
funding_canceled | bool |   

## ClosedChannelsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array ChannelCloseSummary](#channelclosesummary) |   

## ConfirmationUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
block_sha | bytes |  
block_height | int32 |  
num_confs_left | uint32 |   

## ConnectPeerRequest


Parameter | Type | Description
--------- | ---- | ----------- 
addr | [LightningAddress](#lightningaddress) | Lightning address of the peer, in the format `<pubkey>@host` 
perm | bool | If set, the daemon will attempt to persistently connect to the target peer.  Otherwise, the call will be synchronous.  

## ConnectPeerResponse


This message has no parameters.


## DebugLevelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
show | bool |  
level_spec | string |   

## DebugLevelResponse


Parameter | Type | Description
--------- | ---- | ----------- 
sub_systems | string |   

## DeleteAllPaymentsRequest


This message has no parameters.


## DeleteAllPaymentsResponse


This message has no parameters.


## DisconnectPeerRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The pubkey of the node to disconnect from  

## DisconnectPeerResponse


This message has no parameters.


## FeeLimit


Parameter | Type | Description
--------- | ---- | ----------- 
fixed | int64 | The fee limit expressed as a fixed amount of satoshis. 
percent | int64 | The fee limit expressed as a percentage of the payment amount.  

## FeeReportRequest


This message has no parameters.


## FeeReportResponse


Parameter | Type | Description
--------- | ---- | ----------- 
channel_fees | [array ChannelFeeReport](#channelfeereport) | An array of channel fee reports which describes the current fee schedule for each channel. 
day_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected over the past 24 hrs. 
week_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 week. 
month_fee_sum | uint64 | The total amount of fee revenue (in satoshis) the switch has collected over the past 1 month.  

## ForwardingEvent


Parameter | Type | Description
--------- | ---- | ----------- 
timestamp | uint64 | Timestamp is the time (unix epoch offset) that this circuit was completed. 
chan_id_in | uint64 | The incoming channel ID that carried the HTLC that created the circuit. 
chan_id_out | uint64 | The outgoing channel ID that carried the preimage that completed the circuit. 
amt_in | uint64 | The total amount of the incoming HTLC that created half the circuit. 
amt_out | uint64 | The total amount of the outgoign HTLC that created the second half of the circuit. 
fee | uint64 | The total fee that this payment circuit carried.  

## ForwardingHistoryRequest


Parameter | Type | Description
--------- | ---- | ----------- 
start_time | uint64 | Start time is the starting point of the forwarding history request. All records beyond this point will be included, respecting the end time, and the index offset. 
end_time | uint64 | End time is the end point of the forwarding history request. The response will carry at most 50k records between the start time and the end time. The index offset can be used to implement pagination. 
index_offset | uint32 | Index offset is the offset in the time series to start at. As each response can only contain 50k records, callers can use this to skip around within a packed time series. 
num_max_events | uint32 | The max number of events to return in the response to this query.  

## ForwardingHistoryResponse


Parameter | Type | Description
--------- | ---- | ----------- 
forwarding_events | [array ForwardingEvent](#forwardingevent) | A list of forwarding events from the time slice of the time series specified in the request. 
last_offset_index | uint32 | The index of the last time in the set of returned forwarding events. Can be used to seek further, pagination style.  

## GenSeedRequest


Parameter | Type | Description
--------- | ---- | ----------- 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. 
seed_entropy | bytes | seed_entropy is an optional 16-bytes generated via CSPRNG. If not specified, then a fresh set of randomness will be used to create the seed.  

## GenSeedResponse


Parameter | Type | Description
--------- | ---- | ----------- 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This field is optional, as if not provided, then the daemon will generate a new cipher seed for the user. Otherwise, then the daemon will attempt to recover the wallet state linked to this cipher seed. 
enciphered_seed | bytes | enciphered_seed are the raw aezeed cipher seed bytes. This is the raw cipher text before run through our mnemonic encoding scheme.  

## GetInfoRequest


This message has no parameters.


## GetInfoResponse


Parameter | Type | Description
--------- | ---- | ----------- 
identity_pubkey | string | The identity pubkey of the current node. 
alias | string | If applicable, the alias of the current node, e.g. "bob" 
num_pending_channels | uint32 | Number of pending channels 
num_active_channels | uint32 | Number of active channels 
num_peers | uint32 | Number of peers 
block_height | uint32 | The node's current view of the height of the best block 
block_hash | string | The node's current view of the hash of the best block 
synced_to_chain | bool | Whether the wallet's view is synced to the main chain 
testnet | bool | Whether the current node is connected to testnet 
chains | array string | A list of active chains the node is connected to 
uris | array string | The URIs of the current node. 
best_header_timestamp | int64 | Timestamp of the block best known to the wallet 
version | string | The version of the LND software that the node is running.  

## GetTransactionsRequest


This message has no parameters.


## GraphTopologySubscription


This message has no parameters.


## GraphTopologyUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
node_updates | [array NodeUpdate](#nodeupdate) |  
channel_updates | [array ChannelEdgeUpdate](#channeledgeupdate) |  
closed_chans | [array ClosedChannelUpdate](#closedchannelupdate) |   

## HTLC


Parameter | Type | Description
--------- | ---- | ----------- 
incoming | bool |  
amount | int64 |  
hash_lock | bytes |  
expiration_height | uint32 |   

## Hop


Parameter | Type | Description
--------- | ---- | ----------- 
chan_id | uint64 | The unique channel ID for the channel. The first 3 bytes are the block height, the next 3 the index within the block, and the last 2 bytes are the output index for the channel. 
chan_capacity | int64 |  
amt_to_forward | int64 |  
fee | int64 |  
expiry | uint32 |  
amt_to_forward_msat | int64 |  
fee_msat | int64 |   

## HopHint


Parameter | Type | Description
--------- | ---- | ----------- 
node_id | string | The public key of the node at the start of the channel. 
chan_id | uint64 | The unique identifier of the channel. 
fee_base_msat | uint32 | The base fee of the channel denominated in millisatoshis. 
fee_proportional_millionths | uint32 | The fee rate of the channel for sending one satoshi across it denominated in millionths of a satoshi. 
cltv_expiry_delta | uint32 | The time-lock delta of the channel.  

## InitWalletRequest


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password is the passphrase that should be used to encrypt the wallet. This MUST be at least 8 chars in length. After creation, this password is required to unlock the daemon. 
cipher_seed_mnemonic | array string | cipher_seed_mnemonic is a 24-word mnemonic that encodes a prior aezeed cipher seed obtained by the user. This may have been generated by the GenSeed method, or be an existing seed. 
aezeed_passphrase | bytes | aezeed_passphrase is an optional user provided passphrase that will be used to encrypt the generated aezeed cipher seed. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each invdividual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.  

## InitWalletResponse


This message has no parameters.


## Invoice


Parameter | Type | Description
--------- | ---- | ----------- 
memo | string | An optional memo to attach along with the invoice. Used for record keeping purposes for the invoice's creator, and will also be set in the description field of the encoded payment request if the description_hash field is not being used. 
receipt | bytes | An optional cryptographic receipt of payment 
r_preimage | bytes | The hex-encoded preimage (32 byte) which will allow settling an incoming HTLC payable to this preimage 
r_hash | bytes | The hash of the preimage 
value | int64 | The value of this invoice in satoshis 
settled | bool | Whether this invoice has been fulfilled 
creation_date | int64 | When this invoice was created 
settle_date | int64 | When this invoice was settled 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
description_hash | bytes | Hash (SHA-256) of a description of the payment. Used if the description of payment (memo) is too long to naturally fit within the description field of an encoded payment request. 
expiry | int64 | Payment request expiry time in seconds. Default is 3600 (1 hour). 
fallback_addr | string | Fallback on-chain address. 
cltv_expiry | uint64 | Delta to use for the time-lock of the CLTV extended to the final hop. 
route_hints | [array RouteHint](#routehint) | Route hints that can each be individually used to assist in reaching the invoice's destination. 
private | bool | Whether this invoice should include routing hints for private channels.  

## InvoiceSubscription


This message has no parameters.


## LightningAddress


Parameter | Type | Description
--------- | ---- | ----------- 
pubkey | string | The identity pubkey of the Lightning node 
host | string | The network location of the lightning node, e.g. `69.69.69.69:1337` or `localhost:10011`  

## LightningNode


Parameter | Type | Description
--------- | ---- | ----------- 
last_update | uint32 |  
pub_key | string |  
alias | string |  
addresses | [array NodeAddress](#nodeaddress) |  
color | string |   

## ListChannelsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
active_only | bool |  
inactive_only | bool |  
public_only | bool |  
private_only | bool |   

## ListChannelsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
channels | [array Channel](#channel) | The list of active channels  

## ListInvoiceRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pending_only | bool | Toggles if all invoices should be returned, or only those that are currently unsettled.  

## ListInvoiceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
invoices | [array Invoice](#invoice) |   

## ListPaymentsRequest


This message has no parameters.


## ListPaymentsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
payments | [array Payment](#payment) | The list of payments  

## ListPeersRequest


This message has no parameters.


## ListPeersResponse


Parameter | Type | Description
--------- | ---- | ----------- 
peers | [array Peer](#peer) | The list of currently connected peers  

## NetworkInfo


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

## NetworkInfoRequest


This message has no parameters.


## NewAddressRequest


Parameter | Type | Description
--------- | ---- | ----------- 
type | [AddressType](#addresstype) | The address type  

## NewAddressResponse


Parameter | Type | Description
--------- | ---- | ----------- 
address | string | The newly generated wallet address  

## NewWitnessAddressRequest


This message has no parameters.


## NodeAddress


Parameter | Type | Description
--------- | ---- | ----------- 
network | string |  
addr | string |   

## NodeInfo


Parameter | Type | Description
--------- | ---- | ----------- 
node | [LightningNode](#lightningnode) | An individual vertex/node within the channel graph. A node is connected to other nodes by one or more channel edges emanating from it. As the graph is directed, a node will also have an incoming edge attached to it for each outgoing edge. 
num_channels | uint32 |  
total_capacity | int64 |   

## NodeInfoRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded compressed public of the target node  

## NodeUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
addresses | array string |  
identity_key | string |  
global_features | bytes |  
alias | string |   

## OpenChannelRequest


Parameter | Type | Description
--------- | ---- | ----------- 
node_pubkey | bytes | The pubkey of the node to open a channel with 
node_pubkey_string | string | The hex encoded pubkey of the node to open a channel with 
local_funding_amount | int64 | The number of satoshis the wallet should commit to the channel 
push_sat | int64 | The number of satoshis to push to the remote side as part of the initial commitment state 
target_conf | int32 | The target number of blocks that the funding transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the funding transaction. 
private | bool | Whether this channel should be private, not announced to the greater network. 
min_htlc_msat | int64 | The minimum value in millisatoshi we will require for incoming HTLCs on the channel. 
remote_csv_delay | uint32 | The delay we require on the remote's commitment transaction. If this is not set, it will be scaled automatically with the channel size.  

## OpenStatusUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
chan_pending | [PendingUpdate](#pendingupdate) |  
confirmation | [ConfirmationUpdate](#confirmationupdate) |  
chan_open | [ChannelOpenUpdate](#channelopenupdate) |   

## PayReq


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

## PayReqString


Parameter | Type | Description
--------- | ---- | ----------- 
pay_req | string | The payment request string to be decoded  

## Payment


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | string | The payment hash 
value | int64 | The value of the payment in satoshis 
creation_date | int64 | The date of this payment 
path | array string | The path this payment took 
fee | int64 | The fee paid for this payment in satoshis 
payment_preimage | string | The payment preimage  

## PaymentHash


Parameter | Type | Description
--------- | ---- | ----------- 
r_hash_str | string | The hex-encoded payment hash of the invoice to be looked up. The passed payment hash must be exactly 32 bytes, otherwise an error is returned. 
r_hash | bytes | The payment hash of the invoice to be looked up.  

## Peer


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

## PendingChannelsRequest


This message has no parameters.


## PendingChannelsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
total_limbo_balance | int64 | The balance in satoshis encumbered in pending channels 
pending_open_channels | [array PendingOpenChannel](#pendingopenchannel) | Channels pending opening 
pending_closing_channels | [array ClosedChannel](#closedchannel) | Channels pending closing 
pending_force_closing_channels | [array ForceClosedChannel](#forceclosedchannel) | Channels pending force closing 
waiting_close_channels | [array WaitingCloseChannel](#waitingclosechannel) | Channels waiting for closing tx to confirm  

## ClosedChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel to be closed 
closing_txid | string | The transaction id of the closing transaction  

## ForceClosedChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel to be force closed 
closing_txid | string | The transaction id of the closing transaction 
limbo_balance | int64 | The balance in satoshis encumbered in this pending channel 
maturity_height | uint32 | The height at which funds can be sweeped into the wallet 
blocks_til_maturity | int32 | Remaining # of blocks until the commitment output can be swept. Negative values indicate how many blocks have passed since becoming mature. 
recovered_balance | int64 | The total value of funds successfully recovered from this channel 
pending_htlcs | [array PendingHTLC](#pendinghtlc) |   

## PendingChannel


Parameter | Type | Description
--------- | ---- | ----------- 
remote_node_pub | string |  
channel_point | string |  
capacity | int64 |  
local_balance | int64 |  
remote_balance | int64 |   

## PendingOpenChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel 
confirmation_height | uint32 | The height at which this channel will be confirmed 
commit_fee | int64 | The amount calculated to be paid in fees for the current set of commitment transactions. The fee amount is persisted with the channel in order to allow the fee amount to be removed and recalculated with each channel state update, including updates that happen after a system restart. 
commit_weight | int64 | The weight of the commitment transaction 
fee_per_kw | int64 | The required number of satoshis per kilo-weight that the requester will pay at all times, for both the funding transaction and commitment transaction. This value can later be updated once the channel is open.  

## WaitingCloseChannel


Parameter | Type | Description
--------- | ---- | ----------- 
channel | [PendingChannel](#pendingchannel) | The pending channel waiting for closing tx to confirm 
limbo_balance | int64 | The balance in satoshis encumbered in this channel  

## PendingHTLC


Parameter | Type | Description
--------- | ---- | ----------- 
incoming | bool | The direction within the channel that the htlc was sent 
amount | int64 | The total value of the htlc 
outpoint | string | The final output to be swept back to the user's wallet 
maturity_height | uint32 | The next block height at which we can spend the current stage 
blocks_til_maturity | int32 | The number of blocks remaining until the current stage can be swept. Negative values indicate how many blocks have passed since becoming mature. 
stage | uint32 | Indicates whether the htlc is in its first or second stage of recovery  

## PendingUpdate


Parameter | Type | Description
--------- | ---- | ----------- 
txid | bytes |  
output_index | uint32 |   

## PolicyUpdateRequest


Parameter | Type | Description
--------- | ---- | ----------- 
global | bool | If set, then this update applies to all currently active channels. 
chan_point | [ChannelPoint](#channelpoint) | If set, this update will target a specific channel. 
base_fee_msat | int64 | The base fee charged regardless of the number of milli-satoshis sent. 
fee_rate | double | The effective fee rate in milli-satoshis. The precision of this value goes up to 6 decimal places, so 1e-6. 
time_lock_delta | uint32 | The required timelock delta for HTLCs forwarded over the channel.  

## PolicyUpdateResponse


This message has no parameters.


## QueryRoutesRequest


Parameter | Type | Description
--------- | ---- | ----------- 
pub_key | string | The 33-byte hex-encoded public key for the payment destination 
amt | int64 | The amount to send expressed in satoshis 
num_routes | int32 | The max number of routes to return. 
final_cltv_delta | int32 | An optional CLTV delta from the current height that should be used for the timelock of the final hop 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.  

## QueryRoutesResponse


Parameter | Type | Description
--------- | ---- | ----------- 
routes | [array Route](#route) |   

## Route


Parameter | Type | Description
--------- | ---- | ----------- 
total_time_lock | uint32 | The cumulative (final) time lock across the entire route.  This is the CLTV value that should be extended to the first hop in the route. All other hops will decrement the time-lock as advertised, leaving enough time for all hops to wait for or present the payment preimage to complete the payment. 
total_fees | int64 | The sum of the fees paid at each hop within the final route.  In the case of a one-hop payment, this value will be zero as we don't need to pay a fee it ourself. 
total_amt | int64 | The total amount of funds required to complete a payment over this route. This value includes the cumulative fees at each hop. As a result, the HTLC extended to the first-hop in the route will need to have at least this many satoshis, otherwise the route will fail at an intermediate node due to an insufficient amount of fees. 
hops | [array Hop](#hop) | Contains details concerning the specific forwarding details at each hop. 
total_fees_msat | int64 | The total fees in millisatoshis. 
total_amt_msat | int64 | The total amount in millisatoshis.  

## RouteHint


Parameter | Type | Description
--------- | ---- | ----------- 
hop_hints | [array HopHint](#hophint) | A list of hop hints that when chained together can assist in reaching a specific destination.  

## RoutingPolicy


Parameter | Type | Description
--------- | ---- | ----------- 
time_lock_delta | uint32 |  
min_htlc | int64 |  
fee_base_msat | int64 |  
fee_rate_milli_msat | int64 |   

## SendCoinsRequest


Parameter | Type | Description
--------- | ---- | ----------- 
addr | string | The address to send coins to 
amount | int64 | The amount in satoshis to send 
target_conf | int32 | The target number of blocks that this transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the transaction.  

## SendCoinsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The transaction ID of the transaction  

## SendManyRequest


Parameter | Type | Description
--------- | ---- | ----------- 
AddrToAmount | [array AddrToAmountEntry](#addrtoamountentry) | The map from addresses to amounts 
target_conf | int32 | The target number of blocks that this transaction should be confirmed by. 
sat_per_byte | int64 | A manual fee rate set in sat/byte that should be used when crafting the transaction.  

## AddrToAmountEntry


Parameter | Type | Description
--------- | ---- | ----------- 
key | string |  
value | int64 |   

## SendManyResponse


Parameter | Type | Description
--------- | ---- | ----------- 
txid | string | The id of the transaction  

## SendRequest


Parameter | Type | Description
--------- | ---- | ----------- 
dest | bytes | The identity pubkey of the payment recipient 
dest_string | string | The hex-encoded identity pubkey of the payment recipient 
amt | int64 | Number of satoshis to send. 
payment_hash | bytes | The hash to use within the payment's HTLC 
payment_hash_string | string | The hex-encoded hash to use within the payment's HTLC 
payment_request | string | A bare-bones invoice for a payment within the Lightning Network.  With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. 
final_cltv_delta | int32 | The CLTV delta from the current height that should be used to set the timelock for the final hop. 
fee_limit | [FeeLimit](#feelimit) | The maximum number of satoshis that will be paid as a fee of the payment. This value can be represented either as a percentage of the amount being sent, or as a fixed amount of the maximum fee the user is willing the pay to send the payment.  

## SendResponse


Parameter | Type | Description
--------- | ---- | ----------- 
payment_error | string |  
payment_preimage | bytes |  
payment_route | [Route](#route) |   

## SendToRouteRequest


Parameter | Type | Description
--------- | ---- | ----------- 
payment_hash | bytes | The payment hash to use for the HTLC. 
payment_hash_string | string | An optional hex-encoded payment hash to be used for the HTLC. 
routes | [array Route](#route) | The set of routes that should be used to attempt to complete the payment.  

## SignMessageRequest


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message to be signed  

## SignMessageResponse


Parameter | Type | Description
--------- | ---- | ----------- 
signature | string | The signature for the given message  

## StopRequest


This message has no parameters.


## StopResponse


This message has no parameters.


## Transaction


Parameter | Type | Description
--------- | ---- | ----------- 
tx_hash | string | The transaction hash 
amount | int64 | The transaction ammount, denominated in satoshis 
num_confirmations | int32 | The number of confirmations 
block_hash | string | The hash of the block this transaction was included in 
block_height | int32 | The height of the block this transaction was included in 
time_stamp | int64 | Timestamp of this transaction 
total_fees | int64 | Fees paid for this transaction 
dest_addresses | array string | Addresses that received funds for this transaction  

## TransactionDetails


Parameter | Type | Description
--------- | ---- | ----------- 
transactions | [array Transaction](#transaction) | The list of transactions relevant to the wallet.  

## UnlockWalletRequest


Parameter | Type | Description
--------- | ---- | ----------- 
wallet_password | bytes | wallet_password should be the current valid passphrase for the daemon. This will be required to decrypt on-disk material that the daemon requires to function properly. 
recovery_window | int32 | recovery_window is an optional argument specifying the address lookahead when restoring a wallet seed. The recovery window applies to each invdividual branch of the BIP44 derivation paths. Supplying a recovery window of zero indicates that no addresses should be recovered, such after the first initialization of the wallet.  

## UnlockWalletResponse


This message has no parameters.


## VerifyMessageRequest


Parameter | Type | Description
--------- | ---- | ----------- 
msg | bytes | The message over which the signature is to be verified 
signature | string | The signature to be verified over the given message  

## VerifyMessageResponse


Parameter | Type | Description
--------- | ---- | ----------- 
valid | bool | Whether the signature was valid over the given message 
pubkey | string | The pubkey recovered from the signature  

## WalletBalanceRequest


This message has no parameters.


## WalletBalanceResponse


Parameter | Type | Description
--------- | ---- | ----------- 
total_balance | int64 | The balance of the wallet 
confirmed_balance | int64 | The confirmed balance of a wallet(with >= 1 confirmations) 
unconfirmed_balance | int64 | The unconfirmed balance of a wallet(with 0 confirmations)  
