"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 7 - File

The Path class
"""
from pathlib import Path
from random import random

FRIENDS_FILENAME = "friends.txt"
OUTPUT_FILENAME = "random_values.txt"

try:
    input_path = Path(FRIENDS_FILENAME)
    content = input_path.read_text()
except FileNotFoundError as ex:
    print("Can't read_text", ex)
else:
    friends = content.splitlines()

    for friend in friends:
        print("-", friend)

    check = "Will"
    if check in friends:
        print(check, "is a friend")
    else:
        print("I don't know anything about", check)

content = ""
for value in range(10):
    content += str(random()) + '\n'

output_path = Path(OUTPUT_FILENAME)
if output_path.exists():
    print(f"The file {OUTPUT_FILENAME} already exists!")
else:
    # if we don't check, it would overwrite existing data
    output_path.write_text(content)
