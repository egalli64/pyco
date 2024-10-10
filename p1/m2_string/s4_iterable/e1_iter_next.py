"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Iterable - get an iterator on string and consuming it
"""

# a string is an iterable
str = "Hi"
print("The string: ", str)

# create an iterator from the string
it = iter(str)

# iterating on the string by the iterator
ch = next(it)
print(f"The first character in {str} is", ch)

# second iteration
ch = next(it)
print(f"The second character in {str} is", ch)

# next on a consumed iterator generates an exception!
try:
    next(it)
except StopIteration:
    print("Iteration terminated")
