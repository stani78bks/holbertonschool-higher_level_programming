#!/usr/bin/env python3
def uppercase(str):
    new_str = ""
    for letter in str:
        if 97 <= ord(letter) <= 122:
             new_str += chr(ord(letter)-32)
        else:
            new_str += letter
    print(new_str)
