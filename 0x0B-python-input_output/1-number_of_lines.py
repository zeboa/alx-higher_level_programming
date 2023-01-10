#!/usr/bin/python3

"""This module is for number_of_lines."""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file."""
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
        return lines
