
# Python Sets

# 1. Creating sets
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "mango"}

print(numbers)
print(fruits)

# 2. Sets remove duplicates
values = {1, 2, 2, 3, 3, 4}
print(values)

# 3. Creating an empty set
empty_set = set()
print(type(empty_set))

# 4. Adding elements
numbers.add(6)
numbers.update([7, 8, 9])
print(numbers)

# 5. Removing elements
numbers.remove(9)
numbers.discard(100)  # No error if absent
print(numbers)

# 6. Pop an arbitrary element
removed_item = numbers.pop()
print("Removed:", removed_item)

# 7. Membership
print(3 in numbers)

# 8. Union
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a.union(b))

# 9. Intersection
print(a & b)
print(a.intersection(b))

# 10. Difference
print(a - b)
print(b - a)

# 11. Symmetric difference
print(a ^ b)

# 12. Subset and superset
small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))
print(large.issuperset(small))

# 13. Disjoint sets
print({1, 2}.isdisjoint({3, 4}))

# 14. Remove duplicates from a list
items = [1, 2, 2, 3, 3, 4]
unique_items = list(set(items))
print(unique_items)

# Note: Sets are unordered; do not rely on output order.
