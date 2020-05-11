### {{ enum.name }}
{{ enum.description }}
{% if enum.options | length == 0 %}
This enum has no values.
{% else %}
Name | Value | Description
---- | ----- | ----------- {% for option in enum.options %}
{{ option.name }} | {{ option.value }} | {{ option.description }} {% endfor %} {% endif %}
