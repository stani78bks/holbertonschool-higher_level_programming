#!/usr/bin/python3
"""Classe Square avec getter et setter pour l'attribut privé size."""


class Square:
    """Classe qui définit un carré avec accès sécurisé à sa taille."""

    def __init__(self, size=0):
        """Initialise le carré avec une taille optionnelle."""
        self.size = size  # utilise le setter pour validation

    @property
    def size(self):
        """Getter pour récupérer la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour définir la taille avec vérification du type et de la valeur."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l’aire du carré."""
        return self.__size ** 2
