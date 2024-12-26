"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

ABC - minimal example, an ABC that is not abstact
"""

from abc import ABC


class Minimal(ABC):
    """Even though extends ABC, this class is not abstract!"""

    def __str__(self):
        return "Surprise!"


mini = Minimal()

print(mini)
