"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Class - object
"""


class A(object):
    """Class A, explicitly extends object"""

    pass


class B:
    """Class B, implicitly extends object"""

    pass


class C(B):
    """Class C, explicitly extends B, indirectly extends object"""

    pass


obj = object()
a = A()
b = B()
c = C()

print("The type of obj is", type(obj))
print("obj is an object?", isinstance(obj, object))
print()

print("The type of a is", type(a))
print("a is an object?", isinstance(a, object))
print("a is an A?", isinstance(a, A))
print("a is a B?", isinstance(a, B))
print()

print("The type of b is", type(b))

print("The type of c is", type(c))
print("c is an object?", isinstance(c, object))
print("c is an A?", isinstance(c, A))
print("c is a B?", isinstance(c, B))
print("c is a C?", isinstance(c, C))
print()

print("The object attributes:", dir(object))
print()
