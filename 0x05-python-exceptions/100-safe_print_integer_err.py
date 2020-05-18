#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as error_alias:
        print("Exception: {}".format(error_alias), file=stderr)
        return False
    else:
        return True
