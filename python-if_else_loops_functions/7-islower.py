#!/usr/bin/env python3
# 7-islower.py

def islower(letter):

    if ord(letter) >= 97 and ord(letter) <= 122:
        return True
    else:
        return False
