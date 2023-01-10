#!/usr/bin/python3

"""A module pascal_triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of
    n."""
    if n <= 0:
        return ""

    pascal = [[1]]
    for cur_row in range(1, n):
        row = [1]
        prev_row = pascal[cur_row - 1]
        for elem in range(1, cur_row):
            row.append(prev_row[elem] + prev_row[elem - 1])
        row.append(1)
        pascal.append(row)
    return pascal
