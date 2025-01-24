#!/usr/bin/python3
def uniq_add(my_list=[]):
    count_dict = {}  # Dictionnaire pour compter les occurrences de chaque élément
    total = 0  # Initialiser la somme des éléments uniques

    # Remplir le dictionnaire avec les occurrences de chaque élément
    for i in my_list:
        count_dict[i] = count_dict.get(i, 0) + 1

    # Additionner uniquement les éléments qui apparaissent une seule fois
    for i, count in count_dict.items():
        if count == 1:  # Si l'élément apparaît une seule fois
            total += i  # Ajouter l'élément unique à la somme

    return total  # Retourner la somme des éléments uniques
