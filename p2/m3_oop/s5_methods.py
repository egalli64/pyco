"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

Methods
"""


class Dog:
    # class attribute, dog counter
    counter = 0

    def __init__(self, name):
        """Each new instance increases the Dog counter"""
        Dog.counter += 1
        self.name = name

    def bark(self):
        """A plain instance method"""
        print(f"{self.name} barks")

    @classmethod
    def check(cls):
        """A class method, it is meant to access class attributes"""
        print("The counter is currently set to", cls.counter)

    @staticmethod
    def info():
        """A static method, it is _not_ meant to access class attributes"""
        print("Something about dogs")


bob = Dog("bob")
bob.bark()
Dog("tom").bark()
Dog.check()
Dog.info()
