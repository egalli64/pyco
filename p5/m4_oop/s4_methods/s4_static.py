"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Methods - static
"""


class MyMath:
    """A class that acts as a namespace"""

    @staticmethod
    def add(a, b):
        """A static method explicitly decorated as such"""
        return a + b

    def multiply(a, b):
        """This static method has no explicit decoration (less clear)"""
        return a * b


print("Invoking the static method MyMath.add():", MyMath.add(28, 14))
print("Invoking the static method MyMath.multiply():", MyMath.multiply(6, 7))
