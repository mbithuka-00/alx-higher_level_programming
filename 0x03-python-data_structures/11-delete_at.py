#!/usr/bin/python3
# AUTHOR : MATT MBITHUKA


def delete_at(my_list=[], idx=0):
    """Delete item at a specific place."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)


