"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

ABC - Abstract Base Class

Container
"""
from collections import abc


class MyContainer(abc.Container):
    """A concrete Container"""

    def __contains__(self, x):
        """All the odd values are in this container!"""
        return x % 2


xs = MyContainer()
for x in range(-2, 3):
    print(f"Is {x} in my container?", x in xs)
