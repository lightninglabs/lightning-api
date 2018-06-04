### Response {% if endpoint.isStreaming %}(streaming){% endif %}
{% if endpoint.responseParams|length == 0 %}
This response has no parameters.
{% else %}
Field | Type | Description
----- | ---- | ----------- {% for param in endpoint.responseParams %}
{{ param.name }} | {% if param.link is defined %}[{{ param.type }}](#{{ param.link }}){% else %}{{ param.type }}{% endif %} | {{ param.description }} {% endfor %} {% endif %}
