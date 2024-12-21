"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Modify - split and join
"""

s = "one\ntwo\nthree"
print(f"The original string: {s}\n")

tokens = s.split()
print("Split:", tokens)
print("Split (1):", s.split(maxsplit=1))
print("Right split (1):", s.rsplit(maxsplit=1))
print("Split lines (keeping):", s.splitlines(keepends=True))

s = ",".join(tokens)
print("Join on comma:", s)
