"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - Control Flow

Alterate / terminate a loop
The continue statement
"""
s = "Welcome To Pythonville"
print(f"Checking string '{s}'\n")

print("Skip blanks:", end=" ")
for c in s:
    if c == " ":
        continue
    else:
        print(c, end="")
print()

# continue can be often avoided
print("Skip blanks (no continue):", end=" ")
for c in s:
    if c != " ":
        print(c, end="")
print()

print("Skip blanks (no continue /2):", end=" ")
for c in s:
    if c != " ":
        print(c, end="")
    else:
        # placeholder, maybe I should do something if the current char is a blank?
        pass
print()
