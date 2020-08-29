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

{% for file in files %}- [`{{ file }}`]({{ repoUrl }}/blob/{{ commit }}/{{ rpcdir }}/{{file}})
{% endfor %}


This is the reference for the **gRPC API**. Alternatively, there is also a [REST
API which is documented here](#loop-rest-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`{{ commit }}`]({{ repoUrl }}/tree/{{ commit }}).</small>

{% for service in services %}
# Service _{{ service.name }}_

{% for method in service_methods[service.name].methods %}
## {{ method.fullName }}

{% if not method.streamingRequest and not method.streamingResponse %}
#### Unary RPC
{% elif not method.streamingRequest and method.streamingResponse %}
#### Server-streaming RPC
{% elif method.streamingRequest and not method.streamingResponse %}
#### Client-streaming RPC
{% elif method.streamingRequest and method.streamingResponse %}
#### Bidirectional-streaming RPC
{% endif %}

{{ method.description }}

{% include 'grpc/shell.md' %}
{% include 'grpc/other_python.md' %}
{% include 'grpc/other_javascript.md' %}

{% include 'grpc/request.md' %}
{% include 'grpc/response.md' %}
{% endfor %}
{% endfor %}

# gRPC Messages
{% for messageName, message in messages.items() %}
{% include 'grpc/message.md' %}
{% endfor %}

# gRPC Enums
{% for enum in enums %}
{% include 'grpc/enum.md' %}
{% endfor %}
