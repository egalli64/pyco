"""
Python Course

https://github.com/egalli64/pyco

Module 7 - File

Read
"""
FRIENDS_FILENAME = "friends.txt"

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
print("---")

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by chunk):")
    while True:
        # read just 6 characters (or less) each time
        content = f.read(6)
        if content:
            print(content)
            print("---")
        else:
            break

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by line):")
    while True:
        # readline do not strip the tailing newline
        line = f.readline()
        if line:
            print(line, end="")
        else:
            break
print("---")

with open(FRIENDS_FILENAME) as f:
    print("Read from file (by line - implicit form):")
    for line in f:
        print(line, end='')
