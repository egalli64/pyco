"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Read
"""
FRIENDS_FILENAME = "p4/m1_file/friends.txt"

# open file implicitly in read-text mode
with open(FRIENDS_FILENAME) as f:
    # read all the file content in a string
    content = f.read()

print("Read from file (full):")
print(content)
print("---")

with open(FRIENDS_FILENAME) as f:
    print("Read from file (full - by lines):")
    # readlines do not strip the tailing newline
    lines = f.readlines()

for line in lines:
    print(line, end="")
print("---\n")

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by chunk):")

    # read just 6 characters (or less) each time
    while content := f.read(6):
        print(content, end="")
        print("---")
    print("done!\n")

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by line):")
    while line := f.readline():
        # readline do not strip the tailing newline
        print(line, end="")
print("---\n")

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by line - implicit form):")
    for line in f:
        print(line, end="")
