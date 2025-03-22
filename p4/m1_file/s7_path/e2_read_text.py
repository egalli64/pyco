"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The Path class - read_text()
"""

from pathlib import Path

FRIENDS_FILENAME = "p4/m1_file/friends.txt"

try:
    input_path = Path(FRIENDS_FILENAME)
    content = input_path.read_text()
except FileNotFoundError as ex:
    print("Can't read_text", ex)
else:
    print(f"The file {FRIENDS_FILENAME} contains:")

    # generate a list of strings from the file content
    friends = content.splitlines()

    for friend in friends:
        print("-", friend)

    check = "Will"
    if check in friends:
        print(check, "is a friend")
    else:
        print("I don't know anything about", check)
