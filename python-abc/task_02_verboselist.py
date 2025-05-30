#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        # Afficher avant suppression
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]  # Obtenir l'élément à poper
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
