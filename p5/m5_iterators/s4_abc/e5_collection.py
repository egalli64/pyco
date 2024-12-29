"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

ABC - Abstract Base Class

Collection
"""

from collections import abc


class MyCollection(abc.Collection):
    """Is-a Collection, meaning is-a Iterable, Sized, Container"""

    def __init__(self, data):
        """Is-a Collection, and has-a Collection data"""
        self.data = data

    def __iter__(self):
        """Delegate to the composed attribute"""
        return iter(self.data)

    def __len__(self):
        """Delegate to the composed attribute"""
        return len(self.data)

    def __contains__(self, x):
        """Delegate to the composed attribute"""
        return x in self.data


xs = MyCollection([2, 5, 9])

print(f"Is xs a {abc.Collection}?", isinstance(xs, abc.Collection))

print("Iterating on xs:", end=" ")
for x in xs:
    print(x, end=" ")
print()

print("xs len is", len(xs))

for x in 5, 42:
    print(f"Is {x} in xs?", x in xs)
