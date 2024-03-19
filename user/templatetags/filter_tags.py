import re
from django import template


register = template.Library()
TEMPLATE_STRING_IF_INVALID = ""


@register.filter(name="nice_str")
def nice_str(value: str):
    words = value.replace("_", " ").strip().split(" ")
    return " ".join([word.capitalize() for word in words])


@register.filter(name="getattribute")
def getattribute(value, arg):
    """
    Gets an attribute of an object dynamically from a string name
    """
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif re.compile("^\d+$").match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return TEMPLATE_STRING_IF_INVALID
    