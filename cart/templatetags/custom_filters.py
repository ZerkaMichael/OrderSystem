from django import template

register = template.Library()

@register.filter
def to_float(value):
    return float(value)

@register.filter(name='mul')
def mul(value, arg):
    return value * arg