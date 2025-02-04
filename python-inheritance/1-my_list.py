#!/usr/bin/python3
# 1-my_list.py
"""Fonction qui return une MYlist"""


class Mylist(list):
    """Def d'une classe"""
    def print_sorted(self):

        """print obj"""
        print(sorted(self))
