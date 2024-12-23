"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Attributes and properties - properties
"""


class A:
    """A class with a property"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Name getter"""
        return self._name

    @name.setter
    def name(self, name):
        """Name setter, with validation"""
        if not isinstance(name, str) or len(name) < 2:
            raise ValueError(f"'{name}' is not accepted as name")
        self._name = name


bob = A("Bob")
print("Get name by getter:", bob.name)
print("Bypassing getter:", bob._name)

bob.name = "Bobby"
print("After setting name by setter:", bob.name)

try:
    bob.name = "B"
except ValueError as ex:
    print("Validation at work, ValueError:", ex)

try:
    bob.name = ("B", "o", "b")
except ValueError as ex:
    print("Validation at work, ValueError:", ex)

bob._name = None
print("Bypassing setter:", bob.name)
