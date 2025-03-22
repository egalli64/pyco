"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read by for-in: implicit readline()
"""

FRIENDS_FILENAME = "p4/m1_file/friends.txt"

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by line - implicit form):")
    for line in f:
        print(line, end="")
