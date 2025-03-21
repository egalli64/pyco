"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write bytes in a bytearray to binary file by write()
"""

data = bytearray([0, 1, 127, 255])
with open("data.bin", "wb") as f:
    f.write(data)
