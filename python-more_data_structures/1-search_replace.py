#!/usr/bin/python3
def search_replace(my_list, search, replace):
    sec_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            sec_list.append(replace)
        else:
            sec_list.append(my_list[i])

    return sec_list
