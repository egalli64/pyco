"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - Control Flow

For loop
"""
print("in [0..10):", end="\t")
for i in range(10):
    print(i, end=" ")
print()

print("in [5..10):", end="\t")
for i in range(5, 10):
    print(i, end=" ")
print()

# skip odd values
print("even [0..10):", end="\t")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# loop on a string
s = "Python"
print(f"For-looping on each char in {s}")

# for each index in string
print("By index [0 .. len):", end="\t")
for i in range(len(s)):
    print(s[i], end=" ")
print()

# for each char in string
print("On each char [P .. n]:", end="\t")
for c in s:
    print(c, end=" ")
print()
