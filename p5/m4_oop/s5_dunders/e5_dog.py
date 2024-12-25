"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - example of a class with a few dunders
"""


class Dog:
    """A class with some commonly used dunder methods"""

    def __init__(self, *names):
        """Constructing a new dog with names (as a tuple)"""
        self.names = names

    def __str__(self):
        """Generating a user-friendly string describing the object"""
        return f"A dog named {self.names}"

    def __repr__(self):
        """Generating a string describing more precisely the object"""
        return f"Dog{self.names}"

    def __len__(self):
        """Generating the object length as the length of its names tuple"""
        return len(self.names)


bob = Dog("billy", "bob", "Mr. Johnson")
print("Readable bob's description:", bob)
print("Internal bob's representation:", repr(bob))
print(f"Bob has {len(bob)} names")
