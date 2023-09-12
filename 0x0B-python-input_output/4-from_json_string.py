#!/usr/bin/python3
"""
This module defines a function called from_json_string
that parses a JSON string and returns a Python object.
"""

import json


def from_json_string(my_str):
    """
    Parses a JSON string and returns a Python object.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
