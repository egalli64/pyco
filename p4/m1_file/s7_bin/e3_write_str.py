"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write encoded to binary file by write()
"""

FILE_STR_BYTE = "p4/m1_file/s7_bin/string.bin"

# in a string how the characters are actually represented is an internal detail
hello = "こんにちは、世界!"
print("Serializing:", hello)

with open(FILE_STR_BYTE, "wb") as f:
    # use the standard UTF-8 encoding format
    encoded = hello.encode("utf-8")
    f.write(encoded)
