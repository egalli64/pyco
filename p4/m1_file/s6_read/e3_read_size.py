"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read by read() - specifying the buffer max size
"""

FRIENDS_FILENAME = "p4/m1_file/friends.txt"

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by chunk):")

    # read just 6 characters (or less) each time
    while content := f.read(6):
        print(content, end="")
        print("---")
    print("done!\n")
