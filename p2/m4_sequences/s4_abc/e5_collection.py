"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

ABC - Abstract Base Class - collections abc Collection
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

print("Iterating on a MyCollection:", end=" ")
for x in xs:
    print(x, end=" ")
print()

print("A MyCollection len is", len(xs))

for x in 5, 42:
    print(f"Is {x} in my collection?", x in xs)
