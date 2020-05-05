#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)

    if not length:
        return "None"

    max_element = my_list[0]

    for item in my_list[1:]:
        if item > max_element:
            max_element = item

    return max_element
