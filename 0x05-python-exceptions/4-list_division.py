#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element to element.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): The number of elements to be  divided.

    Returns:
        A new list of length list_length containing all the results.
    """
    new_list = []
    for m in range(0, list_length):
        try:
            div = my_list_1[m] / my_list_2[m]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
