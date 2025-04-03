"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

Protobuf - SerializeToString()
"""

import math
import info_pb2

TARGET = "info.bin"

info = info_pb2.Info()
info.price = 1_000_000
info.ratio = math.pi
info.message = "こんにちは、世界"

with open(TARGET, "wb") as f:
    sz = f.write(info.SerializeToString())

print(f"{sz} bytes written to {TARGET}")
