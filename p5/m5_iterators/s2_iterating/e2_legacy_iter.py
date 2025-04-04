"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Iterable and iterator

A legacy iterable class
"""


class IterableIntByGetter:
    """This class implements __getitem__(), so it is iterable"""

    def __init__(self, value):
        self._value = value
        self._buffer = str(value)

    def __getitem__(self, i):
        """Used by Python to create an iterator"""
        return int(self._buffer[i])

    def __repr__(self):
        return f"IterableIntByGetter({self._value})"


digits = IterableIntByGetter(347_123_348_922)
print(f"{digits} starts with {digits[0]} and ends with {digits[-1]}")

print("Each digit in it:", end=" ")
for digit in digits:
    print(digit, end=" ")
print()
