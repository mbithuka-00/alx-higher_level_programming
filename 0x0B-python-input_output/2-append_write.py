#!/usr/bin/python3
"""This script defines a function for appending text to a file."""


def append_to_file(filename="", text=""):
    """Append the provided text string to the end of a text file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to which to append.
        text (str): The text content to be appended to the file.
    Returns:
        int: The number of characters successfully appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

