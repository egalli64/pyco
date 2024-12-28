"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Iterators - Iterable and iterator

Modern iterable and iterator
"""


class IntDigits:
    """This class implements __iter__(), so it is iterable"""

    def __init__(self, value):
        self._value = value
        self._buffer = str(value)

    def __iter__(self):
        """Each time an iteration is required, a new iterator is generated"""
        return DigitIterator(self._buffer)

    def __repr__(self):
        return f"IntDigits({self._value})"


class DigitIterator:
    """
    This class implements __next__(), so it is iterator
    This class implements __iter__(), so it is iterable
    """

    def __init__(self, buffer):
        self._buffer = buffer
        self._index = 0

    def __next__(self):
        if self._index < len(self._buffer):
            cur = int(self._buffer[self._index])
            self._index += 1
            return cur
        else:
            # the end has been reached
            raise StopIteration()

    def __iter__(self):
        """Do not generate a new iterator"""
        return self


if __name__ == "__main__":
    digits = IntDigits(347_123_348_922)
    print(digits)

    try:
        print(f"{digits} starts with {digits[0]} and ends with {digits[-1]}")
    except TypeError as ex:
        print("__getitem__() has not been defined:", ex)

    print("Each digit in it:", end=" ")
    for digit in digits:
        print(digit, end=" ")
    print()
