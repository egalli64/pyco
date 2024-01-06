"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

ABC - Abstract Base Class - collections abc Container
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
