#!/usr/bin/python3
"""
    This module defines a function that checks if an object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class.
"""


def inherits_from(obj, a_class):
    """
    This function checks if the given object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj inherits from a_class, else False.
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
