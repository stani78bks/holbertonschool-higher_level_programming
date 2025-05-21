#!/usr/bin/python3
"""Classe Square avec getter et setter pour l'attribut privé size"""


class Square:
    """Classe qui définit un carré avec validation et accès contrôlé à la taille"""

    def __init__(self, size=0):
        """Initialisation avec vérification"""
        self.size = size  # utilise le setter ici pour validation

    @property
    def size(self):
        """Getter pour accéder à la taille"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour modifier la taille avec vérification"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l’aire du carré"""
        return self.__size ** 2
