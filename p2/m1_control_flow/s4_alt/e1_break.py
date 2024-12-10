"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - Control Flow

Alterate / terminate a loop
The break (else) statement
"""
s = "Welcome To Pythonville"
print(f"Checking string '{s}'\n")

print("Break as soon as a blank is found:", end=" ")
for c in s:
    if c == " ":
        break
    else:
        print(c, end="")
print()

t = "WelcomeToPythonville"
print("Break-else on blank (for a string with no blank):", end=" ")
for c in t:
    if c == " ":
        break
    else:
        print(c, end="")
else:
    print(" - no blank detected in the string", end="")
print()
