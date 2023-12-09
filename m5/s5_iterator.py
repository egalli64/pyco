"""
Python Course

https://github.com/egalli64/pyco

Module 5 - Function

Iterator
"""
values = [1, 2, 3, 4, 5]

# get an iterator from the iterable
it = iter(values)

# use the iterator to loop on the elements
print("Looping by explicit iterator: ", end="")
for cur in it:
    print(cur, end=" ")
print()

# the iterator is exhausted, reset it
it = iter(values)
print("The first value is", next(it))

# create another iterator on the same iterable
it_2 = iter(values)
print("it_2 gives", next(it_2))
print("it gives", next(it))

# complete the loop on an iterator
while True:
    try:
        value = next(it)
        print("and then", value)
    except StopIteration:
        print("No more values in the current iteration")
        break

# the other iterator is still usable
print("it_2 gives", next(it_2))

# usually, let Python do the dirty job
print("Looping by implicit iterator: ", end="")
for value in values:
    print(value, end=" ")
print()
