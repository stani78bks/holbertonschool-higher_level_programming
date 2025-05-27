#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from list and adds a method to print
    the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
