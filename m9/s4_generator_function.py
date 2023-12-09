"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Generator function
"""


def countdown(n):
    """A generator function"""
    while n > 0:
        yield n
        n -= 1


# A generator
it = countdown(5)

# Iterate over the generator
for value in it:
    print(value, end=" ")
print()


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


# an iterator
it = CountdownIterator(5)
for value in it:
    print(value, end=" ")
print()
