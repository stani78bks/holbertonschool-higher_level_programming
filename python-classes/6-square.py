#!/usr/bin/python3
"""Module 6-square : définit une classe Square avec position et affichage."""


class Square:
    """Classe qui définit un carré avec taille et position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré.

        Args:
            size (int): La taille du carré.
            position (tuple): La position (décalage) du carré.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter pour récupérer la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour définir la taille du carré.

        Args:
            value (int): La nouvelle taille.

        Raises:
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est négative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter pour récupérer la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour définir la position du carré.

        Args:
            value (tuple): Le nouveau décalage horizontal et vertical.

        Raises:
            TypeError: Si la position n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: Aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré en tenant compte de la taille et de la position."""
        if self.__size == 0:
            print()
            return

        # Ajoute les lignes vides du décalage vertical
        for _ in range(self.__position[1]):
            print()

        # Affiche le carré avec les espaces du décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
