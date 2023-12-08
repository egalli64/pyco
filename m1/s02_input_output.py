"""
Python Course

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Input and output
"""
# print a single string to the console
print("Hello, Python")

# print more arguments
print("Hello", "Python")

# use an underscore as separator
print("Hello", "Python", sep="_")

# do not add a newline at the end of each print
print("Hello", end="")
print("Python", end="")

# print just a newline
print()

name = input("What's your name? ")
print("Hello,", name)

age = int(input("How old are you? "))
print("I wonder if you are really ", age, ", ", name, sep="")
