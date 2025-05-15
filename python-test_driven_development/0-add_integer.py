#!/usr/bin/python3
"""
0-add_integer module

Defines a function that adds two integers or floats (casted to int).
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): first number.
        b (int or float, optional): second number, defaults to 98.

    Raises:
        TypeError: if either a or b is not an integer or float,
                   or if either is float('inf'), float('-inf') or float('nan').

    Returns:
        int: the sum of a and b casted to integers.
    """
    for var, name in ((a, 'a'), (b, 'b')):
        if not isinstance(var, (int, float)):
            raise TypeError(f"{name} must be an integer")
        # Reject NaN and infinities explicitly
        if isinstance(var, float):
            if var != var or var == float('inf') or var == float('-inf'):
                raise TypeError(f"{name} must be an integer")
    return int(a) + int(b)
