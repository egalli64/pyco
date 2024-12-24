"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Methods - class
"""


class Dog:
    # class attribute, dog counter
    _counter = 0

    def __init__(self, name):
        """Each new instance increases the Dog counter"""
        Dog._counter += 1
        self._name = name

    @classmethod
    def check(cls):
        """A class method, it is meant to access class attributes"""
        print("The Dog counter is currently set to", cls._counter)


Dog.check()

bob = Dog("bob")
print("A dog:", bob)

tom = Dog("tom")
print("Another dog:", tom)

Dog.check()
