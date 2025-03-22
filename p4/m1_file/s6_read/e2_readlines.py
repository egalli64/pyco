"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read by readlines(): all file in a list of strings
"""

FRIENDS_FILENAME = "p4/m1_file/friends.txt"

with open(FRIENDS_FILENAME) as f:
    print("Read all lines from file:")
    # readlines do not strip the tailing newline
    lines = f.readlines()

for line in lines:
    print(line, end="")
print("---\n")
