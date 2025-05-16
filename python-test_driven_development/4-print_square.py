#!/usr/bin/python3
"""This module defines a function that prints a square with the character #."""


def print_square(size):
    """Prints a square of '#' with dimensions size x size.

    Args:
        size (int): The size of the square sides.

    Raises:
        TypeError: If size is not an integer or is a negative float.
        ValueError: If size is a negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
