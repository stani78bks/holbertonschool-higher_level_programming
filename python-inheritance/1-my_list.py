#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class that inherits from built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
