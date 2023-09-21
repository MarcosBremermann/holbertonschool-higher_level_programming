#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if 65 <= value < 91:
        return False

    elif 97 <= value < 123:
        return True
