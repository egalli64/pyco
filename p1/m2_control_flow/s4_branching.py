"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Control Flow

Branching
"""

s = "Welcome To Pythonville"
print(f"Checking string '{s}'")

# break
print("Break as soon as a blank is found:", end=" ")
for c in s:
    if c == " ":
        break
    else:
        print(c, end="")
print()

# break/else
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

# continue
print("Skip blanks (by continue):", end=" ")
for c in s:
    if c == " ":
        continue
    else:
        print(c, end="")
print()

# continue can often be easily avoided
print("Skip blanks (no continue):", end=" ")
for c in s:
    if c != " ":
        print(c, end="")
print()


def print_first_word(s):
    """
    A function that prints up to the first blank
    """
    for c in s:
        if c == " ":
            return
        else:
            print(c, end="")


print("Return as a blank is found:", end=" ")
print_first_word(s)
print()
