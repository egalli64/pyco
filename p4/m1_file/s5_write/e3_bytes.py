"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write bytes to binary file by write()
"""

# an array of small integers - interval [0 .. 255]
data = [0, 1, 127, 255]
print("Serializing:", data)

with open("data.bin", "wb") as f:
    encoded = bytes(data)
    f.write(encoded)

# a string - how the characters are actually represented is an internal detail
hello = "こんにちは、世界"
print("Serializing:", hello)

with open("hello_world.bin", "wb") as f:
    # use the standard UTF-8 encoding format
    encoded = hello.encode("utf-8")
    f.write(encoded)
