#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{}".format(char), end="")
    print()
