#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or not len(a_dictionary):
        return None
    return max(a_dictionary)
