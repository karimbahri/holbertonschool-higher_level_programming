#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    length_Tuple_a = len(tuple_a)
    length_Tuple_b = len(tuple_b)

    if not length_Tuple_a:
        first_tuple = (0, 0)
    elif length_Tuple_a == 1:
        first_tuple = (tuple_a[0], 0)
    else:
        first_tuple = tuple_a

    if not length_Tuple_b:
        second_tuple = (0, 0)
    elif length_Tuple_b == 1:
        second_tuple = (tuple_b[0], 0)
    else:
        second_tuple = tuple_b

    return first_tuple[0] + second_tuple[0], first_tuple[1] + second_tuple[1]
