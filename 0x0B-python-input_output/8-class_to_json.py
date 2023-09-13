#!/usr/bin/python3
"""Defines a function for converting a Python class instance to a JSON-compatible dictionary."""


def class_to_json(obj):
    """Convert a Python class instance to a dictionary representation.

    Args:
        obj (object): The Python class instance to be converted.

    Returns:
        dict: A dictionary representing the object's attributes.
    """
    return obj.__dict__

