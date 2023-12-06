"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 4 - Dictionary and set

Set
"""
# a set
friends = {"bob", "tom", "kim"}
print(friends, type(friends))

# an empty set
enemies = set()
print(enemies, type(enemies))

# a set of six strings!
letters = set("emanuele")

# len()
print("Length of letters is", len(letters))

# operator in on
target = 'a'
if target in letters:
    print(f"'{target}' found in {letters}")

# for loop
for letter in letters:
    print("-", letter)
