#!/usr/bin/python3

"""This is a module for read_file."""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as f:
        read_result = f.read()
        print(read_result, end="")
