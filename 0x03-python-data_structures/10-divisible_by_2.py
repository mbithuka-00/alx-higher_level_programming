#!/usr/bin/python3
# AUTHOR : MATHEW MBITHUKA


def divisible_by_2(my_list=[]):
    """Find numbers divisible by 2."""
    divisible = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisible.append(True)
        else:
            divisble.append(False)

    return (divisible)


