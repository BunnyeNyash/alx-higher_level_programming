#!/usr/bin/python3
"""
    This module defines a function that checks if an object
    is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    This function checks if the given object is exactly
    an instance of the specified class.
    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class, else False.
    """
    return (type(obj) == a_class)
