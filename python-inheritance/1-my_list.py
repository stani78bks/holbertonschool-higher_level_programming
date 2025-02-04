#!/usr/bin/python3
# 1-my_list.py
"""ref une fonction"""


class MyList(list):
    """Classe qui hérite de list et ajoute une méthode pour trier la liste"""
    def print_sorted(self):
        """Affiche la liste triée sans la modifier"""
        print(sorted(self))
