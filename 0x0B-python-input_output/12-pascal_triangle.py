#!/usr/bin/python3
"""
This module defines a function called pascal_triangle
that generates Pascal's triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        row = [1]  # First element in each row is always 1
        for i in range(len(tri) - 1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)  # Last element in each row is always 1
        triangles.append(row)
    return triangles
