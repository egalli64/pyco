"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Foundation

Variables
"""

# 1. defining a variable (with a reasonable name)
user_id = 99

# 2. accessing the object referenced by the variables
print("The variable user_id:", user_id)

# 3. consider this variable as if it was a constant
ANSWER = 42
print("ANSWER is meant to be a constant:", ANSWER)

# 4. another variable referencing the same object
other = user_id
print("The variable other:", other)

# 5. changing an immutable object actually means associating a new object to the variable
other += 1
print("Now other is", other)
print("But user_id still refers to", user_id)

# 6. using an undefined variable is a NameError
# print(message)
