
# Python Conditional Statements

# 1. if statement
age = 22

if age >= 18:
    print("You are an adult.")

# 2. if-else statement
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. if-elif-else statement
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")

# 4. Nested if statements
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("Entry denied.")

# 5. Logical operators in conditions
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("Good weather for a walk.")

# 6. Membership condition
languages = ["Python", "Java", "C++"]

if "Python" in languages:
    print("Python is available.")

# 7. Ternary conditional expression
number = 10
result = "Positive" if number > 0 else "Zero or negative"
print(result)

# 8. pass statement
if age >= 18:
    pass  # Placeholder for future code
