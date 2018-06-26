### {{ endpoint.type }} {{ endpoint.path }}
{{ endpoint.description }}
{% if endpoint.requestParams|length == 0 %}
This request has no parameters.
{% else %}
Field | Type | Placement | Description
----- | ---- | --------- | ----------- {% for param in endpoint.requestParams %}
{{ param.name }} | {% if param.link is defined %}[{{ param.type }}](#{{ param.link }}){% else %}{{ param.type }}{% endif %} | {{ param.placement }} | {{ param.description }}{% endfor %}
{% endif %}
