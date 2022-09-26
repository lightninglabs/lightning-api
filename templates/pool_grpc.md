# Pool gRPC API Reference

Welcome to the gRPC API reference documentation for Lightning Pool.

Lightning Pool is a non-custodial batched uniform clearing-price auction for
Lightning Channel Lease (LCL). A LCL packages up inbound (or outbound!) channel
liquidity (ability to send/receive funds) as a fixed incoming asset (earning
interest over time) with a maturity date expressed in blocks. The maturity date
of each of the channels is enforced by Bitcoin contracts, ensuring that the
funds of the maker (the party that sold the channel) can't be swept until the
maturity height. All cleared orders (purchased channels) are cleared in a
single batched on-chain transaction.

This repository is home to the Pool client and depends on the Lightning Network
daemon lnd. All of lnd’s supported chain backends are fully supported when
using the Pool client: Neutrino, Bitcoin Core, and btcd.

The service can be used in various situations:

* Bootstrapping new users with side car channels
* Bootstrapping new services to Lightning
* Demand fueled routing node channel selection
* Allowing users to instantly receive with a wallet

This site features the documentation for pool (CLI), and the API documentation
for Python and JavaScript clients in order to communicate with a local `poold`
instance through gRPC.

The examples to the right assume that the there is a local `poold` instance
running and listening for gRPC connections on port {{ grpcport }}. `POOL_DIR`
will be used as a placeholder to denote the base directory of the `poold`
instance. By default, this is `~/.pool` on Linux and
`~/Library/Application Support/Pool` on macOS.

At the time of writing this documentation, two things are needed in order to
make a gRPC request to a `pool` instance: a TLS/SSL connection and a macaroon
used for RPC authentication. The examples to the right will show how these can
be used in order to make a successful, secure, and authenticated gRPC request.

The original `*.proto` files from which the gRPC documentation was generated
can be found here:

{% for file in files %}- [`{{ file }}`]({{ repoUrl }}/blob/{{ commit }}/{{ rpcdir }}/{{file}})
{% endfor %}


This is the reference for the **gRPC API**. Alternatively, there is also a [REST
API which is documented here](#pool-rest-api-reference).

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
