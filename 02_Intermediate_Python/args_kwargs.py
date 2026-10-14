# *args and **kwargs
# They let a function accept different numbers of arguments.

# 1. *args collects extra positional arguments into a tuple.
def add_numbers(*args):
    print("Arguments received:", args)
    return sum(args)

print("Sum:", add_numbers(10, 20))
print("Another sum:", add_numbers(5, 10, 15, 20))


# 2. **kwargs collects extra keyword arguments into a dictionary.
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="Maham", role="Engineer", language="Python")


# 3. You can combine normal parameters, *args, and **kwargs.
# Normal parameters come first, followed by *args and then **kwargs.
def describe_person(name, *hobbies, **details):
    print("Name:", name)
    print("Hobbies:", hobbies)
    print("Other details:", details)

describe_person(
    "Sara",
    "reading",
    "coding",
    age=22,
    city="Karachi"
)


# 4. Unpacking a list with * passes its items as separate arguments.
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
print("Product:", multiply(*numbers))


# 5. Unpacking a dictionary with ** matches keys to parameter names.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

person = {"name": "Ali", "age": 24}
introduce(**person)