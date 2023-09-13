#!/usr/bin/python3
"""This script defines a function for writing text to a file."""


def write_to_file(filename="", text=""):
    """Write the provided text string to a text file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to which to write.
        text (str): The text content to be written to the file.
    Returns:
        int: The number of characters successfully written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

