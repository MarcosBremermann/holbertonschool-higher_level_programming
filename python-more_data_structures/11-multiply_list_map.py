#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = [element for element in my_list]
    def mult(n):
        return n * number
    return list(map(mult, new_list))
