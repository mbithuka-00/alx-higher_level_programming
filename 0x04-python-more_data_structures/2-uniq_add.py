#!/usr/bin/python3
# AUTHOR : MATT MBITHUKA
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    number = 0

    for m in uniq_list:
        number += m

    return (number)
