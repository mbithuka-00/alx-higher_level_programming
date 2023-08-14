#!/usr/bin/python3
# AUTHOR : MATTHEW MBITHUKA


def max_integer(my_list=[]):
    """Find the largest integer of a list."""
    if len(my_list) == 0:
        return (None)

    large = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > large:
            large = my_list[i]

    return (large)


