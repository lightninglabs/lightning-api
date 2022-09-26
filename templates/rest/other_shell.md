```shell
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 ${% filter upper %}{{ component }}{% endfilter %}_DIR/regtest/{{ component }}.macaroon)"
$ curl -X {{ endpoint.type }} --cacert ${% filter upper %}{{ component }}{% endfilter %}_DIR/tls.cert --header "$MACAROON_HEADER" https:://localhost:{{ restport }}{{ endpoint.path }}{% if endpoint.type == "POST" %} -d '{ \{% for param in endpoint.requestParams %}
    "{{ param.name }}":<{{ param.type }}>, \{% endfor %}
}'{% endif %}
{ {% for param in endpoint.responseParams %}
    "{{ param.name }}": <{{ param.type }}>, {% endfor %}
}
```
