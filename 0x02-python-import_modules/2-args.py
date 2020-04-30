#!/usr/bin/python3


from sys import argv

length = len(argv)

if length == 1:
    print("0 arguments.")
else:
    print("{}".format(length - 1), end=" ")

    if length == 2:
        print("argument:")
    else:
        print("arguments:")

    for i in range(1, length):
        print("{:d} : {}".format(i, argv[i]))
