"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

ABC - a _real_ minimal example
"""

from abc import ABC, abstractmethod


class Base(ABC):
    """this class is abstract"""

    @abstractmethod
    def do_something(self):
        """An abstract method"""
        pass


class Derived(Base):
    """this class is still abstract"""

    def do_something(self):
        """Override of the abstract method"""
        print("Doing something in the derived class")


d = Derived()
d.do_something()
