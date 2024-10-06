"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Sequence

ABC - Abstract Base Class - collections abc Reversible
"""
from collections import abc


class MyReversible(abc.Reversible):
    """Is-a Reversible, to be concrete must implement both the methods __iter__ and __reversed__"""

    def __init__(self, data):
        """Is-a Reversible, and has-a Reversible data"""
        self.data = data

    def __iter__(self):
        """Delegate to the composed attribute"""
        return iter(self.data)

    def __reversed__(self):
        """Delegate to the composed attribute"""
        return reversed(self.data)


xs = MyReversible([2, 5, 9])

print("Iterating on a MyReversible:", end=" ")
for x in xs:
    print(x, end=" ")
print()

print("Reverse iterating on a MyReversible:", end=" ")
for x in reversed(xs):
    print(x, end=" ")
print()
