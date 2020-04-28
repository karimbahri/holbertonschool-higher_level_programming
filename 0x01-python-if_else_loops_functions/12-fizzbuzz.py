#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 100):
        if not (i % 3) and not (i % 5):
            print("FizzBuzz", end=" ")
        elif not (i % 3):
            print("Fizz", end=" ")
        elif not (i % 5):
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")

    print("Buzz $")
