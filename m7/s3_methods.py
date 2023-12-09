"""
Python Course

https://github.com/egalli64/pyco

Module 7 - Object Oriented Programming

Attributes and methods
"""


class Dog:
    """Define a simple class"""

    def __init__(self, name):
        """Initialize the state of the current dog"""
        self.name = name

    def bark(self):
        """A plain method"""
        print(f"{self.name} is barking")


# instantiate objects of the Dog class
bob = Dog("Bob")
tom = Dog("Tom")

print(bob.name)
print(tom.name)

bob.bark()
tom.bark()
