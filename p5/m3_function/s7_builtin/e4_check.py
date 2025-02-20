"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Builtin - boolean checks on iterables (all - any)
"""

# all
values = (42, 94, 12, 64, 87)
print(f"Are all in {values} truthy?", all(values))

values = ("Bob", "", "Tom")
print(f"Are all in {values} truthy?", all(values))

# any
values = ("", None, {}, "0")
print(f"Is there any truthy in {values}?", any(values))
