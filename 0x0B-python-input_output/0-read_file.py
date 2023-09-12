#!/usr/bin/python3
"""
This module defines a function called read_file
that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
