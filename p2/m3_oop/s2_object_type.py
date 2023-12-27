"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

The class object and type
"""


class A(object):
    pass


print("The A base class is", A.__base__)


class B:
    pass


print("The B base class is", B.__base__)

print("\n*** The object attributes:")
for cur in dir(object):
    print(cur)

print("\n*** The type attributes:")
for cur in dir(type):
    print(cur)
