---
title: Lightning Loop API Reference

language_tabs:
  - shell
  - python
  - javascript

toc_footers:
  - <a href='mailto:loop@lightning.engineering'>Contact Us</a>
  - Powered by <a href='https://github.com/lord/slate'>Slate</a>

search: true
---
# Loop gRPC API Reference

Welcome to the gRPC API reference documentation for Lightning Loop.

Lightning Loop is a non-custodial service offered by Lightning Labs to bridge
on-chain and off-chain Bitcoin using submarine swaps. This repository is home to
the Loop client and depends on the Lightning Network daemon lnd. All of lnd’s
supported chain backends are fully supported when using the Loop client:
Neutrino, Bitcoin Core, and btcd.

The service can be used in various situations:

* Acquiring inbound channel liquidity from arbitrary nodes on the Lightning
  network
* Depositing funds to a Bitcoin on-chain address without closing active
  channels
* Paying to on-chain fallback addresses in the case of insufficient route
  liquidity
* Refilling depleted channels with funds from cold-wallets or exchange
  withdrawals
* Servicing off-chain Lightning withdrawals using on-chain payments, with no
  funds in channels required
* As a failsafe payment method that can be used when channel liquidity along a
  route is insufficient

This site features the documentation for loop (CLI), and the API documentation
for Python and JavaScript clients in order to communicate with a local `loopd`
instance through gRPC. Currently, this communication is unauthenticated, so
exposing this service to the internet is not recommended.

The original `*.proto` files from which the gRPC documentation was generated
can be found here:

- [`client.proto`](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/looprpc/client.proto)



