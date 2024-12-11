"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Set

Set operators
"""
red = {"Tom", "Bob", "Kim"}
print("Red team:", red)

green = {"Al", "Kim", "Joe"}
print("Green team:", green)

# union
yellow = red | green
print("Yellow team, union (by operator |),", yellow)
print("Union (by method union) is", red.union(green))

# intersection
print("Intersection (by operator &) is", red & green)
print("Intersection (by method intersection) is", red.intersection(green))

# difference
print("Difference (by operator -) is", red - green)
print("Difference (by method difference) is", red.difference(green))

# symmetric difference
print("Symmetric difference (by operator ^) is", red ^ green)
print("Symmetric difference (by method symmetric_difference) is", end="")
print(red.symmetric_difference(green))

# subset
print("Is red a subset of yellow?")
print("By operator <=", red <= yellow)
print("By method issubset", red.issubset(yellow))

print("Is red a proper subset of itself?")
print("By operator <", red < red)

# superset
print("Is yellow a superset of green?")
print("By operator >=", yellow >= green)
print("By method issuperset", yellow.issuperset(green))

print("Is green a proper superset of itself?")
print("By operator >", green > green)
