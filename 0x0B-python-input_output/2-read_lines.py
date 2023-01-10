#!/usr/bin/python3

"""This module is for read_lines."""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for i in range(nb_lines):
                print(f.readline(), end="")
