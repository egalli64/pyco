"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 8 - Design Pattern

Factory Method
"""
from abc import ABC, abstractmethod


class Base(ABC):
    """Base class"""

    @staticmethod
    def create(type):
        if type == "Red":
            return Red()
        elif type == "Green":
            return Green()
        else:
            raise ValueError(f"Unexpected type: {type}")

    @abstractmethod
    def greeter(self):
        pass


class Red(Base):
    """A concrete class of the Base hierarchy"""

    def greeter(self):
        print("Hello from a class Red object!")


class Green(Base):
    """Another concrete class of the Base hierarchy"""

    def greeter(self):
        print("Hello from a class Green object!")
