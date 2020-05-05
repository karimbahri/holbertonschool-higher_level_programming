#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]

    if not my_list or not (0 <= idx < len(my_list)):
        return new_list

    new_list[idx] = element
    return new_list
