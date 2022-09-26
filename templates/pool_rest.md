# Pool REST API Reference

Welcome to the REST API reference documentation for Lightning Pool.

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

This site features the API documentation for shell script (CLI), Python and
JavaScript clients in order to communicate with a local `poold` instance through
gRPC.

The examples to the right assume that the there is a local `poold` instance
running and listening for REST connections on port {{ restport }}. `POOL_DIR`
will be used as a placeholder to denote the base directory of the `poold`
instance. By default, this is `~/.pool` on Linux and
`~/Library/Application Support/Pool` on macOS.

At the time of writing this documentation, two things are needed in order to
make an HTTP request to an `poold` instance: a TLS/SSL connection and a
macaroon used for RPC authentication. The examples to the right will show how
these can be used in order to make a successful, secure, and authenticated HTTP
request.

The original `*.swagger.js` files from which the gRPC documentation was generated
can be found here:

{% for file in files %}- [`{{ file }}`]({{ repoUrl }}/blob/{{ commit }}/{{ rpcdir }}/{{file}})
{% endfor %}

**NOTE**: The `byte` field type must be set as the base64 encoded string
representation of a raw byte array. Also, any time this must be used in a URL path
(ie. `/v1/abc/xyz/{payment_hash}`) the base64 string must be encoded using a
[URL and Filename Safe Alphabet](https://tools.ietf.org/html/rfc4648#section-5). This means you must replace `+` with `-`,
`/` with `_`, and keep the trailing `=` as is. Url encoding (ie. `%2F`) will not work.


This is the reference for the **REST API**. Alternatively, there is also a [gRPC
API which is documented here](#pool-grpc-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`{{ commit }}`]({{ repoUrl }}/tree/{{ commit }}).</small>

{% for basePath, endpoints in endpoints.items() %}
## {{ basePath }}
{% for endpoint in endpoints %}

{% include 'rest/other_shell.md' %}
{% include 'rest/other_python.md' %}
{% include 'rest/other_javascript.md' %}

{% include 'rest/request.md' %}
{% include 'rest/response.md' %}

{% endfor %}
{% endfor %}

# REST Messages
{% for property in properties %}
{% include 'rest/property.md' %}
{% endfor %}

# REST Enums
{% for enum in enums %}
{% include 'rest/enum.md' %}
{% endfor %}
