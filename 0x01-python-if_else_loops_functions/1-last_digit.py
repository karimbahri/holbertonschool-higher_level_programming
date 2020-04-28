#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastDigit = number % 10

print("Last digit of", number, "is", lastDigit, "and is", end=" ")

if lastDigit > 5:
    print("and is greater than 5")
elif not lastDigit:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
