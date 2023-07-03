#!/usr/bin/python3

"""This module is composed by a function that adds two numbers"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises: 
        TypeError: If a or b is not an integer or float.
                   If a is a float, it will be casted to an integer.
                   If b is a float, it will be casted to an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
