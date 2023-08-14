#!/usr/bin/python3
# matt mbithuka

def element_at(my_list, idx):
    """Retrive the  element from the list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])


