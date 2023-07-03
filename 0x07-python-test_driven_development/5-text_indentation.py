#!/usr/bin/python3

"""This module contains a function that indents texts"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'

    Args: 
        text: The input text to be processed

    Raises: 
        TypeError: If text is not a string

    Returns: 
        None
    """

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process and print the text
    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'

    lines = result.splitlines()
    for line in lines:
        print(line.strip())
