#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in range(len(my_list)):
        for x in range(i - 1):
            if my_list[x] == my_list[i]:
                my_list[i] = 0
        if i == 0:
            total = my_list[0]
        else:
            total = total + my_list[i]
    return total
