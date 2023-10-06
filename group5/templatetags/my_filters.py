from django import template

register = template.Library()


@register.filter("mobli")
def mobli(conet):
    return conet[:3] + "*****" + conet[-3:]
