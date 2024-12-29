"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

Using an iterator when a generator would be a better choice
"""


class EvenSquaredIterator:
    """An iterator gives more flexibility (but, do we really need it?)"""

    def __init__(self, begin=0, end=10):
        self.current = begin if begin % 2 == 0 else begin + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current**2
            self.current += 2
            return result
        else:
            raise StopIteration


print("Even squared in [0 .. 10)", end=": ")
for cur in EvenSquaredIterator():
    print(cur, end=" ")
print()

print("Even squared in [-3 .. 8)", end=": ")
for cur in EvenSquaredIterator(-3, 8):
    print(cur, end=" ")
print()
