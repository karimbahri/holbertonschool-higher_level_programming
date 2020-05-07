#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    for index, values in sorted(a_dictionary.items()):
        print("{}: {}".format(index, values))
