# Exception Handling in Python
# Exceptions are errors that happen while a program is running.
# try and except allow us to handle errors without crashing the program.

# 1. Handling division by zero
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


# 2. Handling invalid input
# int() raises ValueError when text cannot be converted into an integer.
user_input = "hello"

try:
    number = int(user_input)
    print("Number:", number)
except ValueError:
    print("Error: Please provide a valid integer.")


# 3. Handling multiple possible exceptions
try:
    numbers = [10, 20, 30]
    index = int("5")
    print(numbers[index])
except ValueError:
    print("Error: The index must be an integer.")
except IndexError:
    print("Error: The index is outside the list.")


# 4. The else block runs only when no exception occurs.
try:
    result = 20 / 4
except ZeroDivisionError:
    print("Division failed.")
else:
    print("Division successful:", result)


# 5. The finally block always runs, whether an error occurs or not.
try:
    print("Performing an operation...")
    result = 5 / 1
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block always executes.")


# 6. Raising an exception manually
# raise lets us report invalid values when they break our rules.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    print("Age:", check_age(-2))
except ValueError as error:
    print("Invalid age:", error)


# 7. Handling a missing file
try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The requested file does not exist.")

print("Program continues running.")