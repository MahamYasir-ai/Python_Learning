# Lambda, map(), filter(), and reduce()
# These tools are useful when processing collections of data.

from functools import reduce

# 1. A lambda is a small, anonymous function.
# This one takes a number and returns its square.
square = lambda number: number ** 2
print("Square:", square(5))

# 2. A lambda can accept more than one argument.
add = lambda a, b: a + b
print("Sum:", add(10, 20))

# 3. Sort students by their scores.
# key tells sort() to use the score (index 1), not the student's name.
students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 78),
]
students.sort(key=lambda student: student[1])
print("Sorted by score:", students)

# 4. map() applies a function to every item.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)

# 5. map() can process two lists together, item by item.
first = [1, 2, 3]
second = [10, 20, 30]
sums = list(map(lambda a, b: a + b, first, second))
print("Pairwise sums:", sums)

# 6. filter() keeps only the items that pass a condition.
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 7. Filter words by length.
words = ["python", "AI", "machine learning", "data"]
long_words = list(filter(lambda word: len(word) > 4, words))
print("Long words:", long_words)

# 8. reduce() combines all items into one final value.
# Here, it adds the numbers together.
total = reduce(lambda a, b: a + b, numbers)
print("Total:", total)

# The same idea can multiply all the numbers together.
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)

# 9. Combine filter() and map():
# First keep even numbers from 1 to 10, then square those numbers.
result = list(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, range(1, 11))
    )
)
print("Squares of even numbers:", result)

# 10. For more meaningful logic, a regular named function is often clearer.
def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

print("Discounted price:", calculate_discount(2000, 15))
