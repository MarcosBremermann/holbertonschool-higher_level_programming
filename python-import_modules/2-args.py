#!/usr/bin/python3
import sys

if __name__ == "__main__":
    c = len(sys.argv[1:])
    if c == 0:
        print("{} arguments.".format(c))

    elif c == 1:
        print("{} argument:".format(c))
        for i in range(c):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))

    elif c > 1:
        print("{} arguments:".format(c))
        for i in range(c):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
