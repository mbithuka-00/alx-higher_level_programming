#!/usr/bin/python3
#author: matt mbithuka


import sys


def safe_print_integer_err(value):
    """Prints an integer with this format "{:d}".format().

    If a ValueError message is caught, a corresponding meessage is 
    sent

    Args:
        value (int): The integer to be  printed.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
