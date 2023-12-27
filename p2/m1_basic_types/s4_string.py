"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - More on basic types

String
"""
s = "bob,kim,joe,tim"
print("The string is:", s)

# slice
end = s.find(',')
if(end != -1):
    print("The first friend is", s[:end])

# split
friends = s.split(",")
print("The generated list is:", friends)

# join
s2 = " and ".join(friends)
print("The regenerated string is:", s2)

# empty field in a csv row
s = "bob,kim,,joe,tim"
print(f"Da '{s}' a {s.split(',')}")
