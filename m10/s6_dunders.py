"""
Python Course

https://github.com/egalli64/pyco

Module 10 - More on Object Oriented Programming 

Dunders
"""


class Dog:
    """A class with some commonly used dunder methods"""

    def __init__(self, *names):
        print("Constructing a new dog")
        self.names = names

    def __str__(self):
        print("Generating a user-friendly string describing the object")
        return f"A dog named {self.names}"

    def __repr__(self):
        print("Generating a string describing more precisely the object")
        return f"Dog{self.names}"

    def __len__(self):
        print("Generating the object length as the length of its names tuple")
        return len(self.names)


bob = Dog("billy", "bob", "Mr. Johnson")
print(bob)
info = "Info on: " + str(bob)
print(info)
print("Debugging:", repr(bob))
print(f"The dog has {len(bob)} names")
