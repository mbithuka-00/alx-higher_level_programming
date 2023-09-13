#!/usr/bin/python3
# 6-from_json_string.py
"""This script defines a function for converting a JSON string to a Python object."""
import json

def from_json_string(my_str):
    """Convert a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object representation of the JSON input.
    """
    return json.loads(my_str)

