### gRPC Response: [{{ method.responseFullType }} {% if method.streamingResponse %}(Streaming){% endif %}]({{ gitHubUrl }}/blob/{{ commit }}/lnrpc/{{method.responseMessage.file}}#L{{method.responseMessage.line}})
{{ method.responseMessage.description }}
{% if method.responseMessage.params | length == 0 %}
This response has no parameters.
{% else %}
Parameter | Type | Description
--------- | ---- | ----------- {% for param in method.responseMessage.params %}
{{ param.name }} | {% if param.link is defined %}[{{ param.type }}](#{{ param.link }}){% else %}{{ param.type }}{% endif %} | {{ param.description }} {% endfor %} {% endif %}
