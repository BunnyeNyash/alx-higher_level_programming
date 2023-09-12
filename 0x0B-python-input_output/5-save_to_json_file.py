#!/usr/bin/python3
"""
This module defines a function called save_to_json_file
that saves an object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the text file to save the object to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
