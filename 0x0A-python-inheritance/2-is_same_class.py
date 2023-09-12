#!/usr/bin/python3
"""Defines a function to check if an object belongs to a specific class."""


def is_same_class(obj, a_class):
    """Check if an object belongs to a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj to.
    Returns:
        True if obj belongs to the specified class, otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False

