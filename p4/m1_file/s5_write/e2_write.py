"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write to file by method write()
"""

FILENAME = "my_file.txt"
friends = ["Tom", "Jenny", "Bob", "Kim", "Micky", "Lee"]

# append to file - do not overwrite
with open(FILENAME, "a") as my_file:
    for friend in friends:
        my_file.write(friend)
        my_file.write(" ")
    my_file.write("\n")
