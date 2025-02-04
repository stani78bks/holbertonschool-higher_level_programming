#!/usr/bin/python3
# 1-my_list.py
"""Fonction qui return une list"""


class Mylist(list):
    def print_sorted(self):

        """print obj"""
        print(sorted(self))
