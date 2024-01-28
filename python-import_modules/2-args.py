#!/usr/bin/python3
import sys
if __name__ == "__main__":
    name = sys.argv[0]
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("{0} argument:".format(num_arguments))
        print("{0}: {1}".format(num_arguments, arguments[0]))
    else:
        print("{0} arguments:".format(num_arguments))
        for i in range(num_arguments):
            print("{0}: {1}".format(i+1, arguments[i]))
