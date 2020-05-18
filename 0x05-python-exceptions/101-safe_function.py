#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as error_alias:
        print("Exception: {}".format(error_alias), file=stderr)
        return None
    else:
        return res
