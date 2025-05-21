#!/usr/bin/python3
"""Classe Square avec affichage du carré via my_print()"""


class Square:
    """Classe qui définit un carré avec impression personnalisée"""

    def __init__(self, size=0):
        """Initialisation avec vérification"""
        self.size = size  # appel du setter

    @property
    def size(self):
        """Getter de la taille"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter avec vérification du type et de la valeur"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l’aire du carré"""
        return self.__size ** 2

    def my_print(self):
        """Affiche un carré avec '#' ou une ligne vide si size = 0"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
