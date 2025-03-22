"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read by readline(): read from file line by line
"""

FRIENDS_FILENAME = "p4/m1_file/friends.txt"

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by line):")
    while line := f.readline():
        # readline do not strip the tailing newline
        print(line, end="")
print("---\n")
