#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number *= -1
    lastDigit = number % 10
    number *= -1
else:
    lastDigit = number % 10

print("Last digit of", number, "is", lastDigit, "and is", end=" ")

if lastDigit > 5:
    print("greater than 5")
elif not lastDigit:
    print("0")
else:
    print("less than 6 and not 0")
