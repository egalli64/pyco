"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

F-string formatting - string
"""

s = "Hello, Python!"

# padding and alignment
print(f"Left aligned:   {s:_<20}")
print(f"Right aligned:  {s:_>20}")
print(f"Center aligned: {s:_^20}")
print()

# truncating
print(f"The beginning of a message: {s:.5} ...")

# truncated, padded and aligned
print(f"{s:_^9.5}")
