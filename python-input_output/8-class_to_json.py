#!/usr/bin/python3
"""
Function that returns the dictionary description for JSON serialization
"""
def class_to_json(obj):
    """Returns the dictionary description of an object"""
    return obj.__dict__
