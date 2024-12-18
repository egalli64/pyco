"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - More fundamental concepts

List - zip
"""
names = ["tom", "bob", "kim", "jim"]
colors = ["green", "blue", "yellow", "red"]

couples = list(zip(names, colors))

for name, color in couples:
    print(f"{color} is {name}'s preferred color")
