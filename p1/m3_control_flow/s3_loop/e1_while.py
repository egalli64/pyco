"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - Control Flow

While loop
"""
print("in [0..10):", end="\t")
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()

print("in [5..10):", end="\t")
i = 5
while i < 10:
    print(i, end=" ")
    i += 1
print()

# skip odd values
print("even [0..10):", end="\t")
i = 0
while i < 10:
    print(i, end=" ")
    i += 2
print("\n")

# loop on a string
s = "Python"

print(f"While-looping on each char in {s}:", end=" ")
i = 0
while i < len(s):
    print(s[i], end=" ")
    i += 1
print()
