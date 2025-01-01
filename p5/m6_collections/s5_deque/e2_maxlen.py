"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

deque - append when maxlen is set
"""

from collections import deque

data = deque([9, 8, 7], maxlen=3)
print("A deque with maxlen:", data)
for i in range(5):
    if i % 2:
        data.append(i)
    else:
        data.appendleft(i)
    print(f"After append{"" if i%2 else "left"}:", data)
