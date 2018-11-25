from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """

    :param value: The value from the context dictionary in the views.py file
    :param arg: The substring
    :return: Cuts out all values of 'arg' from the string!
    """
    return value.replace(arg, '')


# register.filter('cut', cut)
