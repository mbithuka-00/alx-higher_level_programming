#!/usr/bin/python3
"""This script defines a function for converting a Python object to a JSON string."""
import json

def to_json_string(my_obj):
    """Convert a Python object to its JSON representation in string format.

    Args:
        my_obj (object): The Python object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the input object as a string.
    """
    return json.dumps(my_obj)

