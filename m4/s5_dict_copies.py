"""
Python Course

https://github.com/egalli64/pyco

Module 4 - Dictionary and set

Dictionary: copy in different ways
"""
from copy import deepcopy

red = {"kim": [1284, 2312], "bob": []}
print("The red team:", red)

green = {"joe": [1841], "tim": []}
print("The green team:", green)

# merge
yellow = {**red, **green}
print("The yellow team:", yellow)
# shallow copy
yellow["tim"].append(7231)
print("tim has changed! (green)", green)

# update
orange = {"nat": [3312]}
print("The orange team:", orange)
orange.update(red)
print("Updated orange:", orange)
# shallow copy
orange["bob"].append(6138)
print("bob has changed! (red)", red)

# 1. reference copy
yellow = green
print("Two variables, one object:", id(yellow) == id(green))

# 2. shallow object copy
yellow = green.copy()
print("Two variables, two objects:", id(yellow) != id(green))
print("Mutable values refer to the same object:", end=" ")
print(id(yellow["tim"]) == id(green["tim"]))

# 3. deep object copy
yellow = deepcopy(green)
print("Two variables, two objects:", id(yellow) != id(green))
print("Mutable values refer to different objects:", end=" ")
print(id(yellow["tim"]) != id(green["tim"]))
