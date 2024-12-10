"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - Control Flow

Alterate / terminate a loop
The break statement
"""

s = "Welcome To Pythonville"
print(f"Checking string '{s}'\n")

print("Break as soon as a blank is found:", end=" ")
blank_flag = False
for c in s:
    if c == " ":
        blank_flag = True
        print()
        break
    else:
        print(c, end="")

if blank_flag:
    print("A blank has been detected!")
