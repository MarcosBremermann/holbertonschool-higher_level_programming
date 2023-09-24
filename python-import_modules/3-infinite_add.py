#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = 0
    add = 0
    for i in argv:
        if count != 0:
            add = add + int(i)
        count += 1
    print("{}".format(add))
