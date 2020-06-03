#!/usr/bin/python3
"""
2-read_lines:
    functions:
        * read_lines
"""


def read_lines(filename="", nb_lines=0):
    """read_lines: read n lines of a file"""
    with open(filename, "r") as my_file:
        i = 0
        for line in my_file:
            if i < nb_lines or nb_lines <= 0:
                print(line, end="")
                i += 1
            else:
                break
