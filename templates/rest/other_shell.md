```shell
$ curl -X {{ endpoint.type }} http://localhost:{{ restport }}{{ endpoint.path }}{% if endpoint.type == "POST" %} -d '{ \{% for param in endpoint.requestParams %}
    "{{ param.name }}":<{{ param.type }}>, \{% endfor %}
}'{% endif %}
{ {% for param in endpoint.responseParams %}
    "{{ param.name }}": <{{ param.type }}>, {% endfor %}
}
```
