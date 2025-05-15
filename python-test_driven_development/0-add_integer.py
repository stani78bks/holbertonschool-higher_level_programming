#!/usr/bin/python3
"""
Module that defines a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).

    Args:
        a (int or float): first number.
        b (int or float, optional): second number, defaults to 98.

    Raises:
        TypeError: if a or b is not an integer or float.
        TypeError: if a or b is float NaN or infinity.

    Returns:
        int: sum of a and b casted to integers.
    """
    for var, name in ((a, "a"), (b, "b")):
        if not isinstance(var, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if isinstance(var, float) and (
            var != var or var == float('inf') or var == float('-inf')
        ):
            raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
