#!/usr/bin/python3
"""
Function that returns the dictionary description for JSON serialization
"""

def class_to_json(obj):
    """Returns all serializable attributes of obj (instance and class-level)"""
    result = {}

    # Récupère les attributs d'instance
    result.update(obj.__dict__)

    # Récupère les attributs de classe accessibles via l'instance
    for attr in dir(obj):
        if not attr.startswith("__"):
            value = getattr(obj, attr)
            if not callable(value) and attr not in result:
                result[attr] = value

    return result
