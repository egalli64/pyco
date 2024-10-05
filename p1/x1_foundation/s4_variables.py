"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Foundation

Variables
"""

# 1. defining a variable (with a reasonable name)
id = 99

# 2. accessing the object referenced by the variables
print("The variable id:", id)

# 3. consider this variable as if it was a constant
ANSWER = 42

# 4. another variable referencing the same object
other = id
print("The variable other:", other)

# 5. changing an immutable variable actually means associating a new object to the variable
other += 1
print("Now other is", other)
print("But id still refers to", id)

# 6. using an undefined variable is a NameError
# print(message)
