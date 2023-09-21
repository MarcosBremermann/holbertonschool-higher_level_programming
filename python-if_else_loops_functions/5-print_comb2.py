#!/usr/bin/python3
for i in range(00, 100):
    if i < 10:
        print("0{}, ".format(i), end="")
        continue

    elif 10 <= i < 99:
        print("{}, ".format(i), end="")
        continue

    elif i >= 99:
        print("{}".format(i))
