#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    elem_1 = set(filter(lambda x: x not in set_2, set_1))

    elem_2 = set(filter(lambda x: x not in set_1, set_2))

    result = elem_1.union(elem_2)

    return result
