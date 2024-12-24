"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - __str__()
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
print("bob as string (same):", bob)
print()

class Cat:
    def __init__(self, name):
        """Each cat has its own name"""
        self._name = name

    def __repr__(self):
        """Internal representation for the current cat"""
        return f"Cat('{self._name}')"

    def __str__(self):
        """Human-friendly representation for the current cat"""
        return f"A cat named '{self._name}'"

    def meow(self):
        """A plain instance cat method"""
        print(f"{self._name} meow")


tom = Cat("Tom")
print("tom representation:", repr(tom))
print("tom as string:", tom)
