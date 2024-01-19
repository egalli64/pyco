"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Input and output
Read from standard input (keyboard)
"""
# print a prompt to standard output, get back the user input
name = input("What's your name? ")
print("Hello,", name)

# I'd like to get an integer, but input return a string
s = input("How old are you? ")

# convert the string to int (beware of ValueError)
age = int(s)
print("I wonder if you are really ", age, ", ", name, sep="")
