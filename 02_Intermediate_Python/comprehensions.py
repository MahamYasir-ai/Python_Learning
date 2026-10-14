# Python Comprehensions
# A comprehension creates a collection using a loop in a shorter form.

# 1. List comprehension: create a list of squares from 1 to 10.
squares = [number ** 2 for number in range(1, 11)]
print("Squares:", squares)

# 2. Add a condition to keep only even numbers.
# The number is included only when its remainder after division by 2 is zero.
even_numbers = [
    number for number in range(1, 21)
    if number % 2 == 0
]
print("Even numbers:", even_numbers)

# 3. Use if/else to label each number.
# Notice that the if/else comes before the for loop in this expression.
labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in range(1, 6)
]
print("Labels:", labels)

# 4. Work with strings: turn every letter into uppercase.
word = "Python"
uppercase_letters = [letter.upper() for letter in word]
print("Uppercase letters:", uppercase_letters)

# 5. Set comprehension: sets automatically remove duplicate values.
words = ["apple", "banana", "kiwi", "pear"]
unique_lengths = {len(word) for word in words}
print("Unique word lengths:", unique_lengths)

# 6. Dictionary comprehension: store each number and its square.
square_dictionary = {
    number: number ** 2 for number in range(1, 6)
}
print("Square dictionary:", square_dictionary)

# 7. Keep only students who scored at least 60.
scores = {"Ali": 85, "Sara": 92, "Ahmed": 58, "Zoya": 76}
passed_students = {
    name: score for name, score in scores.items()
    if score >= 60
}
print("Passed students:", passed_students)

# 8. Flatten a nested list: take every number from each inner row.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [number for row in matrix for number in row]
print("Flattened matrix:", flattened)

# 9. Double every number in every row, keeping the rows separate.
doubled_matrix = [
    [number * 2 for number in row]
    for row in matrix
]
print("Doubled matrix:", doubled_matrix)

# 10. Generator expression: values are produced when requested.
# Converting it to a list lets us see all its values at once.
squares_generator = (number ** 2 for number in range(1, 6))
print("Generator values:", list(squares_generator))

# 11. Remove duplicates while preserving their original order.
items = [3, 1, 3, 2, 1, 4, 2]
unique_items = list(dict.fromkeys(items))
print("Unique items:", unique_items)
