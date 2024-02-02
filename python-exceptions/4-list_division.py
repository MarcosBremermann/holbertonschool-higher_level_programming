#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    try:
        for i in range(list_length):
            if my_list_1[i] is not None and my_list_2[i] is not None:
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] != 0:
                        div_list.append(my_list_1[i] / my_list_2[i])
                    else:
                        print("division by zero")
                        div_list.append(0)
                else:
                    div_list.append(0)
                    print("wrong type")
            else:
                div_list.append(0)
                print("out of range")
    except IndexError:
        print("Index out of range")

    return div_list
