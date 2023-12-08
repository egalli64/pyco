"""
Python Course

https://github.com/egalli64/pyco

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

# an immutable set
people = frozenset(["jo", "bo", "mo"])
print(people, type(people))

# len()
print("Length of letters is", len(letters))

# operator in
target = 'a'
if target in letters:
    print(f"'{target}' found in {letters}")

# for loop
for letter in letters:
    print("-", letter)

# set comprehension

values = {x for x in range(20) if x % 3 == 1}
print(values)
