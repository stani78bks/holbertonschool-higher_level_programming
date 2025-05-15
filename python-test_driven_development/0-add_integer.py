#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """Add two integers or floats, casted to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float, default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or a != a or a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
