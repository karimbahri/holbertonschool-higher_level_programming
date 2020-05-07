#!/usr/bin/python3


def max_in_dict(a_dict={}):
    maxVal = 0
    maxKey = 0
    for key, val in a_dict.items():
        if maxVal < val:
            maxVal = val
            maxKey = key
    return maxKey


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        return max_in_dict(a_dictionary)
