#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses to produce a sound."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        return "Meow"
