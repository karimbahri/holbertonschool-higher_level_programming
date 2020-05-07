#!/usr/bin/python3
def weight_average(my_list=[]):

    if not my_list:
        return 0

    sum = 0
    div = 0
    for nb in my_list:
        sum += nb[0] * nb[1]
        div += nb[1]

    avrg = sum / div
    return avrg
