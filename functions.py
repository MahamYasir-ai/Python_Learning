
# Python Functions

# 1. Basic function
def greet():
    print("Hello, Python!")

greet()

# 2. Parameters and arguments
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Maham")

# 3. Returning a value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# 4. Default parameters
def introduce(name, country="Pakistan"):
    print(f"My name is {name}. I live in {country}.")

introduce("Maham")
introduce("Ali", "Canada")

# 5. Keyword arguments
def describe_person(name, age):
    print(name, age)

describe_person(age=24, name="Maham")

# 6. Variable-length positional arguments
def calculate_sum(*numbers):
    return sum(numbers)

print(calculate_sum(1, 2, 3))
print(calculate_sum(10, 20, 30, 40))

# 7. Variable-length keyword arguments
def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_details(name="Maham", role="Engineer", country="Pakistan")

# 8. Lambda function
square = lambda number: number ** 2
print(square(5))

# 9. Returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)

# 10. Recursion
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(factorial(5))

# 11. Function with a condition
def is_even(number):
    return number % 2 == 0

print(is_even(8))
print(is_even(7))

# 12. Docstring
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(multiply(4, 5))
print(multiply.__doc__)
