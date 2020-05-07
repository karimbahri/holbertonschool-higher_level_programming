#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()

    for key in dictionary.keys():
        dictionary[key] *= 2
    return dictionary
