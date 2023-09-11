#!/usr/bin/python3
"""
    This module defines a class called BaseGeometry with
    area and integer_validator methods.
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

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
