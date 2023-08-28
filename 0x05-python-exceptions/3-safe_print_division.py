#!/usr/bin/python3
#auth: matt mbithuka

def safe_print_division(a, b):
    """Returns the result of  division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
