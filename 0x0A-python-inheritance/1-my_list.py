#!/usr/bin/python3
"""
This module defines a class called MyList that inherits from list.
"""


class MyList(list):
    """
    A class that represents a list and inherits from list.
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
