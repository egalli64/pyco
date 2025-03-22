"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

using struct to generate bytearray
"""

SOURCE = "struct.bin"

import struct

with open(SOURCE, "rb") as f:
    data = f.read()

# the source: an integer (i), a double (d), a (len) string (s)
# !!! getting the string len is a nuisance !!!
unpacked = struct.unpack(f"id24s", data)

print(f"Deserialized: {unpacked[0]}, {unpacked[1]}, and ", end="... ")
print(unpacked[2].decode("utf-8"))
