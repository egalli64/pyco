"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Methods - instance
"""


class Dog:
    def __init__(self, name):
        """Each instance has its own name"""
        self._name = name

    def bark(self):
        """A plain instance method"""
        print(f"{self._name} barks")


bob = Dog("bob")
print("An object:", bob)

print(f"Calling {type(bob.bark)} bob.bark():", end=" ")
bob.bark()

print("Calling bark() on another object:", end=" ")
Dog("tom").bark()
