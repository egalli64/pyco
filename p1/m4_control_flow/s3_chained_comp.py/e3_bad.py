"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Chained comparisons - unreadability
"""

a = 3
b = 5
c = 4

print(f"Check if {a} is positive, {a} is not equal {b}, and {b} is greater than {c}")
print("All the three condition should hold")

print("Plain check", end=" ... ")
if a > 0 and a != b and b > c:
    print("the triplet is good")
else:
    print("unexpected")

print("Chained comparisons (don't do it!)", end=" ... ")
if 0 < a != b > c:
    print("the triplet is good")
else:
    print("unexpected")
