"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read bytes in a bytearray from binary file by read()
"""

# deserialize a byte array
with open("data.bin", "rb") as f:
    data = f.read()
    decoded = list(data)

print(f"Deserializing {data} (bytearray)")
print("As list of (small) integers:", list(data))

# deserialize a UTF-8 string
with open("hello_world.bin", "rb") as f:
    data = f.read()
    decoded = data.decode("utf-8")

print(f"Deserializing {data} (bytearray)")
print("As string:", decoded)
