"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Write to file by print()
"""

FILENAME = "my_file.txt"
friends = ["Tom", "Jenny", "Bob", "Kim", "Micky", "Lee"]

# (re)write the file
with open(FILENAME, "w") as f:
    # print each friend in the file
    for friend in friends:
        print(friend, end=" ", file=f)
    print(file=f)