This is the reference for the **gRPC API**. Alternatively, there is also a [REST
API which is documented here](#loop-rest-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`a90971a697f6b2adb65d3723b6d16d472d24e87b`](https://github.com/lightninglabs/loop/tree/a90971a697f6b2adb65d3723b6d16d472d24e87b).</small>


# Service _SwapClient_


## SwapClient.GetLoopInQuote


#### Unary RPC


 GetQuote returns a quote for a swap with the provided parameters.

```shell

# get a quote for the cost of a swap

$ out  get a quote for the cost of a loop out swap

# --help, -h  show help
```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.QuoteRequest(
        amt=<int64>,
        conf_target=<int32>,
        external_htlc=<bool>,
        swap_publication_deadline=<uint64>,
    )
>>> response = stub.GetLoopInQuote(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "swap_fee": <int64>,
    "prepay_amt": <int64>,
    "miner_fee": <int64>,
    "swap_payment_dest": <bytes>,
    "cltv_delta": <int32>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = { 
  amt: <int64>, 
  conf_target: <int32>, 
  external_htlc: <bool>, 
  swap_publication_deadline: <uint64>, 
};
swapClient.getLoopInQuote(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "swap_fee": <int64>,
//      "prepay_amt": <int64>,
//      "miner_fee": <int64>,
//      "swap_payment_dest": <bytes>,
//      "cltv_delta": <int32>,
//  }
```

### gRPC Request: [looprpc.QuoteRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L390)


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | The amount to swap in satoshis. 
conf_target | int32 | The confirmation target that should be used either for the sweep of the on-chain HTLC broadcast by the swap server in the case of a Loop Out, or for the confirmation of the on-chain HTLC broadcast by the swap client in the case of a Loop In. 
external_htlc | bool | If external_htlc is true, we expect the htlc to be published by an external actor. 
swap_publication_deadline | uint64 | The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee. This only has an effect on loop out quotes.  
### gRPC Response: [looprpc.QuoteResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L420)


Parameter | Type | Description
--------- | ---- | ----------- 
swap_fee | int64 | The fee that the swap server is charging for the swap. 
prepay_amt | int64 | The part of the swap fee that is requested as a prepayment. 
miner_fee | int64 | An estimate of the on-chain fee that needs to be paid to sweep the HTLC for a loop out or to pay to the HTLC for loop in. If a miner fee of 0 is returned, it means the external_htlc flag was set for a loop in and the fee estimation was skipped. If a miner fee of -1 is returned, it means lnd's wallet tried to estimate the fee but was unable to create a sample estimation transaction because not enough funds are available. An information message should be shown to the user in this case. 
swap_payment_dest | bytes | The node pubkey where the swap payment needs to be paid to. This can be used to test connectivity before initiating the swap. 
cltv_delta | int32 | On-chain cltv expiry delta  

## SwapClient.GetLoopInTerms


#### Unary RPC


 GetTerms returns the terms that the server enforces for swaps.

```shell

# Display the current swap terms imposed by the server.

$ loop terms [arguments...]

```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.TermsRequest()
>>> response = stub.GetLoopInTerms(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "min_swap_amount": <int64>,
    "max_swap_amount": <int64>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = {}
swapClient.getLoopInTerms(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "min_swap_amount": <int64>,
//      "max_swap_amount": <int64>,
//  }
```

### gRPC Request: [looprpc.TermsRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L372)


This request has no parameters.

### gRPC Response: [looprpc.TermsResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L375)


Parameter | Type | Description
--------- | ---- | ----------- 
min_swap_amount | int64 | Minimum swap amount (sat) 
max_swap_amount | int64 | Maximum swap amount (sat)  

## SwapClient.GetLsatTokens


#### Unary RPC


 GetLsatTokens returns all LSAT tokens the daemon ever paid for.

```shell

# Shows a list of all LSAT tokens that loopd has paid for

$ loop listauth [arguments...]

```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.TokensRequest()
>>> response = stub.GetLsatTokens(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "tokens": <array LsatToken>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = {}
swapClient.getLsatTokens(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "tokens": <array LsatToken>,
//  }
```

### gRPC Request: [looprpc.TokensRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L454)


This request has no parameters.

### gRPC Response: [looprpc.TokensResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L457)


Parameter | Type | Description
--------- | ---- | ----------- 
tokens | [array LsatToken](#looprpc-lsattoken) | List of all tokens the daemon knows of, including old/expired tokens.  

## SwapClient.ListSwaps


#### Unary RPC


 ListSwaps returns a list of all currently known swaps and their current status.

```shell

# Allows the user to get a list of all swaps that are currently stored in the database

$ loop listswaps [arguments...]

```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.ListSwapsRequest()
>>> response = stub.ListSwaps(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "swaps": <array SwapStatus>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = {}
swapClient.listSwaps(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "swaps": <array SwapStatus>,
//  }
```

### gRPC Request: [looprpc.ListSwapsRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L354)


This request has no parameters.

### gRPC Response: [looprpc.ListSwapsResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L357)


Parameter | Type | Description
--------- | ---- | ----------- 
swaps | [array SwapStatus](#looprpc-swapstatus) | The list of all currently known swaps and their status.  

## SwapClient.LoopIn


#### Unary RPC


 LoopIn initiates a loop in swap with the given parameters. The call returns after the swap has been set up with the swap server. From that point onwards, progress can be tracked via the SwapStatus stream that is returned from Monitor().

```shell

# Send the amount in satoshis specified by the amt argument off-chain.

$ loop in [command options] amt

# --amt value       the amount in satoshis to loop in (default: 0)
# --external        expect htlc to be published externally
# --last_hop value  the pubkey of the last hop to use for this swap
```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.LoopInRequest(
        amt=<int64>,
        max_swap_fee=<int64>,
        max_miner_fee=<int64>,
        last_hop=<bytes>,
        external_htlc=<bool>,
    )
>>> response = stub.LoopIn(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "id": <string>,
    "id_bytes": <bytes>,
    "htlc_address": <string>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = { 
  amt: <int64>, 
  max_swap_fee: <int64>, 
  max_miner_fee: <int64>, 
  last_hop: <bytes>, 
  external_htlc: <bool>, 
};
swapClient.loopIn(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "id": <string>,
//      "id_bytes": <bytes>,
//      "htlc_address": <string>,
//  }
```

### gRPC Request: [looprpc.LoopInRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L187)


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner  fee. 
max_swap_fee | int64 | Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call. 
max_miner_fee | int64 | Maximum in on-chain fees that we are willing to spent. If we want to publish the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap.   max_miner_fee is typically taken from the response of the GetQuote call. 
last_hop | bytes | The last hop to use for the loop in swap. If empty, the last hop is selected based on the lowest routing fee for the swap payment from the server. 
external_htlc | bool | If external_htlc is true, we expect the htlc to be published by an external actor.  
### gRPC Response: [looprpc.SwapResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L224)


Parameter | Type | Description
--------- | ---- | ----------- 
id | string | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | bytes | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
htlc_address | string | The address of the on-chain htlc.  

## SwapClient.LoopOut


#### Unary RPC


 LoopOut initiates an loop out swap with the given parameters. The call returns after the swap has been set up with the swap server. From that point onwards, progress can be tracked via the SwapStatus stream that is returned from Monitor().

```shell

# Attempts loop out the target amount into either the backing lnd's
# wallet, or a targeted address.
# The amount is to be specified in satoshis.
# Optionally a BASE58/bech32 encoded bitcoin destination address may be
# specified. If not specified, a new wallet address will be generated.

$ loop out [command options] amt [addr]

# --channel value               the 8-byte compact channel ID of the channel to loop out (default: 0)
# --addr value                  the optional address that the looped out funds should be sent to, if let blank the funds will go to lnd's wallet
# --amt value                   the amount in satoshis to loop out (default: 0)
# --conf_target value           the number of blocks from the swap initiation height that the on-chain HTLC should be swept within (default: 6)
# --max_swap_routing_fee value  the max off-chain swap routing fee in satoshis, if let blank a default max fee will be used (default: 0)
# --fast                        Indicate you want to swap immediately, paying potentially a higher fee. If not set the swap server might choose to wait up to 30 minutes before publishing the swap HTLC on-chain, to save on chain fees. Not setting this flag might result in a lower swap fee.
```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.LoopOutRequest(
        amt=<int64>,
        dest=<string>,
        max_swap_routing_fee=<int64>,
        max_prepay_routing_fee=<int64>,
        max_swap_fee=<int64>,
        max_prepay_amt=<int64>,
        max_miner_fee=<int64>,
        loop_out_channel=<uint64>,
        sweep_conf_target=<int32>,
        swap_publication_deadline=<uint64>,
    )
>>> response = stub.LoopOut(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "id": <string>,
    "id_bytes": <bytes>,
    "htlc_address": <string>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = { 
  amt: <int64>, 
  dest: <string>, 
  max_swap_routing_fee: <int64>, 
  max_prepay_routing_fee: <int64>, 
  max_swap_fee: <int64>, 
  max_prepay_amt: <int64>, 
  max_miner_fee: <int64>, 
  loop_out_channel: <uint64>, 
  sweep_conf_target: <int32>, 
  swap_publication_deadline: <uint64>, 
};
swapClient.loopOut(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "id": <string>,
//      "id_bytes": <bytes>,
//      "htlc_address": <string>,
//  }
```

### gRPC Request: [looprpc.LoopOutRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L109)


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner fee. 
dest | string | Base58 encoded destination address for the swap. 
max_swap_routing_fee | int64 | Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call. 
max_prepay_routing_fee | int64 | Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call. 
max_swap_fee | int64 | Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call. It includes the prepay amount. 
max_prepay_amt | int64 | Maximum amount of the swap fee that may be charged as a prepayment. 
max_miner_fee | int64 | Maximum in on-chain fees that we are willing to spent. If we want to sweep the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap. If the fee estimate is lower, we publish the sweep tx.  If the sweep tx is not confirmed, we are forced to ratchet up fees until it is swept. Possibly even exceeding max_miner_fee if we get close to the htlc timeout. Because the initial publication revealed the preimage, we have no other choice. The server may already have pulled the off-chain htlc. Only when the fee becomes higher than the swap amount, we can only wait for fees to come down and hope - if we are past the timeout - that the server is not publishing the revocation.  max_miner_fee is typically taken from the response of the GetQuote call. 
loop_out_channel | uint64 | The channel to loop out, the channel to loop out is selected based on the lowest routing fee for the swap payment to the server. 
sweep_conf_target | int32 | The number of blocks from the on-chain HTLC's confirmation height that it should be swept within. 
swap_publication_deadline | uint64 | The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee.  
### gRPC Response: [looprpc.SwapResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L224)


Parameter | Type | Description
--------- | ---- | ----------- 
id | string | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | bytes | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
htlc_address | string | The address of the on-chain htlc.  

## SwapClient.LoopOutQuote


#### Unary RPC


 LoopOutQuote returns a quote for a loop out swap with the provided parameters.

```shell

# get a quote for the cost of a swap

$ out  get a quote for the cost of a loop out swap

# --help, -h  show help
```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.QuoteRequest(
        amt=<int64>,
        conf_target=<int32>,
        external_htlc=<bool>,
        swap_publication_deadline=<uint64>,
    )
>>> response = stub.LoopOutQuote(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "swap_fee": <int64>,
    "prepay_amt": <int64>,
    "miner_fee": <int64>,
    "swap_payment_dest": <bytes>,
    "cltv_delta": <int32>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = { 
  amt: <int64>, 
  conf_target: <int32>, 
  external_htlc: <bool>, 
  swap_publication_deadline: <uint64>, 
};
swapClient.loopOutQuote(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "swap_fee": <int64>,
//      "prepay_amt": <int64>,
//      "miner_fee": <int64>,
//      "swap_payment_dest": <bytes>,
//      "cltv_delta": <int32>,
//  }
```

### gRPC Request: [looprpc.QuoteRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L390)


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | The amount to swap in satoshis. 
conf_target | int32 | The confirmation target that should be used either for the sweep of the on-chain HTLC broadcast by the swap server in the case of a Loop Out, or for the confirmation of the on-chain HTLC broadcast by the swap client in the case of a Loop In. 
external_htlc | bool | If external_htlc is true, we expect the htlc to be published by an external actor. 
swap_publication_deadline | uint64 | The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee. This only has an effect on loop out quotes.  
### gRPC Response: [looprpc.QuoteResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L420)


Parameter | Type | Description
--------- | ---- | ----------- 
swap_fee | int64 | The fee that the swap server is charging for the swap. 
prepay_amt | int64 | The part of the swap fee that is requested as a prepayment. 
miner_fee | int64 | An estimate of the on-chain fee that needs to be paid to sweep the HTLC for a loop out or to pay to the HTLC for loop in. If a miner fee of 0 is returned, it means the external_htlc flag was set for a loop in and the fee estimation was skipped. If a miner fee of -1 is returned, it means lnd's wallet tried to estimate the fee but was unable to create a sample estimation transaction because not enough funds are available. An information message should be shown to the user in this case. 
swap_payment_dest | bytes | The node pubkey where the swap payment needs to be paid to. This can be used to test connectivity before initiating the swap. 
cltv_delta | int32 | On-chain cltv expiry delta  

## SwapClient.LoopOutTerms


#### Unary RPC


 LoopOutTerms returns the terms that the server enforces for a loop out swap.

```shell

# Display the current swap terms imposed by the server.

$ loop terms [arguments...]

```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.TermsRequest()
>>> response = stub.LoopOutTerms(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "min_swap_amount": <int64>,
    "max_swap_amount": <int64>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = {}
swapClient.loopOutTerms(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "min_swap_amount": <int64>,
//      "max_swap_amount": <int64>,
//  }
```

### gRPC Request: [looprpc.TermsRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L372)


This request has no parameters.

### gRPC Response: [looprpc.TermsResponse ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L375)


Parameter | Type | Description
--------- | ---- | ----------- 
min_swap_amount | int64 | Minimum swap amount (sat) 
max_swap_amount | int64 | Maximum swap amount (sat)  

## SwapClient.Monitor


#### Server-streaming RPC


 Monitor will return a stream of swap updates for currently active swaps.

```shell

# Allows the user to monitor progress of any active swaps

$ loop monitor [arguments...]

```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.MonitorRequest()
>>> for response in stub.Monitor(request, metadata=[('macaroon', macaroon)]):
        print(response)
{ 
    "amt": <int64>,
    "id": <string>,
    "id_bytes": <bytes>,
    "type": <SwapType>,
    "state": <SwapState>,
    "initiation_time": <int64>,
    "last_update_time": <int64>,
    "htlc_address": <string>,
    "cost_server": <int64>,
    "cost_onchain": <int64>,
    "cost_offchain": <int64>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = {}
let call = swapClient.monitor(request);
call.on('data', function(response) {
  // A response was received from the server.
  console.log(response);
});
call.on('status', function(status) {
  // The current status of the stream.
});
call.on('end', function() {
  // The server has closed the stream.
});
// Console output:
//  { 
//      "amt": <int64>,
//      "id": <string>,
//      "id_bytes": <bytes>,
//      "type": <SwapType>,
//      "state": <SwapState>,
//      "initiation_time": <int64>,
//      "last_update_time": <int64>,
//      "htlc_address": <string>,
//      "cost_server": <int64>,
//      "cost_onchain": <int64>,
//      "cost_offchain": <int64>,
//  }
```

### gRPC Request: [looprpc.MonitorRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L245)


This request has no parameters.

### gRPC Response: [looprpc.SwapStatus (Streaming)](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L248)


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner fee. 
id | string | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | bytes | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
type | [SwapType](#looprpc-swaptype) | Swap type 
state | [SwapState](#looprpc-swapstate) | State the swap is currently in, see State enum. 
initiation_time | int64 | Initiation time of the swap. 
last_update_time | int64 | Initiation time of the swap. 
htlc_address | string | Htlc address. 
cost_server | int64 | Swap server cost 
cost_onchain | int64 | On-chain transaction cost 
cost_offchain | int64 | Off-chain routing fees  

## SwapClient.SwapInfo


#### Unary RPC


 SwapInfo returns all known details about a single swap.

```shell

# Allows the user to get the status of a single swap currently stored in the database

$ loop swapinfo [command options] id

# --id value  the ID of the swap (default: 0)
```
```python
>>> import grpc
>>> import client_pb2 as loop
>>> import client_pb2_grpc as looprpc
>>> channel = grpc.insecure_channel('localhost:11010')
>>> stub = looprpc.SwapClientStub(channel)
>>> request = loop.looprpc.SwapInfoRequest(
        id=<bytes>,
    )
>>> response = stub.SwapInfo(request, metadata=[('macaroon', macaroon)])
>>> print(response)
{ 
    "amt": <int64>,
    "id": <string>,
    "id_bytes": <bytes>,
    "type": <SwapType>,
    "state": <SwapState>,
    "initiation_time": <int64>,
    "last_update_time": <int64>,
    "htlc_address": <string>,
    "cost_server": <int64>,
    "cost_onchain": <int64>,
    "cost_offchain": <int64>,
}
```
```javascript
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  './client.proto',
  {
     keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
  },
);
const looprpc = grpc.loadPackageDefinition(packageDefinition).looprpc;
const swapClient = new looprpc.SwapClient('localhost:11010', grpc.credentials.createInsecure());
let request = { 
  id: <bytes>, 
};
swapClient.swapInfo(request, function(err, response) {
  console.log(response);
});
// Console output:
//  { 
//      "amt": <int64>,
//      "id": <string>,
//      "id_bytes": <bytes>,
//      "type": <SwapType>,
//      "state": <SwapState>,
//      "initiation_time": <int64>,
//      "last_update_time": <int64>,
//      "htlc_address": <string>,
//      "cost_server": <int64>,
//      "cost_onchain": <int64>,
//      "cost_offchain": <int64>,
//  }
```

### gRPC Request: [looprpc.SwapInfoRequest ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L364)


Parameter | Type | Description
--------- | ---- | ----------- 
id | bytes | The swap identifier which currently is the hash that locks the HTLCs. When using REST, this field must be encoded as URL safe base64.  
### gRPC Response: [looprpc.SwapStatus ](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/lnrpc/client.proto#L248)


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner fee. 
id | string | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | bytes | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
type | [SwapType](#looprpc-swaptype) | Swap type 
state | [SwapState](#looprpc-swapstate) | State the swap is currently in, see State enum. 
initiation_time | int64 | Initiation time of the swap. 
last_update_time | int64 | Initiation time of the swap. 
htlc_address | string | Htlc address. 
cost_server | int64 | Swap server cost 
cost_onchain | int64 | On-chain transaction cost 
cost_offchain | int64 | Off-chain routing fees  



# gRPC Messages

### looprpc.ListSwapsRequest


This message has no parameters.


### looprpc.ListSwapsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
swaps | [array SwapStatus](#looprpc-swapstatus) | The list of all currently known swaps and their status.  

### looprpc.LoopInRequest


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner  fee. 
max_swap_fee | int64 | Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call. 
max_miner_fee | int64 | Maximum in on-chain fees that we are willing to spent. If we want to publish the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap.   max_miner_fee is typically taken from the response of the GetQuote call. 
last_hop | bytes | The last hop to use for the loop in swap. If empty, the last hop is selected based on the lowest routing fee for the swap payment from the server. 
external_htlc | bool | If external_htlc is true, we expect the htlc to be published by an external actor.  

### looprpc.LoopOutRequest


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner fee. 
dest | string | Base58 encoded destination address for the swap. 
max_swap_routing_fee | int64 | Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call. 
max_prepay_routing_fee | int64 | Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call. 
max_swap_fee | int64 | Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call. It includes the prepay amount. 
max_prepay_amt | int64 | Maximum amount of the swap fee that may be charged as a prepayment. 
max_miner_fee | int64 | Maximum in on-chain fees that we are willing to spent. If we want to sweep the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap. If the fee estimate is lower, we publish the sweep tx.  If the sweep tx is not confirmed, we are forced to ratchet up fees until it is swept. Possibly even exceeding max_miner_fee if we get close to the htlc timeout. Because the initial publication revealed the preimage, we have no other choice. The server may already have pulled the off-chain htlc. Only when the fee becomes higher than the swap amount, we can only wait for fees to come down and hope - if we are past the timeout - that the server is not publishing the revocation.  max_miner_fee is typically taken from the response of the GetQuote call. 
loop_out_channel | uint64 | The channel to loop out, the channel to loop out is selected based on the lowest routing fee for the swap payment to the server. 
sweep_conf_target | int32 | The number of blocks from the on-chain HTLC's confirmation height that it should be swept within. 
swap_publication_deadline | uint64 | The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee.  

### looprpc.LsatToken


Parameter | Type | Description
--------- | ---- | ----------- 
base_macaroon | bytes | The base macaroon that was baked by the auth server. 
payment_hash | bytes | The payment hash of the payment that was paid to obtain the token. 
payment_preimage | bytes | The preimage of the payment hash, knowledge of this is proof that the payment has been paid. If the preimage is set to all zeros, this means the payment is still pending and the token is not yet fully valid. 
amount_paid_msat | int64 | The amount of millisatoshis that was paid to get the token. 
routing_fee_paid_msat | int64 | The amount of millisatoshis paid in routing fee to pay for the token. 
time_created | int64 | The creation time of the token as UNIX timestamp in seconds. 
expired | bool | Indicates whether the token is expired or still valid. 
storage_name | string | Identifying attribute of this token in the store. Currently represents the file name of the token where it's stored on the file system.  

### looprpc.MonitorRequest


This message has no parameters.


### looprpc.QuoteRequest


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | The amount to swap in satoshis. 
conf_target | int32 | The confirmation target that should be used either for the sweep of the on-chain HTLC broadcast by the swap server in the case of a Loop Out, or for the confirmation of the on-chain HTLC broadcast by the swap client in the case of a Loop In. 
external_htlc | bool | If external_htlc is true, we expect the htlc to be published by an external actor. 
swap_publication_deadline | uint64 | The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee. This only has an effect on loop out quotes.  

### looprpc.QuoteResponse


Parameter | Type | Description
--------- | ---- | ----------- 
swap_fee | int64 | The fee that the swap server is charging for the swap. 
prepay_amt | int64 | The part of the swap fee that is requested as a prepayment. 
miner_fee | int64 | An estimate of the on-chain fee that needs to be paid to sweep the HTLC for a loop out or to pay to the HTLC for loop in. If a miner fee of 0 is returned, it means the external_htlc flag was set for a loop in and the fee estimation was skipped. If a miner fee of -1 is returned, it means lnd's wallet tried to estimate the fee but was unable to create a sample estimation transaction because not enough funds are available. An information message should be shown to the user in this case. 
swap_payment_dest | bytes | The node pubkey where the swap payment needs to be paid to. This can be used to test connectivity before initiating the swap. 
cltv_delta | int32 | On-chain cltv expiry delta  

### looprpc.SwapInfoRequest


Parameter | Type | Description
--------- | ---- | ----------- 
id | bytes | The swap identifier which currently is the hash that locks the HTLCs. When using REST, this field must be encoded as URL safe base64.  

### looprpc.SwapResponse


Parameter | Type | Description
--------- | ---- | ----------- 
id | string | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | bytes | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
htlc_address | string | The address of the on-chain htlc.  

### looprpc.SwapStatus


Parameter | Type | Description
--------- | ---- | ----------- 
amt | int64 | Requested swap amount in sat. This does not include the swap and miner fee. 
id | string | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | bytes | Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
type | [SwapType](#looprpc-swaptype) | Swap type 
state | [SwapState](#looprpc-swapstate) | State the swap is currently in, see State enum. 
initiation_time | int64 | Initiation time of the swap. 
last_update_time | int64 | Initiation time of the swap. 
htlc_address | string | Htlc address. 
cost_server | int64 | Swap server cost 
cost_onchain | int64 | On-chain transaction cost 
cost_offchain | int64 | Off-chain routing fees  

### looprpc.TermsRequest


This message has no parameters.


### looprpc.TermsResponse


Parameter | Type | Description
--------- | ---- | ----------- 
min_swap_amount | int64 | Minimum swap amount (sat) 
max_swap_amount | int64 | Maximum swap amount (sat)  

### looprpc.TokensRequest


This message has no parameters.


### looprpc.TokensResponse


Parameter | Type | Description
--------- | ---- | ----------- 
tokens | [array LsatToken](#looprpc-lsattoken) | List of all tokens the daemon knows of, including old/expired tokens.  


# gRPC Enums

### SwapState


Name | Value | Description
---- | ----- | ----------- 
INITIATED | 0 | INITIATED is the initial state of a swap. At that point, the initiation call to the server has been made and the payment process has been started for the swap and prepayment invoices. 
PREIMAGE_REVEALED | 1 | PREIMAGE_REVEALED is reached when the sweep tx publication is first attempted. From that point on, we should consider the preimage to no longer be secret and we need to do all we can to get the sweep confirmed. This state will mostly coalesce with StateHtlcConfirmed, except in the case where we wait for fees to come down before we sweep. 
HTLC_PUBLISHED | 2 | HTLC_PUBLISHED is reached when the htlc tx has been published in a loop in swap. 
SUCCESS | 3 | SUCCESS is the final swap state that is reached when the sweep tx has the required confirmation depth. 
FAILED | 4 | FAILED is the final swap state for a failed swap with or without loss of the swap amount. 
INVOICE_SETTLED | 5 | INVOICE_SETTLED is reached when the swap invoice in a loop in swap has been paid, but we are still waiting for the htlc spend to confirm.  

### SwapType


Name | Value | Description
---- | ----- | ----------- 
LOOP_OUT | 0 | LOOP_OUT indicates an loop out swap (off-chain to on-chain) 
LOOP_IN | 1 | LOOP_IN indicates a loop in swap (on-chain to off-chain)  
# Loop REST API Reference

Welcome to the REST API reference documentation for Lightning Loop.

Lightning Loop is a non-custodial service offered by Lightning Labs to bridge
on-chain and off-chain Bitcoin using submarine swaps. This repository is home to
the Loop client and depends on the Lightning Network daemon lnd. All of lnd’s
supported chain backends are fully supported when using the Loop client:
Neutrino, Bitcoin Core, and btcd.

The service can be used in various situations:

* Acquiring inbound channel liquidity from arbitrary nodes on the Lightning
  network
* Depositing funds to a Bitcoin on-chain address without closing active
  channels
* Paying to on-chain fallback addresses in the case of insufficient route
  liquidity
* Refilling depleted channels with funds from cold-wallets or exchange
  withdrawals
* Servicing off-chain Lightning withdrawals using on-chain payments, with no
  funds in channels required
* As a failsafe payment method that can be used when channel liquidity along a
  route is insufficient

This site features the API documentation for shell script (CLI), Python and
JavaScript clients in order to communicate with a local `loopd` instance through
gRPC. Currently, this communication is unauthenticated, so exposing this service
to the internet is not recommended.

The original `*.swagger.js` files from which the gRPC documentation was generated
can be found here:

- [`client.swagger.json`](https://github.com/lightninglabs/loop/blob/a90971a697f6b2adb65d3723b6d16d472d24e87b/looprpc/client.swagger.json)


**NOTE**: The `byte` field type must be set as the base64 encoded string
representation of a raw byte array.


This is the reference for the **REST API**. Alternatively, there is also a [gRPC
API which is documented here](#loop-grpc-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`a90971a697f6b2adb65d3723b6d16d472d24e87b`](https://github.com/lightninglabs/loop/tree/a90971a697f6b2adb65d3723b6d16d472d24e87b).</small>


## /v1/loop/in


```shell
$ curl -X POST http://localhost:8080/v1/loop/in -d '{ \
    "amt":<string>, \
    "max_swap_fee":<string>, \
    "max_miner_fee":<string>, \
    "last_hop":<byte>, \
    "external_htlc":<boolean>, \
}'
{ 
    "id": <string>, 
    "id_bytes": <byte>, 
    "htlc_address": <string>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/in'
>>> data = { 
        'amt': <string>, 
        'max_swap_fee': <string>, 
        'max_miner_fee': <string>, 
        'last_hop': base64.b64encode(<byte>).decode(), 
        'external_htlc': <boolean>, 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "id": <string>, 
    "id_bytes": <byte>, 
    "htlc_address": <string>, 
}
```
```javascript
const request = require('request');
let requestBody = { 
  amt: <string>,
  max_swap_fee: <string>,
  max_miner_fee: <string>,
  last_hop: <byte>,
  external_htlc: <boolean>,
};
let options = {
  url: 'http://localhost:8080/v1/loop/in',
  json: true,
  form: JSON.stringify(requestBody)
};
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "id": <string>, 
//      "id_bytes": <byte>, 
//      "htlc_address": <string>, 
//  }
```

### POST /v1/loop/in
loop: `in` LoopIn initiates a loop in swap with the given parameters. The call returns after the swap has been set up with the swap server. From that point onwards, progress can be tracked via the SwapStatus stream that is returned from Monitor().

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
amt | string | body |  Requested swap amount in sat. This does not include the swap and miner  fee.
max_swap_fee | string | body |  Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call.
max_miner_fee | string | body |  Maximum in on-chain fees that we are willing to spent. If we want to publish the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap.   max_miner_fee is typically taken from the response of the GetQuote call.
last_hop | byte | body |  The last hop to use for the loop in swap. If empty, the last hop is selected based on the lowest routing fee for the swap payment from the server.
external_htlc | boolean | body |  If external_htlc is true, we expect the htlc to be published by an external actor.

### Response 

Field | Type | Description
----- | ---- | ----------- 
id | string |  Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | byte |  Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
htlc_address | string |  The address of the on-chain htlc.  



## /v1/loop/in/quote


```shell
$ curl -X GET http://localhost:8080/v1/loop/in/quote/{amt}
{ 
    "swap_fee": <string>, 
    "prepay_amt": <string>, 
    "miner_fee": <string>, 
    "swap_payment_dest": <byte>, 
    "cltv_delta": <int32>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/in/quote/{amt}'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "swap_fee": <string>, 
    "prepay_amt": <string>, 
    "miner_fee": <string>, 
    "swap_payment_dest": <byte>, 
    "cltv_delta": <int32>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/loop/in/quote/{amt}',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "swap_fee": <string>, 
//      "prepay_amt": <string>, 
//      "miner_fee": <string>, 
//      "swap_payment_dest": <byte>, 
//      "cltv_delta": <int32>, 
//  }
```

### GET /v1/loop/in/quote/{amt}
loop: `quote` GetQuote returns a quote for a swap with the provided parameters.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
amt | string | path |  The amount to swap in satoshis.
conf_target | int32 | query |  The confirmation target that should be used either for the sweep of the on-chain HTLC broadcast by the swap server in the case of a Loop Out, or for the confirmation of the on-chain HTLC broadcast by the swap client in the case of a Loop In.
external_htlc | boolean | query |  If external_htlc is true, we expect the htlc to be published by an external actor.
swap_publication_deadline | string | query |  The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee. This only has an effect on loop out quotes.

### Response 

Field | Type | Description
----- | ---- | ----------- 
swap_fee | string |  The fee that the swap server is charging for the swap. 
prepay_amt | string |  The part of the swap fee that is requested as a prepayment. 
miner_fee | string |  An estimate of the on-chain fee that needs to be paid to sweep the HTLC for a loop out or to pay to the HTLC for loop in. If a miner fee of 0 is returned, it means the external_htlc flag was set for a loop in and the fee estimation was skipped. If a miner fee of -1 is returned, it means lnd's wallet tried to estimate the fee but was unable to create a sample estimation transaction because not enough funds are available. An information message should be shown to the user in this case. 
swap_payment_dest | byte |  The node pubkey where the swap payment needs to be paid to. This can be used to test connectivity before initiating the swap. 
cltv_delta | int32 |  On-chain cltv expiry delta  



## /v1/loop/in/terms


```shell
$ curl -X GET http://localhost:8080/v1/loop/in/terms
{ 
    "min_swap_amount": <string>, 
    "max_swap_amount": <string>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/in/terms'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "min_swap_amount": <string>, 
    "max_swap_amount": <string>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/loop/in/terms',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "min_swap_amount": <string>, 
//      "max_swap_amount": <string>, 
//  }
```

### GET /v1/loop/in/terms
loop: `terms` GetTerms returns the terms that the server enforces for swaps.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
min_swap_amount | string |  Minimum swap amount (sat) 
max_swap_amount | string |  Maximum swap amount (sat)  



## /v1/loop/out


```shell
$ curl -X POST http://localhost:8080/v1/loop/out -d '{ \
    "amt":<string>, \
    "dest":<string>, \
    "max_swap_routing_fee":<string>, \
    "max_prepay_routing_fee":<string>, \
    "max_swap_fee":<string>, \
    "max_prepay_amt":<string>, \
    "max_miner_fee":<string>, \
    "loop_out_channel":<string>, \
    "sweep_conf_target":<int32>, \
    "swap_publication_deadline":<string>, \
}'
{ 
    "id": <string>, 
    "id_bytes": <byte>, 
    "htlc_address": <string>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/out'
>>> data = { 
        'amt': <string>, 
        'dest': <string>, 
        'max_swap_routing_fee': <string>, 
        'max_prepay_routing_fee': <string>, 
        'max_swap_fee': <string>, 
        'max_prepay_amt': <string>, 
        'max_miner_fee': <string>, 
        'loop_out_channel': <string>, 
        'sweep_conf_target': <int32>, 
        'swap_publication_deadline': <string>, 
    }
>>> r = requests.post(url, verify=cert_path, data=json.dumps(data))
>>> print(r.json())
{ 
    "id": <string>, 
    "id_bytes": <byte>, 
    "htlc_address": <string>, 
}
```
```javascript
const request = require('request');
let requestBody = { 
  amt: <string>,
  dest: <string>,
  max_swap_routing_fee: <string>,
  max_prepay_routing_fee: <string>,
  max_swap_fee: <string>,
  max_prepay_amt: <string>,
  max_miner_fee: <string>,
  loop_out_channel: <string>,
  sweep_conf_target: <int32>,
  swap_publication_deadline: <string>,
};
let options = {
  url: 'http://localhost:8080/v1/loop/out',
  json: true,
  form: JSON.stringify(requestBody)
};
request.post(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "id": <string>, 
//      "id_bytes": <byte>, 
//      "htlc_address": <string>, 
//  }
```

### POST /v1/loop/out
loop: `out` LoopOut initiates an loop out swap with the given parameters. The call returns after the swap has been set up with the swap server. From that point onwards, progress can be tracked via the SwapStatus stream that is returned from Monitor().

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
amt | string | body |  Requested swap amount in sat. This does not include the swap and miner fee.
dest | string | body |  Base58 encoded destination address for the swap.
max_swap_routing_fee | string | body |  Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call.
max_prepay_routing_fee | string | body |  Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call.
max_swap_fee | string | body |  Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call. It includes the prepay amount.
max_prepay_amt | string | body |  Maximum amount of the swap fee that may be charged as a prepayment.
max_miner_fee | string | body |  Maximum in on-chain fees that we are willing to spent. If we want to sweep the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap. If the fee estimate is lower, we publish the sweep tx.  If the sweep tx is not confirmed, we are forced to ratchet up fees until it is swept. Possibly even exceeding max_miner_fee if we get close to the htlc timeout. Because the initial publication revealed the preimage, we have no other choice. The server may already have pulled the off-chain htlc. Only when the fee becomes higher than the swap amount, we can only wait for fees to come down and hope - if we are past the timeout - that the server is not publishing the revocation.  max_miner_fee is typically taken from the response of the GetQuote call.
loop_out_channel | string | body |  The channel to loop out, the channel to loop out is selected based on the lowest routing fee for the swap payment to the server.
sweep_conf_target | int32 | body |  The number of blocks from the on-chain HTLC's confirmation height that it should be swept within.
swap_publication_deadline | string | body |  The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee.

### Response 

Field | Type | Description
----- | ---- | ----------- 
id | string |  Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release. 
id_bytes | byte |  Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. 
htlc_address | string |  The address of the on-chain htlc.  



## /v1/loop/out/quote


```shell
$ curl -X GET http://localhost:8080/v1/loop/out/quote/{amt}
{ 
    "swap_fee": <string>, 
    "prepay_amt": <string>, 
    "miner_fee": <string>, 
    "swap_payment_dest": <byte>, 
    "cltv_delta": <int32>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/out/quote/{amt}'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "swap_fee": <string>, 
    "prepay_amt": <string>, 
    "miner_fee": <string>, 
    "swap_payment_dest": <byte>, 
    "cltv_delta": <int32>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/loop/out/quote/{amt}',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "swap_fee": <string>, 
//      "prepay_amt": <string>, 
//      "miner_fee": <string>, 
//      "swap_payment_dest": <byte>, 
//      "cltv_delta": <int32>, 
//  }
```

### GET /v1/loop/out/quote/{amt}
loop: `quote` LoopOutQuote returns a quote for a loop out swap with the provided parameters.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
amt | string | path |  The amount to swap in satoshis.
conf_target | int32 | query |  The confirmation target that should be used either for the sweep of the on-chain HTLC broadcast by the swap server in the case of a Loop Out, or for the confirmation of the on-chain HTLC broadcast by the swap client in the case of a Loop In.
external_htlc | boolean | query |  If external_htlc is true, we expect the htlc to be published by an external actor.
swap_publication_deadline | string | query |  The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee. This only has an effect on loop out quotes.

### Response 

Field | Type | Description
----- | ---- | ----------- 
swap_fee | string |  The fee that the swap server is charging for the swap. 
prepay_amt | string |  The part of the swap fee that is requested as a prepayment. 
miner_fee | string |  An estimate of the on-chain fee that needs to be paid to sweep the HTLC for a loop out or to pay to the HTLC for loop in. If a miner fee of 0 is returned, it means the external_htlc flag was set for a loop in and the fee estimation was skipped. If a miner fee of -1 is returned, it means lnd's wallet tried to estimate the fee but was unable to create a sample estimation transaction because not enough funds are available. An information message should be shown to the user in this case. 
swap_payment_dest | byte |  The node pubkey where the swap payment needs to be paid to. This can be used to test connectivity before initiating the swap. 
cltv_delta | int32 |  On-chain cltv expiry delta  



## /v1/loop/out/terms


```shell
$ curl -X GET http://localhost:8080/v1/loop/out/terms
{ 
    "min_swap_amount": <string>, 
    "max_swap_amount": <string>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/out/terms'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "min_swap_amount": <string>, 
    "max_swap_amount": <string>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/loop/out/terms',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "min_swap_amount": <string>, 
//      "max_swap_amount": <string>, 
//  }
```

### GET /v1/loop/out/terms
loop: `terms` LoopOutTerms returns the terms that the server enforces for a loop out swap.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
min_swap_amount | string |  Minimum swap amount (sat) 
max_swap_amount | string |  Maximum swap amount (sat)  



## /v1/loop/swap


```shell
$ curl -X GET http://localhost:8080/v1/loop/swap/{id}
{ 
    "result": <looprpcSwapStatus>, 
    "error": <runtimeStreamError>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/swap/{id}'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "result": <looprpcSwapStatus>, 
    "error": <runtimeStreamError>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/loop/swap/{id}',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "result": <looprpcSwapStatus>, 
//      "error": <runtimeStreamError>, 
//  }
```

### GET /v1/loop/swap/{id}
loop: `swapinfo` SwapInfo returns all known details about a single swap.

Field | Type | Placement | Description
----- | ---- | --------- | ----------- 
id | string | path |  The swap identifier which currently is the hash that locks the HTLCs. When using REST, this field must be encoded as URL safe base64.

### Response 

Field | Type | Description
----- | ---- | ----------- 
result | [looprpcSwapStatus](#looprpcswapstatus) |  
error | [runtimeStreamError](#runtimestreamerror) |   



## /v1/loop/swaps


```shell
$ curl -X GET http://localhost:8080/v1/loop/swaps
{ 
    "swaps": <array looprpcSwapStatus>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/loop/swaps'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "swaps": <array looprpcSwapStatus>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/loop/swaps',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "swaps": <array looprpcSwapStatus>, 
//  }
```

### GET /v1/loop/swaps
loop: `listswaps` ListSwaps returns a list of all currently known swaps and their current status.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
swaps | [array looprpcSwapStatus](#looprpcswapstatus) |  The list of all currently known swaps and their status.  



## /v1/lsat/tokens


```shell
$ curl -X GET http://localhost:8080/v1/lsat/tokens
{ 
    "tokens": <array looprpcLsatToken>, 
}
```
```python
>>> import base64, json, requests
>>> url = 'http://localhost:8080/v1/lsat/tokens'
>>> r = requests.get(url, verify=cert_path)
>>> print(r.json())
{ 
    "tokens": <array looprpcLsatToken>, 
}
```
```javascript
const request = require('request');
let options = {
  url: 'http://localhost:8080/v1/lsat/tokens',
  json: true
};
request.get(options, function(error, response, body) {
  console.log(body);
});
// Console output:
//  { 
//      "tokens": <array looprpcLsatToken>, 
//  }
```

### GET /v1/lsat/tokens
loop: `listauth` GetLsatTokens returns all LSAT tokens the daemon ever paid for.

This request has no parameters.

### Response 

Field | Type | Description
----- | ---- | ----------- 
tokens | [array looprpcLsatToken](#looprpclsattoken) |  List of all tokens the daemon knows of, including old/expired tokens.  




# REST messages

### looprpcListSwapsResponse

Field | Type | Description
----- | ---- | ----------- 
swaps | [array looprpcSwapStatus](#looprpcswapstatus) |  The list of all currently known swaps and their status.


### looprpcLoopInRequest

Field | Type | Description
----- | ---- | ----------- 
amt | string |  Requested swap amount in sat. This does not include the swap and miner  fee.
max_swap_fee | string |  Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call.
max_miner_fee | string |  Maximum in on-chain fees that we are willing to spent. If we want to publish the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap.   max_miner_fee is typically taken from the response of the GetQuote call.
last_hop | byte |  The last hop to use for the loop in swap. If empty, the last hop is selected based on the lowest routing fee for the swap payment from the server.
external_htlc | boolean |  If external_htlc is true, we expect the htlc to be published by an external actor.


### looprpcLoopOutRequest

Field | Type | Description
----- | ---- | ----------- 
amt | string |  Requested swap amount in sat. This does not include the swap and miner fee.
dest | string |  Base58 encoded destination address for the swap.
max_swap_routing_fee | string |  Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call.
max_prepay_routing_fee | string |  Maximum off-chain fee in msat that may be paid for payment to the server. This limit is applied during path finding. Typically this value is taken from the response of the GetQuote call.
max_swap_fee | string |  Maximum we are willing to pay the server for the swap. This value is not disclosed in the swap initiation call, but if the server asks for a higher fee, we abort the swap. Typically this value is taken from the response of the GetQuote call. It includes the prepay amount.
max_prepay_amt | string |  Maximum amount of the swap fee that may be charged as a prepayment.
max_miner_fee | string |  Maximum in on-chain fees that we are willing to spent. If we want to sweep the on-chain htlc and the fee estimate turns out higher than this value, we cancel the swap. If the fee estimate is lower, we publish the sweep tx.  If the sweep tx is not confirmed, we are forced to ratchet up fees until it is swept. Possibly even exceeding max_miner_fee if we get close to the htlc timeout. Because the initial publication revealed the preimage, we have no other choice. The server may already have pulled the off-chain htlc. Only when the fee becomes higher than the swap amount, we can only wait for fees to come down and hope - if we are past the timeout - that the server is not publishing the revocation.  max_miner_fee is typically taken from the response of the GetQuote call.
loop_out_channel | string |  The channel to loop out, the channel to loop out is selected based on the lowest routing fee for the swap payment to the server.
sweep_conf_target | int32 |  The number of blocks from the on-chain HTLC's confirmation height that it should be swept within.
swap_publication_deadline | string |  The latest time (in unix seconds) we allow the server to wait before publishing the HTLC on chain. Setting this to a larger value will give the server the opportunity to batch multiple swaps together, and wait for low-fee periods before publishing the HTLC, potentially resulting in a lower total swap fee.


### looprpcLsatToken

Field | Type | Description
----- | ---- | ----------- 
base_macaroon | byte |  The base macaroon that was baked by the auth server.
payment_hash | byte |  The payment hash of the payment that was paid to obtain the token.
payment_preimage | byte |  The preimage of the payment hash, knowledge of this is proof that the payment has been paid. If the preimage is set to all zeros, this means the payment is still pending and the token is not yet fully valid.
amount_paid_msat | string |  The amount of millisatoshis that was paid to get the token.
routing_fee_paid_msat | string |  The amount of millisatoshis paid in routing fee to pay for the token.
time_created | string |  The creation time of the token as UNIX timestamp in seconds.
expired | boolean |  Indicates whether the token is expired or still valid.
storage_name | string |  Identifying attribute of this token in the store. Currently represents the file name of the token where it's stored on the file system.


### looprpcQuoteResponse

Field | Type | Description
----- | ---- | ----------- 
swap_fee | string |  The fee that the swap server is charging for the swap.
prepay_amt | string |  The part of the swap fee that is requested as a prepayment.
miner_fee | string |  An estimate of the on-chain fee that needs to be paid to sweep the HTLC for a loop out or to pay to the HTLC for loop in. If a miner fee of 0 is returned, it means the external_htlc flag was set for a loop in and the fee estimation was skipped. If a miner fee of -1 is returned, it means lnd's wallet tried to estimate the fee but was unable to create a sample estimation transaction because not enough funds are available. An information message should be shown to the user in this case.
swap_payment_dest | byte |  The node pubkey where the swap payment needs to be paid to. This can be used to test connectivity before initiating the swap.
cltv_delta | int32 |  On-chain cltv expiry delta


### looprpcSwapResponse

Field | Type | Description
----- | ---- | ----------- 
id | string |  Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs. DEPRECATED: To make the API more consistent, this field is deprecated in favor of id_bytes and will be removed in a future release.
id_bytes | byte |  Swap identifier to track status in the update stream that is returned from the Start() call. Currently this is the hash that locks the htlcs.
htlc_address | string |  The address of the on-chain htlc.


### looprpcSwapStatus

Field | Type | Description
----- | ---- | ----------- 
result | [looprpcSwapStatus](#looprpcswapstatus) | 
error | [runtimeStreamError](#runtimestreamerror) | 


### looprpcTermsResponse

Field | Type | Description
----- | ---- | ----------- 
min_swap_amount | string |  Minimum swap amount (sat)
max_swap_amount | string |  Maximum swap amount (sat)


### looprpcTokensResponse

Field | Type | Description
----- | ---- | ----------- 
tokens | [array looprpcLsatToken](#looprpclsattoken) |  List of all tokens the daemon knows of, including old/expired tokens.


### protobufAny

Field | Type | Description
----- | ---- | ----------- 
type_url | string | 
value | byte | 


### runtimeStreamError

Field | Type | Description
----- | ---- | ----------- 
grpc_code | int32 | 
http_code | int32 | 
message | string | 
http_status | string | 
details | [array protobufAny](#protobufany) | 



# REST Enums

### looprpcSwapState


Name | Value | Description
---- | ----- | ----------- 
INITIATED | 0 | INITIATED is the initial state of a swap. At that point, the initiation call to the server has been made and the payment process has been started for the swap and prepayment invoices.  
PREIMAGE_REVEALED | 1 | PREIMAGE_REVEALED is reached when the sweep tx publication is first attempted. From that point on, we should consider the preimage to no longer be secret and we need to do all we can to get the sweep confirmed. This state will mostly coalesce with StateHtlcConfirmed, except in the case where we wait for fees to come down before we sweep.  
HTLC_PUBLISHED | 2 | HTLC_PUBLISHED is reached when the htlc tx has been published in a loop in swap.  
SUCCESS | 3 | SUCCESS is the final swap state that is reached when the sweep tx has the required confirmation depth.  
FAILED | 4 | FAILED is the final swap state for a failed swap with or without loss of the swap amount.  
INVOICE_SETTLED | 5 | INVOICE_SETTLED is reached when the swap invoice in a loop in swap has been paid, but we are still waiting for the htlc spend to confirm.  

### looprpcSwapType


Name | Value | Description
---- | ----- | ----------- 
LOOP_OUT | 0 |  
LOOP_IN | 1 |   
# Other API References

This is the gRPC and REST API reference for the `loopd` daemon. There are separate API reference documents for the
following daemons:

- [LND API Reference](lnd.html)

<br/><br/><br/>