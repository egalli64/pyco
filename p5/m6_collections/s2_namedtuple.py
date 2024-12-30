"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

The namedtuple() factory
"""

from collections import namedtuple

# create the Point class, subclassing tuple
# Point = namedtuple("Point", "x,y")

# alternative way to pass the attributes to the factory
Point = namedtuple("Point", ("x", "y"))

print("The new namedtuple class:", Point)

a = Point(1, 2)
print("An instance of the namedtuple:", a)
print("Is Point a tuple?", issubclass(Point, tuple))

if issubclass(Point, tuple):
    print("Since Point is a tuple, access its components by index:", a[0], a[1])

print(f"But it is a namedtuple, too: a.x={a.x}, a.y={a.y}")

# can't change a named tuple
try:
    a.x = 42
except AttributeError as ex:
    print("Named tuples are immutable:", ex)
