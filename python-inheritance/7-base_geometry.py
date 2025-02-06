#!/usr/bin/python3
# 7-base_geometry.py
"""Définition de la classe BaseGeometry avec des méthodes de validation."""


class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Lève une exception car cette méthode doit
        être implémentée dans les sous-classes."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier strictement positif.

        Args:
            name (str): Nom du paramètre (pour le message d'erreur).
            value (int): Valeur à vérifier.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
