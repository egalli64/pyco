"""
Python Course

https://github.com/egalli64/pyco

Module 7 - File

Write
"""
FILENAME = "my_file.txt"
friends = ["Tom", "Jenny", "Bob", "Kim", "Micky", "Lee"]

# (re)write the file
with open(FILENAME, "w") as f:
    # print each friend in the file
    for friend in friends:
        print(friend, end=" ", file=f)
    print(file=f)

# same, but append, and using write instead of print
with open(FILENAME, "a") as f:
    for friend in friends:
        f.write(friend)
        f.write(" ")
    f.write("\n")
