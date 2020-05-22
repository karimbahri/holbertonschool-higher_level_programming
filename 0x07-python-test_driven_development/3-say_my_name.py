#!/usr/bin/python3
"""
3-say_my_name
    Functions: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: print first_name and last_name
                args:
                    @first_name: first_name
                    @last_name:  last_name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
        return
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
        return

    print("My name is {} {}".format(first_name, last_name))
