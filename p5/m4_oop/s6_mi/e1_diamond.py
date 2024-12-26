"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

MI - a diamond hierarchy
"""


class Base:
    """Base class"""

    def hello(self):
        print("Hello from Base")


class Left(Base):
    def hello(self):
        print("Hello from Left")


class Right(Base):
    def hello(self):
        print("Hello from Right")


class Bottom(Left, Right):
    pass


print("The bottom MRO:", Bottom.mro())

bottom = Bottom()
bottom.hello()
