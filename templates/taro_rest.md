# Taro REST API Reference

Welcome to the gRPC API reference documentation for Taro.

The Taro Daemon `tarod` implements the [Taro
protocol](https://github.com/Roasbeef/bips/blob/bip-taro/bip-taro.mediawiki) for
issuing assets on the Bitcoin blockchain. Taro leverages Taproot transactions to
commit to newly created assets and their transfers in an efficient and scalable
manner. Multiple assets can be created and transferred in a single bitcoin UTXO,
while witness data is transacted and kept off-chain.

**Features**:

- Mint assets
- Send and receive assets
- Export and import Taro proofs
- Create and manage profiles

This site features the API documentation for shell script (CLI), Python and
JavaScript clients in order to communicate with a local `tarod` instance through
gRPC.

The examples to the right assume that the there is a local `tarod` instance
running and listening for REST connections on port {{ restport }}. `TARO_DIR`
will be used as a placeholder to denote the base directory of the `tarod`
instance. By default, this is `~/.taro` on Linux and
`~/Library/Application Support/Taro` on macOS.

At the time of writing this documentation, two things are needed in order to
make an HTTP request to an `tarod` instance: a TLS/SSL connection and a
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
API which is documented here](#taro-grpc-api-reference).

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
