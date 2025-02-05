#!/usr/bin/python3
# 2-is_same_class.py
"""ref une fonction"""


def is_kind_of_class(obj, a_class):
    """Retourne True si obj est une instance de a_class ou d'une sous-classe"""
    return isinstance(obj, a_class)
