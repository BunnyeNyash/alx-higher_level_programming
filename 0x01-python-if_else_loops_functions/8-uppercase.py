#!/usr/bin/python3
def uppercase(string):
    for char in string:
        ascii_value = ord(char)
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end="")

    print('\n', end="")
