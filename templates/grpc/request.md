### gRPC Request: [{{ method.requestFullType }} {% if method.streamingRequest %}(Streaming){% endif %}]({{ gitHubUrl }}/blob/{{ commit }}/lnrpc/{{method.requestMessage.file}}#L{{method.requestMessage.line}})
{{ method.requestMessage.description }}
{% if method.requestMessage.params|length == 0 %}
This request has no parameters.
{% else %}
Parameter | Type | Description
--------- | ---- | ----------- {% for param in method.requestMessage.params %}
{{ param.name }} | {% if param.link is defined %}[{{ param.type }}](#{{ param.link }}){% else %}{{ param.type }}{% endif %} | {{ param.description }} {% endfor %} {% endif %}
