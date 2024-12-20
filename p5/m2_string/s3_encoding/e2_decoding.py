"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Encoding and decoding - decoding
"""

# a bytes object, utf-8 coded
bs = b"Caf\xc3\xa8 Ol\xc3\xa8"
print(f"A bytes object: {bs}, {type(bs)}, len={len(bs)}")

s = bs.decode(encoding="utf-8")
print(f"As string: {s}, {type(s)}, len={len(s)}")

try:
    s = bs.decode(encoding="ascii")
except UnicodeDecodeError as ex:
    print("UnicodeDecodeError:", ex)

# a bytes object, utf-16 coded
bs = b"\xff\xfeC\x00a\x00f\x00\xe8\x00 \x00O\x00l\x00\xe8\x00"
print(f"\nA bytes object: {bs}, {type(bs)}, len={len(bs)}")

s = bs.decode(encoding="utf-16")
print(f"As string: {s}, {type(s)}, len={len(s)}")

try:
    s = bs.decode(encoding="utf-8")
except UnicodeDecodeError as ex:
    print("UnicodeDecodeError:", ex)
