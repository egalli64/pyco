"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

The classes object and type
"""


class A(object):
    pass


class B:
    pass


class C(B):
    pass


print(f"The {object.__name__} base class is {object.__base__}")
print(f"The {A.__name__} base class is {A.__base__}")
print(f"The {B.__name__} base class is {B.__base__}")
print(f"The {C.__name__} base class is {C.__base__}")

print("\n*** The object attributes:")
for cur in dir(object):
    print(cur)
print()

# the metaclass type is-a object
print(f"{type.__name__}, that extends {type.__base__}, is callable?", callable(type))
print("*** The type attributes:")
for cur in dir(type):
    print(cur)

x = C()
print("Is x an object of class C?", isinstance(x, C))
print("Is x an object of class B?", isinstance(x, B))
print("Is x an object of class A?", isinstance(x, A))
print("Is x an object of class object?", isinstance(x, object))