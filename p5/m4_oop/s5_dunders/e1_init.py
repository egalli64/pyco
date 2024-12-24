"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - __init__()
"""


class Dog:
    def __init__(self, name):
        """Each instance has its own name"""
        print("Inside the Dog initialization")
        self._name = name

    def bark(self):
        """A plain instance method"""
        print(f"{self._name} barks")


print("Before creating a new Dog object")
bob = Dog("Bob")
print("After creating a new Dog object\n")

bob.bark()
