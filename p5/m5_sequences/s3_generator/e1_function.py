"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Sequence

Generator function
"""


def countdown(n):
    """A simple generator function"""
    while n > 0:
        yield n
        n -= 1


# A generator
gen = countdown(5)
print("Calling the function generator we get:", gen)

# Iterate over the generator
print("Countdown by generator:", end=" ")
for cur in gen:
    print(cur, end=" ")
print()

try:
    next(gen)
except StopIteration:
    print("At the end the generator is exhausted")


class CountdownIterator:
    """An iterator with the same behavior of the generator above"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > 0:
            result = self.start
            self.start -= 1
            return result
        else:
            raise StopIteration


print("Countdown by iterator:", end=" ")
for cur in CountdownIterator(5):
    print(cur, end=" ")
print()
