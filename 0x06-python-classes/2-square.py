#author: matt mbithuka
#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the generated square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be of  integer type")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size