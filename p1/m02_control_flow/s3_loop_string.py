"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Control Flow

While and for loop on a string
"""
s = "Python"

print("while loop")

# while index is in string
print("[0 .. len):", end="\t")
i = 0
while i < len(s):
    print(s[i], end=" ")
    i += 1
print()

print("\nfor loops")

# for each index in string
print("[0 .. len):", end="\t")
for i in range(len(s)):
    print(s[i], end=" ")
print()

# for each char in string
print("[P .. n]:", end="\t")
for c in s:
    print(c, end=" ")
print()
