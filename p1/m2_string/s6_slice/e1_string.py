"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - slice on string
"""
# a string
name = "slartibartfast"
print("A string:", name)
print()

# 'normal'
print("'Normal' slice [1..4):", end=" ")
print(name[1:4])

# header
print("First three chars:", end=" ")
print(name[:3])

# rest
print("After the first three:", end=" ")
print(name[3:])

# tail
print("The last three:", end=" ")
print(name[-3:])

# skip every second char
print("Alternate from first:", end=" ")
print(name[::2])

# skip every first char
print("Alternate from second:", end=" ")
print(name[1::2])

# no exception on slicing
print("Wrong interval, empty slice:", end=" ")
print(f"'{name[42:18]}'")
print()

# alias - different variables, same object
name2 = name
if name is name2 and name == name2:
    print("Alias: the object is the same")

# object copy could be optimized out by the Python compiler!
name2 = name[:]
if name is name2 and name == name2:
    print("Copy: could be the same object!")
