#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        number *= -1
        lastDigit = number % 10
        number *= -1
        print("{:d}".format(lastDigit), end="")
    else:
        lastDigit = number % 10
        print("{:d}".format(lastDigit), end="")

    return lastDigit
