#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Retourne True si l'objet est exactement
    une instance de la classe spécifiée."""
    return type(obj) is a_class
