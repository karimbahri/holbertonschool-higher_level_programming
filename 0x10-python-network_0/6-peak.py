#!/usr/bin/python3
"""peak"""


def find_peak(list_of_integers):
    """find peak in unsorted list"""
    ls = list_of_integers
    if not ls or ls == []:
        return None
    for i in range(1, len(ls) - 1):
        if ls[i] > ls[i - 1] and ls[i + 1] < ls[i]:
            return ls[i]
    return max(ls[0], ls[-1])
