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

# Giving slice start and stop: -lar--...
print("Plain slice [1..4):", end=" ")
print(name[1:4])

# Giving only slice stop: sla--
print("Implicit start from zero [0..3):", end=" ")
print(name[:3])

# Giving only slice start: ---rti...
print("Implicit stop to the end [3..len(name)]:", end=" ")
print(name[3:])

# Giving only slice start (negative): ...--ast
print("Implicit stop to the end, negative start: [-3..len(name)]", end=" ")
print(name[-3:])

# Giving only the step, start from end tsaf...
print("Implicit start/stop, reverse the string:", end=" ")
print(name[::-1])

# Giving only the step, skip every second char s-a-t-...
print("Implicit start/stop, alternate from first:", end=" ")
print(name[::2])

# Giving start and step, skip every first char -l-r-i...
print("Implicit stop, alternate from second:", end=" ")
print(name[1::2])

# No exception on slicing
print("Wrong interval, empty slice:", end=" ")
print(f"'{name[42:18]}'")
print()
