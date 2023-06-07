#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if ord('a') <= ascii_val <= ord('z'):
            ascii_val -= ord('a') - ord('A')
        print(chr(ascii_val), end="")
    print()
