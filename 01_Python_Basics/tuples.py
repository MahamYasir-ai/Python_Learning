
# Python Tuples

# 1. Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed = (1, "Python", True)

print(coordinates)
print(colors)
print(mixed)

# 2. Single-element tuple
single_item = (10,)
print(type(single_item))

# 3. Indexing and slicing
print(colors[0])
print(colors[-1])
print(colors[0:2])

# 4. Tuples are immutable
# colors[0] = "yellow"  # This raises TypeError

# 5. Tuple methods
values = (1, 2, 2, 3, 4, 2)

print(values.count(2))
print(values.index(3))

# 6. Length and membership
print(len(values))
print(3 in values)

# 7. Tuple unpacking
x, y = coordinates
print(x)
print(y)

# 8. Extended unpacking
first, *middle, last = (10, 20, 30, 40, 50)

print(first)
print(middle)
print(last)

# 9. Tuple concatenation
tuple_a = (1, 2)
tuple_b = (3, 4)

print(tuple_a + tuple_b)

# 10. Tuple repetition
print(("Hi",) * 3)

# 11. Converting between list and tuple
my_list = list(colors)
my_list.append("yellow")

new_tuple = tuple(my_list)
print(new_tuple)

# 12. Nested tuples
nested = ((1, 2), (3, 4))
print(nested[1][1])
