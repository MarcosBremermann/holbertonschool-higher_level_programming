#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = list(a_dictionary)
    b_dictionary.sort()
    c_dictionary = {i: a_dictionary[i] for i in b_dictionary}
    for key, value in c_dictionary.items():
        print("{}: {}".format(key, value))
