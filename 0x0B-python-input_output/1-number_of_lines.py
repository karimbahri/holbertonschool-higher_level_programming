#!/usr/bin/python3
"""1-number_of_lines
        functions:
            number_of_lines
"""


def number_of_lines(filename=""):
    """number_of_lines: return number of lines"""
    with open(filename, "r") as my_file:
        size = 0
        while my_file.readline():
            size += 1
        return size
