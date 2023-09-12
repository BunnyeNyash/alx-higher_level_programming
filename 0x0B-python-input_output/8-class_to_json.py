#!/usr/bin/python3
"""
This module defines a function to convert a class object to
a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Converts a class object to a JSON-serializable dictionary.

    Args:
        obj: The instance of the class to convert.

    Returns:
        dict: A dictionary containing the serializable attributes
        of the object.
    """
    return obj.__dict__
