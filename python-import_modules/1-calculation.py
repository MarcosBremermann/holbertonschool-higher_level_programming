#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    if add(a, b):
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    if sub(a, b):
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    if mul(a, b):
        print("{0} * {1} = {2}".format(a, b, a * b))
    if div(a, b):
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
