"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - More fundamental concepts

The namedtuple() factory
"""
from collections import namedtuple

# create the Point class, subclassing tuple
Point = namedtuple("Point", "x y")

# alternative way to pass the attributes to the factory
# Point = namedtuple("Point", ("x", "y"))

# a Point is-a tuple too
a = Point(1, 2)
print(isinstance(a, Point))
print(isinstance(a, tuple))

# accessing the attributes
print(a.x, a.y)
print(a[0], a[1])

# can't change a named tuple
try:
    a.x = 42
except AttributeError as ex:
    print("Named tuples are immutable:", ex)
