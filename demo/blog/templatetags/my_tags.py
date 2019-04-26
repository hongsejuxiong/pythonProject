
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def simpleTagFunc(v1, v2, v3):

    return v1 + v2 + v3

@register.filter
def filterFunc(v1, v2):
    return v1 + v2