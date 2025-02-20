"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Object Oriented Programming

Attributes and methods
"""


class Dog:
    """Definition of a simple class"""

    def __init__(self, name):
        """Initialize the state of the current dog"""
        self.name = name

    def bark(self):
        """A plain method"""
        print(f"{self.name} is barking")

    def __del__(self):
        """Finalize the current object - Python can't guarantee it is actually called!"""
        print(f"{self.name} is garbage collected")


# instantiate objects of the Dog class
bob = Dog("Bob")
tom = Dog("Tom")

print("bob name:", bob.name)
print("tom name:", tom.name)

bob.bark()
tom.bark()
