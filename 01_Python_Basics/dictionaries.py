
# Python Dictionaries

# 1. Creating a dictionary
student = {
    "name": "Maham",
    "age": 24,
    "department": "Electronics Engineering"
}

print(student)

# 2. Accessing values
print(student["name"])
print(student.get("age"))
print(student.get("grade", "Not assigned"))

# 3. Adding and updating
student["grade"] = "A"
student["age"] = 25
print(student)

# 4. Removing items
student.pop("grade")
print(student)

# 5. Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# 6. Checking keys
print("name" in student)
print("grade" not in student)

# 7. Looping through keys
for key in student:
    print(key)

# 8. Looping through values
for value in student.values():
    print(value)

# 9. Looping through key-value pairs
for key, value in student.items():
    print(key, ":", value)

# 10. Dictionary comprehension
squares = {number: number ** 2 for number in range(1, 6)}
print(squares)

# 11. Merging dictionaries
first = {"a": 1, "b": 2}
second = {"c": 3, "d": 4}

merged = first | second
print(merged)

# 12. Nested dictionaries
students = {
    "student1": {"name": "Ali", "marks": 85},
    "student2": {"name": "Sara", "marks": 92}
}

print(students["student1"]["name"])
print(students["student2"]["marks"])

# 13. Counting items
letters = ["a", "b", "a", "c", "b", "a"]
frequency = {}

for letter in letters:
    frequency[letter] = frequency.get(letter, 0) + 1

print(frequency)

# 14. Copying a dictionary
student_copy = student.copy()
print(student_copy)
