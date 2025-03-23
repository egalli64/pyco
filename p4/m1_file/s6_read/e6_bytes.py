"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read bytes from binary file by read()
"""

# deserialize bytes
with open("data.bin", "rb") as f:
    data = f.read()
    decoded = list(data)

print(f"Deserializing {data} (bytes)")
print("As list of (small) integers:", list(data))

# deserialize a UTF-8 string
with open("hello_world.bin", "rb") as f:
    data = f.read()
    decoded = data.decode("utf-8")

print(f"Deserializing {data} (bytes)")
print("As string:", decoded)
