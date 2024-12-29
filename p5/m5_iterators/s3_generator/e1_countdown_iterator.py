"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

Using an iterator when a generator would be a better option
"""


class CountdownIterator:
    """A countdown iterator"""

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


print("Countdown by iterator (for-in):", end=" ")
for cur in CountdownIterator(5):
    print(cur, end=" ")
print()

print("Countdown by iterator (iterating):", end=" ")
iter = CountdownIterator(5)
while True:
    try:
        print(next(iter), end=" ")
    except StopIteration:
        print()
        break
