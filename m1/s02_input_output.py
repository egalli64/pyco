"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 1 - Fundamental concepts

Input and output
"""
# print a single string to the console
print("Hello, Python")

# print three values: string, integer, string
print("Hello", 42, "Python")

# use an underscore as separator
print("Hello", 42, "Python", sep="_")

# do not to the next line at the end of each print
print("Hello", end="")
print(42, end="")
print("Python", end="")

# print just a new line
print()

name = input("What's your name? ")
print("Hello,", name)

age = int(input("How old are you? "))
print("I wonder if you are really ", age, ", ", name, sep="")
