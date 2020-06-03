#!/usr/bin/python3
"""0-read_file
        functions:
            read_file
"""


def read_file(filename=""):
    """read_file: read a given file"""
    with open(filename, "r") as my_file:
        content = my_file.read()
        print(content)
