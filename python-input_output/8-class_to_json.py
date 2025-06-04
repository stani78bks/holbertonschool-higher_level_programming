#!/usr/bin/python3
"""
Returns the dictionary description for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description of obj for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of obj.
    """
    return obj.__dict__
