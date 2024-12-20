"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Encoding and decoding - encoding
"""

# a string with non-ASCII char in it
s = "Cafè Olè"
print(f"A string: {s}, {type(s)}, len={len(s)}")

bs = s.encode(encoding="utf-8")
print(f"As bytes (utf-8, default): {bs}, {type(bs)}, len={len(bs)}\n")

try:
    bs = s.encode(encoding="ascii")
except UnicodeEncodeError as ex:
    print("UnicodeEncodeError:", ex)

bs = s.encode(encoding="utf-16")
print(f"As bytes (utf-16): {bs}, len={len(bs)}")

bs = s.encode(encoding="ISO-8859-1")
print(f"As bytes (Latin-1): {bs}, len={len(bs)}")
