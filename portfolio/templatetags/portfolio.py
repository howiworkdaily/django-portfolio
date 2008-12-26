from django import template
register = template.Library()

def split(value, splitter):
    return value.split(splitter)

register.filter("split",split)
