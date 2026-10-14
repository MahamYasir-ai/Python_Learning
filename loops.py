
# Python Loops

# 1. for loop
for i in range(1, 6):
    print(i)

# 2. range with a step
for i in range(2, 11, 2):
    print(i)

# 3. Loop through a string
for character in "Python":
    print(character)

# 4. Loop through a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# 5. while loop
count = 1

while count <= 5:
    print(count)
    count += 1

# 6. break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 7. continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 8. Nested loops
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

# 9. Loop with else
for i in range(3):
    print(i)
else:
    print("Loop completed.")

# 10. Enumerate
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# 11. List comprehension
squares = [number ** 2 for number in range(1, 6)]
print(squares)

# 12. Multiplication table
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
