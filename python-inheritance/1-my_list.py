#!/usr/bin/python3
"""Module that defines a subclass MyList of list."""


class MyList(list):
    """Subclass of list with a method to print sorted list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
