"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - __repr__()
"""


class Dog:
    def __init__(self, name):
        """Each instance has its own name"""
        self._name = name

    def __repr__(self):
        """Internal representation for the current object"""
        return f"Dog('{self._name}')"

    def bark(self):
        """A plain instance method"""
        print(f"{self._name} barks")


bob = Dog("Bob")
print("bob representation:", repr(bob))

bob_clone = eval(repr(bob))
print("Let the bob clone bark", end=" ... ")
bob_clone.bark()
