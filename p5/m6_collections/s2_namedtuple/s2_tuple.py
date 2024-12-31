"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

The namedtuple() factory, attributes by string iterable
"""

from collections import namedtuple

Point = namedtuple("Point", ("x", "y"))

print("The new namedtuple class:", Point)

a = Point(1, 2)
print("A Point instance:", a)
print("Is Point a tuple?", issubclass(Point, tuple))

if issubclass(Point, tuple):
    print(f"Point is a tuple, access its components by index: a[0]={a[0]}, a[1]={a[1]}")

print(f"But Point is a namedtuple, too: a.x={a.x}, a.y={a.y}")

# can't change a named tuple
try:
    a.x = 42
except AttributeError as ex:
    print("Named tuples are immutable:", ex)
