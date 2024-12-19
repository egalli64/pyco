"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Alterate / terminate a loop
The return statement
"""
s = "Welcome To Pythonville"
print(f"Checking string '{s}'\n")


def print_first_word(s):
    """
    A function that prints up to the first blank
    """
    for c in s:
        if c == " ":
            print()
            return
        else:
            print(c, end="")
    print()


print("Return as soon as a blank is found:")
print_first_word(s)
print_first_word("Hello")
