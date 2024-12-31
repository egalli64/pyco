"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

The namedtuple() factory, attributes by CSV string
"""

from collections import namedtuple

Point = namedtuple("Point", "x,y")
# a blank is accepted as separator, too
# Point = namedtuple("Point", "x y")

print("The new namedtuple class:", Point)

a = Point(1, 2)
print("A Point instance:", a)
