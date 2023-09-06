#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent your custom rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of your custom rectangle.
            height (int): The height of your custom rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of your custom Rectangle."""
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
        """Get/set the height of your custom Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of your custom Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of your custom Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Get a visual representation of your custom Rectangle.

        Represents your rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ['#' * self.__width for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Get a string representation of your custom Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Say goodbye when deleting your custom Rectangle."""
        print("Farewell, your rectangle is no more...")

