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

{% for file in files %}- [`{{ file }}`]({{ repoUrl }}/blob/{{ commit }}/{{ rpcdir }}/{{file}})
{% endfor %}

**NOTE**: The `byte` field type must be set as the base64 encoded string
representation of a raw byte array.


This is the reference for the **REST API**. Alternatively, there is also a [gRPC
API which is documented here](#loop-grpc-api-reference).

<small>This documentation was
[generated automatically](https://github.com/lightninglabs/lightning-api) against commit
[`{{ commit }}`]({{ repoUrl }}/tree/{{ commit }}).</small>

{% for basePath, endpoints in endpoints.items() %}
## {{ basePath }}
{% for endpoint in endpoints %}

{% include 'rest/loop_shell.md' %}
{% include 'rest/loop_python.md' %}
{% include 'rest/loop_javascript.md' %}

{% include 'rest/request.md' %}
{% include 'rest/response.md' %}

{% endfor %}
{% endfor %}

# REST messages
{% for property in properties %}
{% include 'rest/property.md' %}
{% endfor %}

# REST Enums
{% for enum in enums %}
{% include 'rest/enum.md' %}
{% endfor %}
