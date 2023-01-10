#!/usr/bin/python3

"""A module for load_from_json_file."""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
