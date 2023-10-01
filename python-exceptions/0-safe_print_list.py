#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        if i < len(my_list):
            end = "" if i < x - 1 else "\n"
            print("{}".format(my_list[i]), end=end)
            count += 1
    return count
