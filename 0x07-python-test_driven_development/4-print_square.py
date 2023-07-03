#!/usr/bin/python3
"""This module contain a function that prints a square"""

def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero

    Returns: 
        None
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")


    # Check if size is a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")


    # Print the square
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
