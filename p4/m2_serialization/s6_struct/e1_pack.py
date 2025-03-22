"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

using struct to generate bytearray
"""

TARGET = "struct.bin"

import math
import struct

price = 1_000_000
ratio = math.pi
b_message = "こんにちは、世界".encode("utf-8")
b_len = len(b_message)

# the source: an integer (i), a double (d), a (len) string (s)
packed = struct.pack(f"id{b_len}s", price, ratio, b_message)

print("Serializing the data")

with open(TARGET, "wb") as f:
    sz = f.write(packed)

print(f"{sz} bytes written to {TARGET}, string is sized {b_len}")
