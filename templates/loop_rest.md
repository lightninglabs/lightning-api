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
gRPC.

The examples to the right assume that the there is a local `loopd` instance
running and listening for REST connections on port {{ restport }}. `LOOP_DIR`
will be used as a placeholder to denote the base directory of the `loopd`
instance. By default, this is `~/.loop` on Linux and
`~/Library/Application Support/Loop` on macOS.

At the time of writing this documentation, two things are needed in order to
make an HTTP request to an `loopd` instance: a TLS/SSL connection and a
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
API which is documented here](#loop-grpc-api-reference).

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
