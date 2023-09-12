#!/usr/bin/python3
"""Defines a function for checking if an object inherits from a specific class."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherits from another class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj to.
        
    Returns:
        True if obj is an instance of a class that inherits from a_class, 
        but not if obj is an instance of a_class itself. Otherwise, False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

