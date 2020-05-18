#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        stderr.write(value)
        return False
    else:
        return True
