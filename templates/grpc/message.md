## {{ messageName }}
{{ message.description }}
{% if message.params | length == 0 %}
This message has no parameters.
{% else %}
Parameter | Type | Description
--------- | ---- | ----------- {% for param in message.params %}
{{ param.name }} | {% if param.link is defined %}[{{ param.type }}](#{{ param.link }}){% else %}{{ param.type }}{% endif %} | {{ param.description }} {% endfor %} {% endif %}
