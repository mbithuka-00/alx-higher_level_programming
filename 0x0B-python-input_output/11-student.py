#!/usr/bin/python3
"""Defines a class Student for representing student information."""


class Student:
    """Represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list): (Optional) A list of attributes to include in the representation.

        Returns:
            dict: A dictionary containing the specified attributes and their values.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student using a dictionary.

        Args:
            json (dict): A dictionary containing key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)

