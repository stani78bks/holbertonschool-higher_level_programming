#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math  


class VerboseList(list):

    def append(self, item):
        super(list).append(item)
        print(f"Added [{item}] to the list.")
    def extend(self, item):
        super(list).extend(item)
        print(f"Extended the list with [{item}].")
    def remove(self, item):
        super(list).extend(item)
        print(f"Removed [{item}] from the list.")
    def pop(self, item=-1):
        super(list).extend(item)
        print(f"Popped [{item}] from the list.")