#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        item = next(self._iterator)  # Cela lèvera StopIteration automatiquement
        self._count += 1
        return item

    def get_count(self):
        return self._count

    def __iter__(self):
        return self

