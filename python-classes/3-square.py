#!/usr/bin/python3
# 3-square.py

"""Def une Instance area."""


class Square:
    """Représente une Instance area = size**2."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Renvoie l'aire du carré."""
        return self.__size ** 2
