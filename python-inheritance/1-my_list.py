#!/usr/bin/python3
"""
Module MyList
Ce module définit une classe MyList qui hérite de list et ajoute une méthode print_sorted().
"""

class MyList(list):
    """
    Classe MyList qui hérite de la classe list.
    Elle ajoute une méthode print_sorted() pour afficher une version triée de la liste.
    """

    def print_sorted(self):
        """
        Affiche une version triée de la liste.
        La liste d'origine n'est pas modifiée.
        """
        print(sorted(self))