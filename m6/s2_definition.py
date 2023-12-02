"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 6 - Object Oriented Programming

Class, object, constructor
"""


class Empty:
    """Define a minimal class"""


# instantiate an object of the Empty class
empty = Empty()
print(empty)


class Dog:
    """Define a simple class"""

    def __init__(self, name):
        """Initialize the state of the current dog"""
        self.name = name

    def bark(self):
        """A plain method"""
        print(f"{self.name} is barking")


# instantiate an object of the Dog class
bob = Dog("Bob")
# invoking a method on the dog instance
bob.bark()
