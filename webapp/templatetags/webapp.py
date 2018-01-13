from django import template

register = template.Library()


@register.filter(name='battery_quarters')
def battery_quarters(value):
    """Returns the battery quarters for displaying a battery icon"""
    return round(value / 25.0)
