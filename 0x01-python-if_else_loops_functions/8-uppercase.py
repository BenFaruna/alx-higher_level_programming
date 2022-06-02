#!/usr/bin/python3
def uppercase(str):
    for char in str:
        new_ord = ord(char)
        if (ord("a") <= ord(char) <= ord("z")):
            new_ord = ord(char) - 32
        print(f"{chr(new_ord)}", end="")
    print("")
