```shell
{% if method.subcommand and method.commandInfo %}{% for description in method.commandInfo.description %}
# {{ description }}{% endfor %}

$ {{ method.commandInfo.usage }}
{% for option in method.commandInfo.options %}
# {{ option }}{% endfor %}{% endif %}
```
