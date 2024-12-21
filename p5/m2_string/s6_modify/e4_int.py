"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Modify - convert int to str
"""

value = 42
print("Integer are print using decimal representation:", value, type(value))

s = str(value)
print(f"The constructor str() uses the decimal representation: {s} {type(s)}")
print("\nUse:")
print(" bin() for binary:", bin(value))
print(" oct() for octal:", oct(value))
print(" hex() for hexadecimal:", hex(value))
