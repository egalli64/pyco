"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write to file by method write()
"""

FILENAME = "my_file.txt"
friends = ["Tom", "Jenny", "Bob", "Kim", "Micky", "Lee"]

# append to file - do not overwrite
with open(FILENAME, "a") as f:
    for friend in friends:
        f.write(friend)
        f.write(" ")
    f.write("\n")
