#!/usr/bin/python3
"""
3-write_file
    Functions:
        write_file
"""


def write_file(filename="", text=""):
    """write in a file"""
    with open(filename, "w") as my_file:
        my_file.write(text)
    return len(text)
