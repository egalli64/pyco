"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

Methods
"""


class Dog:
    # class attribute, dog counter
    _counter = 0

    def __init__(self, name):
        """Each new instance increases the Dog counter"""
        Dog._counter += 1
        self._name = name

    def __repr__(self) -> str:
        return f"Dog('{self._name}')"

    def bark(self):
        """A plain instance method"""
        print(f"{self._name} barks")

    @classmethod
    def check(cls):
        """A class method, it is meant to access class attributes"""
        print("The counter is currently set to", cls._counter)

    @staticmethod
    def info():
        """A static method, it is _not_ meant to access class attributes"""
        print("Something about dogs")

    def info2():
        """Another static method, not explicitly qualified as such"""
        print("Something else about dogs")


bob = Dog("bob")
print("An object:", bob)

print(f"Calling {type(bob.bark)} bob.bark():", end=" ")
bob.bark()

print("Calling bark() on another object:", end=" ")
Dog("tom").bark()

print(f"Calling {type(Dog.check)} Dog.check():", end=" ")
Dog.check()

print(f"Calling {type(Dog.info)} Dog.info():", end=" ")
Dog.info()

print(f"Calling {type(Dog.info2)} Dog.info2():", end=" ")
Dog.info2()
