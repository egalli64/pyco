"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Sequence

ABC - Abstract Base Class - collections abc Sized
"""
from collections import abc


class MySized(abc.Sized):
    """Is-a Sized, to be concrete must implement the method __len__"""

    def __init__(self, data):
        """Is-a Sized, and has-a Sized data"""
        self.data = data

    def __len__(self):
        """Delegate to the composed attribute"""
        return len(self.data)


xs = MySized([6, 3, 5])
print("A MySized len is", len(xs))
