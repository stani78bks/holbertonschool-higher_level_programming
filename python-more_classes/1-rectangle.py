#!/usr/bin/python3
"""Module 1-rectangle : définit un rectangle avec largeur et hauteur."""


class Rectangle:
    """Classe qui définit un rectangle par sa largeur et sa hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec largeur et hauteur optionnelles."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter pour la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter pour la largeur avec vérifications."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter pour la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter pour la hauteur avec vérifications."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
