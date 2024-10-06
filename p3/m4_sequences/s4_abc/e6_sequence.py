"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 6 - Sequence

ABC - Abstract Base Class - collections abc Sequence
"""
from collections import abc


class MySequence(abc.Sequence):
    """Is-a Sequence"""

    def __init__(self, data):
        """Is-a Sequence, and has-a Sequence data"""
        self.data = data

    def __iter__(self):
        """Delegate to the composed attribute"""
        return iter(self.data)

    def __len__(self):
        """Delegate to the composed attribute"""
        return len(self.data)

    def __contains__(self, x):
        """Delegate to the composed attribute"""
        return x in self.data

    def __getitem__(self, i):
        """Delegate to the composed attribute"""
        return self.data[i]


xs = MySequence([2, 5, 9])

print("Iterating on a MySequence:", end=" ")
for x in xs:
    print(x, end=" ")
print()

print("A MySequence len is", len(xs))

for x in 5, 42:
    print(f"Is {x} in my sequence?", x in xs)

for x in 5, 42:
    try:
        print(f"Index of {x} is", xs.index(x))
    except ValueError:
        print(x, "not found")

print(f"There are {xs.count(42)} instances of 42 in my sequence")
