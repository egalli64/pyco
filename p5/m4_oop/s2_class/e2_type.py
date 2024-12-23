"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Class - type
"""


class A(object):
    pass


class B:
    pass


class C(B):
    pass


print("The type of the class object is", type(object))
print(f"Its name is '{object.__name__}', its base class is {object.__base__}")
print(f"The '{A.__name__}' base class is {A.__base__}")
print(f"The '{B.__name__}' base class is {B.__base__}")
print(f"The '{C.__name__}' base class is {C.__base__}")

# the metaclass type is-a object
print(f"{type.__name__}, that extends {type.__base__}, is callable?", callable(type))
print("The type attributes:", dir(type))
