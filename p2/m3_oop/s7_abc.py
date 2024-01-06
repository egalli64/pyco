"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

Abstract Base Classes and abstract methods
"""
from abc import ABC, abstractmethod, ABCMeta


class Minimal(ABC):
    """Even though extends ABC, this class is not abstract!"""

    def __str__(self):
        return "Surprise!"


print(Minimal())


class Shape(ABC):
    """An abstract class"""

    @abstractmethod
    def area(self):
        """An abstract method"""
        pass

    @abstractmethod
    def perimeter(self):
        """An abstract method"""
        pass


try:
    # Can't instantiate abstract class
    Shape()
except TypeError as ex:
    print(ex)


class Circle(Shape):
    """Extends an abstract class, overrides its abstract methods, it is a concrete class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """A concrete class can't have an abstract method"""
        return 3.14 * self.radius**2

    def perimeter(self):
        """A concrete class can't have an abstract method"""
        return 2 * 3.14 * self.radius


class Square(Shape):
    """Extends an abstract class, overrides its abstract methods, it is a concrete class"""

    def __init__(self, side):
        self.side = side

    def area(self):
        """A concrete class can't have an abstract method"""
        return self.side**2

    def perimeter(self):
        """A concrete class can't have an abstract method"""
        return 4 * self.side


circle = Circle(5)
print("Circle with radius", circle.radius)
print(f"Area {circle.area():.2f} and perimeter {circle.perimeter():.2f}")

square = Square(5)
print("Square with side", square.side)
print(f"Area {square.area()} and perimeter {square.perimeter()}")
