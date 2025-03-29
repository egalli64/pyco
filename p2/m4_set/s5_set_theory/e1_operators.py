"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Set theory - by operators
"""

red = {"Tom", "Bob", "Kim"}
green = {"Al", "Kim", "Joe"}

print(f"Union: {red} | {green} is", red | green)
print(f"Intersection: {red} & {green} is", red & green)

print(f"Difference: {red} - {green} is", red - green)
print(f"Symmetric difference: {red} ^ {green} is", red ^ green)
print()

yellow = red | green

print(f"Subset: {red} <= {yellow} is", red <= yellow)
print(f"Proper subset: {red} < {red} is", red < red)

# superset
print(f"Superset: {yellow} >= {green} is", yellow >= green)
print(f"Proper superset: {green} > {green} is", green > green)
