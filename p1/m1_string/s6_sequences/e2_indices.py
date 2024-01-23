"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Strings and variables

Sequences - index() and in operator
"""
# a string is a sequence
str = "welcome to Python's world"
print("A string:", str)
# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print("A list:", lis)
print()

# looking for a substring in a string
for target in "w", "wa":
    print(f"Searching for {target} in {str}")
    try:
        pos = str.index(target)
        print(f"\tfound at {pos}")
    except ValueError as ex:
        print("\t", ex)
print()

# looking for a value in a list
for target in "tim", "zoe":
    print(f"Searching for {target} in {lis}")
    try:
        pos = lis.index(target)
        print(f"\tfound at {pos}")
    except ValueError as ex:
        print("\t", ex)
print()

# operator (not) in
if "elc" in str:
    print("substring 'elc' is in the string!")

if "tom" in lis:
    print("element 'tom' is in the list!")

if "z" not in str:
    print("substring 'z' is not in the string!")

if "zoe" not in lis:
    print("element 'zoe' is not in the list!")
