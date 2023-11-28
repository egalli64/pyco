"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 4 - Dictionary

Views, looping
"""
friends = {"kim": 1284, "bob": 4423, "tom": 1284, "jim": 1299}

print("The dictionary:", friends)
print("As list of tuples:", friends.items())
print("The keys:", friends.keys())
print("The values:", friends.values())
print("---")

print("All the pairs:")
for key, value in friends.items():
    print(f"{key}, {value}")
print("---")

print("All the keys:")
for key in friends.keys():
    print(key)
print("---")

print("All the keys (implicit):")
for key in friends:
    print(key)
print("---")

print("All the values:")
for value in friends.values():
    print(value)
print("---")

print("All the keys (sorted):")
for key in sorted(friends.keys()):
    print(key)
print("---")

print("All the values (sorted):")
for value in sorted(friends.values()):
    print(value)
print("---")

print("All the pairs (sorted):")
for key, value in sorted(friends.items()):
    print(f"{key}, {value}")
print("---")

print("All the values (no duplicates):")
for value in set(friends.values()):
    print(value)
print("---")

print("All the values (no duplicates, sorted):")
for value in sorted(set(friends.values())):
    print(value)
print("---")
