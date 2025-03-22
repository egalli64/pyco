"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

Protobuf - ParseFromString()
"""

import info_pb2

SOURCE = "info.bin"

data = info_pb2.Info()
with open(SOURCE, "rb") as f:
    data.ParseFromString(f.read())

print(f"Deserialized: {data.price}, {data.ratio}, and {data.message}")
