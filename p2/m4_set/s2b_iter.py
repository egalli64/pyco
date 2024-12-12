"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Set as iterable
"""

# a set
letters = set("emanuele")
print("A set from an iterable:", letters)

# len()
print("Its length is", len(letters))

# operator in / not in
targets = {"a", "z"}
for target in targets:
    if target in letters:
        print(f"The element '{target}' is in the set")
    elif target not in letters:
        print(f"The element '{target}' is not in the set")

# for loop
print("Looping on the set:", end=" ")
for letter in letters:
    print(letter, end=" ")
print()
