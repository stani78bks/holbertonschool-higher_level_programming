#!/usr/bin/python3
"""
Function that returns the dictionary description for JSON serialization
"""

def class_to_json(obj):
    """Returns a dict with all serializable attributes of an object"""
    attrs = {}

    for attr in dir(obj):
        if attr.startswith("__"):
            continue
        value = getattr(obj, attr)
        if not callable(value):
            attrs[attr] = value

    return attrs
