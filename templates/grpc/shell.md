```shell
{% if method.lncliCommand %}{% for description in method.lncliInfo.description %}
# {{ description }}{% endfor %}

$ {{ method.lncliInfo.usage }}
{% for option in method.lncliInfo.options %}
# {{ option }}{% endfor %}{% endif %}
```
