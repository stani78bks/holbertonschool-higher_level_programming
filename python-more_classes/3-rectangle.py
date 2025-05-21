#!/usr/bin/python3
"""Module 3-rectangle : définition d'un rectangle avec affichage."""


class Rectangle:
    """Classe qui définit un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle.

        Args:
            width (int): largeur du rectangle (par défaut 0)
            height (int): hauteur du rectangle (par défaut 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec vérification.

        Args:
            value (int): nouvelle largeur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur avec vérification.

        Args:
            value (int): nouvelle hauteur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcule et retourne le périmètre.

        Retourne 0 si width ou height est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une chaîne représentant le rectangle avec des #.

        Retourne une chaîne vide si largeur ou hauteur est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
