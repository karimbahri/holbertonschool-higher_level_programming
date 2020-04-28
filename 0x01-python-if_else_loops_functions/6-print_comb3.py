#!/usr/bin/python3

for d in range(0, 8):
    for u in range(0, 10):
        if d < u:
            print("{:d}{:d},".format(d, u), end=" ")

print("89")
