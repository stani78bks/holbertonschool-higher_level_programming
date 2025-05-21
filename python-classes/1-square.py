#!/usr/bin/python3
"""Définit une classe Square avec un attribut privé"""


class Square:
    """Classe qui définit un carré avec une taille privée"""

    def __init__(self, size):
        """Initialise un carré avec la taille donnée"""
        self.__size = size
