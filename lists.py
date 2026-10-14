
# Python Lists

# 1. Creating lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Python", 25, True]

print(fruits)
print(numbers)
print(mixed)

# 2. Indexing and slicing
print(fruits[0])
print(fruits[-1])
print(numbers[1:4])
print(numbers[::-1])

# 3. Modifying elements
fruits[1] = "orange"
print(fruits)

# 4. Adding elements
fruits.append("grapes")
fruits.insert(1, "banana")
fruits.extend(["kiwi", "peach"])
print(fruits)

# 5. Removing elements
fruits.remove("apple")
fruits.pop()
del fruits[0]
print(fruits)

# 6. Sorting and reversing
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

# 7. Useful functions and methods
values = [12, 5, 8, 20, 3]

print(len(values))
print(min(values))
print(max(values))
print(sum(values))
print(values.count(5))
print(values.index(8))

# 8. Membership
print(12 in values)
print(100 not in values)

# 9. Looping through a list
for value in values:
    print(value)

# 10. List comprehension
squares = [number ** 2 for number in range(1, 6)]
print(squares)

# 11. Filtering with a condition
even_numbers = [number for number in range(1, 11)
                if number % 2 == 0]
print(even_numbers)

# 12. Unpacking
first, second, *remaining = [10, 20, 30, 40, 50]

print(first)
print(second)
print(remaining)

# 13. Copying a list
original = [1, 2, 3]
copied = original.copy()
copied.append(4)

print(original)
print(copied)

# 14. Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])
