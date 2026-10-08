# String Basics

name = "Maham"
course = "Python"

print(name)
print(course)

print(name[0])
print(name[1])
print(name[-1])

print(len(name))

print(name.upper())
print(name.lower())

print(name + " is learning " + course)

# String Methods

text = "  Python Programming  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())

word = "python"

print(word.capitalize())
print(word.title())
print(word.startswith("py"))
print(word.endswith("on"))

# String Slicing

text = "Python Programming"

print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
print(text[:])
print(text[::2])
print(text[::-1])

# F-Strings

name = "Maham"
age = 24
field = "Electronics Engineering"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I studied {field}.")

print(f"My name is {name} and I am {age} years old.")