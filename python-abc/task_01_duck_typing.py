#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    if not (hasattr(shape, "area") and callable(shape.area)):
        raise TypeError("Passed object has no callable 'area' method")
    if not (hasattr(shape, "perimeter") and callable(shape.perimeter)):
        raise TypeError("Passed object has no callable 'perimeter' method")

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
