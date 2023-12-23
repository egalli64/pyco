"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - List

Sequences - slicing
"""
# a list
friends = ["bob", "tom", "kim", "abe", "luc"]
print("friends:", friends)

# 'normal' slice
friends_1_4 = friends[1:4]
print("friends [1..4):", friends_1_4)

# get the three heading friends
first_3 = friends[:3]
print("First three friends:", first_3)

# get the last friends, from index 3 on
rest_3 = friends[3:]
print("After the third friend:", rest_3)

tail_3 = friends[-3:]
print("The last three friends:", tail_3)

# slicing to skip one element in each couple
even_friends = friends[::2]
print("friends with even index", even_friends)

# no exception on slicing
print("Wrong interval, empty slice:", friends[42:18])

# shallow copy
friends_alias = friends
friends_alias[0] = "bobby"
print(f"Shallow copy: '{friends[0]}' and '{friends_alias[0]}'")

# deep copy
friends_copy = friends[:]
friends[0] = "bob"
print(f"Deep copy: '{friends[0]}' vs '{friends_copy[0]}'")
