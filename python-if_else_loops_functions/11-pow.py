#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
            return (a ** b)
    if b < 0:
        return (1 / (a ** abs(b)))
