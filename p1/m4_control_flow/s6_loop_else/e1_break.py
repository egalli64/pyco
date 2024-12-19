"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Alterate / terminate a loop
The loop - else statement
"""

s = "Welcome To Pythonville"
print(f"Checking string '{s}'\n")

print("Break as soon as a blank is found:", end=" ")
for c in s:
    if c == " ":
        print()
        break
    else:
        print(c, end="")
else:
    print("\nNo blank has been detected in the string!")
