#!/usr/bin/python3
# 2-is_same_class.py
"""ref une fonction"""


class BaseGeometry:
    """Base"""
    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
