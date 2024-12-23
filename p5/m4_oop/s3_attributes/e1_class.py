"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Attributes and properties - class attributes
"""


class A:
    """A class with two class attributes"""

    x = 12
    y = x + 27


a1 = A()
a2 = A()
print("The preferred way to access a class attribute:", A.x)
print("But passing through an instance is OK, too:", a1.x)
print("Each instance leads to the same class attribute:", a1.x)

print("Accessing the docstring:", A.__doc__)
