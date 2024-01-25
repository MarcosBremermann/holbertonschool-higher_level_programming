#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        asci = ord(char)
        if 123 > asci > 96:
            result += chr(asci - 32)
        else:
            result += char
    print(result)
