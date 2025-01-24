#!/usr/bin/python3
"""
module : function print to sqaure

"""


def print_square(size):

    """
    Fonction pour imprimer un carré
    Function to print a square

    Paramètres :
    size : int
    La longueur du côté du carré.
    (size is the length of the square's side)

    Exceptions :
    TypeError
    Si le paramètre `size` n'est pas un entier.
    (If `size` is not an integer)

    ValueError
    Si le paramètre `size` est négatif.
    (If `size` is negative)

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
