#!/usr/bin/python3
# author: matt mbithuka
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    list_keys = list(new_dic.keys())

    for m in list_keys:
        new_dic[m] *= 2

    return (new_dic)
