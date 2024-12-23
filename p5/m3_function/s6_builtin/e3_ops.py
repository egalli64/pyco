"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Builtin - operations on iterables
"""

values = (42, 94, 12, 64, 87)
print("Values:", values)

# sum
print("Sum:", sum(values))

# min
print("Min:", min(values))

# max
print("Max:", max(values))

# ...
names = ("Tom", "Bob", "Joe", "Jim")
print("Names:", names)

# zip - notice: names is the shortest iterable passed in
pairs = tuple(zip(names, values))
print("Zip names+values:", pairs)

# enumerate
pairs = tuple(enumerate(names))
print("Enumerate names:", pairs)

pairs = tuple(enumerate(values, 1))
print("Enumerate values:", pairs)
