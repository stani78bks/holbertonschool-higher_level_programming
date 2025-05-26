#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    This function introspects any valid Python object (including classes,
    instances, types, etc.) and returns a sorted list of names of its
    accessible attributes and methods.

    Parameters:
        obj (any): The object to inspect.

    Returns:
        list: A sorted list of attribute and method names.

    Raises:
        TypeError: If obj is not a valid object.
    """
    # Vérification basique que l'objet n'est pas None
    if obj is None:
        raise TypeError("lookup() expected a non-None object.")

    # Vérification que l'objet a bien une représentation en attributs
    if not hasattr(obj, "__class__"):
        raise TypeError("lookup() expected a valid Python object.")

    # Vérification que dir() peut être utilisé et retourne une liste
    try:
        attributes = dir(obj)
    except Exception as e:
        raise TypeError(f"lookup() failed to introspect the object: {e}")

    if not isinstance(attributes, list):
        raise TypeError("lookup() failed: dir() did not return a list.")

    # On supprime les doublons (par précaution) et on trie
    seen = {}
    clean_list = []
    for item in attributes:
        if isinstance(item, str) and item not in seen:
            seen[item] = True
            clean_list.append(item)

    return sorted(clean_list)
