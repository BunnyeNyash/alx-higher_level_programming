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

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1
        if i > 0:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
