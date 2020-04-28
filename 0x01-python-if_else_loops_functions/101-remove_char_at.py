#!/usr/bin/python3


def remove_char_at(str, n):
    deleted_str = ""

    for i in range(0, len(str)):
        if i != n:
            deleted_str = deleted_str + str[i]

    return deleted_str
