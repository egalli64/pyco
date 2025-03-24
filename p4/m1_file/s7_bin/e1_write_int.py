"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write bytes to binary file by write()
"""

FOLDER = "p4/m1_file/s7_bin/"
FILE_1_BYTE = FOLDER + "data_1.bin"

with open(FILE_1_BYTE, "wb") as f:
    # when the numbers are in [0 .. 255], no need to convert each of them to byte
    data = [0, 1, 127, 255]
    print("Serializing:", data)

    encoded = bytes(data)
    f.write(encoded)

FILE_4_BYTES = FOLDER + "data_4.bin"

with open(FILE_4_BYTES, "wb") as f:
    # we should know the int size to manage it correctly
    data = [-2_147_483_648, 0, 2_147_483_647]
    print("Serializing:", data)

    for cur in data:
        buffer = cur.to_bytes(4, byteorder="little", signed=True)
        print(f"{cur} to bytes: {buffer}")
        f.write(buffer)
