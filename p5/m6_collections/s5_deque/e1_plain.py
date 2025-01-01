"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

deque
"""

from collections import deque

# 1. create a deque from an iterable
data = deque([1, 2, 3])
print("The initial data in deque:", data)
print()

# 2. append
data.append(4)
print("After append:", data)
data.appendleft(0)
print("After append left:", data)
print()

# 3. pop
data.pop()
print("After pop:", data)
data.popleft()
print("After pop left:", data)
print()

# 4. rotate
data.rotate(1)
print("After rotate 1 (right):", data)
data.rotate(-2)
print("After rotate -2 (left):", data)
