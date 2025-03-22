"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The Path class - exists()
"""

from pathlib import Path

for filename in ("p4/m1_file/friends.txt", "missing"):
    path = Path(filename)

    print(f"The file '{filename}'", end=" ")
    if path.exists():
        print("exists")
    else:
        print("does not exist")
