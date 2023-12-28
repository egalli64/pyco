"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - More on types

List - zip
"""
names = ["tom", "bob", "kim", "jim"]
colors = ["green", "blue", "yellow", "red"]

couples = list(zip(names, colors))

for name, color in couples:
    print(f"{color} is {name}'s preferred color")
