#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    list_res = my_list[:]

    for i in range(len(list_res)):
        if not (list_res[i] % 2):
            list_res[i] = True
        else:
            list_res[i] = False
    return list_res
