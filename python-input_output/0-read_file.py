#!/usr/bin/python3

def read_file(filename=""):
    """ Ouverture du fichier en mode lecture avec """
    """ 'with', qui garantit sa fermeture automatique """
    with open(filename) as file:
        """Lecture du contenu du fichier"""
        content = file.read()
        """Affichage du contenu du fichier dans la console"""
        print(content)
