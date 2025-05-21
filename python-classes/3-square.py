#!/usr/bin/python3
"""Définit une classe Square avec validation de la taille et méthode d'aire"""


class Square:
    """Classe qui définit un carré avec une taille validée"""

    def __init__(self, size=0):
        """Initialise un carré avec vérification de la taille"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne l’aire du carré"""
        return self.__size ** 2
