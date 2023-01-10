#!/usr/bin/python3

"""This is a module for write_file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written."""
    with open(filename, 'w') as f:
        return f.write(text)
