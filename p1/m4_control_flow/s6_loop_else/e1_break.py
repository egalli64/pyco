"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Alterate / terminate a loop
The loop - else statement
"""

# s = "Welcome To Pythonville"
s = "WelcomeToPythonville"
print(f"Checking string '{s}'\n")

print("Break as soon as a blank is found (for-else):", end=" ")
for c in s:
    if c == " ":
        print()
        break
    else:
        print(c, end="")
else:
    print("\nNormal exit from loop - no blank has been detected in the string\n")

# same, without for-else
print("Break as soon as a blank is found (check flag):", end=" ")
flag = True
for c in s:
    if c == ' ':
        print()
        flag = False
        break
    else:
        print(c, end="")
if flag:
    print("\nNormal exit from loop - no blank has been detected in the string\n")
