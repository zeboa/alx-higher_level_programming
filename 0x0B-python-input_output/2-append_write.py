#!/usr/bin/python3

"""This module is for append_write."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number
    of characters added."""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
