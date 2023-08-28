#!/usr/bin/python3
#author : matt mbithuka

def magic_calculation(a, b):
    result = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            else:
                result += a ** b / m
        except:
            result = b + a
            break
    return (result)
