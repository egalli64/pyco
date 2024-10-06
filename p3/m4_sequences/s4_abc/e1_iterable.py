"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Sequence

ABC - Abstract Base Class - collections abc Iterable
"""
from collections import abc


class MyAbstractIterable(abc.Iterable):
    """It is-a Iterable - no __iter__() implementation - this class is abstract"""

    pass


try:
    # the class MyAbstractIterable is abstract!
    bad = MyAbstractIterable()
except TypeError as ex:
    print(ex)


class MyIterable(abc.Iterable):
    """A concrete Iterable"""

    def __init__(self, data):
        """Is-a iterable, and has-a iterable data"""
        self.data = data

    def __iter__(self):
        """Delegate to the composed attribute"""
        return iter(self.data)


xs = MyIterable([6, 3, 5])

print("Iterating on a MyIterable:", end=" ")
for x in xs:
    print(x, end=" ")
print()
