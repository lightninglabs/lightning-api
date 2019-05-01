## {{ enumName }}
{{ enum.description }}

Alias            | Code               | Description
---------------- | ------------------ | ----------- {% for param in enum.params %}
<code>{{ param.name }}</code> | <code>{{ param.number }}</code> | {{ param.description }} {% endfor %}
