#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of your new rectangle.
            height (int): The height of your new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of your Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of your Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    @property
    def area(self):
        """Calculate the area of your Rectangle."""
        return self.__width * self.__height

    @property
    def perimeter(self):
        """Calculate the perimeter of your Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Get a visual representation of your Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ['#' * self.__width for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Get a string representation of your Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
