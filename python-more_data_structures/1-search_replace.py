#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    On itère sur chaque élément de la liste my_list et,
    pour chaque élément item, on fait une comparaison avec la valeur
    search. Si item est égal à search, cet élément est remplacé par replace.
    Si ce n'est pas le cas, l'élément reste inchangé.
    """
    return [replace if item == search else item for item in my_list]
