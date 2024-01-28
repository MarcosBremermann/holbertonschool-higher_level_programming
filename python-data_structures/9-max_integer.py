#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if i == 0:
                temp = my_list[i]
            else:
                if my_list[i] > temp:
                    temp = my_list[i]
                else:
                    continue
    return temp
