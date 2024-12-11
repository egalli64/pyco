"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Views
"""
# a dictionary
friends = {"kim": 1284, "bob": 4423, "tom": 1284, "jim": 1299}

print("The dictionary:", friends)

# its items
print("As list of tuples:", friends.items())

# its keys
print("The keys:", friends.keys())

# its values
print("The values:", friends.values())
print("---")

print("Each pair:")
for key, value in friends.items():
    print(f"{key}, {value}")
print("---")

print("Each key:")
for key in friends.keys():
    print(key)
print("---")

print("Each key (implicit):")
for key in friends:
    print(key)
print("---")

print("Each value:")
for value in friends.values():
    print(value)
print("---")

print("Each key (sorted):")
for key in sorted(friends.keys()):
    print(key)
print("---")

print("Each value (sorted):")
for value in sorted(friends.values()):
    print(value)
print("---")

print("Each pair (sorted):")
for key, value in sorted(friends.items()):
    print(f"{key}, {value}")
print("---")

print("Each value (no duplicates):")
for value in set(friends.values()):
    print(value)
print("---")

print("Each value (no duplicates, sorted):")
for value in sorted(set(friends.values())):
    print(value)
print("---")
