#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        last_row = triangles[-1]
        new_row = [1]
        for m in range(len(last_row) - 1):
            new_row.append(last_row[m] + last_row[m + 1])
        new_row.append(1)
        triangles.append(new_row)
    return triangles

