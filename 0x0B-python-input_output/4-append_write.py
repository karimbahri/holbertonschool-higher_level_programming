#!/usr/bin/python3
"""
4-append_write:
    functions:
        * append_write
"""


def append_write(filename="", text=""):
    """append to file"""
    with open(filename, "a") as my_file:
        my_file.write(text)
    return len(text)
