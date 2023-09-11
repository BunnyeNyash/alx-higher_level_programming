#!/usr/bin/python3
"""
    This module defines a function that retrieves
    the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    This function takes an object as input and returns a list 
    containing all the available attributes and methods of the object.
    
    :param obj: The object to inspect.
    :return: A list of available attributes and methods.
    """
    return dir(obj)
