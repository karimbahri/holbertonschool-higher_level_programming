#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if (ord('a') <= ord(i) <= ord('z')):
            i = ord(i) - (ord('a') - ord('A'))
        else:
            i = ord(i)

        print("{:c}".format(i), end="")
    print("")
