#!/usr/bin/python3
def islower(c):
    variable = ord(c)
    if 122 >= variable >= 97:
        return True
    if variable < 97:
        return False
