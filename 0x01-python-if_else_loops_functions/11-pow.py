#!/usr/bin/python3


def pow(a, b):
    i = 1
    p = a

    if not b:
        return 0

    while i < b:
        p *= a
        i += 1
    return p
