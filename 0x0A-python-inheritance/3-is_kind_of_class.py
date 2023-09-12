#!/usr/bin/python3
"""Defines a function to check if an object is an instance or inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj to.
    Returns:
        True if obj is an instance or inherited instance of the specified class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False

