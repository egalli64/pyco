"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - More fundamental concepts

Boolean
"""
flag = True
print(type(flag), flag, not flag)

a = 0
b = 3
c = 10
print(f"a = {a}, b = {b}, c = {c}")

# if b in [a .. c]
if a <= b and b <= c:
    print(f"{b} is in [{a} .. {c}]")

# chained comparison
if a <= b <= c:
    print(f"{b} is in [{a} .. {c}]")
print()

# boolean cast
for cur in a, b:
    if cur == False:
        print("Zero is False:", a)
    else:
        print("Any other number is not False:", b)

if 1 == True:
    print("One is True")

two = 2
if two != True and two != False:
    print("Two (and every other non-zero number) is not True nor False!")

if two:
    print("Two (and every other non-zero number) is truthy!")

for x in range(3):
    # implicit check against "not equal zero"
    if x % 2:
        print(x, "is odd")
    else:
        print(x, "is even")
print()

# conditional expression

# 1. explicit, more readable
if a:
    result = a
else:
    result = b
print("result = 'a' if 'a' is truthy, otherwise is 'b':", result)

# 2. conditional expression by if - else, compact and flexible
result = a if a else b
print("same (conditional expression by if - else):", result)

# 3. conditional expression by or, very compact
result = a or b
print("same (conditional expression by or):", result)

# 4. conditional expression by and
result = b and c
print("result = 'b' if 'b' is falsy, otherwise is 'c':", result)
