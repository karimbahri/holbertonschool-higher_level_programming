#!/usr/bin/python3


def search_replace(my_list, search, replace):
    replaced_list = my_list[:]

    for i, element in enumerate(my_list):
        if element == search:
            replaced_list[i] = replace
    return replaced_list
