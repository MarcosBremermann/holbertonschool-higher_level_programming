#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [element for element in my_list]
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            continue
    return new_list
