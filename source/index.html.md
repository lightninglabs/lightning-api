---
title: API Reference

language_tabs:
  - shell
  - python

toc_footers:
  - <a href='http://dev.lightning.community'>Developer site</a>
  - <a href='mailto:max@lightning.engineering'>Contact Us</a>
  - <a href='https://github.com/tripit/slate'>Documentation Powered by Slate</a>

includes:

search: true
---

# Introduction

Welcome to the API documentation for LND, the Lightning Network
Daemon.

This page serves purely as a reference, generally for those who already
understand how to work with LND. If this is your first time, please check out
our [developer site](https://dev.lightning.community) and
[tutorial](https://dev.lightning.community/tutorial).

This site features API documentation for command line arguments, gRPC in Python
and Javscript, and the gRPC REST proxy.



# WalletBalance



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.WalletBalance(ln.WalletBalanceRequest(
        witness_only=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    balance: <int64>,
}

```

### WalletBalanceRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
witness_only | bool | optional |  


### WalletBalanceResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
balance | int64 | optional |  




# ChannelBalance



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.ChannelBalance(ln.ChannelBalanceRequest())

```

> `response` will be structured similar to this:

```python

{ 
    balance: <int64>,
}

```

### ChannelBalanceRequest


This request has no parameters.


### ChannelBalanceResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
balance | int64 | optional |  




# GetTransactions



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.GetTransactions(ln.GetTransactionsRequest())

```

> `response` will be structured similar to this:

```python

{ 
    transactions: <Transaction>,
}

```

### GetTransactionsRequest


This request has no parameters.


### TransactionDetails


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
transactions | Transaction | repeated |  




# SendCoins



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.SendCoins(ln.SendCoinsRequest(
        addr=<YOUR_PARAM>,
        amount=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    txid: <string>,
}

```

### SendCoinsRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
addr | string | optional |  
amount | int64 | optional |  


### SendCoinsResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
txid | string | optional |  




# SubscribeTransactions



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.SubscribeTransactions(ln.GetTransactionsRequest())

```

> `response` will be structured similar to this:

```python

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

### GetTransactionsRequest


This request has no parameters.


### Transaction


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
tx_hash | string | optional |  
amount | int64 | optional |  
num_confirmations | int32 | optional |  
block_hash | string | optional |  
block_height | int32 | optional |  
time_stamp | int64 | optional |  
total_fees | int64 | optional |  




# SendMany



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.SendMany(ln.SendManyRequest(
        AddrToAmount=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    txid: <string>,
}

```

### SendManyRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
AddrToAmount | AddrToAmountEntry | repeated |  


### SendManyResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
txid | string | optional |  




# NewAddress



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.NewAddress(ln.NewAddressRequest(
        type=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    address: <string>,
}

```

### NewAddressRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
type | AddressType | optional |  


### NewAddressResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
address | string | optional |  




# NewWitnessAddress



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.NewWitnessAddress(ln.NewWitnessAddressRequest())

```

> `response` will be structured similar to this:

```python

{ 
    address: <string>,
}

```

### NewWitnessAddressRequest


This request has no parameters.


### NewAddressResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
address | string | optional |  




# SignMessage



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.SignMessage(ln.SignMessageRequest(
        msg=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    signature: <string>,
}

```

### SignMessageRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
msg | bytes | optional |  


### SignMessageResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
signature | string | optional |  




# VerifyMessage



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.VerifyMessage(ln.VerifyMessageRequest(
        msg=<YOUR_PARAM>,
        signature=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    valid: <bool>,
    pubkey: <string>,
}

```

### VerifyMessageRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
msg | bytes | optional |  
signature | string | optional |  


### VerifyMessageResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
valid | bool | optional |  
pubkey | string | optional |  




# ConnectPeer



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.ConnectPeer(ln.ConnectPeerRequest(
        addr=<YOUR_PARAM>,
        perm=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    peer_id: <int32>,
}

```

### ConnectPeerRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
addr | LightningAddress | optional |  
perm | bool | optional |  


### ConnectPeerResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
peer_id | int32 | optional |  




# DisconnectPeer



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.DisconnectPeer(ln.DisconnectPeerRequest(
        pub_key=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{}

```

### DisconnectPeerRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional |  


### DisconnectPeerResponse


This response is empty.




# ListPeers



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.ListPeers(ln.ListPeersRequest())

```

> `response` will be structured similar to this:

```python

{ 
    peers: <Peer>,
}

```

### ListPeersRequest


This request has no parameters.


### ListPeersResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
peers | Peer | repeated |  




# GetInfo



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.GetInfo(ln.GetInfoRequest())

```

> `response` will be structured similar to this:

```python

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

### GetInfoRequest


This request has no parameters.


### GetInfoResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
identity_pubkey | string | optional |  
alias | string | optional |  
num_pending_channels | uint32 | optional |  
num_active_channels | uint32 | optional |  
num_peers | uint32 | optional |  
block_height | uint32 | optional |  
block_hash | string | optional |  
synced_to_chain | bool | optional |  
testnet | bool | optional |  
chains | string | repeated |  




# PendingChannels



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.PendingChannels(ln.PendingChannelRequest())

```

> `response` will be structured similar to this:

```python

{ 
    total_limbo_balance: <int64>,
    pending_open_channels: <PendingOpenChannel>,
    pending_closing_channels: <ClosedChannel>,
    pending_force_closing_channels: <ForceClosedChannel>,
}

```

### PendingChannelRequest


This request has no parameters.


### PendingChannelResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
total_limbo_balance | int64 | optional |  
pending_open_channels | PendingOpenChannel | repeated |  
pending_closing_channels | ClosedChannel | repeated |  
pending_force_closing_channels | ForceClosedChannel | repeated |  




# ListChannels



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.ListChannels(ln.ListChannelsRequest())

```

> `response` will be structured similar to this:

```python

{ 
    channels: <ActiveChannel>,
}

```

### ListChannelsRequest


This request has no parameters.


### ListChannelsResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channels | ActiveChannel | repeated |  




# OpenChannelSync



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.OpenChannelSync(ln.OpenChannelRequest(
        target_peer_id=<YOUR_PARAM>,
        node_pubkey=<YOUR_PARAM>,
        node_pubkey_string=<YOUR_PARAM>,
        local_funding_amount=<YOUR_PARAM>,
        push_sat=<YOUR_PARAM>,
        num_confs=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    funding_txid: <bytes>,
    funding_txid_str: <string>,
    output_index: <uint32>,
}

```

### OpenChannelRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
target_peer_id | int32 | optional |  
node_pubkey | bytes | optional |  
node_pubkey_string | string | optional |  
local_funding_amount | int64 | optional |  
push_sat | int64 | optional |  
num_confs | uint32 | optional |  


### ChannelPoint


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
funding_txid | bytes | optional |  
funding_txid_str | string | optional |  
output_index | uint32 | optional |  




# OpenChannel



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.OpenChannel(ln.OpenChannelRequest(
        target_peer_id=<YOUR_PARAM>,
        node_pubkey=<YOUR_PARAM>,
        node_pubkey_string=<YOUR_PARAM>,
        local_funding_amount=<YOUR_PARAM>,
        push_sat=<YOUR_PARAM>,
        num_confs=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    chan_pending: <PendingUpdate>,
    confirmation: <ConfirmationUpdate>,
    chan_open: <ChannelOpenUpdate>,
}

```

### OpenChannelRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
target_peer_id | int32 | optional |  
node_pubkey | bytes | optional |  
node_pubkey_string | string | optional |  
local_funding_amount | int64 | optional |  
push_sat | int64 | optional |  
num_confs | uint32 | optional |  


### OpenStatusUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
chan_pending | PendingUpdate | optional |  
confirmation | ConfirmationUpdate | optional |  
chan_open | ChannelOpenUpdate | optional |  




# CloseChannel



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.CloseChannel(ln.CloseChannelRequest(
        channel_point=<YOUR_PARAM>,
        time_limit=<YOUR_PARAM>,
        force=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    close_pending: <PendingUpdate>,
    confirmation: <ConfirmationUpdate>,
    chan_close: <ChannelCloseUpdate>,
}

```

### CloseChannelRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel_point | ChannelPoint | optional |  
time_limit | int64 | optional |  
force | bool | optional |  


### CloseStatusUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
close_pending | PendingUpdate | optional |  
confirmation | ConfirmationUpdate | optional |  
chan_close | ChannelCloseUpdate | optional |  




# SendPayment



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.SendPayment(ln.SendRequest(
        dest=<YOUR_PARAM>,
        dest_string=<YOUR_PARAM>,
        amt=<YOUR_PARAM>,
        payment_hash=<YOUR_PARAM>,
        payment_hash_string=<YOUR_PARAM>,
        payment_request=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    payment_error: <string>,
    payment_preimage: <bytes>,
    payment_route: <Route>,
}

```

### SendRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
dest | bytes | optional |  
dest_string | string | optional |  
amt | int64 | optional |  
payment_hash | bytes | optional |  
payment_hash_string | string | optional |  
payment_request | string | optional |  


### SendResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payment_error | string | optional |  
payment_preimage | bytes | optional |  
payment_route | Route | optional |  




# SendPaymentSync



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.SendPaymentSync(ln.SendRequest(
        dest=<YOUR_PARAM>,
        dest_string=<YOUR_PARAM>,
        amt=<YOUR_PARAM>,
        payment_hash=<YOUR_PARAM>,
        payment_hash_string=<YOUR_PARAM>,
        payment_request=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    payment_error: <string>,
    payment_preimage: <bytes>,
    payment_route: <Route>,
}

```

### SendRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
dest | bytes | optional |  
dest_string | string | optional |  
amt | int64 | optional |  
payment_hash | bytes | optional |  
payment_hash_string | string | optional |  
payment_request | string | optional |  


### SendResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payment_error | string | optional |  
payment_preimage | bytes | optional |  
payment_route | Route | optional |  




# AddInvoice



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.AddInvoice(ln.Invoice(
        memo=<YOUR_PARAM>,
        receipt=<YOUR_PARAM>,
        r_preimage=<YOUR_PARAM>,
        r_hash=<YOUR_PARAM>,
        value=<YOUR_PARAM>,
        settled=<YOUR_PARAM>,
        creation_date=<YOUR_PARAM>,
        settle_date=<YOUR_PARAM>,
        payment_request=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    r_hash: <bytes>,
    payment_request: <string>,
}

```

### Invoice


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional |  
receipt | bytes | optional |  
r_preimage | bytes | optional |  
r_hash | bytes | optional |  
value | int64 | optional |  
settled | bool | optional |  
creation_date | int64 | optional |  
settle_date | int64 | optional |  
payment_request | string | optional |  


### AddInvoiceResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
r_hash | bytes | optional |  
payment_request | string | optional |  




# ListInvoices



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.ListInvoices(ln.ListInvoiceRequest(
        pending_only=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    invoices: <Invoice>,
}

```

### ListInvoiceRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pending_only | bool | optional |  


### ListInvoiceResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
invoices | Invoice | repeated |  




# LookupInvoice



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.LookupInvoice(ln.PaymentHash(
        r_hash_str=<YOUR_PARAM>,
        r_hash=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

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

### PaymentHash


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
r_hash_str | string | optional |  
r_hash | bytes | optional |  


### Invoice


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional |  
receipt | bytes | optional |  
r_preimage | bytes | optional |  
r_hash | bytes | optional |  
value | int64 | optional |  
settled | bool | optional |  
creation_date | int64 | optional |  
settle_date | int64 | optional |  
payment_request | string | optional |  




# SubscribeInvoices



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.SubscribeInvoices(ln.InvoiceSubscription())

```

> `response` will be structured similar to this:

```python

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

### InvoiceSubscription


This request has no parameters.


### Invoice


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
memo | string | optional |  
receipt | bytes | optional |  
r_preimage | bytes | optional |  
r_hash | bytes | optional |  
value | int64 | optional |  
settled | bool | optional |  
creation_date | int64 | optional |  
settle_date | int64 | optional |  
payment_request | string | optional |  




# DecodePayReq



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.DecodePayReq(ln.PayReqString(
        pay_req=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    destination: <string>,
    payment_hash: <string>,
    num_satoshis: <int64>,
}

```

### PayReqString


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pay_req | string | optional |  


### PayReq


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
destination | string | optional |  
payment_hash | string | optional |  
num_satoshis | int64 | optional |  




# ListPayments



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.ListPayments(ln.ListPaymentsRequest())

```

> `response` will be structured similar to this:

```python

{ 
    payments: <Payment>,
}

```

### ListPaymentsRequest


This request has no parameters.


### ListPaymentsResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
payments | Payment | repeated |  




# DeleteAllPayments



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.DeleteAllPayments(ln.DeleteAllPaymentsRequest())

```

> `response` will be structured similar to this:

```python

{}

```

### DeleteAllPaymentsRequest


This request has no parameters.


### DeleteAllPaymentsResponse


This response is empty.




# DescribeGraph



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.DescribeGraph(ln.ChannelGraphRequest())

```

> `response` will be structured similar to this:

```python

{ 
    nodes: <LightningNode>,
    edges: <ChannelEdge>,
}

```

### ChannelGraphRequest


This request has no parameters.


### ChannelGraph


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
nodes | LightningNode | repeated |  
edges | ChannelEdge | repeated |  




# GetChanInfo



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.GetChanInfo(ln.ChanInfoRequest(
        chan_id=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

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

### ChanInfoRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
chan_id | uint64 | optional |  


### ChannelEdge


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
channel_id | uint64 | optional |  
chan_point | string | optional |  
last_update | uint32 | optional |  
node1_pub | string | optional |  
node2_pub | string | optional |  
capacity | int64 | optional |  
node1_policy | RoutingPolicy | optional |  
node2_policy | RoutingPolicy | optional |  




# GetNodeInfo



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.GetNodeInfo(ln.NodeInfoRequest(
        pub_key=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    node: <LightningNode>,
    num_channels: <uint32>,
    total_capacity: <int64>,
}

```

### NodeInfoRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional |  


### NodeInfo


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
node | LightningNode | optional |  
num_channels | uint32 | optional |  
total_capacity | int64 | optional |  




# QueryRoutes



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.QueryRoutes(ln.QueryRoutesRequest(
        pub_key=<YOUR_PARAM>,
        amt=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    routes: <Route>,
}

```

### QueryRoutesRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
pub_key | string | optional |  
amt | int64 | optional |  


### QueryRoutesResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
routes | Route | repeated |  




# GetNetworkInfo



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.GetNetworkInfo(ln.NetworkInfoRequest())

```

> `response` will be structured similar to this:

```python

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

### NetworkInfoRequest


This request has no parameters.


### NetworkInfo


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



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.StopDaemon(ln.StopRequest())

```

> `response` will be structured similar to this:

```python

{}

```

### StopRequest


This request has no parameters.


### StopResponse


This response is empty.




# SubscribeChannelGraph



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)

>>> response = stub.SubscribeChannelGraph(ln.GraphTopologySubscription())

```

> `response` will be structured similar to this:

```python

{ 
    node_updates: <NodeUpdate>,
    channel_updates: <ChannelEdgeUpdate>,
    closed_chans: <ClosedChannelUpdate>,
}

```

### GraphTopologySubscription


This request has no parameters.


### GraphTopologyUpdate


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
node_updates | NodeUpdate | repeated |  
channel_updates | ChannelEdgeUpdate | repeated |  
closed_chans | ClosedChannelUpdate | repeated |  




# SetAlias



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.SetAlias(ln.SetAliasRequest(
        new_alias=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{}

```

### SetAliasRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
new_alias | string | optional |  


### SetAliasResponse


This response is empty.




# DebugLevel



```shell
```

```python
>>> import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
>>> import grpc
>>> channel = grpc.insecure_channel('localhost:10009')
>>> stub = lnrpc.LightningStub(channel)
>>> response = stub.DebugLevel(ln.DebugLevelRequest(
        show=<YOUR_PARAM>,
        level_spec=<YOUR_PARAM>,
    ))

```

> `response` will be structured similar to this:

```python

{ 
    sub_systems: <string>,
}

```

### DebugLevelRequest


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
show | bool | optional |  
level_spec | string | optional |  


### DebugLevelResponse


Field | Type | Label | Description
----- | ---- | ----- | ----------- 
sub_systems | string | optional |  


