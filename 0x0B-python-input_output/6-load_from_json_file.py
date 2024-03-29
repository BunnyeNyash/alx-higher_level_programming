#!/usr/bin/python3
"""
This module defines a function called load_from_json_file
that loads an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The object loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
