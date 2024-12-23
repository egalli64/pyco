"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Attributes and properties - calculated properties
"""


class Rectangle:
    """A class with a calculated property"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        """A calculated property"""
        return self.width * self.height


rect = Rectangle(6, 7)

print("The calculated area of the rectangle is", rect.area)
