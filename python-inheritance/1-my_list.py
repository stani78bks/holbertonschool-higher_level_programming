#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""

class MyList(list):
    """Custom list class that inherits from Python's built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying original)."""
        print(sorted(self))
