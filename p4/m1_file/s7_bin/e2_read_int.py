"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read bytes from binary file by read()
"""

FOLDER = "p4/m1_file/s7_bin/"

# deserialize a byte array
FILE_1_BYTE = FOLDER + "data_1.bin"

with open(FILE_1_BYTE, "rb") as f:
    data = f.read()
    decoded = list(data)

print(f"Deserializing {data} (bytes)")
print("As list of (small) integers:", list(data))

# deserialize a byte array
FILE_4_BYTES = FOLDER + "data_4.bin"

with open(FILE_4_BYTES, "rb") as f:
    values = []
    # notice I should know size and how many integers to read
    for i in range(3):
        buffer = f.read(4)
        print(f"Buffer {i}: {buffer}")
        cur = int.from_bytes(buffer, byteorder="little", signed=True)
        values.append(cur)

print("As list of (32 bit) signed integers:", values)
