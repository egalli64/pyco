"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Builtin - basic functions
"""

# len
names = ("Tom", "Bob", "Joe", "Jim")
print(f"Names {names} has len {len(names)}")

# range
print("Values in a range:", end=" ")
for i in range(3, 12, 4):
    print(i, end=" ")
print()

# type
print("Type of names is", type(names))

# isinstance
print("Is names instance of tuple?", isinstance(names, tuple))

# reversed
print("Names, reversed:", tuple(reversed(names)))

# sorted
print("Names, sorted:", sorted(names))
