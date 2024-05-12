#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        A peak value from the list, or None if the list is empty.
    """

    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    left = 0
    right = length - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
