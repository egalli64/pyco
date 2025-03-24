"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read a UTF-8 binary string by read() and decode() it
"""

FILE_STR_BYTE = "p4/m1_file/s7_bin/string.bin"

with open(FILE_STR_BYTE, "rb") as f:
    data = f.read()
    decoded = data.decode("utf-8")

print(f"Deserializing {data} (bytes)")
print("As string:", decoded)
