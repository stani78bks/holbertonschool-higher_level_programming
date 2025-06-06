#!/usr/bin/python3
"""
Function that returns the dictionary description for JSON serialization
"""

def class_to_json(obj):
    """Returns all serializable attributes of obj (instance and class)"""
    result = {}

    # 1. Attributs d'instance
    result.update(obj.__dict__)

    # 2. Attributs de classe (non callable, non spéciaux, non déjà présents)
    for attr in dir(obj):
        if not attr.startswith("__"):
            value = getattr(obj, attr)
            if not callable(value) and attr not in result:
                result[attr] = value

    return result
