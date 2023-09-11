#!/usr/bin/python3
"""
    This module defines a function that checks if an object
    is an instance of, or inherits from, a specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    This function checks if the given object is an instance of, or inherits from, the specified class.
    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of or inherits from a_class, else False.
    """
    return (isinstance(obj, a_class))
