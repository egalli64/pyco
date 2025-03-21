"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read by read() - all the file content in a string
"""

FRIENDS_FILENAME = "p4/m1_file/friends.txt"

# open file implicitly in read-text mode
with open(FRIENDS_FILENAME) as f:
    content = f.read()

print("Read from file (full):")
print(content)
print("---")
