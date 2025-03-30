"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Set theory - by methods
"""

red = {"Tom", "Bob", "Kim"}
green = {"Al", "Kim", "Joe"}

print(f"{red}.union({green}) is", red.union(green))
print(f"{red}.intersection({green}) is", red.intersection(green))

print(f"{red}.difference({green}) is", red.difference(green))
print(f"{red}.symmetric_difference({green}) is", red.symmetric_difference(green))
print()

yellow = red | green

print(f"{red}.issubset({yellow}) is", red.issubset(yellow))
print(f"{yellow}.issuperset({green}) is", yellow.issuperset(green))
