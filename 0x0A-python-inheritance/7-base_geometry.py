#!/usr/bin/python3
"""Defines a base geometry class called BaseGeometry."""


class BaseGeometry:
    """Represents basic geometry operations."""

    def area(self):
        """Calculate the area of a geometric shape.

        This method is not yet implemented and should be overridden in subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

