#!/usr/bin/python3
"""Module 3-rectangle : définit un rectangle avec affichage personnalisé."""


class Rectangle:
    """Classe qui définit un rectangle avec aire, périmètre et affichage graphique."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec largeur et hauteur optionnelles."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter de la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter de la largeur avec vérification du type et de la valeur."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter de la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter de la hauteur avec vérification du type et de la valeur."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle.
        Retourne 0 si l’un des côtés est nul.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation en string du rectangle avec des #.
        Retourne une chaîne vide si la largeur ou la hauteur vaut 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)
