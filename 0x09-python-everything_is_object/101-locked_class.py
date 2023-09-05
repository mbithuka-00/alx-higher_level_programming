#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes named 'first_name'.
    """

    __slots__ = ["first_name"]

