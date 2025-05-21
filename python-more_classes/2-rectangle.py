#!/usr/bin/python3
"""Module 2-rectangle : définit un rectangle avec aire et périmètre."""


class Rectangle:
    """Classe qui définit un rectangle avec validations."""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec largeur et hauteur optionnelles."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter pour la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter pour la largeur avec validation du type et de la valeur."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter pour la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter pour la hauteur avec validation du type et de la valeur."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle.
        Retourne 0 si largeur ou hauteur est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
