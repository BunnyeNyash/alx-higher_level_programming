#!/usr/bin/python3
"""
    This module defines a class called BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class that provides a base for geometry-related classes.
    """

    def area(self):
        """
        This method raises an Exception indicating that
        area() is not implemented.
        """
        raise Exception("area() is not implemented")
