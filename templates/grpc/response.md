### gRPC Response: {{ method.responseType }} {% if method.streamingResponse %}(Streaming){% endif %}
{{ method.responseMessage.description }}
{% if method.responseMessage.params | length == 0 %}
This response has no parameters.
{% else %}
Parameter | Type | Description
--------- | ---- | ----------- {% for param in method.responseMessage.params %}
{{ param.name }} | {% if param.link is defined %}[{{ param.type }}](#{{ param.link }}){% else %}{{ param.type }}{% endif %} | {{ param.description }} {% endfor %} {% endif %}
