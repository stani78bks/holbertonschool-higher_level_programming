#!/usr/bin/python3

"""
Module for say_my_name function
"""


def say_my_name(first_name, last_name=""):

    """


    Imprime le prénom et le nom. Lève une exception si l'un des
    paramètres n'est pas
    une chaîne de caractères.
    parametres:

    first_name (str): Le prénom.
    last_name (str): Le nom de famille. (Optionnel)
    Raises:
    TypeError: Si l'un des paramètres n'est pas une chaîne de caractères.

    >>> say_my_name("John", "Doe")
    My name is John Doe
    >>> say_my_name("Jane")
    My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
