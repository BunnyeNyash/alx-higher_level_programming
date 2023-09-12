#!/usr/bin/python3
"""
This module defines a function called append_after that inserts a line of text
to a file after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file
    after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text
        to insert after lines containing search_string.
    """
    updated_lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)
    with open(filename, "w") as file:
        file.writelines(updated_lines)
