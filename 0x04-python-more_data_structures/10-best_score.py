#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        maxVal = 0
        maxKey = 0
        for key, val in a_dictionary.items():
            if maxVal < val:
                maxVal = val
                maxKey = key
        return maxKey
