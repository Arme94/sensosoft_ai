from django import template

register = template.Library()

@register.filter
def attr(field, args):
    attrs = {}
    definition = args.split(',')
    for d in definition:
        key, val = d.split(':')
        attrs[key] = val
    return field.as_widget(attrs=attrs)
