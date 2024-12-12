"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Set theory
"""

red = {"Tom", "Bob", "Kim"}
print("Red team:", red)

green = {"Al", "Kim", "Joe"}
print("Green team:", green)

# union
yellow = red | green
print("Yellow team, union (by |),", yellow)
print("Union (by union()) is", red.union(green))

# intersection
print("Intersection (by &) is", red & green)
print("Intersection (by intersection()) is", red.intersection(green))

# difference
print("Difference (by -) is", red - green)
print("Difference (by difference()) is", red.difference(green))

# symmetric difference
print("Symmetric difference (by ^) is", red ^ green)
print("Symmetric difference (by symmetric_difference()) is ", end="")
print(red.symmetric_difference(green))

# subset
print("Is red a subset of yellow? By <= is", red <= yellow, end=", ")
print("by issubset() is", red.issubset(yellow))

print("Is red a proper subset of itself?", end=" ")
print("By < is", red < red)

# superset
print("Is yellow a superset of green? By >= is", yellow >= green, end=", ")
print("by issuperset() is", yellow.issuperset(green))

print("Is green a proper superset of itself?", end=" ")
print("By > is", green > green)
