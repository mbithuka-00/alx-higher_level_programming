#!/usr/bin/python3
# author : matt mbithuka

def print_reversed_list_integer(my_list=[]):
    """ prints list in reverse."""
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
