#!/usr/bin/python3
"""This is a module for to_json_string."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
