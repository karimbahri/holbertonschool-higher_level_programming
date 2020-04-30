#!/usr/bin/python3


def checkOperator(Op):
    opIndex = 1
    for i in "+-*/:
        if Op == i:
            return opIndex
        opIndex += 1

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    length = len(argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = checkOperator(argv[2])

    a = int(argv[1])
    b = int(argv[3])

    result = 0

    if op == 1:
        result = add(a, b)
    elif op == 2:
        result = sub(a, b)
    elif op == 3:
        result = mul(a, b)
    elif op == 4:
        result = div(a, b)

    print("{} {} {} = {}".format(a, argv[2], b, result))
