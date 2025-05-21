#!/usr/bin/python3
"""Classe Square avec position et impression décalée"""


class Square:
    """Classe qui définit un carré avec taille et position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise avec taille et position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter pour la taille"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter avec validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter pour la position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter avec validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l’aire"""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec décalage selon position"""
        if self.__size == 0:
            print()
            return
        # Décalage vertical
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            # Décalage horizontal + carré
            print(" " * self.__position[0] + "#" * self.__size)
