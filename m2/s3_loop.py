"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 2 - Control Flow

While and for loop
"""
print("while loops")

# while [0 .. 10)
print("[0 .. 10):", end="\t")
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()

# while [5 .. 10)
print("[5 .. 10):", end="\t")
i = 5
while i < 10:
    print(i, end=" ")
    i += 1
print()

# while even [0 .. 10)
print("even < 10:", end="\t")
i = 0
while i < 10:
    print(i, end=" ")
    i += 2
print()

print("\nfor loops")

# for [0 .. 10)
print("[0 .. 10):", end="\t")
for i in range(10):
    print(i, end=" ")
print()

# for [5 .. 10)
print("[5 .. 10):", end="\t")
for i in range(5, 10):
    print(i, end=" ")
print()

# for even [0 .. 10)
print("even < 10:", end="\t")
for i in range(0, 10, 2):
    print(i, end=" ")
print()
