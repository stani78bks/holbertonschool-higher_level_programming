#!/usr/bin/python3
"""Classe Square qui définit un carré."""


class Square:
    """Classe qui définit un carré avec taille privée et sécurisée."""

    def __init__(self, size=0):
        """Initialise le carré avec une taille donnée (valide)."""
        self.size = size

    @property
    def size(self):
        """Getter : récupère la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : définit la taille du carré avec vérification stricte."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et retourne l’aire du carré."""
        return self.__size ** 2
